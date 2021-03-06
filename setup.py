#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'github_http_api'
DESCRIPTION = 'A simple github HTTP api handler in python.'
URL = 'https://github.com/ThaaoBlues/github_api'
EMAIL = 'thaaoblues81@gmail.com'
AUTHOR = '_ThaaoBlues_'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.2.5'

# What packages are required for this module to be executed?
REQUIRED = [
    'requests'
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION



# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=["github_http_api"],
    # If your package is a single module, use this instead of 'packages':
    py_modules=['github_http_api'],

    #entry_points={
    #     'console_scripts': ['pmanager_cli=pmanager.__main__:main'],
    #},
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='CC BY-NC-ND 4.0',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: Other/Proprietary License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],

)