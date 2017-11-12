#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

with open('README.rst') as readme_file:
    readme = readme_file.read()


# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements_dev.txt', session=PipSession())

dev_reqs = [str(ir.req) for ir in install_reqs]

requirements = [
    'requests',
]

setup_requirements = dev_reqs

test_requirements = dev_reqs


setup(
    name='neo-python-rpc',
    version='0.1.5',
    description="A Python RPC Client for the NEO Blockchain",
    long_description=readme,
    author="Thomas Saunders",
    author_email='tom@cityofzion.io',
    url='https://github.com/CityOfZion/neo-python-rpc',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='neo, python, rpc, client',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
