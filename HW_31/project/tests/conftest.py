from pytest_factoryboy import register

from tests.factories import *

pytest_plugins = "tests.fixtures"

register(UserFactory)
register(CatFactory)
register(AdFactory)
