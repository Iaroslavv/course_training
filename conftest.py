import pytest
from interfaces import RequestsInterface

@pytest.fixture(scope='session')
def dogs_tracker():
    tracker = RequestsInterface('https://dog.ceo/api/')
    yield tracker
    del tracker

@pytest.fixture(scope='session')
def brewery_tracker():
    tracker = RequestsInterface('https://api.openbrewerydb.org/breweries/')
    yield tracker
    del tracker

@pytest.fixture(scope='session')
def json_tracker():
    tracker = RequestsInterface('https://jsonplaceholder.typicode.com/')
    yield tracker
    del tracker

@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope='session')
def status_code(request):
    return request.config.getoption("--status_code")

def pytest_addoption(parser):
    parser.addoption('--url', action='store', default="https://ya.ru")
    parser.addoption('--status_code', action='store', default=200)
