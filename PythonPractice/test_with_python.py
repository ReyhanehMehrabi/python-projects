import pytest

from calculator import add, divide, double_divide, modulus, multiply, subtract
@pytest.yield_fixture(autouse=True, scope='session')
def test_suite_cleanup_thing():
    # setup
    yield
def test_add():
    result = add(5,8)

    assert 13 == result

