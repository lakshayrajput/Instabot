from Get_user_id import get_user_id
from constants import Base_url,App_Access_Token
import requests
import urllib
from PIL import Image


#-----get user latest post-----#
def get_user_post_info(username) :

    user_id = get_user_id(username)
    request_url = (Base_url + "users/%s/media/recent/?access_token=%s"%(user_id,App_Access_Token))
    #print("Get request url: "+request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200 :

        if len(user_info['data']) :
             print("Comments : %s"%(user_info['data'][0]['comments']['count']))

             if (user_info ['data'][0]['caption']) is not None:
                    var = 0
             else :
                 print("Caption: "+str(user_info['data'][0]['caption']))

             print("Pic id : %s" % (user_info['data'][0]['id']))
             print("Pic likes : %s" % (user_info['data'][0]['likes']['count']))

             image_name = username+'.jpg'
             image_url = user_info['data'][0]['images']['standard_resolution']['url']
             urllib.urlretrieve(image_url, image_name)       #-----saving the user's latest post-----#
             original = Image.open(image_name)
             original.show()
             print("Your image has been successfully saved..")
             return (user_info['data'][0]['id'])


        else:
            print("No info exist")
    else:
        print("HTTP code other than 200..")

