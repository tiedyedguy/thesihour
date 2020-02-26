import praw
import requests
from datetime import date

d0 = date(2020, 1, 2)
d1 = date.today()
delta = d1 - d0
whichpicture = delta.days

URL = "https://openaccess-api.clevelandart.org/api/artworks/"
PARAMS = {'cc0': 1, 'has_image': 1, 'limit': 1, 'skip': whichpicture}

r = requests.get(url=URL, params=PARAMS)
data = r.json()

title = data["data"][0]["title"]
print(data["data"][0]["creators"])
if (data["data"][0]["creators"] and data["data"][0]["creators"][0]["description"] is not None):
    title = title + " - " + \
        data["data"][0]["creators"][0]["description"]
title = title + " - " + data["data"][0]["creation_date"]
print(title)
print(data["data"][0]["images"]["web"]["url"])

reddit = praw.Reddit('bot1', user_agent='bot1 user agent')
reddit.subreddit('artdaily').submit(
    title, None, data["data"][0]["images"]["web"]["url"])
