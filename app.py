import os
import json
import urllib.request
from base64 import b64encode
from flask import Flask, request, jsonify
from urllib.parse import urlparse
import requests
import validators

app = Flask(__name__)

@app.get('/insecure/optimize')
def insecure_optimize_website():
    url = request.json.get('url')    
    response  = urllib.request.urlopen(url)
    html = response.read()
    domain_name = urlparse(url).netloc   
    data_dict = {
        'raw_data': b64encode(html).decode(),
        'domain': domain_name,        
        'url': url
    }
    return jsonify({"data": data_dict}), 200

@app.get('/secure/optimize')
def secure_optimize_website():
    blocked_urls = ['localhost', '127.0.0.1', '169.254.169.254']
    url = request.json.get('url') 
    verify_url = validators.url(url)
    hostname = urlparse(url).hostname      
    if not verify_url or not hostname or hostname in blocked_urls:
        return jsonify({"message": "Invalid URL"}), 400   
    response  = requests.get(url)
    html = response.content
    domain_name = urlparse(url).netloc
    data_dict = {
        'raw_data': b64encode(html).decode(),
        'domain': domain_name,        
        'url': url
    }
    return jsonify({"data": data_dict}), 200    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')    
