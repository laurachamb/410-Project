import requests, json, defines

# just a help function to make the api calls and put the data into a dictionary
# the key json_data should be used to get the information from the get call
# the key json_data_pretty should be used to print info, good for debugging
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
def instagramPageId():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['fields'] = 'instagram_business_account'
    url = url = params['endpoint_base'] + params['page_id']
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['instagram_business_account']['id']


# returns the number of followers the account has (an integer)
def igFollowers():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['fields'] = 'followers_count'
    endpointParams['access_token'] = params['page_access_token']
    url = params['endpoint_base'] + params['ig_page_id']
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['followers_count']


# returns the number of posts the account has (an integer)
def igPostCount():
    params = defines.getCreds()
    endpointParams = dict()
    endpointParams['access_token'] = params['page_access_token']
    endpointParams['fields'] = 'media_count'
    url = params['endpoint_base'] + params['ig_page_id']
    response = makeApiCall(url, endpointParams, params['debug'])
    return response['json_data']['media_count']


# FOR NEXT THREE FUNCTIONS: I am thinking of combining the three functions into one to make for less api calls
# This would include a dictionary with keys impressions, reach, and profile views whose values are the dictionaries
# returned by each function

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
    endpointParams['fields'] = 'business_discovery.username(' + params['ig_username'] + '){media{comments_count,like_count}}'
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



id = instagramPageId()
print('Page id: ' + str(id))

followers = igFollowers()
print('Followers: ' + str(followers))

posts = igPostCount()
print('Number of Posts: ' + str(posts))

imp = impressions()
print("Impressions: ")
print("Day:" + str(imp['day']))
print("Week:" + str(imp['week']))
print("Last 28 Days:" + str(imp['days_28']))

r = reach()
print("Reach: ")
print("Day:" + str(r['day']))
print("Week:" + str(r['week']))
print("Last 28 Days:" + str(r['days_28']))

views = profileViews()
print("Profile views in the past day: " + str(views))

info = mediaInfo()
print("Media Ids:")
for id in info:
    print("Id: " + str(id['id']) + " Like Count: " + str(id['like_count']) + " Comment Count: " + str(id['comments_count']))

insights = postInsights(info[0]['id'])
print("Insights for post id " + info[0]['id'] + ": ")
print("Impressions: " + str(insights['impressions']))
print("Reach: " + str(insights['reach']))
print("Engagement: " + str(insights['engagement']))
