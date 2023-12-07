# How to Group the test cases -

import pytest

def test_loginpage():
    print("Login successful")

def test_logoff():
    print("Logoff")

@pytest.mark.sanity
def test_addition():
    assert 2+2 == 4