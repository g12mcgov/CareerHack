#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-12-11 01:13:26
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   grantmcgovern
# @Last Modified time: 2015-12-11 01:14:18

from setuptools import setup, find_packages

## Get our requirements from our .txt file
with open('requirements.txt') as requirements:
	modules = [line.strip('\n') for line in requirements]

setup(name = 'CareerHack',
	version = '0.1',
	description = 'A web app for nailing your technical interviews.',
	author = 'Grant McGovern',
	author_email = 'mcgoga12@wfu.edu',
	install_requires = modules
)