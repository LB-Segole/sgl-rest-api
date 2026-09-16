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
import re
# import jsonify
import requests
from flask import Flask, jsonify

###### Endpoint 1: Health Check ######

app = Flask (__name__)

@app.route('/api/health', methods = ['GET'])

def health_check():
    return jsonify({'status': 'SGL Threat API is live'}), 200

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)