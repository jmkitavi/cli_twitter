#!/usr/bin/env python3
from twitter import *
import sys
import json

# new app kit Africa Security
# consumer_key= 'Q8JAqDHNfIh7cAK0Q7VGQXh1p'
# consumer_secret = 'aTu7agaQDEvQls3MCHGONR9R3U1UnSzvq1BxDulUG2fOr1ckqo'
# token = '833663699764256768-86z6wYa96UdEJK5mVVtY7Rv6thrPOZt'
# token_secret = 'BTWoRhPrMPnLg3WkA79EHqWG10XRWayZx2WKOstgN36cw'

# cli kitavi Africa Security
consumer_key = "ocFrr3g3h2UVvRXuzGnkK0Etc"
consumer_secret = "Uxd7WigHJXVbT15CXUGRtSWS9vxGVFCjbjBvgHwvJ71Ozys6j7"
token = "833663699764256768-gGfV2HXaZ81z0YVvB3TwFRflBH4oBXQ"
token_secret = "K3MvLn5erxhZu5w1ZcvjInj1MJQUmF9FaNBrbG0TiR75e"

t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

count = 10
if len(sys.argv) > 1:
    first = str(sys.argv[1])
    second = ""
    third = ""
if len(sys.argv) > 2:
    second = str(sys.argv[2])
    third = ""
if len(sys.argv) > 3:
    third = str(sys.argv[3])

if first == "timeline":
	if second and second.isdigit() is True:
		count = int(second)
	if second.isdigit() is True or second == "":		
		for x in t.statuses.home_timeline(count=count):
			print(x['user']['screen_name'] + ":  :" + x['text'])

	if second and second!="":
		if third and third.isdigit() is True:
			count = int(third)
		if third.isdigit() is True or third == "":		
			for x in t.statuses.user_timeline(screen_name=second, count=count):
				print(x['user']['screen_name'] + ":  :" + x['text'])
				

# 	t.statuses.update(status=sys.argv[1])
# # for x in t.statuses.home_timeline(count=1):
# 	for y in x['entities']['user_mentions']:
# 		print(str(y))
    # print( x['entities']['user_mentions'][0]['screen_name'] + ": -" + x['text'])
