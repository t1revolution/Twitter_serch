import config
import json
from requests_oauthlib import OAuth1Session

ck = config.consumer_key
cs = config.consumer_secret
at = config.access_token
ats = config.access_token_secret
twitter = OAuth1Session(ck, cs, at, ats)  #OAuth認証

url = "https://api.twitter.com/1.1/statuses/update.json"   #エンドポイント指定

print("内容は？")
tweet = input('>> ')

param = {"status" : tweet}

res = twitter.post(url, params = param)  #post

if res.status_code == 200:
    print("Posted")
else:
    print("Failed : %d"% res.status_code)






