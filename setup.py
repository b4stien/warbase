# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='mozbase',
    version='0.5.4',
    packages=find_packages(),
    test_suite='tests',
    install_requires=[
        'SQLAlchemy==0.9.6',
        'voluptuous==0.8.5',
        'dogpile.cache==0.5.4',
        'click==2.1',
    ],
    scripts=('scripts/mozbase',),
    author='Bastien GANDOUET',
    author_email="bastien@mozaiqu.es"
)
