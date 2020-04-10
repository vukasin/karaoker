#!/usr/bin/env python
# coding: utf8

"""  Distribution script. """

import sys

from os import path
from setuptools import setup

__email__ = 'vukasin@toroman.name'
__author__ = 'Vukasin Toroman'
__license__ = 'MIT License'

# Default project values.
project_name = 'karaoker'
project_version = '0.0.1'

here = path.abspath(path.dirname(__file__))
readme_path = path.join(here, 'README.md')
with open(readme_path, 'r') as stream:
    readme = stream.read()

# Package setup entrypoint.
setup(
    name=project_name,
    version=project_version,
    description='''
    The Karaoker makes karaokee
    ''',
    long_description=readme,
    long_description_content_type='text/markdown',
    author=__author__,
    author_email=__email__,
    url='https://github.com/vukasin/karaoker',
    license='MIT License',
    packages=['karaoker'],
    python_requires='>=3.6, <3.8',
    include_package_data=True,
    install_requires=["youtube-dl", "spleeter"],
    entry_points={
        'console_scripts': ['karaoker=karaoker.__main__:entrypoint']
    },
    classifiers=[
        'Environment :: Console',
        'Environment :: MacOS X',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Artistic Software',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'Topic :: Utilities']
)
