# Contributing

If you want to add other awesome repositories, you must implement the README parsers for them on `awesome/parsers` named `<title>.py` (example: `awesome/parsers/ruby.py`) and register the parser to `awesome/parser_loader.py`

<br>

## How it works?

1. Make a parser for a specific awesome repository to `awesome/parsers/`
2. Register this parser to `awesome/parser_loader.py`
3. The main will load the parsers automatically 

<br>

## How to make parsers

All parsers have same form based on `AbstractAwesomeParser` on `awesome/parsers/__init__.py`. You need to implement the `find_content` method which finds only awesome content and `parse_awesome_content` which parses the content line by line. (**category header** or **line with link**)

The awesome READMEs have common format as following:

* TOC will be not used
* Separator will be used for getting only awesome content without TOC
* **category header** means `## category`
* **line with link** means `* [title](link) - description`
* `# others` is useless part (Optional. Some repositories does not have it)

```
------------------------------------
... table of content ...               <- TOC

{separator between TOC and content}    <- Separator such as '----'

## category                            <- Awesome content
    * [title](link) - description      <-
    * [title](link) - description      <-
    * [title](link) - description      <-

# others                               <- Useless parts
    * ...                              <-
------------------------------------
```

This is an example [`AwesomePythonParser`](/awesome/parsres/python.py) for **awesome-python** repository

```Python
from . import AbstractAwesomeParser


class AwesomePythonParser(AbstractAwesomeParser):
    AWESOME_TITLE = 'python'
    AWESOME_README_URL = 'https://raw.githubusercontent.com/vinta/awesome-python/master/README.md'

    def find_content(self):
        readme = self.read_readme()
        content = readme.split('- - -')[1]  # '- - -' is separator
        lines = []
        for line in content.split('\n'):
            lines.append(line)
        return lines

    def parse_awesome_contents(self, content):
        awesome_blocks = []
        for line in content:
            # Parse the header title
            if line.startswith('##'):  # 'category header'
                plain_title = self.parse_category_title(line)
                awesome_blocks.append({
                    'type': 'category',
                    'line': plain_title,
                })
            # Parse the list item
            elif line.strip().startswith('* ['):  # line with link
                plain_line, link = self.parse_link_line(line)
                awesome_blocks.append({
                    'type': 'awesome',
                    'line': plain_line,
                    'link': link,
                })
            # Ignore last useless parts
            elif line.startswith('#'):  # useless part of awesome-python
                break
        return awesome_blocks
```

<br>

## Development

You can test it on local with  `pip install -e .` or `pip3 install -e .`.
