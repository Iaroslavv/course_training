from base_interface import load_data_from_file

import pytest


@pytest.mark.jsonapi
def test_get_resource_by_id(json_tracker):
    reference_dict = {
        'userId': 1,
        'id': 1,
        'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
        'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
        }

    api_response = json_tracker.send_data_api('get', 'posts/1')
    assert api_response == reference_dict

@pytest.mark.jsonapi
def test_get_all_resources(json_tracker):
    api_response = json_tracker.send_data_api('get', 'posts')
    assert len(api_response) == 100

@pytest.mark.jsonapi
def test_post_resource(json_tracker):
    reference_dict = {
        "title": "Title number one",
        "body": "Let's say it is an empty body ",
        "userId": 1,
        "id": 101
    }
    api_response = json_tracker.send_data_api('post', 'posts', load_data_from_file('post_data.json'))
    assert reference_dict == api_response

@pytest.mark.jsonapi
@pytest.mark.parametrize('user_id', [1,2,5,8,10])
def test_get_resource_by_userid(json_tracker, user_id):
    api_response = json_tracker.send_data_api('get', f'posts?userId={user_id}')
    assert api_response[0]['userId'] == user_id

@pytest.mark.jsonapi
@pytest.mark.parametrize('post_id', [2, 5, 9, 55, 99, 100])
def test_get_resource_by_ids(json_tracker, post_id):
    api_response = json_tracker.send_data_api('get', f'posts/{post_id}')
    assert api_response['id'] == post_id