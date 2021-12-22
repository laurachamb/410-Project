import Lidefine, requests, json

def makeGetAPICall(url,params):
    data = requests.get(url, params=params)
    res = json.dumps(data.json(), indent=1)
    return res

def viewProfileInfo():
    paramsLinked = dict()
    paramsLinked = Lidefine.getCreds()
    url = paramsLinked['main_domain_linkedin'] + '/me'
    paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
    res = makeGetAPICall(url, paramsforURL)
    print(res)

def Numofconnections():
    paramsLinked = dict()
    paramsLinked = Lidefine.getCreds()
    url = paramsLinked['main_domain_linkedin'] + '/numConnections/{id}'
    paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
    res = makeGetAPICall(url, paramsforURL)
    print(res)

def connectionId():
    paramsLinked = dict()
    paramsLinked = Lidefine.getCreds()
    paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
    url = paramsLinked['main_domain_linkedin'] + '/connections/{id}'
    res = makeGetAPICall(url, paramsforURL)
    return response['json_data']['data'][0]['id']

def getshareIds():
    paramsLinked = dict()
    paramsLinked = Lidefine.getCreds()
    paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
    url = paramsLinked['main_domain_linkedin'] + '/shares'
    res = makeGetAPICall(url, paramsforURL)
    ids = []
    for i in range(len(res['json_data']['data'])):
        ids += [res['json_data']['data'][i]['id']]
    return ids

def viewShare():
    paramsLinked = dict()
    paramsLinked = Lidefine.getCreds()
    url = paramsLinked['main_domain_linkedin'] + '/shares?q=owners&owners=urn:li:person:'+paramsLinked['profile_id']+'&sortBy=LAST_MODIFIED&sharesPerOwner=100'
    paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
    res = makeGetAPICall(url, paramsforURL)
    print(res)

def viewactivity():
    paramsLinked = dict()
    paramsLinked = Lidefine.getCreds()
    url = paramsLinked['main_domain_linkedin'] + '/socialActions/{target}'
    paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
    res = makeGetAPICall(url, paramsforURL)
    print(res)

def getlikes():
        paramsLinked = dict()
        paramsLinked = Lidefine.getCreds()
        url = paramsLinked['main_domain_linkedin'] + '/socialActions/{target}/likes'
        paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
        res = makeGetAPICall(url, paramsforURL)
        print(res)


def getreactions():
    paramsLinked = dict()
    paramsLinked = Lidefine.getCreds()
    url = paramsLinked['main_domain_linkedin'] + '/reactions/{reactionsId}' //get_all_method
    paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
    res = makeGetAPICall(url, paramsforURL)
    print(res)

def getactivity():
    paramsLinked = dict()
    paramsLinked = Lidefine.getCreds()

    url = paramsLinked['main_domain_linkedin'] + '/activities'  //batchgetmethod
    paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
    res = makeGetAPICall(url, paramsforURL)
    print(res)


def getcomments():
    paramsLinked = dict()
    paramsLinked = Lidefine.getCreds()
    paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
    url = paramsLinked['main_domain_linkedin'] + '/activities' // batchgetmethod
    res = makeGetAPICall(url, paramsforURL)
    print(res)


def engagedUsers():
    paramsLinked = dict()
    paramsLinked = Lidefine.getCreds()
    paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
    url = paramsLinked['main_domain_linkedin'] + '/dmpEngagementSourceTypes'
    res = makeGetAPICall(url, paramsforURL)
    users = dict()
    for i in range(len(res['json_data']['data'])):
        if res['json_data']['data'][i]['period'] == 'day':
            users['day'] = res['json_data']['data'][i]['values'][1]['value']
        if res['json_data']['data'][i]['period'] == 'week':
            users['week'] = res['json_data']['data'][i]['values'][1]['value']
        if res['json_data']['data'][i]['period'] == 'days_28':
            users['days_28'] = res['json_data']['data'][i]['values'][1]['value']
    return users

def profileViews():
    paramsLinked = dict()
    paramsLinked = Lidefine.getCreds()
    paramsforURL = {'oauth2_access_token': paramsLinked['access_token']}
    url = paramsLinked['main_domain_linkedin'] + '/dmpEngagementSourceTypes'
    res = makeGetAPICall(url, paramsforURL)
    views = dict()
    for i in range(len(res['json_data']['data'])):
        if res['json_data']['data'][i]['period'] == 'day':
            views['day'] = res['json_data']['data'][i]['values'][1]['value']
        if res['json_data']['data'][i]['period'] == 'week':
            views['week'] = res['json_data']['data'][i]['values'][1]['value']
        if res['json_data']['data'][i]['period'] == 'days_28':
            views['days_28'] = res['json_data']['data'][i]['values'][1]['value']
    return views