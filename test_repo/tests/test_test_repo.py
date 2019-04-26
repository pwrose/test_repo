"""
Unit and regression test for the test_repo package.
"""

# Import package, test suite, and other packages as needed
import test_repo
import pytest
import sys

def test_test_repo_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "test_repo" in sys.modules
