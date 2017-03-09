#!/usr/bin/env python3
from twitter import *
import sys

consumer_key = "ocFrr3g3h2UVvRXuzGnkK0Etc"
consumer_secret = "Uxd7WigHJXVbT15CXUGRtSWS9vxGVFCjbjBvgHwvJ71Ozys6j7"
token = "833663699764256768-gGfV2HXaZ81z0YVvB3TwFRflBH4oBXQ"
token_secret = "K3MvLn5erxhZu5w1ZcvjInj1MJQUmF9FaNBrbG0TiR75e"

t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))


t.statuses.update(status=sys.argv[1])
for x in t.statuses.home_timeline(count=1):
	for y in x['entities']['user_mentions']:
		print(str(y))
	# print( x['entities']['user_mentions'][0]['screen_name'] + ": -" + x['text'])
