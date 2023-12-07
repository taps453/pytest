import pytest
''''
@pytest.fixture
def setup():
    print("Launch browser")
    print("Login")
    print("Browse products")
    print("Browser find")

def test_addItemtoCart(setup):
    print("Item added")

def test_RemoveItem(setup):
    print("removed item")

'''
# setup_and_teardown

'''
yield -
yield statement is often used to provide a setup and teardown mechanism.
When a fixture includes a yield statement, the code before the yield is
executed as setup, and the code after the yield is executed as teardown.
This allows you to perform actions before and after a test using a single
fixture.

'''
# @pytest.yield_fixture
@pytest.fixture
def setup():
    print("Launch browser")
    print("Login")
    yield
    print("Browse products")
    print("Browser find")

def test_addItemtoCart(setup):
    print("Item added")

def test_RemoveItem(setup):
    print("removed item")
