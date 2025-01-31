"""
The Flask micro-framework uses decorators to define its routes:

http://flask.pocoo.org/

The goal of this exercise is to build a simplified version of this routing system.
"""

import pytest

from pythonist.flask_ingles.app import RouteNotFound, route, route_dispatch


# Fixture to create a user route
@pytest.fixture(scope='session')
def user():
    """
    Registers the '/user'route and defines a function
    that saves a user's name
    """
    @route('/user')
    def user_route(name):
        return f'saving {name}'

    return user_route


# Fixture to create a car route
@pytest.fixture(scope='session')
def car():
    """
    Registers the '/car' route and defines a function
    that describes a car with its name and year
    """
    @route('/car')
    def car_route(name, year):
        return f'{name} year {year}'

    return car_route


def test_execution_without_parameter():
    """
    Tests if the home route is executed through the route_dispatch
    function after being mapped to the '/' path
    """
    @route('/')
    def home():
        return 'home executed'

    assert home() == route_dispatch('/') == 'home executed'


def test_execution_with_positional_parameter(user):
    """
    Tests if the '/user' route is executed correctly with a positional argument.
    """
    assert user('Matheus') == route_dispatch('/user', 'Matheus') == 'saving Matheus'


def test_execution_with_named_parameter(user):
    """
    Tests if the '/user' route is executed correctly with a named argument.
    """
    assert user('Foo') == route_dispatch('/user', name='Foo') == 'saving Foo'


def test_execution_with_positional_parameters(car):
    """
    Tests if the '/car' route is executed correctly with two positional arguments.
    """
    assert car('Fusca', 88) == route_dispatch('/car', 'Fusca', 88) == 'Fusca year 88'


def test_execution_with_named_parameters(car):
    """
    Tests if the '/car' route is executed correctly with named arguments.
    """
    assert car('Gol', 2000) == route_dispatch('/car', year=2000, name='Gol') == 'Gol year 2000'


def test_execution_with_positional_and_named_parameter(car):
    """
    Tests if the '/car' route is executed correctly with two positional arguments.
    """
    assert car('Celta', 99) == route_dispatch('/car', 'Celta', 99) == 'Celta year 99'


def test_incorrect_parameters():
    """
    Tests if calling a route without required parameters raises a TypeError.
    """
    with pytest.raises(TypeError):
        route_dispatch('/car')


def test_non_existent_route():
    """
    Tests if calling a non-existent route raises a RouteNotFound exception.
    """
    with pytest.raises(RouteNotFound) as excinfo:
        route_dispatch('/nonexistent')

    assert str(excinfo.value) == 'Route not found: /nonexistent'
