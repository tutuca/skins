#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='Skins',
    version='0.1',
    author=u'Matías Iturburu',
    author_email='maturburu@gmail.com',
    url='http://github.com/tutuca',
    description='Basic skin scaffolding',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PasteScript',
    ],
    entry_points={
        'paste.paster_create_template': [
            'skin=skintemplate:SkinTemplate',
        ],
    }
)
