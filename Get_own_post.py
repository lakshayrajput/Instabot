from constants import Base_url,App_Access_Token
import requests
from datetime import datetime, timedelta
import urllib

def get_own_post() :
    request_url = (Base_url + "users/self/media/recent/?access_token=%s") % (App_Access_Token)
    #print("Get request url: %s"%(request_url))
    own_media = requests.get(request_url).json()
    #print(own_media)
    if own_media ['meta']['code'] == 200 :
        if len(own_media['data']) :
            print ("comments: %s"%(own_media['data'][0]['comments']['count']))
            print("Pic id: %s"%(own_media['data'][0]['id']))
            print ("Caption id: %s" % (own_media['data'][0]['caption']['id']))

            time = int(own_media['data'][0]['caption']['created_time'])
            date = datetime.fromtimestamp(time / 1000.0)
            image_name = 'lakshay.jpg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print("Your image has been successfully saved..")
            print ("Created Time: %s" % (date))
            print ("Total likes: %s" % (own_media['data'][0]['likes']['count']))
            return (own_media['data'][0]['id'])
        else:
            print("Post does not exist")
    else :
        print("Status code is wrong")
