#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'rmAPI',
    version = '4.3.0',
    license = 'GPL',
    description = 'Python library for RainMachine REST API',
    author = 'Rain Machine',
    author_email = '',
    url = 'https://github.com/legrego/rainmachine-developer-resources',
    packages=find_packages(),
    classifiers = [
        'Programming Language :: Python'
    ],
    install_requires=[],
    zip_safe=True,
)
