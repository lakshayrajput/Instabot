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
#\n 9. Download all posts of other user...\n 10. Download the most commented own post...\n 11.Download most liked own post...\n 12.Download the most commented user's post...\n 13.Download the most liked user's post...\n 14.Get a pie-chat of all -ve and +ve comments of own post...\n 15.Targeted comments based on user's post caption...