from constants import Base_url,App_Access_Token
from Self_info import self_info
from Get_own_post import get_own_post
from Get_user_id import get_user_id,user_name
from Get_user_info import get_user_info
from Get_user_post_info import get_user_post_info
from Like_a_post import like_a_post
import requests
import urllib

#--------------------------------------------------MAIN FUNCTION---------------------------------------#
var = True
while var :

    print(" What do you want to do ?.\n 1.Self-information...\n 2.Get own-post...\n 3.Get user-id...\n 4.Get user-info\n 5.Get user post-info\n 6.Like a user-post\n 7.Exit")
    get = raw_input("Please enter your choice : ")
    if get == 1 :
        # ----getting my own info----#
        self_info()
    elif get == 2 :
        # ----getting my recent post info & saving it as(lakshay.jpg)----#
        get_own_post()
    elif get == 3 :
        # -----getting user-ID-----#

        get_user_id(user_name)
    elif get == 4 :
        # -----getting user-INFO----#
        get_user_info()
    elif get == 5 :
        # -----getting user recent-POST & saving it as (danish.jpg)------#
        get_user_post_info()
    elif get == 6 :
        # -----give a like to user's recent post------#
        like_a_post()
    elif get == 7 :
        var = False

    else :
        print("Please enter a valid number..")













