from Self_info import self_info
from Get_own_post import get_own_post
from Get_user_id import get_user_id
from Get_user_info import get_user_info
from Get_user_post_info import get_user_post_info
from Like_a_post import like_a_post
from Post_a_comment import post_a_comment
from Recent_liked_pic import user_post_like_by_me
from Get_all_posts_of_user import get_all_posts
from Most_commented_own_post import most_commented_post
from Most_liked_own_post import most_liked_post
from Most_commented_user_post import most_commented_user_post
from Most_liked_user_post import most_liked_user_post
from Pie_chart import pie_chart
from Caption import caption_comment



#--------------------------------------------------MAIN FUNCTION---------------------------------------#
def main():
    var = True
    while var :
        print("--------------------------------------------------------------------------------------------------------------")
        print(" What do you want to do ?.\n 1.Self-information...\n 2.Get own-post...\n 3.Get user-id...\n 4.Get user-info...\n 5.Get user post-info...\n 6.Like a user-post...\n 7.Post a comment on user-id...\n 8.Get the recent post liked by you of the other user...\n 9.Download all posts of other user...\n 10.Download the most commented own post...\n 11.Download most liked own post...\n 12.Download the most commented user's post...\n 13.Download the most liked user's post...\n 14.Draw a pie-chat of all -ve and +ve comments of own post...\n 15.Targeted comments based on user's post caption...\n 16.Exit..."
              "")
        get = int(raw_input("Please enter your choice : "))
        if get == 1 :
                # ----getting my own info----#
            self_info()
            print("-----------------------------------------------------------------------------------------------------")
        elif get == 2 :
                # ----getting my recent post info & saving it as(lakshay.jpg)----#
            get_own_post()
            print("-----------------------------------------------------------------------------------------------------")
        elif get == 3 :
                # -----getting user-ID-----#
            username=raw_input("Enter the username: ")
            get_user_id(username)
            print("-----------------------------------------------------------------------------------------------------")
        elif get == 4 :
                # -----getting user-INFO----#
            username = raw_input("Enter the username: ")
            get_user_info(username)
            print("-----------------------------------------------------------------------------------------------------")
        elif get == 5 :
                # -----getting user recent-POST & saving it as (danish.jpg)------#
            username = raw_input('enter the username: ')
            get_user_post_info(username)
            print("-----------------------------------------------------------------------------------------------------")
        elif get == 6 :
                # -----give a like to user's recent post------#

            like_a_post()
            print("-----------------------------------------------------------------------------------------------------")
        elif get == 7 :
                #------Hit a comment on user post----------#
            post_a_comment()
        elif get == 8 :
                #--------Get to know which recent pic is liked by me of the user & download it-------#
            user_post_like_by_me()
        elif get == 9 :
            #--------- Download the all posts of user--------#
            get_all_posts()
        elif get == 10 :
            #-------Download most commented own post-------#
            most_commented_post()
        elif get == 11 :
            #------- download most liked own post-------#
            most_liked_post()
        elif get == 12:
            #-------Download most commented user post--------#
            most_commented_user_post()
        elif get == 13 :
            #-------Download most liked user post-------#
            most_liked_user_post()
        elif get == 14 :
            #---------Get a pie chart---------#
            pie_chart()
        elif get == 15 :
            #-------Target a comment on user's post caption------#
            caption_comment()
        elif get == 16 :
                #--------Press 9 if u wanna terminate the program------#
            var = False
            print("-----------------------------------------------------------------------------------------------------")

        else :
            print("Please enter a valid number..")




main()








