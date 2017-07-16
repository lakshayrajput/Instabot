from Get_user_recent_post_id import get_user_recent_post_id
from constants import Base_url,App_Access_Token
import requests



def post_a_comment():
    username = raw_input("Enter your friend name: ")
    while username.isalpha() is not True:
        username = raw_input("Pleaze enter valid name: ")
    media_id = get_user_recent_post_id(username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": App_Access_Token, "text" : comment_text}
    request_url = (Base_url + 'media/%s/comments') % (media_id)
    #print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"

