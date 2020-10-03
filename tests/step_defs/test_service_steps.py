import pytest
import requests

from pytest_bdd import scenario, given, then, parsers

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'

@scenario('../features/service.feature', 'Basic DuckDuckGo API Query', example_converters=dict(phrase=str))
def test_init():
    # tudo que estiver aqui será exceutado após todos os passos do cenário
    pass

@pytest.fixture
@given('the DuckDuckGo API is queried with "<phrase>"')
def ddg_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response

@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code

@then('the response contains results for "<phrase>"')
def ddg_response_contents(ddg_response, phrase):
    assert phrase.lower() == ddg_response.json()['Heading'].lower()