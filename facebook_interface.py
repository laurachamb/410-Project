import requests, json
from flasktest import defines

# This functions makes the API calls for facebook using the defines dictionary
# you pass in the url with endpoint parameters and the requests.get() function issues a get request with those
# the response dictionary is returned and has four keys
# keys : 'url' stored the url of the requests
#       'endpoint_params' stores endpoint parameters in json
#       'json_data' stores the json representation of the data returned by the get call
#       'json_data_pretty' stores a nicer representation of the json data, useful for debugging
def makeApiCall(url, endpointParams, debug='no'):
    data = requests.get(url, endpointParams)
    response = dict()
    response['url'] = url
    response['endpoint_params'] = json.dumps(endpointParams, indent=4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4 )

    return response

# gets page id for Facebook page
# I stored the ids in defines so there is no need to call this function further
def pageId():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + 'me'
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['id']

# returns a list of all post ids to help get post information
# list is sorted from most recent to oldest and stores posts within the last 2 years
def postIds():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + 'me/posts'
    response = makeApiCall(url, endpointParams, params['debug'])
    ids = []
    for i in range(len(response['json_data']['data'])):
        ids += [response['json_data']['data'][i]['id']]
    return ids


# returns friend count
#def friend_count():
 #   params = defines.getCreds()
 #   endpointParams = dict()
 #   endpointParams['access_token'] = params['user_access_token']
 #   url = params['endpoint_base'] + 'me/friends'
#    response = makeApiCall(url, endpointParams, params['debug'])
 #   return response['json_data']['summary']['total_count']


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
# returns a dictionary with three keys
# keys: 'day' stores the number of impressions within the last day
#       'week' stores the number of impressions within the last week
#       'days_28' stores the number of impressions within the last 28 days
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
# returns a dictionary with three keys
# keys: 'day' stores the number of unique impressions within the last day
#       'week' stores the number of unique impressions within the last week
#       'days_28' stores the number of unique impressions within the last 28 days
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
# returns a dictionary with three keys
# keys: 'day' stores the number of post impressions within the last day
#       'week' stores the number of post impressions within the last week
#       'days_28' stores the number of post impressions within the last 28 days
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
# returns a dictionary with three keys
# keys: 'day' stores the number of unqiue post impressions within the last day
#       'week' stores the number of unique post impressions within the last week
#       'days_28' stores the number of unique post impressions within the last 28 days
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
# returns a dictionary with three keys
# keys: 'day' stores the number of engaged users within the last day
#       'week' stores the number of engaged users within the last week
#       'days_28' stores the number of engaged users within the last 28 days
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


# The number of times a Page's profile has been viewed by logged in and logged out people.
# returns a dictionary with three keys
# keys: 'day' stores the number of engaged users within the last day
#       'week' stores the number of engaged users within the last week
#       'days_28' stores the number of engaged users within the last 28 days
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
# returns a dictionary with three keys
# keys: 'day' stores the number of post engagements within the last day
#       'week' stores the number of post engagements within the last week
#       'days_28' stores the number of post engagements within the last 28 days
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
# returns a dictionary with three keys
# keys: 'day' stores the number of negative reactions within the last day
#       'week' stores the number of negative reactions within the last week
#       'days_28' stores the number of negative reactions within the last 28 days
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


# post likes for a specific post given the post id
# you can get post ids from postIDs()
# likes for Facebook since they have many positive reactions will be like, love, and wow reactions
# returns one value represnting the likes for that post
def getPostLikes( postId ):
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['metric'] = 'post_reactions_like_total,post_reactions_love_total,post_reactions_wow_total'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + postId + '/insights'
    response = makeApiCall(url, endpointParams, params['debug'])
   # print(response['json_data_pretty'])
    likes = response['json_data']['data'][0]['values'][0]['value']
    loves = response['json_data']['data'][1]['values'][0]['value']
    wows = response['json_data']['data'][2]['values'][0]['value']
    return likes + loves + wows


# gets total likes (again like are like, love, or wow reactions on facebook) for last number of posts starting from
# the most recent
# number of posts should be passed in
def getMultiplePostLikes( num ):
    ids = postIds()
    total = 0
    for id in ids[:num]:
        total += getPostLikes(id)
    return total




id = pageId()
print('Page id: ' + id)
pids = postIds()
print('Post ids:')
for i in postIds():
    print(i)
#friends = friend_count()
#print('Friends: ' + str(friends))

followers = follower_count()
print('Followers: ' + str(followers))

impressions = getImpressions()
print("Total Post Engagement:")
print('Day: ' + str(impressions['day']))
print('Week: ' + str(impressions['week']))
print('Month: ' + str(impressions['days_28']))

uimpressions = getUniqueImpressions()
print("Impressions:")
print('Day: ' + str(uimpressions['day']))
print('Week: ' + str(uimpressions['week']))
print('Month: ' + str(uimpressions['days_28']))

pimpressions = getPostImpressions()
print("Post Impressions:")
print('Day: ' + str(pimpressions['day']))
print('Week: ' + str(pimpressions['week']))
print('Month: ' + str(pimpressions['days_28']))

upimpressions = getUniquePostImpressions()
print("Unique Post Impressions:")
print('Day: ' + str(upimpressions['day']))
print('Week: ' + str(upimpressions['week']))
print('Month: ' + str(upimpressions['days_28']))

views = pageViews()
print("Page Views:")
print('Day: ' + str(views['day']))
print('Week: ' + str(views['week']))
print('Month: ' + str(views['days_28']))

engagements = totalPostEngagement()
print("Total Post Engagement:")
print('Day: ' + str(engagements['day']))
print('Week: ' + str(engagements['week']))
print('Month: ' + str(engagements['days_28']))

users = engagedUsers()
print("Total Engaged Users:")
print('Day: ' + str(users['day']))
print('Week: ' + str(users['week']))
print('Month: ' + str(users['days_28']))

neg = negativeFeedback()
print("Total Post Engagement:")
print('Day: ' + str(neg['day']))
print('Week: ' + str(neg['week']))
print('Month: ' + str(neg['days_28']))

likes = getPostLikes('1503119803264962_288051243325880')
print('Post likes for post with post id 1503119803264962_288051243325880: ')
print(likes)

likes3 = getMultiplePostLikes(3)
print('Total likes for last 3 posts:')
print(likes3)
