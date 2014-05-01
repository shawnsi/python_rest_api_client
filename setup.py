#!/usr/bin/env python

import os
from setuptools import setup


setup(
    name='ultradns',
    version='0.0.1',
    author='Jon Bodner',
    author_email='jon@bodnerfamily.com',
    description='Python REST API for UltraDNS',
    license='Apache',
    keywords='ultradns',
    packages=['ultradns'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
    ],
    install_requires=[
        'docopt',
    ],
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
