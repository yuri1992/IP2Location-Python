#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='IP2Location',
        version='9.0.0',
        description='Python API for IP2Location database',
        author='IP2Location',
        author_email='support@ip2location.com',
        url='http://www.ip2location.com',
        packages=find_packages(),
        package_data={'upsell_tracker': ['*bin']},
        )
