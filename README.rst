|PyPI| |Python| |GitHub|

*pytest-passrunner*: A Pytest plugin that provides the 'run_on_pass' marker
===========================================================================
The *pytest-passrunner* plugin for Pytest introduces a new marker called `run_on_pass`, which can be used to mark an entire test suite to only run a test if all previous tests in it passed successfully.
This allows for the user to use test structures, where previous tests setup future ones.
If previous tests were to fail, the future ones cannot run properly, and thus should be 'xfailed' (expected failure) instead of attempted anyway.
See below for some examples.


Installation & Use
==================
How to install
--------------
*pytest-passrunner* can be easily installed directly from `PyPI`_ with::

    $ pip install pytest-passrunner

If required, one can also clone the `repository`_ and install *pytest-passrunner* manually::

    $ git clone https://github.com/1313e/pytest-passrunner
    $ cd pytest-success
    $ pip install .

The `run_on_pass` marker can now be used in tests with `pytest.mark.run_on_pass`.

.. _repository: https://github.com/1313e/pytest-passrunner
.. _PyPI: https://pypi.org/project/pytest-passrunner

Example use
-----------
The `run_on_pass` marker, when used on a Pytest suite, marks all tests in the suite to solely run if all previous tests in the suite passed.
Another way of saying this is that if a test in a marked test suite fails, all remaining tests are automatically flagged as 'xfail' (expected fail) and do not run.

One use-case of this marker is when you want to write a test suite, where a specific object is being modified throughout the tests.
In this scenario, it is not uncommon that a particular test in the test suite can only run correctly if all previous tests passed, as otherwise the object is not in the expected state.
The following illustrates this scenario:

.. code:: python

    # Import pytest
    import pytest


    # Define Pytest suite
    class Test_list(object):
        # Create fixture that is shared between all tests in the suite
        # In this case, a list object
        @pytest.fixture(scope='class')
        def lst(self):
            # Create empty list
            lst = []

            # Return it
            return(lst)

        # Perform test that sets up this list
        def test_1(self, lst):
            # Append 1 to the list
            lst.append(1)

            # Test that 1 was appended
            assert lst == [1]

        # Perform test that requires lst to be [1]
        def test_2(self, lst):
            # Append 2 to the list
            lst.append(2)

            # Test that 1 and 2 are in the list now
            assert lst == [1, 2]

In this simple test script, a list object is being shared between all the tests in the `Test_list` test suite.
In the second test, `test_2`, it is assumed that this list object was correctly set up by the first test.
If `test_1` were to fail for whatever reason, `test_2` cannot possibly pass anymore, as the list object was never set up properly.
However, `test_2` (and any further tests after it) will still be ran, wasting time and cluttering the final pytest summary overview with unhelpful errors.

In order to solve this, we can apply the `run_on_pass` marker:

.. code:: python

    # Import pytest
    import pytest


    # Define Pytest suite with the 'run_on_pass' marker
    @pytest.mark.run_on_pass
    class Test_list(object):
        # Create fixture that is shared between all tests in the suite
        # In this case, a list object
        @pytest.fixture(scope='class')
        def lst(self):
            # Create empty list
            lst = []

            # Return it
            return(lst)

        # Perform test that sets up this list
        def test_1(self, lst):
            # Append 1 to the list
            lst.append(1)

            # Test that 1 was appended
            assert lst == [1]

        # Perform test that requires lst to be [1]
        def test_2(self, lst):
            # Append 2 to the list
            lst.append(2)

            # Test that 1 and 2 are in the list now
            assert lst == [1, 2]

If now the execution of `test_1` fails, `test_2` (and any further tests after it in this test suite) will not be ran and be flagged as 'xfail' instead.
Tests that are xfailed do not generate any error messages in the pytest summary overview and are not seen as failed/errored tests either.
This keeps the summary cleaner, and no time is wasted on tests that cannot pass.


.. |PyPI| image:: https://img.shields.io/pypi/v/pytest-passrunner.svg?logo=pypi&logoColor=white&label=PyPI
    :target: https://pypi.python.org/pypi/pytest-passrunner
    :alt: PyPI - Latest Release
.. |Python| image:: https://img.shields.io/pypi/pyversions/pytest-passrunner?logo=python&logoColor=white&label=Python
    :target: https://pypi.python.org/pypi/pytest-passrunner
    :alt: PyPI - Python Versions
.. |GitHub| image:: https://img.shields.io/github/workflow/status/1313e/pytest-passrunner/Test?logo=github&logoColor=white&label=Actions
    :target: https://github.com/1313e/pytest-passrunner/actions
    :alt: GitHub Actions - Build Status
