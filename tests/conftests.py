import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tests.factories import AdFactory, UserFactory, SelectionFactory
pytest_plugins = "tests.fixtures"

# Factories
register(AdFactory)
register(SelectionFactory)
register(UserFactory)


@pytest.fixture
def api_client(db, user):
	client = APIClient()
	token = RefreshToken.for_user(user)
	client.credentials(HTTP_AUTHORIZATION=f'Bearer{token.access_token}')
	return client
