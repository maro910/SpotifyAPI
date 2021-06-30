import requests
import spotipy

CLIENT_ID = '3e41ad3ebb614ccb8dbea32352b448b2'
CLIENT_SECRET = '47683e1c9c8f4f989da1418fcd318017'

AUTH_URL = 'https://accounts.spotify.com/api/token'

#Post
auth_response = requests.post(AUTH_URL, {
  'grant_type': 'client_credentials', 
  'client_id' : CLIENT_ID,
  'client_secret' : CLIENT_SECRET, #this might be an extra comma
})

print(auth_response.status_code)

auth_response_data = auth_response.json()
print(auth_response_data)

access_token = auth_response_data['access_token']
headers = {
  'Authorization' : 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'
track_id = '6mFkJmJqdDVQ1REhVfGgd1'

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

r = r.json()
print(r)