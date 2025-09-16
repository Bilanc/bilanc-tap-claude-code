#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="tap-claude-code",
    version="0.1.0",
    description="Singer.io tap for extracting data from the CLaude code API",
    author="llemanh",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap-claude-code"],
    install_requires=[
        "singer-python==5.12.1",
        "requests==2.29.0",
        "urllib3==1.26.20",
        "backoff==1.8.0",
        "python-dateutil==2.8.2",
    ],
    extras_require={"dev": ["pylint==2.6.2", "ipdb", "nose", "requests-mock==1.9.3"]},
    entry_points="""
          [console_scripts]
          tap-claude-code=tap_claude_code:main
      """,
    packages=["tap_claude_code"],
    package_data={"tap_claude_code": ["schemas/*.json"]},
    include_package_data=True,
)
