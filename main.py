import requests
import warnings, random
warnings.filterwarnings("ignore")
lol = ["True", "False"]


def widget(guildid, token):
    data = {'channel_id': "1",
            'enabled': next(lol),
    }
    headers = {
        "Authorization": token,
        "Accept-Language": "en-US",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.308 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "*/*",
    }

    r = requests.patch(f"https://discord.com/api/v8/guilds/{guildid}/widget", headers=headers, json=data, verify=False)
    print(r.status_code)


guildid = input("Insert Guild ID > ")
token = input("Insert Token > ")

while True:
    widget(guildid, token)
