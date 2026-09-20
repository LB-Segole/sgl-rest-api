# password =  "password1234"

# for x in password:
#     print(f"{x}")



    # what's the logic i need to use here?




# password = input("")

# for x in password:
#     if x >= 8 characters
#         return



# ??? something like this?

# or



# password = input("")

# while password >= 8 characters
#     return 



# but what do we need it to return?
# should it not proceed to other check?

# so something like this?



# password = input("")
# while password >= 8 characters
#     continue



# nah i get the instict that it should be a for loop not a while loop
# why? because the conditions are known, that when a password has 8 or more characters it continues

# therefore:
# password = "" # no need for input actually since we don't use cli to check
# but for the sake of the testing now, let's use it

# questions, how do you check how many characters does something have? or rather, what's the syntax for it
# because to check how many characters it has, a for loop is perfect
# now how do we read that?


# password = input("Password:")

# for x in password:
#     if x >= 8 #(this is just wrong):
#         continue
#     else:
#         print(f"Password should have 8 or more characters")


# TypeError: '>=' not supported between instances of 'str' and 'int'

# so how the hell do i check the number of characters? 

# okei, so i'm doing too much, there's a simple built-in function
# that looks up the lengths of characters, so let's try that

def password_check():

    point = 0

    data = request.get_json()
    password = data['password']
    length = len(password)

    if length >= 8:
        point += 4

    else:
        point = 0

    #length check done, now for upper case
    upper = any(char.isupper() for char in password)
    if upper == True:
        point += 1.5

    return jsonify ({'point': point }), 200

"""
the outer password = input(...) creates a real string. 
That string gets handed into the function through the parentheses at the call site. 
Inside the function, the parameter password is just a local name pointing at that same string, for the duration of the function's run.
"""
# rules to remember: 
# A function is like a machine. You put it in, it gives you something out. 
# To keep what it gives you, you catch it in a box (a variable); but you catch it
# outside the machine, not inside it.

# Check the def line's brackets. Copy what's there into your call's brackets. 
# Nothing there? Nothing goes in.

# okei cool, so the above only prints the else statement but not the proceed
# makes sense cause if the password doesn't meet the required conditions
# oh and i need to loop that if the password doesn't meet the condition yoou MUST retry, but 
# that's not in the description of the first version tbf, so let's pause a bit on that, we'll that perhaps in v 1.1

# so with that in mind, this works well enough, now for the point system... fuck
# conditions work well, cool, 
# now:

# if length >= 8:
#     point = +4
# else:
#     point = +0

# this feels good

# then at the end we add all the points together out of 10
# but how does it know which point belongs to which?
# does it mean it has to be under a function?

# oh right yes, hence we have functions, at the end we add all the function results to there
# so the functions' results should return a number/ point