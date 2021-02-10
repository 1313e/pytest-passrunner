# -*- coding: utf-8 -*-

"""
Setup file for the *pytest-passrunner* plugin.

"""


# %% IMPORTS
# Built-in imports
from codecs import open
import re

# Package imports
from setuptools import find_packages, setup


# %% SETUP DEFINITION
# Get the long description from the README file
with open('README.rst', 'r') as f:
    long_description = f.read()

# Get the requirements list
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

# Read the __version__.py file
with open('pytest_passrunner/__version__.py', 'r') as f:
    vf = f.read()

# Obtain version from read-in __version__.py file
version = re.search(r"^_*version_* = ['\"]([^'\"]*)['\"]", vf, re.M).group(1)

# Setup function declaration
setup(name="pytest-passrunner",
      version=version,
      author="Ellert van der Velden",
      author_email='ellert_vandervelden@outlook.com',
      description=("Pytest plugin providing the 'run_on_pass' marker"),
      long_description=long_description,
      project_urls={
          'Source Code': "https://github.com/1313e/pytest-passrunner",
          },
      license='BSD-3',
      platforms=['Windows', 'Mac OS-X', 'Linux', 'Unix'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Utilities',
          'Framework :: Pytest'
          ],
      keywords=("pytest passrunner plugin marker"),
      python_requires='>=3.6, <4',
      packages=find_packages(),
      package_dir={'pytest_passrunner': "pytest_passrunner"},
      entry_points={
             'pytest11': [
                 "pytest_passrunner = pytest_passrunner"]},
      include_package_data=True,
      install_requires=requirements,
      zip_safe=False,
      )
