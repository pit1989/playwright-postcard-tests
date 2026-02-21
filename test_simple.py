import requests
import pytest

def test_get_trainer_info():

    url = "https://pokemonbattle.me:9104/trainers"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    print(data[0]['trainer_id'], data[0]['trainer_name'])

   