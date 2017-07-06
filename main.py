from constants import Base_url,App_Access_Token
from Self_info import self_info
from Get_own_post import get_own_post
import requests
import urllib

#--------------------------------------------------MAIN FUNCTION---------------------------------------#

#----getting my own info----#
self_info()

#----getting my recent post info & saving it as(lakshay.jpg)----#
get_own_post()