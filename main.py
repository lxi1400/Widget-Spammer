import requests
import warnings, random
warnings.filterwarnings("ignore")

def my_request():
    url = "https://discord.com/api/v8/guilds/SERVERID/widget"
    data = {'channel_id': RANDOMCHANNELID,
            'enabled': True,

           }
    headers = {
        "Authorization": "TOKENHERE",
        "Accept-Language": "en-US",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.308 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "*/*",
    }
    url2 = "https://discord.com/api/v8/guilds/SERVERID/widget"
    data2 = {'channel_id': RANDOMCHANNELID,
            'enabled': False,

           }
    headers2 = {
        "Authorization": "TOKENHEREk",
        "Accept-Language": "en-US",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.308 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "*/*",
    }
    r = requests.patch(url, headers=headers, json=data, verify=False)
    r2 = requests.patch(url2, headers=headers2, json=data2, verify=False)

for i in range(999999):
    my_request()
