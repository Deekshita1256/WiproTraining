import pytest

@pytest.fixture(scope = 'function', autouse= True)
def setup_teardown():
    print('STARTING....')
    yield
    print('ENDING......')


