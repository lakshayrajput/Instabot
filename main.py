from constants import Base_url,App_Access_Token
from Self_info import self_info
from Get_own_post import get_own_post
from Get_user_id import get_user_id
from Get_user_info import get_user_info
from Get_user_post_info import get_user_post_info
import requests
import urllib

#--------------------------------------------------MAIN FUNCTION---------------------------------------#

#----getting my own info----#
self_info()

#----getting my recent post info & saving it as(lakshay.jpg)----#
get_own_post()

#-----getting user-ID-----#
get_user_id()

#-----getting user-INFO----#
get_user_info()

#-----getting user recent-POST & saving it as (danish.jpg)------#
get_user_post_info()