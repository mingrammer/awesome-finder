<br><br>

<h1 align="center">Awesome Finder</h1>

<p align="center">
  <a href="https://badge.fury.io/py/awesome-finder"><img src="https://badge.fury.io/py/awesome-finder.svg"/></a>
  <a href="https://docs.python.org/3/index.html"><img src="https://img.shields.io/badge/python-3.5, 3.6-blue.svg"/></a>
  <a href="https://www.python.org/dev/peps/pep-0008"><img src="https://img.shields.io/badge/code%20style-PEP8-brightgreen.svg"/></a>
  <a href="/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg"/></a>
</p>

<p align="center">
  Find and search the awesome things without browser
</p>

<br><br><br>

> What does mean awesome? The awesome seires provide a curated list of awesome frameworks, libraries, software and resources for a specific topic. An example is [awesome-python](https://github.com/vinta/awesome-python)

A TUI based finder for searching the awesome resources on awesome series such as `awesome-python`, `awesome-go` and so on.

With it, you can browse the awesome libraries, resources on your terminal without browser.

[![asciicast](https://asciinema.org/a/OOdH9rLVBvReK3K6n7pZvruf9.png)](https://asciinema.org/a/OOdH9rLVBvReK3K6n7pZvruf9)

<br>

## Installation

It supports **Python 3+** only now.

```bash
pip install awesome-finder # or pip3 install awesome-finder 
```

<br>

## Usage

```bash
# Find awesome things from awesome-<topic>
awesome-hub <topic>

# Find awesome things from latest awesome-<topic> (not use cache)
awesome-hub <topic> -f (--force)

# Show help messages (can see supported awesome topics)
awesome-hub -h (--help)
```

There are some helper keys:

| Key               | Description                              |
| ----------------- | ---------------------------------------- |
| Key up (**↑**)    | Move and scroll up                       |
| Key down  (**↓**) | Move and scroll down                     |
| Enter (↵)         | Open the selected awesome link on default browser |
| Esc               | Close the awesome finder                 |

<br>

## Supported awesome topics

>  *Updated: 2018-01-21*

These will be updated continuously

- awesome
- awesome-android
- awesome-elixir
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

<br>

## Contributing

Details on [CONTRIBUTING](CONTRIBUTING.md)

<br>

## Changelog

Details on [CHANGELOG](CHANGELOG.md)

<br>

## TODO

* [ ] Query highlighting
* [ ] Supports paging with Key left (←) and Key right (→)
* [ ] Smart parsing with hierachical structure
* [ ] Supports all awesome series
* [x] Supports initial query (example: `awesome python -q 'django oauth'`)
* [ ] Add options to open the Issue and Pull Request page of a specific awesome series
