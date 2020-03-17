#!/usr/bin/env python

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
    scripts=["bin/chfn", "bin/chsh"],  # possible hack to install perl scripts.
    entry_points={
        "console_scripts": [
            "rbquota = rbquota.__main__:main",
            "rbusers = rbusers.__main__:main",
        ],
    },
)
