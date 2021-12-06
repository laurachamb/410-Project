import requests
import json

def getCreds():
    creds = dict()
    #empty values should be generated/accessed through the facebook developer account
    creds['user_access_token'] = 'EAAI3fQapZATcBANavKcIGQcut5dH45y01mMNvdrmS2go96qEP8PfXdKcUqChnO57g9UwKoPFZC8qkv5I1KZB8zBiAdg0MbVVWgUfXZBoDefjaZA6uD9PbgMCc48FMvA3eFpLEyWbZAH3yJ2AZARIH5yVJYmy9ZAs9DgRJQ96nduHkQZDZD'
    creds['page_access_token'] = 'EAAI3fQapZATcBALvcDr7oIZAOF7DcNZCA3xIVGXdfewUzHNklltFY78k08IoHolZAR0B0TIXtO0yurHL3epDesxrdmjuh44y652fACrBYYjOgm9N1ZAqCd4qp5ZAPJMoXtT7xKgTv1rtuaFKZAp9RpxwUjakrYrRLMu7hEB3AJikoebOSPJHVLx'
    creds['client_id'] = '623960075625783'
    creds['client_secret'] = ''
    creds['ig_username'] = 'impactfinctr'

    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v12.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['page_id'] = '1503119803264962'
    creds['ig_page_id'] = '17841404219581713'
    return creds
