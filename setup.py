# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='scaledrone',
    version='0.2.0',
    description='Official Scaledrone Python API client',
    author='Serge Herkül',
    author_email='info@scaledrone.com',
    license='MIT',
    url="https://github.com/Scaledrone/scaledrone-python",
    download_url="https://github.com/Scaledrone/scaledrone-python/tarball/0.2",
    install_requires=[
        'requests >= 2.9.1'
    ],
    packages=[
        'scaledrone'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
