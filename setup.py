"""Packaging settings."""
from codecs import open

from setuptools import setup, find_packages

import os


NAME = 'hs_solver'
WORKING_DIR = os.path.dirname(__file__)

if WORKING_DIR != '':
    os.chdir(WORKING_DIR)

ABS_PATH = os.path.abspath(WORKING_DIR)
REQUIREMENTS_DIRECTORY = 'requirements'
REQUIREMENTS_PATH = os.path.join(ABS_PATH, REQUIREMENTS_DIRECTORY)
BASE_REQ_FILE = os.path.join(REQUIREMENTS_PATH, 'requirements_base.txt')
VERSION_FILE = os.path.join(ABS_PATH, 'src', NAME, '__init__.py')
README_FILE = os.path.join(ABS_PATH, 'README.md')

exec(open(VERSION_FILE).read())
VERSION = __version__ # noqa


def read_file(file_name):
    with open(file_name, encoding='utf-8') as open_file:
        return open_file.read()


setup(
    name=NAME,
    version=VERSION,
    description='Solve HS challenges',
    long_description=read_file(README_FILE),
    url='https://github.com/tahoward/hs-solver',
    author='Trevor Howard',
    author_email='thatrevguy@gmail.com',
    license='UNLICENSE',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Intended Audience :: Lazy People',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='hiringsolved hiring solved challenge',
    install_requires=read_file(BASE_REQ_FILE),
    entry_points={
        'console_scripts': [
            'hs-solver=hs_solver.cli:main',
        ],
    }
)
