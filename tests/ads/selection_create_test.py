import json

import pytest
from rest_framework import status


@pytest.mark.django_db
def test_selection_create(api_client, user, ad):

    data = {
        "owner": user.id,
        "name": "Test selection",
        "items": [ad.id]
    }


    response = api_client.post(
        "/selection/create/",
        data=json.dumps(data),
        content_type='application/json',
    )
    res_data = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert res_data['name'] == data['name']
    assert res_data['owner'] == data['owner']
