#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from thumbor_greenthumb_filter import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'colorama',
    'preggy',
    'ipdb',
    'coveralls',
    'numpy',
]

setup(
    name='thumbor_greenthumb_filter',
    version=__version__,
    description='GreenThumb CV',
    long_description='''
Text filter for thumbor.
''',
    keywords='thumbor filter',
    author='GreenThumb.io',
    author_email='justin@greenthumb.io',
    url='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pillow',
    ],
    extras_require={
        'tests': tests_require,
    }
)
