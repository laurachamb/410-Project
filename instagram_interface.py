import requests, json, defines


def makeApiCall(url, endpointParams, debug='no'):
    data = requests.get(url, endpointParams)
    response = dict()
    response['url'] = url
    response['endpoint_params'] = json.dumps(endpointParams, indent=4)
    response['json_data'] = json.loads(data.content)
 #printing this will help with visualizing json data
   # response['json_data_pretty'] = json.dumps(response['json_data'], indent=4 )

    return response


def pageId():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    url = params['endpoint_base'] + 'me/accounts'
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['data'][0]['id']


def instagramPageId():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    endpointParams['fields'] = 'instagram_business_account'

    url = params['endpoint_base'] + str(pageId())
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['instagram_business_account']['id']



def igFollowers():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    endpointParams['fields'] = 'business_discovery.username(' + params['ig_username'] + '){follower_count}'
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + str(instagramPageId())
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['business_discovery']['follower_count']


def ifPostCount():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    endpointParams['fields'] = 'business_discovery.username(' + params['ig_username'] + '){media_count}'
    endpointParams['access_token'] = params['access_token']
    url = params['endpoint_base'] + '/'+ str(instagramPageId())
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['business_discovery']['media_count']
    return response['json_data']['business_discovery']['media_count']
