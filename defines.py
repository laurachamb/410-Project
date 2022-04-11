import requests
import json


# Returns a dictionary with information to help make API calls for facebook and instagram
# Keys: page_access_token: stores the access token that contains all of the permissions we need to access information
#                          on this facebook/instagram page
#                          this is a long-lived access token and needs to be replaced every 3 months
#       client_id: id for the facebook app we have created, can be found on the facebook developer account
#       client_secret: secret for the facebook app we have created, can be found on the facebook developer account
#       ig_username: instagram username for the client
#       graph_domain: every API call starts with 'https://graph.facebook.com/' so we stored it in graph_domain to reduce
#                     repetition
#       graph_version: there are different versions of the graph API and it also needs to be passed into the url for
#                      most API calls so we stored it in our dictionary to remain consistent
#       endpoint_base: combination of graph domain and graph version, this is used as the first part of the url for
#                      most API calls
#       debug: no for if you don't want to debug, yes if you do
#       page_id: page id for facebook page, stored so we don't have to make that API call multiple times
#       ig_page_id: busniess account id for instagram account, stored so we don't have to make that API call multiple times
def getCreds():
    creds = dict()
    creds['page_access_token'] = ''
    creds['client_id'] = ''
    creds['client_secret'] = ''
    creds['ig_username'] = 'impactfinctr'

    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v12.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['page_id'] = '1503119803264962'
    creds['ig_page_id'] = '17841404219581713'
    return creds
