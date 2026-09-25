# sgl-threat-api
# A live REST API that analyses passwords, IP addresses, and file hashes against known-bad signatures and returns a real-time security verdict over HTTP.

###### imports ######

import re
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

@app.route('/api/password/check', methods = ['POST'])

def password_check():

    point = 0

    data = request.get_json()
    password = data['password']

    length = len(password)
    if length >= 8:
        point += 4
    else:
        point = 0

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