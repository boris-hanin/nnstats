#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'tqdm>=4.11.2',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='nnstats',
    version='0.1.0',
    description="Exctraction and analysis of statistics of weights, activations, gradients for deep neural nets.",
    long_description=readme + '\n\n' + history,
    author="Boris Hanin",
    author_email='bhanin@gmail.com',
    url='https://github.com/boris-hanin/nnstats',
    packages=[
        'nnstats',
    ],
    package_dir={'nnstats':
                 'nnstats'},
    entry_points={
        'console_scripts': [
            'nnstats=nnstats.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='nnstats',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
