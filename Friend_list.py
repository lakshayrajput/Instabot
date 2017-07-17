
friend_list = ['danish','yogesh','nitish','shivam','sahil']
def userName():
    var1 = True
    print("Your Friend-List: ")
    count = 1
    for name in friend_list:
         print("                 " +str(count) + "."+name)
         count = count + 1
    name = raw_input("Enter the username: ")
    while name.isalpha() is not True :
        name = raw_input("Name only contain character b/w (a-z or A-Z): ")
    while var1 == True :
        if name in friend_list :
            var1 = False
        else :
            name = raw_input("Please enter a valid name from your Friend-List: ")
    return name
