# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ssh-proxy-server',
    version='0.3.0',
    author='Manfred Kaiser',
    author_email='ssh-mitm@logfile.at',
    description='ssh mitm proxy server',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="ssh mitm proxy audit network security",
    python_requires='>= 3.6',
    url="https://ssh-mitm.logfile.at/",
    project_urls={
        'Source': 'https://github.com/ssh-mitm/ssh-proxy-server',
        'Tracker': 'https://github.com/ssh-mitm/ssh-mitm/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: System :: Networking",
        "Development Status :: 4 - Beta"
    ],
    install_requires=[
        'ssh-mitm>=0.3.0',
    ]
)
