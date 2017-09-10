import os

CACHE_DIRECTORY = os.path.join(os.path.expanduser('~'), '.awesome_cache')


def exists(awesome_title):
    """

    Args:
        awesome_title: Awesome repository title

    Returns:
        True if exists, False otherwise
    """
    awesome_cache_directory = os.path.join(CACHE_DIRECTORY, awesome_title)
    awesome_cached_readme = os.path.join(awesome_cache_directory, 'README.md')
    return os.path.exists(awesome_cached_readme)


def save_readme(awesome_title, readme):
    """Save the README on local cache directory

    Args:
        awesome_title: Awesome repository title
        readme: Readme content

    Returns:
        None
    """
    awesome_cache_directory = os.path.join(CACHE_DIRECTORY, awesome_title)
    awesome_cached_readme = os.path.join(awesome_cache_directory, 'README.md')
    if not os.path.exists(CACHE_DIRECTORY):
        os.mkdir(CACHE_DIRECTORY)
    if not os.path.exists(awesome_cache_directory):
        os.mkdir(awesome_cache_directory)
    with open(awesome_cached_readme, 'w+', encoding='utf8') as readme_md:
        readme_md.write(readme)


def load_readme(awesome_title):
    """Loads the cached readme content

    Args:
        awesome_title: Awesome repository title

    Returns:
        A string of cached readme content, None if there is no cached readme
    """
    awesome_cache_directory = os.path.join(CACHE_DIRECTORY, awesome_title)
    awesome_cached_readme = os.path.join(awesome_cache_directory, 'README.md')
    if not os.path.exists(awesome_cache_directory):
        raise NotADirectoryError('{} does not exists'.format(awesome_cache_directory))
    if not os.path.exists(awesome_cached_readme):
        raise FileNotFoundError('{} does not exists'.format(awesome_cached_readme))
    with open(awesome_cached_readme, 'r', encoding='utf8') as readme_md:
        return readme_md.read()
