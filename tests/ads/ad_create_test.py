import json

import pytest
from rest_framework import status


@pytest.mark.django_db
def test_ad_create(api_client, user):
	data = {
		"name": "John",
		"author_id": user.id,
		"price": 10
	}

	response = api_client.post(
		"/ad/create/",
		data=json.dumps(data),
		content_type='application/json'
	)
	res_data = response.json()
	assert res_data['name'] == data['name']
	assert res_data['price'] == data['price']
	assert res_data['author'] == data['author']


@pytest.mark.django_db
def test_list_ad(api_client, ad):
	response = api_client.get("/ad/")
	assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_ad_by_id(api_client, ad):
	response = api_client.get('ad/<int:pk>/')
	assert response.status_code == status.HTTP_200_OK
	assert response.json()['id'] == ad.id
