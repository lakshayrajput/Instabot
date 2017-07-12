from Get_user_id import get_user_id

from constants import Base_url,App_Access_Token
import requests
import urllib



def get_all_posts() :
    username=raw_input("Enter the useranme: ")
    user_id = get_user_id(username)
    request_url = (Base_url + "users/%s/media/recent/?access_token=%s" % (user_id, App_Access_Token))
    #print("Get request url: " + request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:

        if len(user_info['data']):

            for post in range(0,len(user_info['data'])):
                pic_no = post + 1

                pic_id = user_info['data'][post]['id']
                image_name =username +str(pic_no)+".jpg"
                image_url = user_info['data'][post]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url,image_name)
                if pic_no == 1 :
                    print(str(pic_no)+" pic has been saved....")
                else :
                    print(str(pic_no) + " pics has been saved....")




        else:
            print("No info exist")
    else:
        print("Incorrect code..")



