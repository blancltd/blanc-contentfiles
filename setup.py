#!/usr/bin/env python
from codecs import open

from setuptools import find_packages, setup


with open("README.rst", "r", "utf-8") as f:
    readme = f.read()


setup(
    name="devsoc-contentfiles",
    version="0.2.6",
    description="DEV Content Files",
    long_description=readme,
    url="https://github.com/developersociety/devsoc-contentfiles",
    maintainer="The Developer Society",
    maintainer_email="studio@dev.ngo",
    platforms=["any"],
    packages=find_packages(),
    python_requires=">=3.5",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.2",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license="BSD",
)
