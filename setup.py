import io
import os
import sys
from shutil import rmtree

from setuptools import setup, find_packages, Command

import awesome

HERE = os.path.abspath(os.path.dirname(__file__))

# Package meta-data.
NAME = 'awesome-finder'
DESCRIPTION = 'A TUI based awesome curated list finder'
URL = 'https://github.com/mingrammer/awesome-finder'
EMAIL = 'k239507@gmail.com'

# What packages are required for this module to be executed?
REQUIRED = []
with io.open(os.path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        REQUIRED.append(line)

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(HERE, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


setup(
    name=NAME,
    version=awesome.__version__,
    description=DESCRIPTION,
    long_description=long_description,
    author=awesome.__author__,
    author_email=EMAIL,
    url=URL,
    keywords='awesome finder curses tui',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['awesome-hub=awesome.__main__:main'],
    },
    install_requires=REQUIRED,
    include_package_data=True,
    license=awesome.__license__,
    python_requires='>=3',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Terminals',

    ],
    # $ setup.py publish support.
    cmdclass={
        'publish': PublishCommand,
    },
)
