import webbrowser

import curses
import curses.textpad

from textwrap import shorten


class SearchScreen(object):
    """A window screen for searching the awesome list without browser"""
    UP = -1
    DOWN = 1

    query = ''

    def __init__(self, awesome_title, awesome_blocks):
        """ Initialize the screen window

        Args
            awesome_title: Awesome topic title
            awesome_blocks: A list of formatted awesome content.
                It has a set of names and web links for crawled awesome content.

        Attributes
            window: A full curses screen window
            result_window: A window for showing the results
            search_window: A window for search bar

            y: Current y coordinates

            width: The width of `window`
            height: The height of `window`

            awesome_title: Awesome title
            awesome_blocks: It holds given `awesome_blocks` argument
            matched_blocks: A list of found awesome content

            max_lines: Maximum visible line count for `result_window`
            top: Available top line position for current page (used on scrolling)
            bottom: Available bottom line position for whole pages (as length of found lines)
            current: Current highlighted line number

            query: Query string for searching the awesome content

        Returns
            None
        """
        self.window = None
        self.result_window = None
        self.search_window = None

        self.y = 0

        self.width = 0
        self.height = 0

        self.awesome_title = awesome_title
        self.awesome_blocks = awesome_blocks
        self.matched_blocks = awesome_blocks

        self.init_curses()
        self.init_layout()

        self.max_lines = curses.LINES - 4
        self.top = 0
        self.bottom = self.max_lines
        self.current = 0

        self.run()

    def init_curses(self):
        """Setup the curses"""
        self.window = curses.initscr()
        self.window.keypad(True)

        curses.noecho()
        curses.cbreak()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

        self.current = curses.color_pair(2)

    def init_layout(self):
        """Initialize the each windows with their size and shape"""
        self.height, self.width = self.window.getmaxyx()

        # Title section
        self.window.addstr(0, 0, '[awesome-{}] Find awesome things!'.format(self.awesome_title), curses.color_pair(1))
        self.window.hline(1, 0, curses.ACS_HLINE, self.width)

        # Search result section
        self.result_window = curses.newwin(self.height - 4, self.width, 2, 0)
        self.result_window.keypad(True)

        # Search bar section
        self.window.hline(self.height - 2, 0, curses.ACS_HLINE, self.width)
        self.window.addch(self.height - 1, 0, '>')
        self.search_window = curses.newwin(1, self.width - 1, self.height - 1, 2)
        self.search_window.keypad(True)

        self.window.refresh()

    def reset_top(self):
        """Reset the top

        It is used to move up the scroll page to top position for next query
        """
        self.top = 0

    def run(self):
        """Continue running the awesome finder until interrupted"""
        try:
            self.input_stream()
        except KeyboardInterrupt:
            pass
        finally:
            curses.endwin()

    def input_stream(self):
        """Waiting an input and run a proper method according to type of input"""
        while True:
            self.search(self.query)
            self.display()

            ch = self.search_window.getch()
            if curses.ascii.isprint(ch):
                self.write(ch)
                self.reset_top()
            elif ch in (curses.ascii.BS, curses.ascii.DEL, curses.KEY_BACKSPACE):
                self.delete()
                self.reset_top()
            elif ch == curses.KEY_UP:
                self.scroll(self.UP)
            elif ch == curses.KEY_DOWN:
                self.scroll(self.DOWN)
            elif ch in (curses.ascii.LF, curses.ascii.NL):
                self.open_link()
            elif ch == curses.ascii.ESC:
                break

    def write(self, ch):
        """Write a character and append it to the query"""
        self.search_window.addch(ch)
        self.query += chr(ch)

    def delete(self):
        """Delete an ending character"""
        self.y, _ = self.search_window.getyx()
        if len(self.query) > 0:
            self.search_window.move(self.y, len(self.query) - 1)
        self.search_window.delch()
        self.query = self.query[:-1]

    def scroll(self, direction):
        """Scrolling the result window when pressing up/down arrow keys

        Args:
            direction: Up or Down

        Returns:
            None
        """
        next_line = self.current + direction

        # Paging
        if direction == self.UP and (self.current == 0 and self.top != 0):
            self.top += self.UP
            return
        if direction == self.DOWN and (next_line == self.max_lines) and (self.top + self.max_lines != self.bottom):
            self.top += self.DOWN
            return
        # Scrolling on result window
        if direction == self.UP and (self.current != 0 or self.top != 0):
            self.current = next_line
            return
        if direction == self.DOWN and (self.top + self.current + 1 != self.bottom) and (self.current != self.max_lines):
            self.current = next_line
            return

    def open_link(self):
        """Open the link of highlighted awesome content"""
        index = self.top + self.current
        if self.matched_blocks and self.matched_blocks[index]['type'] == 'awesome':
            webbrowser.open(self.matched_blocks[index]['link'], new=2)

    def search(self, query):
        """Search the awesome content with given query

        Args:
            query: Query string

        Returns:
            None
        """
        matched_blocks = []
        if query:
            query_tokens = query.lower().split()
            for block in self.awesome_blocks:
                if all([token in block['line'].lower() for token in query_tokens]):
                    matched_blocks.append(block)
        else:
            matched_blocks = self.awesome_blocks

        # Set the bottom to length of matched blocks
        self.bottom = len(matched_blocks)

        # When reached bottom line, stop scrolling
        if self.current > self.bottom:
            self.current = self.bottom - 1
        self.matched_blocks = matched_blocks

    def display(self):
        """Display the found awesome content on result window"""
        self.result_window.erase()
        for idx, val in enumerate(self.matched_blocks[self.top:self.top + self.max_lines]):
            if val['type'] == 'category':
                if idx == self.current:
                    self.result_window.addstr(idx, 0, shorten(val['line'], self.width, placeholder='...'),
                                              curses.color_pair(2))
                else:
                    self.result_window.addstr(idx, 0, shorten(val['line'], self.width, placeholder='...'),
                                              curses.color_pair(1))
            elif val['type'] == 'awesome':
                if idx == self.current:
                    self.result_window.addstr(idx, 2, shorten(val['line'], self.width - 3, placeholder='...'),
                                              curses.color_pair(2))
                else:
                    self.result_window.addstr(idx, 2, shorten(val['line'], self.width - 3, placeholder='...'))
        self.result_window.refresh()
