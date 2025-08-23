import requests
import json
import string
import random

#base_url:
base_url = 'https://reqres.in'

#Auth Token:
auth_token = 'reqres-free-v1'

#GET Request
def get_request():
    url = base_url + '/api/users/2'
    #headers =
    response = requests.get(url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: ",json_str)

#POST Request
def post_request():
    url = base_url + '/api/users'
    headers = {"Authorization": auth_token}
    data = {
        "name": "Atul Singh",
        "job": "leader"
    }
    response = requests.post(url,json=data,headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: ", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Atul Singh"
    return user_id

#PUT Request
def put_request(user_id):
    url = base_url + f'/api/users/{user_id}'
    headers = {"Authorization": auth_token}
    data = {
        "name": "Atul Singh Automation",
        "job": "QA Engineer"
    }
    response = requests.put(url,json=data,headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Atul Singh Automation"

#Delete Request
def delete_request():
    url = base_url + '/api/users/2'
    headers = {"Authorization": auth_token}
    response = requests.delete(url,headers=headers)
    assert response.status_code == 204




#call_Function
#get_request()
#post_request()
#put_request()
delete_request()
