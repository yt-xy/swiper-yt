import requests

# Sid: 053328ba5585f76d66b9a229f5a38c29
# Token: da15c58aec401d4671628a6b40b91660
# AppID: a2d8353ced6b4ecbaac3b7c6188daaf7

args = {
     "sid":"053328ba5585f76d66b9a229f5a38c29",
     "token":"da15c58aec401d4671628a6b40b91660",
     "appid":"a2d8353ced6b4ecbaac3b7c6188daaf7",
     "templateid":"518847",
     "param":"8888",
     "mobile":"18855098944",
}

api = 'https://open.ucpaas.com/ol/sms/sendsms'

response = requests.post(api, json=args)