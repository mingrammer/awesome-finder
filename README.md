<br><br>

<h1 align="center">Awesome Finder</h1>

<p align="center">
  <a href="/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg"/></a>
  <a href="https://app.fossa.io/projects/git%2Bgithub.com%2Fmingrammer%2Fawesome-finder?ref=badge_shield" alt="FOSSA Status"><img src="https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmingrammer%2Fawesome-finder.svg?type=shield"/></a>
  <a href="https://badge.fury.io/py/awesome-finder"><img src="https://badge.fury.io/py/awesome-finder.svg"/></a>
  <a href="https://docs.python.org/3/index.html"><img src="https://img.shields.io/badge/python-3.5,3.6-blue.svg"/></a>
  <a href="https://www.python.org/dev/peps/pep-0008"><img src="https://img.shields.io/badge/code%20style-PEP8-brightgreen.svg"/></a>
</p>

<p align="center">
  Search the awesome curated list without browser
</p>

<br><br><br>

> What does mean awesome? The awesome series provide a curated list of awesome frameworks, libraries, software and resources for a specific topic. An example is [awesome-python](https://github.com/vinta/awesome-python)

A TUI based finder for searching the awesome resources on awesome series such as `awesome-python`, `awesome-go` and so on.

With it, you can browse the awesome libraries, resources on your terminal without browser.

[![asciicast](https://asciinema.org/a/OOdH9rLVBvReK3K6n7pZvruf9.png)](https://asciinema.org/a/OOdH9rLVBvReK3K6n7pZvruf9)

## Installation

It supports **Python 3+** only.

```bash
pip install awesome-finder # or pip3 install awesome-finder 
```

## Usage

```console
# Find awesome things from awesome-<topic>
awesome-hub <topic>

# Find awesome things from latest awesome-<topic> (not use cache)
awesome-hub <topic> -f (--force)

# Find awesome things with initial query
awesome-hub <topic> -q (--query) 'query string you want to search'

# Show help messages (can see supported awesome topics)
awesome-hub -h (--help)
```

There are some helpful key bindings:

| Key               | Description                              |
| ----------------- | ---------------------------------------- |
| Key up (**↑**)    | Scroll up                                |
| Key down  (**↓**) | Scroll down                              |
| Key left (**←**)  | Page up                                  |
| Key right (**→**) | Page down                                |
| Enter (↵)         | Open the selected awesome link on default browser |
| Esc               | Close the awesome finder                 |

## Supported awesome topics

>  *Updated: 2018-03-04*

These will be updated continuously

- awesome
- awesome-android
- awesome-elixir
- awesome-erlang
- awesome-go
- awesome-ios
- awesome-java
- awesome-javascript
- awesome-nodejs
- awesome-php
- awesome-python
- awesome-ruby
- awesome-rust
- awesome-scala
- awesome-swift
- awesome-vue

## Contributing

Details on [CONTRIBUTING](CONTRIBUTING.md)

## Changelog

Details on [CHANGELOG](CHANGELOG.md)

## TODO

* [ ] Query highlighting
* [x] Supports paging with Key left (←) and Key right (→)
* [ ] Smart parsing with hierachical structure
* [ ] Supports all awesome series
* [x] Supports initial query (example: `awesome python -q 'django oauth'`)
* [ ] Add options to open the Issue and Pull Request page of a specific awesome series

## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmingrammer%2Fawesome-finder.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fmingrammer%2Fawesome-finder?ref=badge_large)
