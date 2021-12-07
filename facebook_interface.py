import requests, json, defines
def makeApiCall(url, endpointParams, debug='no'):
    data = requests.get(url, endpointParams)
    response = dict()
    response['url'] = url
    response['endpoint_params'] = json.dumps(endpointParams, indent=4)
    response['json_data'] = json.loads(data.content)
# printing this will help with visualizing json data
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4 )

    return response

# gets page id for Facebook page
def pageId():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['user_access_token']
    url = params['endpoint_base'] + 'me/accounts'
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['data'][0]['id']

# returns a list of all post ids to help get post information
def postIds():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + 'me/posts'
    response = makeApiCall(url, endpointParams, params['debug'])
    ids = []
    for i in range(len(response['json_data']['data'])):
        d = dict()
        d['id'] = response['json_data']['data'][i]['id']
        d['timestamp'] = response['json_data']['data'][i]['created_time']
        ids += [d]
    return ids


# return page follower count
def follower_count():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['fields'] = 'followers_count'
    url = params['endpoint_base'] + params['page_id']
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['followers_count']

# The number of times any content from your Page or about your Page entered a person's screen.
# This includes posts, stories, ads, as well other content or information on your Page.
def getImpressions():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['metric'] = 'page_impressions'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + params['page_id'] + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    impressions = dict()
    for i in range(len(response['json_data']['data'])):
        if response['json_data']['data'][i]['period'] == 'day':
            impressions['day'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'week':
            impressions['week'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'days_28':
            impressions['days_28'] = response['json_data']['data'][i]['values'][1]['value']
    return impressions


# The number of people who had any content from your Page or about your Page enter their screen.
# This includes posts, stories, check-ins, ads, social information from people who interact with your Page and more.
def getUniqueImpressions():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['metric'] = 'page_impressions_unique'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + params['page_id'] + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    impressions = dict()
    for i in range(len(response['json_data']['data'])):
        if response['json_data']['data'][i]['period'] == 'day':
            impressions['day'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'week':
            impressions['week'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'days_28':
            impressions['days_28'] = response['json_data']['data'][i]['values'][1]['value']
    return impressions

# The number of times your Page's post entered a person's screen. Posts include statuses, photos, links, videos and more.
def getPostImpressions():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['metric'] = 'page_posts_impressions'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + params['page_id'] + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    impressions = dict()
    for i in range(len(response['json_data']['data'])):
        if response['json_data']['data'][i]['period'] == 'day':
            impressions['day'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'week':
            impressions['week'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'days_28':
            impressions['days_28'] = response['json_data']['data'][i]['values'][1]['value']
    return impressions

# The number of people who had your Page's post enter their screen. Posts include statuses, photos, links, videos and more.
def getUniquePostImpressions():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['metric'] = 'page_posts_impressions_unique'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + params['page_id'] + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    impressions = dict()
    for i in range(len(response['json_data']['data'])):
        if response['json_data']['data'][i]['period'] == 'day':
            impressions['day'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'week':
            impressions['week'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'days_28':
            impressions['days_28'] = response['json_data']['data'][i]['values'][1]['value']
    return impressions

# The number of people who engaged with your Page. Engagement includes any click.
def engagedUsers():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['metric'] = 'page_engaged_users'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + params['page_id'] + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    users = dict()
    for i in range(len(response['json_data']['data'])):
        if response['json_data']['data'][i]['period'] == 'day':
            users['day'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'week':
            users['week'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'days_28':
            users['days_28'] = response['json_data']['data'][i]['values'][1]['value']
    return users


#
def pageViews():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['metric'] = 'page_views_total'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + params['page_id'] + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    views = dict()
    for i in range(len(response['json_data']['data'])):
        if response['json_data']['data'][i]['period'] == 'day':
            views['day'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'week':
            views['week'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'days_28':
            views['days_28'] = response['json_data']['data'][i]['values'][1]['value']
    return views


# The number of times people have engaged with your posts through reactions, comments, shares and more.
def totalPostEngagement():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['metric'] = 'page_post_engagements'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + params['page_id'] + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    engagements = dict()
    for i in range(len(response['json_data']['data'])):
        if response['json_data']['data'][i]['period'] == 'day':
            engagements['day'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'week':
            engagements['week'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'days_28':
            engagements['days_28'] = response['json_data']['data'][i]['values'][1]['value']
    return engagements


# The number of times people took a negative action (e.g., un-liked or hid a post).
def negativeFeedback():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['metric'] = 'page_negative_feedback'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + params['page_id'] + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    neg = dict()
    for i in range(len(response['json_data']['data'])):
        if response['json_data']['data'][i]['period'] == 'day':
            neg['day'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'week':
            neg['week'] = response['json_data']['data'][i]['values'][1]['value']
        if response['json_data']['data'][i]['period'] == 'days_28':
            neg['days_28'] = response['json_data']['data'][i]['values'][1]['value']
    return neg


# post likes for a specific post
# likes for Facebook since they have many positive reactions will be like, love, and wow reactions
def getPostLikes( postId ):
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['metric'] = 'post_reactions_like_total,post_reactions_love_total,post_reactions_wow_total'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + postId + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
    likes = response['json_data']['data'][0]['values'][0]['value']
    loves = response['json_data']['data'][1]['values'][0]['value']
    wows = response['json_data']['data'][2]['values'][0]['value']
    return likes + loves + wows


# gets total likes for last num posts
def getMultiplePostLikes( num ):
    ids = postIds()
    total = 0
    for id in ids[:num]:
        total += getPostLikes(id)
    return total

def longLivedAccessToken():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['grant_type'] = 'fb_exchange_token'  # tell facebook we want to exchange token
    endpointParams['client_id'] = params['client_id']  # client id from facebook app
    endpointParams['client_secret'] = params['client_secret']  # client secret from facebook app
    endpointParams['fb_exchange_token'] = params['page_access_token']  # access token to get exchange for a long lived token
    url = params['endpoint_base'] + 'oauth/access_token'
    response = makeApiCall(url , endpointParams)

ids = postIds()
print(ids[0]['timestamp'])
