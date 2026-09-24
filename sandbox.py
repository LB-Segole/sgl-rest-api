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

# password = input("Password:")

# def password_check(password):

#     length = len(password)

#     if length >= 8:
#         return 4

#     else:
#         return 0

# length_points = password_check(password)

# print(f"{length_points}")

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
# import os
# from dotenv import load_dotenv

# def ip_rep():
#     load_dotenv("ABUSEIPDB_API_KEY") # No, but why? ohh we're loading the import
#     #reads .env files and adds variables inside environment
#     os.getenv('PROJECT_API_KEY') # fetches api key from insde the .env file

# print(f"{ip_rep}")

"""
Fetch the API key from the environment (once, near the top of the file to avoid multiple requests)
Build the outgoing request: URL, headers (with the key), and params (with the IP) all together, since requests.get() needs all three at once
Send the request to AbuseIPDB
Read the response back as JSON
Pull out abuseConfidenceScore from inside data
Decide your own threshold: pick the number now, out of 100, above which you call an IP "flagged"
Compare the score to your threshold
Build my own jsonify response using ip, the score, and your flagged true/false verdict
"""

import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

def ip_rep():
    # no.1: fetch API key
    load_dotenv()

    api_key = os.getenv("ABUSEIPDB_API_KEY") # but has to  be above, not just in fuction, we'll fix it
    # no.1 done

    #no.2 : outgoing requests. # POST right? Yes: submits an entity to the specified resource
    # oh no, we're not giving them something, we're asking and getting somthing from them, so we use the GET
    # i need the url to post to and based on docs: https://api.abuseipdb.com/api/v2/check
    # what are we sending? the ip, the url and what else? the type of data we want back which is a json. what else?
    url = "https://api.abuseipdb.com/api/v2/check"
    ip = input("") # for testing sake we'll have an input
    response = requests.get({'key': api_key, 'url': url, 'ip address': ip})
    # wrong according to docs

    # we can do this, store the values in variables or a list/ dict, then call the list in the requests.get


# cleaner version:

import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()
api_key = os.getenv("ABUSEIPDB_API_KEY")

def ip_rep():
    data = request.get_json() # i don't fully understand here: flask module knowledge gap
    url = "https://api.abuseipdb.com/api/v2/check"
    ip = data ['ip'] # i don't fully understand here: flask gap again
    response = requests.get(url, headers = {"Key": api_key}, params = {"ipAddress": ip})

    return jsonify({'report': response.json()}) # needs to be captured

# since i specifically need to score it and have my own threshold

#complete version of endpoint 3

import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()
api_key = os.getenv("ABUSEIPDB_API_KEY")

def ip_rep():
    data = request.get_json() # i don't fully understand here: flask module knowledge gap
    url = "https://api.abuseipdb.com/api/v2/check"
    ip = data ['ip'] # i don't fully understand here: flask gap again
    response = requests.get(url, headers = {"Key": api_key}, params = {"ipAddress": ip})
    result = response.json()
    score = result ['data']['abuseConfidenceScore']
    flagged = score > 60
    return jsonify ({'ip': ip, 'score': score, 'flagged': flagged})
