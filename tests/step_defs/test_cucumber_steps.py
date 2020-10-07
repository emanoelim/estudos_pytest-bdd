import pytest
from pytest_bdd import scenario, given, when, then, scenarios

from cucumbers import CucumberBasket


# @scenario('../features/cucumbers.feature', 'Add cucumbers to a basket', example_converters=dict(start=int, add=int, total=int))
# def test_add():
#     # tudo que estiver aqui será exceutado após todos os passos do cenário
#     pass
#
#
# @scenario('../features/cucumbers.feature', 'Add to many cucumbers to a basket', example_converters=dict(start=int, add=int, total=int))
# def test_add_to_many():
#     # tudo que estiver aqui será exceutado após todos os passos do cenário
#     pass
#
#
# @scenario('../features/cucumbers.feature', 'Remove cucumbers from a basket', example_converters=dict(start=int, remove=int, total=int))
# def test_remove():
#     # tudo que estiver aqui será exceutado após todos os passos do cenário
#     pass


CONVERTERS = {
    'start': int,
    'add': int,
    'remove': int,
    'total': int
}
scenarios('../features/cucumbers.feature', example_converters=CONVERTERS)


@pytest.fixture
@given("the basket has <start> cucumbers")
def basket(start):
    # usada com fixture para os outros passos
    return CucumberBasket(initial_count=start)


@when("<add> cucumbers are added to the basket")
def add_cucumbers(basket, add):
    basket.add(add)


@when("<remove> cucumbers are removed from the basket")
def remove_cucumbers(basket, remove):
    basket.remove(remove)


@then("the basket contains <total> cucumbers")
def basket_has_total(basket, total):
    assert basket.count == total
