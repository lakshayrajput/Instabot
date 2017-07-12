from Get_user_id import get_user_id
from constants import Base_url,App_Access_Token
import requests

service = ['#food' ,'#shop' ,'#bike' ,'#weather' ,'#iphoneonly' ,'#cool' ,'#life' ,'#lol' ,'#instamood' ,'#life' ,'#style'
           ,'#amazing' ,'#summer' ,'#fashion' ,'#friends' ,'#cute' ,'#happy' ,'#feeling','#monogram','#thanks_everyone']


def caption_comment() :
    user_name = raw_input("Enter user name: ")
    user_id = get_user_id(user_name)
    request_url = (Base_url + "users/%s/media/recent/?access_token=%s" % (user_id, App_Access_Token))
    #print("Get request url: " + request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:

        if len(user_info['data']):

            for post in range(0, len(user_info['data'])):
                pic_no = post + 1
                for temp in service:
                    if user_info['data'][post]['caption'] == None:
                        print("Sorry there is no hashtag inside the image...")

                    elif temp in user_info['data'][post]['caption']['text']:
                        print(user_info['data'][post]['caption']['text'])
                        pic_id = user_info['data'][post]['id']
                        comment_text = raw_input("Your comment: ")
                        payload = {"access_token": App_Access_Token, "text": comment_text}
                        request_url = (Base_url + 'media/%s/comments') % (pic_id)
                        print 'POST request url : %s' % (request_url)

                        make_comment = requests.post(request_url, payload).json()

                        if make_comment['meta']['code'] == 200:
                            print "Successfully added a new comment!"
                        else:
                            print "Unable to add comment. Try again!"
                    else :
                        print("Sorry hashtag didn't match.Go further...")
            print("End of images...")
        else:
            print("No info exist")
    else:
        print("Incorrect code..")

