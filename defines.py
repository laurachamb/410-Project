import requests
import json

def getCreds():
    creds = dict()
    #empty values should be generated/accessed through the facebook developer account
    creds['user_access_token'] = ''
    creds['page_access_token'] = ''
    creds['client_secret'] = '●●●●●●●●'
    creds['ig_username'] = 'impactfinctr'

    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v12.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['page_id'] = '1503119803264962'
    creds['ig_page_id'] = '17841404219581713'
    return creds
