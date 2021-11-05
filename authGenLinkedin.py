import requests
import string
import random
CLIENT_ID    = '78rer0f910lajx'
CLIENT_SECRET = 'qRQGjuI30HebJATM'
REDIRECT_URI = 'https://www.google.com'

# Generate a random string to protect against cross-site request forgery
letters = string.ascii_lowercase
CSRF_TOKEN = ''.join(random.choice(letters) for i in range(24))


# Request authentication URL
auth_params = {'response_type': 'code',
               'client_id': CLIENT_ID,
               'redirect_uri': REDIRECT_URI,
               'state': CSRF_TOKEN,
               'scope': 'r_liteprofile,r_emailaddress,w_member_social'}

html = requests.get("https://www.linkedin.com/oauth/v2/authorization",
                    params = auth_params)

# Print the link to the approval page
print(html.url)
# Click the link below to be taken to your redirect page.
