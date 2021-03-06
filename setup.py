#!/usr/bin/env python
import versioneer

from pathlib import Path

from setuptools import setup, find_packages


PROJECT_ROOT = Path(__file__).resolve().parent
REQUIREMENTS_FILE = PROJECT_ROOT / "requirements.txt"
README_FILE = PROJECT_ROOT / "README.md"
VERSION_FILE = PROJECT_ROOT / "symbolic_pymc" / "__init__.py"

NAME = "symbolic-pymc"
DESCRIPTION = "Tools for symbolic math in PyMC"
AUTHOR = "PyMC Developers"
AUTHOR_EMAIL = "pymc.devs@gmail.com"
URL = ("https://github.com/pymc-devs/symbolic-pymc",)


def get_long_description():
    with open(README_FILE, "rt") as buff:
        return buff.read()


setup(
    name=NAME,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=[
        "numpy>=1.18.1",
        "scipy>=1.4.0",
        "Theano>=1.0.4",
        "tf-estimator-nightly==2.1.0.dev2020012309",
        "tf-nightly==2.2.0.dev20200301",
        "tfp-nightly==0.10.0.dev20200201",
        "multipledispatch>=0.6.0",
        "logical-unification>=0.4.3",
        "miniKanren>=1.0.1",
        "etuples>=0.3.2",
        "cons>=0.4.0",
        "toolz>=0.9.0",
        "cachetools",
        "pymc3>=3.6",
        "pymc4 @ git+https://github.com/pymc-devs/pymc4.git@master#egg=pymc4-0.0.1",
    ],
    packages=find_packages(exclude=["tests"]),
    tests_require=["pytest"],
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
    ],
)
