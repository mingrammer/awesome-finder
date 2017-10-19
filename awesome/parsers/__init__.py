"""parsers

Retrieve a README file from awesome repository and parse it to get awesome list.
"""
import os
import re
import sys
from abc import abstractmethod

import requests

from awesome.cache import exists, load_readme, save_readme

sys.path.append(os.path.abspath(os.path.pardir))


class AbstractAwesomeParser(object):
    """An abstract parser class for providing the common methods for parsing the markdown based README

    Each Awesome README has slightly different formats,
        So should implements each parsers corresponding to each languages or topics
    """
    AWESOME_TITLE = ''
    AWESOME_README_URL = ''

    def __init__(self, force_request=False):
        """Initialize the parser

        Args:
            force_request: If true, the parser does not use cached, but always request the README from remote repository
        """
        self._markdown_header_regex = re.compile('#+\s+(.*)')
        self._markdown_link_line_regex = re.compile('\s?\[([^<>]+|(?:\[\w+\]))\]\s?\(([^\(\)]+)\)\s?(?::\w+:)?\s?(?:[-—]\s?(.*))?')
        self.force_request = force_request

    def is_cached(self):
        """Check if there exists cached README"""
        return exists(self.AWESOME_TITLE)

    def from_cache(self):
        """Retrieve the cached README from cache directory"""
        return load_readme(self.AWESOME_TITLE)

    def cache(self, readme):
        """Cache the readme to cache directory"""
        save_readme(self.AWESOME_TITLE, readme)

    def read_readme(self):
        """Read the README content from remote awesome repository"""
        if self.is_cached() and not self.force_request:
            print('Fetching the README from cache...')
            readme = self.from_cache()
            print('Done.')
            return readme
        print('Fetching the README from awesome place ...')
        response = requests.get(self.AWESOME_README_URL)
        print('Done.')
        if response.status_code == 200:
            readme = response.content.decode('utf8')
            self.cache(readme)
            return readme
        raise requests.RequestException('Error occurs when getting the README from {}'.format(self.AWESOME_README_URL))

    def parse(self):
        """Parse the all content of README of Awesome repository"""
        content = self.find_content()
        awesome_blocks = self.parse_awesome_content(content)
        return awesome_blocks

    @abstractmethod
    def find_content(self):
        """Find only awesome content from README content"""
        raise NotImplementedError

    @abstractmethod
    def parse_awesome_content(self, content):
        """Parses the raw awesome content and returns a structured list as following form:

        The README is formed as follow:

        ------------------------------------
        ... table of content ...              <- TOC

        {separator between TOC and content}   <- Separator such as '----'

        ## category                            <- Awesome content
            * [title](link) - description      <-
            * [title](link) - description      <-
            * [title](link) - description      <-

        # others                               <- Useless parts
            * ...                              <-
        ------------------------------------

        awesome_blocks = [
            {
                'type': <'category'|'awesome'>,
                'line': 'line text',
                'link'; [optional],
            },
        ]

        Args
            content: All content of the awesome README
        """
        raise NotImplementedError

    def parse_category_title(self, line):
        """Parse the header to get category title"""
        title = self._markdown_header_regex.findall(line)[0]
        plain_title = '[{}]'.format(title)
        return plain_title

    def parse_link_line(self, line):
        """Parse the line which has awesome link, title or description"""
        name, link, desc = self._markdown_link_line_regex.findall(line)[0]
        if desc:
            plain_line = '[{}] - {}'.format(name, desc)
        else:
            plain_line = '[{}]'.format(name)
        return plain_line, link
