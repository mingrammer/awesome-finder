from . import AbstractAwesomeParser


class AwesomeIosParser(AbstractAwesomeParser):
    AWESOME_TITLE = 'ios'
    AWESOME_README_URL = 'https://raw.githubusercontent.com/vsouza/awesome-ios/master/README.md'

    def find_content(self):
        readme = self.read_readme()
        content = readme.split('- [Contributing](#contributing-and-license)')[1]
        lines = []
        for line in content.split('\n'):
            lines.append(line)
        return lines

    def parse_awesome_content(self, content):
        awesome_blocks = []
        for line in content:
            # Parse the header title
            if line.startswith('##'):
                plain_title = self.parse_category_title(line)
                awesome_blocks.append({
                    'type': 'category',
                    'line': plain_title,
                })
            # Parse the list item
            elif line.strip().startswith('* [') or line.strip().startswith('- ['):
                plain_line, link = self.parse_link_line(line)
                awesome_blocks.append({
                    'type': 'awesome',
                    'line': plain_line,
                    'link': link,
                })
            # Ignore last useless parts
            elif line.startswith('## Contributing and License'):
                break
        return awesome_blocks
