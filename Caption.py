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
            count = 0
            no_caption = set()
            no_matched_caption = set()
            for post in range(0, len(user_info['data'])):
                pic_no = post + 1
                if user_info['data'][post]['caption'] == None:
                    no_caption.add(pic_no)
                for temp in service:


                    if user_info['data'][post]['caption'] == None:
                        var = 0

                    elif temp in user_info['data'][post]['caption']['text']:
                        #print(user_info['data'][post]['caption']['text'])
                        pic_id = user_info['data'][post]['id']

                        print("Caption matched in pic no: "+str(pic_no))
                        comment_text = raw_input("Write your comment here: ")
                        payload = {"access_token": App_Access_Token, "text": comment_text}
                        request_url = (Base_url + 'media/%s/comments') % (pic_id)
                        #print 'POST request url : %s' % (request_url)

                        make_comment = requests.post(request_url, payload).json()

                        if make_comment['meta']['code'] == 200:
                            print "Successfully added a new comment!"
                        else:
                            print "Unable to add comment. Try again!"
                    else :

                        no_matched_caption.add(pic_no)
                        count = pic_no
            print("No caption in pics: "+str(no_caption))
            print("No caption matched in pics: "+str(no_matched_caption))
            print("Total no of pics: "+str(count))
            print("End of images...")
        else:
            print("No info exist")
    else:
        print("Incorrect code..")

