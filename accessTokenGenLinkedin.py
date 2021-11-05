
# Click the link below to be taken to your redirect page.

AUTH_CODE ='AQSIJRddEThgthA7uBo7Mx3qo01Tl6kHFIXuZtXHpn9KUh0xX--j9eBnbsaV75yWUFOjwUwJn8vqFcEumuzpYIsbib0PQTFXgadnc9scsztq8pknjlkw4frVcGf74yBSSWg7zufjmLEstwWB-StCWWDI7RGva7s9nVJtt9PhYWOMw5kMHU6HNt2pCmrS02_WlGWrr2WQUIK219ObNjo'

ACCESS_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'

qd = {'grant_type': 'authorization_code',
      'code': AUTH_CODE,
      'redirect_uri': REDIRECT_URI,
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET}

response = requests.post(ACCESS_TOKEN_URL, data=qd, timeout=60)

response = response.json()
print(response)
access_token = response['access_token']

print ("Access Token:", access_token)
print ("Expires in (seconds):", response['expires_in'])

import json

params = {'oauth2_access_token': access_token}
response = requests.get('https://api.linkedin.com/v2/me', params = params)

print(json.dumps(response.json(), indent=1))

params = {'oauth2_access_token': access_token,
          'fields': ["localizedFirstName,localizedLastName,id"]}
response = requests.get('https://api.linkedin.com/v2/me', params = params)

print(json.dumps(response.json(), indent=1))

params = {'oauth2_access_token': access_token,
          'fields': ['lastName:(preferredLocale:(country,language))']}
response = requests.get('https://api.linkedin.com/v2/me', params = params)

print(json.dumps(response.json(), indent=1))

import os
import csv

CSV_FILE = os.path.join('./', 'resources', 'Connections.csv')

csvReader = csv.DictReader(open(CSV_FILE), delimiter=',', quotechar='"')
contacts = [row for row in csvReader]

workingAtGoogle = 0

for contact in contacts:
    for t in contact['Company'].split('/'):
        if (t == 'Google'):
            workingAtGoogle = workingAtGoogle+1
print('There are %d people who are working at Google.' % (workingAtGoogle))
