[![PyPI version](https://badge.fury.io/py/awesome-finder.svg)](https://badge.fury.io/py/awesome-finder) [![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mingrammer/awesome-finder/blob/master/LICENSE)

# Awesome finder

> Find the awesome things without browser.
>
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
awesome <topic>

# Find awesome things from latest awesome-<topic> (not use cache)
awesome <topic> -f (--force)

# Show help messages (can see supported awesome topics)
awesome -h (--help)
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

>  *Updates: 2017-09-10*

These will be updated continuously

- awesome
- awesome-elixir
- awesome-go
- awesome-java
- awesome-javascript
- awesome-php
- awesome-python
- awesome-ruby
- awesome-rust
- awesome-scala
- awesome-swift

<br>

## Contributing

Details on [CONTRIBUTING](CONTRIBUTING.md)

<br>

## TODO

* [ ] Query highlighting
* [ ] Supports paging with Key left (←) and Key right (→)
* [ ] Smart parsing with hierachical structure
* [ ] Supports all awesome series
* [ ] Supports initial query (example: `awesome python -q 'django oauth'`)
* [ ] Add options to open the Issue and Pull Request page of a specific awesome series
