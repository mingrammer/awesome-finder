#!/usr/bin/env python3

import argparse
import os

from awesome import __author__, __version__
from awesome.parser_loader import load_parsers
from awesome.tui import SearchScreen

awesome_parsers = load_parsers()


def set_short_esc_delay():
    """Make the ESC key delay short"""
    os.environ.setdefault('ESCDELAY', '50')


def get_awesome_blocks(awesome_title, force):
    parser = awesome_parsers[awesome_title](force_request=force)
    awesome_blocks = parser.parse()
    return awesome_blocks


def parse_command():
    parser = argparse.ArgumentParser(description='awesome command')
    parser.add_argument('--version', action='version', version='awesome-finder version {version}, (c) 2017-2018 by {author}.'.format(version=__version__, author=__author__))

    subparsers = parser.add_subparsers(dest='title', title='title', description='the title of awesome you want to find')
    subparsers.required = True

    # Register awesome commands
    for title in awesome_parsers.keys():
        if title == 'awesome':
            subparser = subparsers.add_parser(title, help='search the {}'.format(title))
        else:
            subparser = subparsers.add_parser(title, help='search the awesome-{}'.format(title))
        subparser.add_argument('--force', '-f', type=bool, nargs='?', const=True, default=False)
        subparser.add_argument('--query', '-q', type=str, default='', help='pass the initial query')
    return parser.parse_args()


def main():
    set_short_esc_delay()

    args = parse_command()
    awesome_blocks = get_awesome_blocks(args.title, args.force)
    initial_query = args.query

    SearchScreen(args.title, awesome_blocks, initial_query=initial_query)


if __name__ == '__main__':
    main()
