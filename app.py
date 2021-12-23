from flask import Flask, render_template
from facebook_interface import*
from instagram_interface import*
from twitter_interface import*


app = Flask(__name__)

# Homepage: calls the index.html template and passes in a dictionary
# info:
#   Keys:
#       followers: holds the sum of the followers across all platforms
#       f_percent: holds the percentage of followers facebook has of followers across all platforms
#       i_percent: holds the percentage of followers instagram has of followers across all platforms
@app.route("/")
def homepage():
    info = dict()
    info['followers'] = follower_count() + igFollowers()
    info['f_percent'] = round(follower_count() / info['followers'] * 100, 1)
    info['i_percent'] = round(igFollowers() / info['followers'] * 100, 1)
    return render_template('index.html', info = info)

# Facebook Dashboard: calls the facebook.html template and passes in a dictionary called info and a list called mInfo
# info:
#   Keys:
#       followers: holds the number of facebook followers as an integer
#       impressions: a dictionary with three keys hold the number of impressions over certain periods of time
#                    Keys:
#                       day: number impressions over the last day as an integer
#                       week: number impressions over the last week as an integer
#                       days_28: number impressions over the last 28 days as an integer
#       views: a dictionary with three keys hold the number of page views over certain periods of time
#                    Keys:
#                       day: number page views over the last day as an integer
#                       week: number page views over the last week as an integer
#                       days_28: number page views over the last 28 days as an integer
#       users: a dictionary with three keys hold the number of engaged users over certain periods of time
#                    Keys:
#                       day: number engaged users over the last day as an integer
#                       week: number engaged users over the last week as an integer
#                       days_28: number engaged users over the last 28 days as an integer
#       pimpressions: a dictionary with three keys hold the number of post impressions over certain periods of time
#                    Keys:
#                       day: number post impressions over the last day as an integer
#                       week: number post impressions over the last week as an integer
#                       days_28: number post impressions over the last 28 days as an integer
#       avg_likes: the average likes over the past 10 posts as an integer
#       likes: a list of like counts for the past 10 posts
# mInfo: a list containing 10 dictionaries of information for the past 10 posts
#   Keys:
#        id: id for that post
#        timestamp: timestamp for that post

@app.route("/facebook")
def facebook():
    info = dict()
    info['followers'] = follower_count()
    info['impressions'] = dict()
    impressions = getImpressions()
    info['impressions']['day'] = impressions['day']
    info['impressions']['week'] = impressions['week']
    info['impressions']['days_28'] = impressions['days_28']
    views = pageViews()
    info['views'] = dict()
    info['views']['day'] = views['day']
    info['views']['week'] = views['week']
    info['views']['days_28'] = views['days_28']
    users = engagedUsers()
    info['users'] = dict()
    info['users']['day'] = users['day']
    info['users']['week'] = users['week']
    info['users']['days_28'] = users['days_28']
    info['pimpressions'] = dict()
    pimpressions = getPostImpressions()
    info['pimpressions']['day'] = pimpressions['day']
    info['pimpressions']['week'] = pimpressions['week']
    info['pimpressions']['days_28'] = pimpressions['days_28']

    mInfo = postIds()
    info['likes'] = []
    info['avg_likes'] = 0
    for i in range(10):
        l = getPostLikes(mInfo[i]['id'])
        info['likes'] += [l]
        info['avg_likes'] += l
    info['avg_likes'] /= 10

    return render_template('facebook.html', info = info, mInfo = mInfo)


# Instagram Dashboard: calls the instagram.html template and passes in a dictionary called info and a list called mInfo
# info:
#   Keys:
#       followers: holds the number of instagram followers as an integer
#       posts: holds the number of instagram posts as an integer
#       views: holds the number of daily instagram profile views as an integer
#       impressions: a dictionary with three keys hold the number of impressions over certain periods of time
#                    Keys:
#                       day: number impressions over the last day as an integer
#                       week: number impressions over the last week as an integer
#                       days_28: number impressions over the last 28 days as an integer
#       views: a dictionary with three keys hold the reach over certain periods of time
#                    Keys:
#                       day: reach over the last day as an integer
#                       week: reach over the last week as an integer
#                       days_28: reach over the last 28 days as an integer
#       avg_likes: the average likes over the past 10 posts as an integer
#       avg_comments: the average comments over the past 10 posts as an integer
#       avg_impressions: the average impressions over the past 10 posts as an integer
#       avg_reach: the average reach over the past 10 posts as an integer
#       avg_engagement: the average engagement over the past 10 posts as an integer
# mInfo: a list containing 10 dictionaries of information for the past 10 posts
#   Keys:
#        like_count: number of likes for that post as an integer
#        comments_count: number of comments for that post as an integer
#        insights: a dictionary storing that posts insights
#           Keys:
#               impressions: the number of impressions that post has
#               reach: reach that post has
#               engagement: the amount of engagement that post has
@app.route("/instagram")
def instagram():
    info = dict()
    info['followers'] = igFollowers()
    info['posts'] = igPostCount()
    info['views'] = profileViews()
    info['impressions'] = dict()
    imp = impressions()
    info['impressions']['day'] = imp['day']
    info['impressions']['week'] = imp['week']
    info['impressions']['days_28'] = imp['days_28']

    info['reach'] = dict()
    r = reach()
    info['reach']['day'] = r['day']
    info['reach']['week'] = r['week']
    info['reach']['days_28'] = r['days_28']
    info['avg_likes'] = 0
    info['avg_comments'] = 0
    info['avg_impressions'] = 0
    info['avg_reach'] = 0
    info['avg_engagement'] = 0
    mInfo = mediaInfo()
    for i in range(10):
        info['avg_likes'] += mInfo[i]['like_count']
        info['avg_comments'] += mInfo[i]['comments_count']
        mInfo[i]['insights'] = postInsights(mInfo[i]['id'])
        info['avg_impressions'] += mInfo[i]['insights']['impressions']
        info['avg_reach'] += mInfo[i]['insights']['reach']
        info['avg_engagement'] += mInfo[i]['insights']['engagement']
    info['avg_likes'] /= 10
    info['avg_comments'] /= 10
    info['avg_impressions'] /= 10
    info['avg_reach'] /= 10
    info['avg_engagement'] /= 10
    return render_template('instagram.html', info = info, mInfo = mInfo)


@app.route("/twitter")
def twitter():

    finalList = []
    finalList = start_program()

    info1 = addData(finalList[1])
    info2 = addData(finalList[2])
    info3 = addData(finalList[3])

    strList = []
    strList = strMonths(finalList)
    # change this soon
    username = 'impactfinctr'

    return render_template('twitter.html', finalList=finalList,info1=info1,info2=info2,info3=info3,strList=strList, username=username)
