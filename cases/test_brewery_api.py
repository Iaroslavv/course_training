import pytest

@pytest.mark.breweryapi
@pytest.mark.parametrize('city', ['san_diego', 'new_york', 'los_angeles'])
def test_get_brews_by_cities(brewery_tracker, city):
    api_response = brewery_tracker.send_data_api('get', f'?by_city={city}')
    assert city.replace('_', '-') in api_response[0]['id']

@pytest.mark.breweryapi
@pytest.mark.parametrize("page_num", [1, 20, 40, 50])
def test_get_brews_by_pages(brewery_tracker, page_num):
    api_response = brewery_tracker.send_data_api('get', f'?per_page={page_num}')
    assert len(api_response) == page_num

@pytest.mark.breweryapi
def test_get_max_brews_by_pages(brewery_tracker):
    api_response = brewery_tracker.send_data_api('get', '?per_page=51')
    assert len(api_response) == 50

@pytest.mark.breweryapi
def test_brews_by_sort_name(brewery_tracker):
    api_response = brewery_tracker.send_data_api('get', '?by_state=ohio&sort=name:asc')
    sorted_api_response = sorted(api_response, key=lambda item: item['name'])
    assert api_response == sorted_api_response

@pytest.mark.breweryapi
def test_brews_by_sort_desc_name(brewery_tracker):
    api_response = brewery_tracker.send_data_api('get', '?by_state=ohio&sort=name:desc')
    sorted_api_response = sorted(api_response, key=lambda item: item['name'], reverse=True)
    assert api_response == sorted_api_response
