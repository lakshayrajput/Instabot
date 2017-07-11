from constants import Base_url,App_Access_Token
import requests

user_name = raw_input("Please enter your friend name: ")
def get_user_id(user_name) :

    request_url = ((Base_url + "users/search?q=%s&access_token=%s") % (user_name,App_Access_Token))
    print("Get request url: %s"%(request_url))
    user_info = requests.get(request_url).json()
    if user_info ['meta']['code'] == 200 :
        if len(user_info['data']) :
            print "User id: %s" %  (user_info['data'][0]['id'])
            return user_info['data'][0]['id']
        else:
            print("Incorrect id..")
    else:
        print("Wrong code..")
