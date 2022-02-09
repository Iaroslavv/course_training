import pytest
from jsonschema import validate

@pytest.mark.dogsapi
def test_get_all_breeds(dogs_tracker):
    api_response = dogs_tracker.send_data_api('get', 'breeds/list/all')
    json_schema = {
        "type" : "object",
        "properties": {
            "message":{"type":"object"},
            "status":{"type":"string"},
        },
        "required":["message", "status"]
    }
    validate(instance=api_response, schema=json_schema)

@pytest.mark.dogsapi
def test_get_random_dog(dogs_tracker):
    api_response = dogs_tracker.send_data_api('get', 'breeds/image/random')
    assert len(api_response) == 2

@pytest.mark.dogsapi
@pytest.mark.parametrize("num", [1,19,40,50, pytest.param(51, marks=pytest.mark.xfail)])
def test_get_breed(dogs_tracker, num):
    api_response = dogs_tracker.send_data_api('get', f'breeds/image/random/{num}')
    assert len(api_response.get('message')) == num

@pytest.mark.dogsapi
@pytest.mark.parametrize('breed', ['hound', 'husky', 'keeshond', 'newfoundland'])
def test_get_dogs_by_breed(dogs_tracker, breed):
    api_response = dogs_tracker.send_data_api('get', f'breed/{breed}/images')
    assert all(breed for breed in api_response['message'])

@pytest.mark.dogsapi
@pytest.mark.parametrize('breed', ['hound', 'husky', 'keeshond', 'newfoundland'])
def test_random_image_breed_collection(dogs_tracker, breed):
    api_response = dogs_tracker.send_data_api('get', f'breed/{breed}/images/random')
    assert breed in api_response['message']