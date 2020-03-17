#!/usr/bin/env python
"""install rb user scripts"""

from setuptools import find_namespace_packages, setup

setup(
    name="rb-user-scripts",
    version="1.0",
    description="Redbrick Scripts for users",
    author="Redbrick",
    author_email="admins@redbrick.dcu.ie",
    url="https://github.com/redbrick/user-scripts",
    install_requires=["utmp"],
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    # possible hack to install perl and bash scripts.
    scripts=[
        "bin/perl/chfn",
        "bin/perl/chsh",
        "bin/bash/noforward",
        "bin/bash/nohelp",
        "bin/bash/nopermwarn",
        "bin/bash/news",
        "bin/bash/usenet",
    ],
    entry_points={
        "console_scripts": [
            "rbquota = rbquota.__main__:main",
            "rbusers = rbusers.__main__:main",
            "help = help.__main__:main",
        ],
    },
)
