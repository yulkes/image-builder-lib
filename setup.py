#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from pkg_resources import parse_requirements
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = parse_requirements("requirements.txt")

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Eyal Yavor",
    author_email='yulkes@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python library to generate images by combining templates and data",
    entry_points={
        'console_scripts': [
            'image_builder_library=image_builder_library.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='image_builder_library',
    name='image_builder_library',
    packages=find_packages(include=['image_builder_library']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/yulkes/image_builder_library',
    version='0.1.0',
    zip_safe=False,
)
