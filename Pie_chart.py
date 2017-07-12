import matplotlib.pyplot as plt
from Get_own_post_id import get_own_post_id
from constants import Base_url,App_Access_Token
import requests
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

negative_comment = []
positive_comment = []
total_comment = []
def pie_chart():
    pic = get_own_post_id()
    request_url = (Base_url + 'media/%s/comments/?access_token=%s') % (pic, App_Access_Token)
    #print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                post_id = comment_info['data'][x]['id']

                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                total_comment.append(comment_text)
                    #print("All comments: %d"%(len(total_comment)))

                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                        negative_comment.append(comment_text)
                        print 'Negative comment : %s' % (comment_text)

                else:
                        positive_comment.append(comment_text)

                        print 'Positive comment : %s\n' % (comment_text)

        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'
    len_of_total_comment = float(len(total_comment))
    print("total comment %d" % (len_of_total_comment))
    len_of_pos_comment = float(len(positive_comment))
    print("pos comment: %d" % (len_of_pos_comment))
    len_of_neg_comment = float(len(negative_comment))
    print("neg comment: %d" % (len_of_neg_comment))
    neg_comment_percentage = ((len_of_neg_comment) / (len_of_total_comment) * (100))

    print("negative comment percentage: %.2f" % (neg_comment_percentage) + "%..")
    pos_comment_percentage = float((len_of_pos_comment) / (len_of_total_comment) * (100))

    print("positive comment pecentage: %.2f" % (pos_comment_percentage) + "%..")
    pos_comment = str(pos_comment_percentage)+" % +ve comment"
    neg_comment = str(neg_comment_percentage)+"% -ve comment"
    activities = [pos_comment, neg_comment]

    slices = [pos_comment_percentage, neg_comment_percentage]
    cols = ['r', 'k']
    plt.pie(slices, labels=activities, colors=cols, startangle=90, shadow=True)
    plt.title('%age graph representation....')
    plt.show()




