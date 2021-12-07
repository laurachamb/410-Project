import requests
import json

def getCreds():
    creds = dict()
    #empty values should be generated/accessed through the facebook developer account
    creds['user_access_token'] = 'EAAI3fQapZATcBAMHgm5LJnaBb29sc9xGYRKM7UL6s9A6aTaLjQC5UPOW93E3vFVZC5FIcRQhWBnGmVzbuazfof9DHA52yzNyRl2AbLoOXCn6L6kmAsI5HrsLMSfyNHaqvMfOAoZC4D30yS0ZCMqtZBAmHxhobAd6MKTc1JZCnehirZB4qeeUrfZB7FxHFcKYZASshwf4WYGl8jPWNC6Yg6djUqFkR153qlFPBu4y0fBPe9qO0S2b0ud4D'
    creds['page_access_token'] = 'EAAI3fQapZATcBAO0CYhbAQ3o4O6E7IBgUTnA1tkUFLshRZAcX1N4qlM4aNYuWVZCf5CaZChS1BEq4drACO4IYEnBDY8UZCHZCJd2ijVvBsUTWgCLJba89P7XZBY77ZCzbzlT1kwFZBlnKrNHgU7G19zJfAKmVB77rVAtqRPBC0ebELdu50AOCiHX2ZB1A39NBRmWpN6JLsbZAqwV1MiitUgn3Rk'
    creds['client_id'] = '623960075625783'
    creds['client_secret'] = ''
    creds['ig_username'] = 'impactfinctr'

    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v12.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['page_id'] = '1503119803264962'
    creds['ig_page_id'] = '17841404219581713'
    return creds
