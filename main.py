from json import dumps
from requests import post
from os import environ


import requests
from urllib.parse import urljoin


def main():

    token = environ.get('token')
    if not token:
        return 'AnPush: 未配置token，无法进行消息推送。'

    url = urljoin("https://api.anpush.com/push/", token)

    payload = 'title=每日新闻推送 bot&content=your_content&channel=57009'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)


if __name__ == '__main__':
    main()
