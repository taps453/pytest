import pytest

#pytest.fixture() allows you to parametrize fixture functions

@pytest.fixture(params=["a", "b"])
def demo_fixture(request):
    print(request.param)

def test_demo(demo_fixture):
    print("login successful")

    

#pytest.amrk.parametrize is for parametrize the functions

@pytest.mark.parametrize("a, b, final" ,[(2, 7, 9),(4,5,9),(2,3,5)])
def test_login(a,b,final):
    assert a+b == final


