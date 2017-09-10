from . import AbstractAwesomeParser


class AwesomeParser(AbstractAwesomeParser):
    AWESOME_TITLE = 'awesome'
    AWESOME_README_URL = 'https://raw.githubusercontent.com/sindresorhus/awesome/master/readme.md'

    def find_content(self):
        readme = self.read_readme()
        content = readme.split('https://awesome.re')[1]
        lines = []
        for line in content.split('\n'):
            lines.append(line)
        return lines

    def parse_awesome_content(self, content):
        awesome_blocks = []
        for line in content:
            # Ignore last useless parts
            if line.startswith('## License'):
                break
            # Parse the header title            
            elif line.startswith('##'):
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
        return awesome_blocks
