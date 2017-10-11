#!/usr/local/bin/python3

import argparse
import os

from . import __author__, __version__
from .parser_loader import load_parsers
from .tui import SearchScreen

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

    parser.add_argument('--version', action='version', version='awesome-finder version {version}, (c) 2017-2017 by {author}.'.format(version=__version__, author=__author__))

    subparsers = parser.add_subparsers(dest='title', title='title',
                                       description='The title of awesome you want to find')
    subparsers.required = True

    # Register awesome commands
    for title in awesome_parsers.keys():
        if title == 'awesome':
            subparsers.add_parser(title, help='Search the {}'.format(title)) \
                .add_argument('--force', '-f', type=bool, nargs='?', const=True, default=False)
        else:
            subparsers.add_parser(title, help='Search the awesome-{}'.format(title)) \
                .add_argument('--force', '-f', type=bool, nargs='?', const=True, default=False)

    return parser.parse_args()


def main():
    set_short_esc_delay()

    args = parse_command()
    awesome_blocks = get_awesome_blocks(args.title, args.force)

    SearchScreen(args.title, awesome_blocks)


if __name__ == '__main__':
    main()
