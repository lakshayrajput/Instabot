from constants import Base_url,App_Access_Token
import requests
import urllib



user_name = 'dude pic'
def user_post_like_by_me() :
    request_url = (Base_url + "users/self/media/liked?access_token=%s")%(App_Access_Token)
    print("Get request url: "+request_url)
    result = requests.get(request_url).json()
    if result ['meta']['code'] == 200 :
        if len(result['data']) :
            image_name = user_name + '.jpg'
            image_url = result['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print("Your image has been downloaded as : "+image_name)
        else:
            print("Post does not exist...")
    else:
        print("Http code other than 200....")
