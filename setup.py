#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import inspect

import setuptools
from setuptools import setup
from setuptools.command.test import test as TestCommand

if sys.version_info < (3, 4, 0):
    sys.stderr.write('FATAL: STUPS eeds to be run with Python 3.4+\n')
    sys.exit(1)

__location__ = os.path.join(os.getcwd(), os.path.dirname(inspect.getfile(inspect.currentframe())))


def read_version(package):
    data = {}
    with open(os.path.join(package, '__init__.py'), 'r') as fd:
        exec(fd.read(), data)
    return data['__version__']


NAME = 'stups'
MAIN_PACKAGE = 'stups'
VERSION = read_version(MAIN_PACKAGE)
DESCRIPTION = 'STUPS meta package'
LICENSE = 'Apache License 2.0'
URL = 'https://github.com/zalando-stups/stups-cli'
AUTHOR = 'Henning Jacobs'
EMAIL = 'henning.jacobs@zalando.de'

COVERAGE_XML = True
COVERAGE_HTML = False
JUNIT_XML = True

# Add here all kinds of additional classifiers as defined under
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: CPython',
]

CONSOLE_SCRIPTS = ['stups = stups.cli:main']


class PyTest(TestCommand):

    user_options = [('cov-html=', None, 'Generate junit html report')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.cov = None
        self.pytest_args = ['--cov', 'stups', '--cov-report', 'term-missing']
        self.cov_html = False

    def finalize_options(self):
        TestCommand.finalize_options(self)
        if self.cov_html:
            self.pytest_args.extend(['--cov-report', 'html'])

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def get_install_requirements(path):
    content = open(os.path.join(__location__, path)).read()
    return [req for req in content.split('\\n') if req != '']


def read(fname):
    return open(os.path.join(__location__, fname), encoding='utf-8').read()


def setup_package():
    install_reqs = get_install_requirements('requirements.txt')

    setup(
        name=NAME,
        version=VERSION,
        url=URL,
        description=DESCRIPTION,
        author=AUTHOR,
        author_email=EMAIL,
        license=LICENSE,
        keywords='stups cloud aws account cloud formation mai piu senza zign pierone',
        long_description=read('README.rst'),
        classifiers=CLASSIFIERS,
        cmdclass={'test': PyTest},
        test_suite='tests',
        packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
        install_requires=install_reqs,
        tests_require=['pytest-cov', 'pytest'],
        setup_requires=['flake8'],
        entry_points={'console_scripts': CONSOLE_SCRIPTS},
    )


if __name__ == '__main__':
    setup_package()
