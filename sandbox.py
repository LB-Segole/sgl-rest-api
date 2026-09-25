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

# import os
# import requests
# from dotenv import load_dotenv
# from flask import Flask, jsonify, request

# def ip_rep():
#     # no.1: fetch API key
#     load_dotenv()

#     api_key = os.getenv("ABUSEIPDB_API_KEY") # but has to  be above, not just in fuction, we'll fix it
#     # no.1 done

#     #no.2 : outgoing requests. # POST right? Yes: submits an entity to the specified resource
#     # oh no, we're not giving them something, we're asking and getting somthing from them, so we use the GET
#     # i need the url to post to and based on docs: https://api.abuseipdb.com/api/v2/check
#     # what are we sending? the ip, the url and what else? the type of data we want back which is a json. what else?
#     url = "https://api.abuseipdb.com/api/v2/check"
#     ip = input("") # for testing sake we'll have an input
#     response = requests.get({'key': api_key, 'url': url, 'ip address': ip})
    # wrong according to docs

    # we can do this, store the values in variables or a list/ dict, then call the list in the requests.get


# cleaner version:

# import os
# import requests
# from dotenv import load_dotenv
# from flask import Flask, jsonify, request

# load_dotenv()
# abuse_api_key = os.getenv("ABUSEIPDB_API_KEY")
# virus_api_key = os.getenv("VIRUSTOTAL_API_KEY")

# def ip_rep():
#     data = request.get_json() # i don't fully understand here: flask module knowledge gap
#     url = "https://api.abuseipdb.com/api/v2/check"
#     ip = data ['ip'] # i don't fully understand here: flask gap again
#     response = requests.get(url, headers = {"Key": abuse_api_key}, params = {"ipAddress": ip})

#     return jsonify({'report': response.json()}) # needs to be captured

# since i specifically need to score it and have my own threshold

#complete version of endpoint 3

# import os
# import requests
# from dotenv import load_dotenv
# from flask import Flask, jsonify, request

# load_dotenv()
# api_key = os.getenv("ABUSEIPDB_API_KEY")

# def ip_report():
#     data = request.get_json() #client hands me a note and asks me to check if the ip is trustworthy # i don't fully understand here: flask module knowledge gap
#     url = "https://api.abuseipdb.com/api/v2/check" # i pick up the phone and dial this number (url) to the AbuseIPDB office to check about the IP
#     ip = data ['ip'] # in the note i got, i'm only looking at the value next to ip and ignoring therest of the contents on the note while the phone is ringing
#     response = requests.get(url, headers = {"Key": api_key}, params = {"ipAddress": ip}) # when the AbuseIPDB office answer's the phone, i tell them that hey, i just dialed your number (url), 
#     # here's my ID badge number to prove i have authorisation to ask (header: api key),  and here's the ip i want you to look up for me (params: which is the number next to the words ip i am looking at on the customer's note)
#     # they say they'll check and send me an email
#     result = response.json() # they sent me an email and i just opened it and read it
#     score = result ['data']['abuseConfidenceScore'] # it's a long document so i look for exactly where it tells me the risk number of the ip the customer just gave me
#     flagged = score > 60 # i'm shocked at what i see so i make a rule based on my experience that any score above 60 is a risk
#     return jsonify ({'ip': ip, 'score': score, 'flagged': flagged}) # then i finnally relay the message to the customer to say whether the ip is safe or not, based on my expertise


import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()
abuse_api_key = os.getenv("ABUSEIPDB_API_KEY")
virus_api_key = os.getenv("VIRUSTOTAL_API_KEY")
'''
Here the case is a bit different:
the client still hands me a note to ask me to check the hash
but immediately when i dial the number to the VirusTotal, they already know the hash i'm asking them about
but i still have to ptovide my ID badge number
then in their email to me, i have to go through layers of documentation
then i dentify which of the 4 counts does the hash i found belong to
i also have to determine just in case, what to respond to my client, if the hash has never been submitted to VirusTotal
then also based on my expertise, determine whether the hash is cool or not to my client
then return/give them my report that answers their question
'''
# 1st attempt

# def file_hash():
#     data = request.get_json()
#     url = "https://www.virustotal.com/api/v3/files/{hash}"
#     response = requests.get({'x-apikey': virus_api_key})
#     if response == 404:
#         return "Hash not found"
#     result = response.json() #need to set a condition incase of a 404 before this (done)
#     score = result['data'] ['attributes'] ['last_analysis_stats']
#     # condition for what's bad or not
#     flag  = 
#     return jsonify ({'hash': {hash}, 'score': score,'flagged': flag}, )

#     result = response.json()
#     signature = '' #need to find out about their docs on hashes

#     # then simple if logic on if == this the rate whether virus or something
#     return jsonify ({})


# # 2nd attempt

# def file_hash():
#     data = request.get_json()
#     hash = data['hash']
#     url = f"https://www.virustotal.com/api/v3/files/{hash}"
#     response = requests.get(url, headers = {"Key": virus_api_key})
#     # code = response.status_code
#     if response.status_code == 404:
#         return "Hash not found"
#     result = response.json() #need to set a condition incase of a 404 before this (done)
#     print (f'{result}')
#     score = result['data'] ['attributes'] ['last_analysis_stats'] # no need to create conditions
#     # i can say if score == malicious print malicious etc.
#     # condition for what's bad or not
#     flag  = # then meaning no need for flag. unless i find out what types to ranking is given for each of the 4,
#     # but i can use their rules, which is honestly safer since i don't know much about hashes
#     return jsonify ({'hash': {hash}, 'score': score,'flagged': flag}, )

#     # then simple if logic on if == this the rate whether virus or something
#     return jsonify ({})

# # sandy
# # 2nd attempt

# def file_hash():
#     data = request.get_json()
#     url = "https://www.virustotal.com/api/v3/files/{hash}"
#     response = requests.get({'x-apikey': virus_api_key})
#     if response == 404:
#         return "Hash not found"
#     result = response.json() #need to set a condition incase of a 404 before this (done)
#     score = result['data'] ['attributes'] ['last_analysis_stats']
#     print (f'{score}')
#     # condition for what's bad or not
#     return jsonify ({'hash': {hash}, 'score': score}, )

#     # then simple if logic on if == this the rate whether virus or something
#     return jsonify ({})


# 3rd attempt

# def file_hash():
#     data = request.get_json()
#     file_hash = data['hash']
#     url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
#     response = requests.get(url, headers = {"x-apikey": virus_api_key})
#     # code = response.status_code
#     if response.status_code == 404:
#         return ({'error': 'Hash not found'}), 404
#     result = response.json()
#     print (f'{result}')
#     score = result['data'] ['attributes'] ['last_analysis_stats'] # no need to create conditions

#     return jsonify ({'hash': file_hash, 'score': score} )

# reason for not flagging scores: more alignment to the long term goal of the threat hunter


# final clean and revised version

def file_hash ():

    data = request.get_json()
    file_hash = data ['hash']

    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    response = requests.get(url, headers = {"x-apikey": virus_api_key})

    if response.status_code == 404:
        return jsonify ({'error': 'Hash not found'}), 404
    
    result = response.json()
    score = result['data'] ['attributes'] ['last_analysis_stats']

    return jsonify ({'hash': file_hash, 'score': score})

# add error handling for other types of errors outside 200 and 404

# final clean and revised version

def file_hash ():

    data = request.get_json()
    file_hash = data ['hash']

    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    response = requests.get(url, headers = {"x-apikey": virus_api_key})

    if response.status_code != 200:
        error_body = response.json()
        vt_message = error_body.get('error', {}).get('message', 'Unknown error')
        return jsonify ({'error': vt_message}), response.status_code
    
    result = response.json()
    score = result['data'] ['attributes'] ['last_analysis_stats']

    return jsonify ({'hash': file_hash, 'score': score})

# i'll add specific errors later but so far it's defensible
# though for now, what if i add the error explantion
# what is the dict/key value i need to pull

'''
# sgl-threat-api
# A live REST API that analyses passwords, IP addresses, and file hashes against known-bad signatures and returns a real-time security verdict over HTTP.

# how do we start with this?
""" first there's the imports
then we come with the health check endpoint
then the password strength checker endpoint
then the ip reputation checker endpoint
then it's the file hashes checker endpoint
the run analysis
the run entire script
"""
###### imports ######

import re # allows for searching strings for patterns
# import jsonify
import requests
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

###### API call ######

load_dotenv()
abuse_api_key = os.getenv("ABUSEIPDB_API_KEY")
virus_api_key = os.getenv("VIRUSTOTAL_API_KEY")

###### Endpoint 1: Health Check ######

app = Flask (__name__)

@app.route('/api/health', methods = ['GET'])

def health_check():
    return jsonify({'status': 'SGL Threat API is live'}), 200

###### Endpoint 2: Password Strength Check ######

# @app.route('/api/password/check', methods = ['GET'])
# checked the dicuments it's post not get since the rules have to be checked against the password so they have to saty in the server
@app.route('/api/password/check', methods = ['POST'])



# def password_strength(): # functions that checks the conditions for the password, requirements in note
# we can use re module instead of looping manually, but for learning's sake let's try the manual looping
# how do we loop again? for/ while loops

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

    lower = any(low.islower() for low in password)
    if lower == True:
        point += 1.5

    digit = any(num.isdigit() for num in password)
    if digit == True:
        point += 1.5

    special = any(not char.isalnum() for char in password)
    if special == True:
        point += 1.5

    # tier = sum([length, upper, lower, digit, special])

    tier = point

    if tier < 4:
        tier = 'Weak'

    elif tier <= 7:
        tier = 'Medium'

    else:
        tier = 'Strong'

    return jsonify ({'point': point, 'tier': tier }), 200

###### Endpoin 3: IP Reputation ######

@app.route('/api/ip/check', methods = ['POST'])

def ip_check():

    data = request.get_json() 
    url = "https://api.abuseipdb.com/api/v2/check"
    ip = data ['ip']
    response = requests.get(url, headers = {"Key": abuse_api_key}, params = {"ipAddress": ip})

    result = response.json()
    score = result ['data']['abuseConfidenceScore']
    flagged = score > 60

    return jsonify ({'ip': ip, 'score': score, 'flagged': flagged})

###### Endpoint 4: File Hashes ######

@app.route('/api/file/hashes', methods = ['POST'])

def file_hash ():

    data = request.get_json()
    file_hash = data ['hash']

    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    response = requests.get(url, headers = {"x-apikey": virus_api_key})

    if response.status_code != 200:
        error_body = response.json()
        vt_message = error_body.get('error', {}).get('message', 'Unknown error')
        return jsonify ({'error': vt_message}), response.status_code
    
    result = response.json()
    score = result['data'] ['attributes'] ['last_analysis_stats']

    return jsonify ({'hash': file_hash, 'score': score})

 
####### Main Execution Block ######
if __name__ == '__main__':
    app.run(debug=True, port=5000)
'''