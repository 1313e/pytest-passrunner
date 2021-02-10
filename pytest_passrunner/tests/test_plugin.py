# -*- coding: utf-8 -*-

# %% GLOBALS
# Set which additional pytest plugins to use
pytest_plugins = ['pytester']


# %% PYTEST CLASSES AND FUNCTIONS
# Test if the default use of the marker works
def test_default(testdir):
    # Create a temporary test file
    testdir.makepyfile(
        """
        import pytest

        @pytest.mark.run_on_pass
        class Test(object):
            def test_a(self):
                pass

            def test_b(self):
                raise Exception

            def test_c(self):
                pass
        """)

    # Run tests
    result = testdir.runpytest()

    # Check if one passed, one failed and one xfailed
    result.assert_outcomes(passed=1, failed=1, xfailed=1)
