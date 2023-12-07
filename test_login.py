import pytest

def test_loginpage():
    print("Login successful")

@pytest.mark.sanity
def test_logoff():
    print("Logoff")

def test_addition():
    assert 2+5 == 7