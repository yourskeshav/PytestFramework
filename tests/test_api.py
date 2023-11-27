import pytest
import requests

@pytest.mark.apitest
def test_API_get_request():

    base_url = "https://rahulshettyacademy.com/maps/api/place/get/json?key=qaclick123&place_id=a8a4c575523f5b255650166340190e2e"
    response = requests.get(base_url)
    assert response.status_code ==200
    print("response that is printed",response.text)

    json_response = response.json()
    assert 'latitude' in json_response['location']
    assert 'longitude' in json_response['location']

    # Check if the 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', and 'language' fields exist
    assert 'accuracy' in json_response
    assert 'name' in json_response
    assert 'phone_number' in json_response
    assert 'address' in json_response
    assert 'types' in json_response
    assert 'website' in json_response
    assert 'language' in json_response

    # You can also check specific values
    assert json_response['location']['latitude'] == "-38.383494"
    assert json_response['location']['longitude'] == "33.427362"
    assert json_response['name'] == "Frontline house"
    assert json_response['address'] == "70 winter walk, USA"

@pytest.mark.apitest
def test_api_post_request():
    base_url = "https://rahulshettyacademy.com/maps/api/place/add/json?key=qaclick123"

    post_data = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }



    response = requests.post(base_url,json=post_data)

    assert response.status_code ==200

    print("reponse body:")
    print(response.text)

