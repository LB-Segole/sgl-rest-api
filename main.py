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
api_key = os.getenv("ABUSEIPDB_API_KEY")

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
    response = requests.get(url, headers = {"Key": api_key}, params = {"ipAddress": ip})

    result = response.json()
    score = result ['data']['abuseConfidenceScore']
    flagged = score > 60

    return jsonify ({'ip': ip, 'score': score, 'flagged': flagged})

###### Endpoint 4: File Hashes ######

@app.route('/api/file/hashes', methods = ['POST'])

def file_hash():
    signatures = request.get_json()
    url = ""
    hashes = signatures ['hash(e.g)']
    response = requests.get()

    result = response.json()
    signature = '' #need to find out about their docs on hashes

    # then simple if logic on if == this the rate whether virus or something
    return jsonify ({'hashes': hashes, 'signature': signature})



 
####### Main Execution Block ######
if __name__ == '__main__':
    app.run(debug=True, port=5000)