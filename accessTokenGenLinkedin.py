

import requests
import string
import random
import json
import os
import csv

CLIENT_ID    = '78rer0f910lajx'
CLIENT_SECRET = 'qRQGjuI30HebJATM'
REDIRECT_URI = 'https://www.google.com'

# Generate a random string to protect against cross-site request forgery
AUTH_CODE ='AQTW9HkKyC5-CLLyKp9Uy812kaGzwOsQxlZLPpeLHZfGZ5kPYZ67TQJCCI12R8QvzObWmHH6yehL3KgVk9H5YGHRZqifHhBvrRDut9z9YRrPd0Cy91ybKHaHslSCu5yeDYvInUSfhB9NX9IBmcnptF9KuGbAlbL8_YSJpyfozp4j2_oUmcJfxTwCIHiuwN0sYJHP4QMS_HtBV8GE-b0'
ACCESS_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'
qd = {'grant_type': 'authorization_code',
      'code': AUTH_CODE,
      'redirect_uri': REDIRECT_URI,
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET}

response = requests.post(ACCESS_TOKEN_URL, params=qd, timeout=60)

response = response.json()
print(response)
access_token = response['access_token']

print ("Access Token:", access_token)
print ("Expires in (seconds):", response['expires_in'])


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



CSV_FILE = os.path.join('./', 'resources', 'Connections.csv')

csvReader = csv.DictReader(open(CSV_FILE), delimiter=',', quotechar='"')
contacts = [row for row in csvReader]

workingAtGoogle = 0

for contact in contacts:
    for t in contact['Company'].split('/'):
        if (t == 'Google'):
            workingAtGoogle = workingAtGoogle+1
print('There are %d people who are working at Google.' % (workingAtGoogle))
