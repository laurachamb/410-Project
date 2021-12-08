import requests
import json



params = {'oauth2_access_token': 'AQWcdbfGJzdwD_0CwFzxabj5b0rx-5Cc3CSyFk5baTDvRf7l4JAcUpgaXeHDFSW4GeOFMbkhvGzEtzRhdQu1kMNEWobPoTnjUIuVklXzitEoH9cEaLTJiraHAS999ImM3HILURa_AJXHZ_2x_lsDtlL-J6jcRB8KGy8ZC05YehWIZE75kLd_5x1kHm0VxUpXt8LngueW3YMiBm_DSdXozmpGJTLwE4oFscHn0Db6j1lwbBsRfH8AErV6Vws-XctbbCx3ZdVkrvRhTV3WM0wqQw-WcTlfnTc7X4Evts3iiSzZYBqbF-UZlZHft7AAqvVKpSwBkehgeAHyt6aRiyJFFhtQltTgRg'}
response = requests.get('https://api.linkedin.com/v2/me', params = params)

print(json.dumps(response.json(), indent=1))


profile_id = 'LH8kpyHYnrD'

#scope: w_member_social,r_liteprofile
access_token = 'AQWcdbfGJzdwD_0CwFzxabj5b0rx-5Cc3CSyFk5baTDvRf7l4JAcUpgaXeHDFSW4GeOFMbkhvGzEtzRhdQu1kMNEWobPoTnjUIuVklXzitEoH9cEaLTJiraHAS999ImM3HILURa_AJXHZ_2x_lsDtlL-J6jcRB8KGy8ZC05YehWIZE75kLd_5x1kHm0VxUpXt8LngueW3YMiBm_DSdXozmpGJTLwE4oFscHn0Db6j1lwbBsRfH8AErV6Vws-XctbbCx3ZdVkrvRhTV3WM0wqQw-WcTlfnTc7X4Evts3iiSzZYBqbF-UZlZHft7AAqvVKpSwBkehgeAHyt6aRiyJFFhtQltTgRg'

url = "https://api.linkedin.com/v2/ugcPosts"

headers = {'Content-Type': 'application/json',
           'X-Restli-Protocol-Version': '2.0.0',
           'Authorization': 'Bearer ' + access_token}


post_data = {
    "author": "urn:li:person:"+profile_id,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Hello World! This is my first Share on LinkedIn!!"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

response = requests.post(url, headers=headers, json=post_data)

print(response)