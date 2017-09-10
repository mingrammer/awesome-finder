from .parsers.awesome import AwesomeParser
from .parsers.elixir import AwesomeElixirParser
from .parsers.go import AwesomeGoParser
from .parsers.java import AwesomeJavaParser
from .parsers.javascript import AwesomeJavaScriptParser
from .parsers.php import AwesomePHPParser
from .parsers.python import AwesomePythonParser
from .parsers.ruby import AwesomeRubyParser
from .parsers.rust import AwesomeRustParser
from .parsers.scala import AwesomeScalaParser
from .parsers.swift import AwesomeSwiftParser


def load_parsers():
    return {
        'awesome': AwesomeParser,
        'elixir': AwesomeElixirParser,
        'go': AwesomeGoParser,
        'java': AwesomeJavaParser,
        'javascript': AwesomeJavaScriptParser,
        'php': AwesomePHPParser,
        'python': AwesomePythonParser,
        'ruby': AwesomeRubyParser,
        'rust': AwesomeRustParser,
        'scala': AwesomeScalaParser,
        'swift': AwesomeSwiftParser,
    }
