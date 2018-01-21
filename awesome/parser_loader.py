from .parsers.android import AwesomeAndroidParser
from .parsers.awesome import AwesomeParser
from .parsers.elixir import AwesomeElixirParser
from .parsers.go import AwesomeGoParser
from .parsers.ios import AwesomeIosParser
from .parsers.java import AwesomeJavaParser
from .parsers.javascript import AwesomeJavaScriptParser
from .parsers.php import AwesomePHPParser
from .parsers.python import AwesomePythonParser
from .parsers.ruby import AwesomeRubyParser
from .parsers.rust import AwesomeRustParser
from .parsers.scala import AwesomeScalaParser
from .parsers.shell import AwesomeShellParser
from .parsers.swift import AwesomeSwiftParser
from .parsers.vue import AwesomeVueParser
from .parsers.nodejs import AwesomeNodejsParser


def load_parsers():
    return {
        'android': AwesomeAndroidParser,
        'awesome': AwesomeParser,
        'elixir': AwesomeElixirParser,
        'go': AwesomeGoParser,
        'ios': AwesomeIosParser,
        'java': AwesomeJavaParser,
        'javascript': AwesomeJavaScriptParser,
        'php': AwesomePHPParser,
        'python': AwesomePythonParser,
        'ruby': AwesomeRubyParser,
        'rust': AwesomeRustParser,
        'scala': AwesomeScalaParser,
        'shell': AwesomeShellParser,
        'swift': AwesomeSwiftParser,
        'vue': AwesomeVueParser,
        'nodejs': AwesomeNodejsParser,
    }
