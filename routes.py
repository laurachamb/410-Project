from flask import Flask, render_template
import requests
import json 

#from flasktest.helper import*
from flasktest.facebook_interface import*
from flasktest.defines import*


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return (render_template('home.html'))

@app.route('/facebook')
def facebook():
    
     id = pageId()
     pids = postIds()

     test1 = follower_count()
     impressions = getImpressions()

     # last 28 days
     test2 = str(impressions['days_28'])

     uimpressions = getUniqueImpressions()
     test3 = str(uimpressions['days_28'])
    
     pimpressions = getPostImpressions()
     test4 = str(pimpressions['days_28'])

     upimpressions = getUniquePostImpressions()
     test5 = str(upimpressions['days_28'])

     views = pageViews()
     test6=str(views['days_28'])

     return render_template('facebook.html', test1=test1, test2 = test2, test3=test3, test4=test4, test5=test5, test6=test6)

