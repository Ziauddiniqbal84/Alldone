# Automated the Twitter API using Requests Module in python.
# Did three get requests.

import base64
import requests

client_key = 'YdGt64nv79VCU1cNraIN4dTnI'
client_secret = '4jrVN4PDLKI0Vm8czc6sJLh9gurhVoaAoO3J430nLetZGLS0Ap'

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

# to get the bearer token.
auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
print(auth_resp.json().keys())
access_token = auth_resp.json()['access_token']  # it will display the access token.


# first get request.  to retrieve the information about the word elections.

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_params = {
    'q': 'elections',
    'result_type': 'recent',
    'count': 2
}

search_url = '{}1.1/search/tweets.json'.format(base_url)
search_resp = requests.get(search_url, headers=search_headers, params=search_params)
print(search_resp.status_code)
tweet_data = search_resp.json()
print(search_resp.url)
for x in tweet_data['statuses']:
    print(x['text'] + '\n')


# GET /2/users
Url = '{}2/users'.format(base_url)
search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

id = ('790159376992595968', '447977892')
payloads = {'ids':','.join(id)}

response_users = requests.get(Url,headers = search_headers,params=payloads)
print(response_users.status_code)
print(response_users.json())
print(response_users.url)

# GET /2/users/:id/followers
#Returns a list of users who are followers of the specified user ID.

Url = '{}2/users/790159376992595968/followers'.format(base_url)
search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

payloads={'max_results':10}

response_users = requests.get(Url,headers = search_headers,params =payloads)
print(response_users.status_code)
print(response_users.json())
print(response_users.url)

