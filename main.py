from Self_info import self_info
from Get_own_post import get_own_post
from Get_user_id import get_user_id
from Get_user_info import get_user_info
from Get_user_post_info import get_user_post_info
from Like_a_post import like_a_post
from Post_a_comment import post_a_comment



#--------------------------------------------------MAIN FUNCTION---------------------------------------#
def main():
    var = True
    while var :
        print("--------------------------------------------------------------------------------------------------------------")
        print(" What do you want to do ?.\n 1.Self-information...\n 2.Get own-post...\n 3.Get user-id...\n 4.Get user-info...\n 5.Get user post-info...\n 6.Like a user-post...\n 7.Post a comment on user-id...\n 8.Exit")
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
        elif get ==7 :
            post_a_comment()
        elif get == 8 :
            var = False
            print("-----------------------------------------------------------------------------------------------------")

        else :
            print("Please enter a valid number..")




main()








