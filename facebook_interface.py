import requests, json, defines
import datetime

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
# printing this will help with visualizing json data
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4 )

    return response


# Returns a dictionary of information on our access token
# The important key to us is 'expires_at': stores when the access token expires
# The value stored here can be converted to a readable time with datetime.datetime.fromtimestamp( value )
# Values is that number stored at key 'expires_at'
def debugAccessToken():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['input_token'] = params['page_access_token']
    endpointParams['access_token'] = params['page_access_token']
    url = params['graph_domain'] + '/debug_token'
    response = makeApiCall(url, endpointParams, params['debug'])
    return response



# Output: a list of post ids as strings from most recent to least recent
# This can be used in functions like getPostLikes( id ) where you can pass in the string and get the likes if that
# post back
# Example use: If you want the most recent post id, call function:
#               ids = postIds()
#               ids[0] will have the most recent post id
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


# Output: returns the follower count of this Facebook account as an integer
def follower_count():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['fields'] = 'followers_count'
    url = params['endpoint_base'] + params['page_id']
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['followers_count']

# Impressions: The number of times any content from your Page or about your Page entered a person's screen.
# This includes posts, stories, ads, as well other content or information on your Page.
# Output: a dictionary with three keys
#        Keys: 'day' stores the impressions over the last day
#              'week' stores the impressions over the last week
#              'days_28' stores the impressions over the last 28 days
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


# Unique Impressions: The number of people who had any content from your Page or about your Page enter their screen.
# This includes posts, stories, check-ins, ads, social information from people who interact with your Page and more.
# Output: a dictionary with three keys
#        Keys: 'day' stores the unique impressions over the last day
#              'week' stores the unique impressions over the last week
#              'days_28' stores the unique impressions over the last 28 days
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

# Post Impressions: The number of times your Page's post entered a person's screen.
# Posts include statuses, photos, links, videos and more.
# Output: a dictionary with three keys
#        Keys: 'day' stores the post impressions over the last day
#              'week' stores the post impressions over the last week
#              'days_28' stores the post impressions over the last 28 days
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

# Unique Post Impressions: The number of people who had your Page's post enter their screen.
# Posts include statuses, photos, links, videos and more.
# Output: a dictionary with three keys
#        Keys: 'day' stores the unique post impressions over the last day
#              'week' stores the unique post impressions over the last week
#              'days_28' stores the unique post impressions over the last 28 days
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

# Engaged Users: The number of people who engaged with your Page. Engagement includes any click.
# Output: a dictionary with three keys
#        Keys: 'day' stores the engaged users over the last day
#              'week' stores the engaged users over the last week
#              'days_28' stores the engaged users over the last 28 days
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


# Page Views: The number of times a Page has been viewed by logged-in and logged-out people.
# Output: a dictionary with three keys
#        Keys: 'day' stores the page views over the last day
#              'week' stores the page views over the last week
#              'days_28' stores the page views over the last 28 days
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


# Post Engagement: The number of times people have engaged with your posts through reactions, comments, shares and more.
# Output: a dictionary with three keys
#        Keys: 'day' stores the post engagement over the last day
#              'week' stores the post engagement over the last week
#              'days_28' stores the post engagement over the last 28 days
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


# Negative Feedback: The number of times people took a negative action (e.g., un-liked or hid a post).
# Output: a dictionary with three keys
#        Keys: 'day' stores the negative feedback over the last day
#              'week' stores the negative feedback over the last week
#              'days_28' stores the negative feedback over the last 28 days
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


# Post likes for a specific post
# Likes for Facebook since they have many positive reactions will be like, love, and wow reactions.
# Input: the id of the post id you want the like count for passed in as a string
# Output: The number of positive reactions on that post as an integer
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


# Gets the sum of likes over the last specified number of posts
# Input: num is the number of posts you would like to see the likes for
#        Facebook only saves post information over the past 2 years so num will be reset to the number of posts saved
#        if num is greater than the number of posts saved
def getMultiplePostLikes( num ):
    ids = postIds()
    if num > len(ids):
        num = len(ids)
    total = 0
    for id in ids[:num]:
        total += getPostLikes(id)
    return total

# Allows you to get a long lived access token with a short-lived access token
# Output: a dictionary with two keys
#       Keys: 'access_token' stores the long-lived access token
#             'expires_in' stores when the access token expires
#             The value stored here can be converted to a readable time with datetime.datetime.fromtimestamp( value )
#             Value is that number stored at 'expires_in'
#             Long lived access tokens expire in 3 months.
def longLivedAccessToken():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['grant_type'] = 'fb_exchange_token'  # tell facebook we want to exchange token
    endpointParams['client_id'] = params['client_id']  # client id from facebook app
    endpointParams['client_secret'] = params['client_secret']  # client secret from facebook app
    endpointParams['fb_exchange_token'] = params['page_access_token']  # access token to get exchange for a long lived token
    url = params['endpoint_base'] + 'oauth/access_token'
    response = makeApiCall(url , endpointParams)
    return response



