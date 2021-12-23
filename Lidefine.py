import requests
import json

def getCreds():
    creds = dict()
    #empty values should be generated/accessed through the facebook developer account
    creds['access_token'] = 'AQWcdbfGJzdwD_0CwFzxabj5b0rx-5Cc3CSyFk5baTDvRf7l4JAcUpgaXeHDFSW4GeOFMbkhvGzEtzRhdQu1kMNEWobPoTnjUIuVklXzitEoH9cEaLTJiraHAS999ImM3HILURa_AJXHZ_2x_lsDtlL-J6jcRB8KGy8ZC05YehWIZE75kLd_5x1kHm0VxUpXt8LngueW3YMiBm_DSdXozmpGJTLwE4oFscHn0Db6j1lwbBsRfH8AErV6Vws-XctbbCx3ZdVkrvRhTV3WM0wqQw-WcTlfnTc7X4Evts3iiSzZYBqbF-UZlZHft7AAqvVKpSwBkehgeAHyt6aRiyJFFhtQltTgRg'
    creds['client_id'] = ''
    creds['client_secret'] = ''
    creds['Li_username'] = ''

    creds['main_domain_linkedin'] = 'https://api.linkedin.com/v2'
    creds['debug'] = 'no'
    creds['profile_id'] = 'LH8kpyHYnrD'

    return creds