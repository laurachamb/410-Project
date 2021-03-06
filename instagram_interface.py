import requests, json, defines

# this function should be used to make any API call
# input: url: the first part of the API url (usually consists of the creds['endpoint_base'] and any edges)
#        endpointParams: and additional information like access_token or fields in a dictionary where the key is
#        the correct name
# output: dictionary with the json data returned by the API call
# Example: If you wanted to get the API for the follower count you would make an API call to
#          'https://graph.facebook.com/{graph-api-version}/{pageid}?fields=followers_count'
# Input:
#          url: https://graph.facebook.com/{graph-api-version}/{pageid}
#          endpointParams: endpointParams['access_token'] = {your-access-token} (this is always needed)
#                          endpointParams['fields'] = 'followers_count'
# Output: response['json_data'] = {
#                                   "followers_count": 1206,
#                                   "id": "1503119803264962"
#                                 }
#       key 'json_data_pretty' can be used for debugging
#       if printed it will show json data like above in nice formatting
def makeApiCall(url, endpointParams, debug='no'):
    data = requests.get(url, endpointParams)
    response = dict()
    response['url'] = url
    response['endpoint_params'] = json.dumps(endpointParams, indent=4)
    response['json_data'] = json.loads(data.content)
 #printing this will help with visualizing json data
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4 )

    return response


# used to get the instagram business account id
# not necessary to call more than once, this id is stored in the defines file
# stored in ig_page_id key in getCreds() dictionary
# Output: instagram business account id as a string
def instagramPageId():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['fields'] = 'instagram_business_account'
    url = url = params['endpoint_base'] + params['page_id']
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['instagram_business_account']['id']


# Gets the number of followers for the client's instagram account
# Output: number of followers as an integer
def igFollowers():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['fields'] = 'followers_count'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + params['ig_page_id']
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['followers_count']


# Gets the number of posts the client's instagram account has
# Output: The number of posts as an integer
def igPostCount():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['fields'] = 'media_count'
    url = params['endpoint_base'] + params['ig_page_id']
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['media_count']



# Total number of times the IG User's IG Media have been viewed.
# Includes ad activity generated through the API, Facebook ads interfaces, and the Promote feature.
# Does not include profile views.
# returns a dictionary with the number of impressions over multiple time periods
# Keys : 'day' for the number of impressions in the last day
#        'week' for the number of impressions in the last week
#        'days_28' for the number of impressions in the last 28 days
def impressions():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['metric'] = 'impressions'
    endpointParams['period'] = 'day,week,days_28'
    url = params['endpoint_base'] + params['ig_page_id'] + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    imp = dict()
    imp['day'] = response['json_data']['data'][0]['values'][0]['value']
    imp['week'] = response['json_data']['data'][1]['values'][0]['value']
    imp['days_28'] = response['json_data']['data'][2]['values'][0]['value']
    return imp


# Total number of unique users who have viewed at least one of the IG User's IG Media.
# Repeat views and views across different IG Media owned by the IG User by the same user are only counted as a single view.
# Includes ad activity generated through the API, Facebook ads interfaces, and the Promote feature.
# returns a dictionary with the number of  over multiple time periods
# Keys : 'day' for the total reach in the last day
#        'week' for the total reach in the last week
#        'days_28' for the total reach in the last 28 days
def reach():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['metric'] = 'reach'
    endpointParams['period'] = 'day,week,days_28'
    url = params['endpoint_base'] + params['ig_page_id'] + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    r = dict()
    r['day'] = response['json_data']['data'][0]['values'][0]['value']
    r['week'] = response['json_data']['data'][1]['values'][0]['value']
    r['days_28'] = response['json_data']['data'][2]['values'][0]['value']
    return r


# Total number of users who have viewed the IG User's profile within the specified period.
# returns a dictionary with the number of  over multiple time periods
# Keys : 'day' for the number of profile views in the last day
#        'week' for the number of profile views in the last week
#        'days_28' for the number of profile views in the last 28 days
def profileViews():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['metric'] = 'profile_views'
    endpointParams['period'] = 'day'
    url = params['endpoint_base'] + params['ig_page_id'] + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['data'][0]['values'][0]['value']


# Returns a list of dictionaries containing information for each post. Each element is for a different post going from
# most recent to least recent.
# Each dictionary contains keys for each piece of information.
# Keys: 'id' for the post id
#       'like_count' for the number of likes a post has
#       'comments_count' for the number of comments a post has
# Example: If you want to access the id of the most recent post you would access it as info[0]['id] where info is
# the variable you stored the array in
def mediaInfo():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['fields'] = 'business_discovery.username(' + params['ig_username'] + '){media{comments_count,like_count,timestamp}}'
    url = params['endpoint_base'] + params['ig_page_id']
    response = makeApiCall(url, endpointParams, params['debug'])
    info = []
    for id in response['json_data']['business_discovery']['media']['data']:
        info += [id]
    return info

# This returns a dictionary with post insights where the id of the post is passed in as an argument
# Keys: 'impressions' holds the total number of times the IG Media object has been seen
#       'reach' holds the total number of unique Instagram accounts that have seen the IG Media object
#       'engagement' hold the sum of likes_count, comment_count and saved counts on the IG Media
def postInsights( id ):
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['metric'] = 'impressions,reach,engagement'
    url = params['endpoint_base'] + str(id) + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    insights = dict()
    insights['impressions'] = response['json_data']['data'][0]['values'][0]['value']
    insights['reach'] = response['json_data']['data'][1]['values'][0]['value']
    insights['engagement'] = response['json_data']['data'][2]['values'][0]['value']
    return insights

