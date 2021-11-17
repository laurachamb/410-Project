import requests, json, defines


def makeApiCall(url, endpointParams, debug='no'):
    data = requests.get(url, endpointParams)
    response = dict()
    response['url'] = url
    response['endpoint_params'] = json.dumps(endpointParams, indent=4)
    response['json_data'] = json.loads(data.content)
 #printing this will help with visualizing json data
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4 )

    return response


# needs to be updated
def instagramPageId():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    url = url = params['endpoint_base'] + "/me/instagram_accounts"
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['data'][0]['id']



def igFollowers():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['fields'] = 'followed_by_count'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + params['ig_page_id']
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['followed_by_count']


def igPostCount():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['fields'] = 'media_count'
    url = params['endpoint_base'] + params['ig_page_id']
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['media_count']


#def media():
#    params = defines.getCreds()
#    endpointParams = dict()
#   endpointParams['access_token'] = params['page_access_token']

id = instagramPageId()
print('Page id: ' + str(id))
followers = igFollowers()
print('Followers: ' + str(followers))
posts = igPostCount()
print('Number of Posts: ' + str(posts))

