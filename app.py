from flask import Flask, render_template
from facebook_interface import*
from instagram_interface import*
app = Flask(__name__)

@app.route("/")
def homepage():
    info = dict()
    info['followers'] = follower_count() + igFollowers()
    info['f_percent'] = round(follower_count() / info['followers'] * 100, 1)
    info['i_percent'] = round(igFollowers() / info['followers'] * 100, 1)
    return render_template('index.html', info = info)
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
    return render_template('facebook.html', info = info, impressions = impressions)

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



    return render_template('instagram.html', info = info)

@app.route("/linkedin")
def linkedin():
    return 'under construction :D'

@app.route("/twitter")
def twitter():
    return 'under construction :D'
