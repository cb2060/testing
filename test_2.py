import pytest


@pytest.fixture
def initialize():
    print('\nsetting up')
    yield 'some value'
    print('\nclosing down')


def test_this(initialize):
    print(initialize)
