# -*- coding: utf-8 -*-

"""
pytest-passrunner
=================
Pytest plugin providing the 'run_on_pass' marker.

"""


# %% IMPORTS AND DECLARATIONS
# pytest-passrunner imports
from .__version__ import __version__

# Package imports
import _pytest
import pytest

# All declaration
__all__ = []

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"


# %% PYTEST CONFIGURATION
# Add the run_on_success marker
def pytest_configure(config):
    config.addinivalue_line("markers",
                            "run_on_pass: Mark test suite to xfail all "
                            "remaining tests when one fails.")


# This introduces a marker that auto-fails tests if a previous one failed
def pytest_runtest_makereport(item, call):
    if "run_on_pass" in item.keywords:
        if(call.excinfo is not None and
           call.excinfo.type is not _pytest.outcomes.Skipped):
            parent = item.parent
            parent._previousfailed = item


# This makes every marked test auto-fail if a previous one failed as well
def pytest_runtest_setup(item):
    if "run_on_pass" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("Previous test failed (%s)" % (previousfailed.name))
