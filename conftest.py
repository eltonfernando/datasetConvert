import os
import pytest

@pytest.fixture(scope="session")
def environ():
    """
    environment variable used for pytest 
    """
    os.environ("TEST",True)