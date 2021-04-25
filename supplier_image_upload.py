#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module
os.chdir('</path/to/images>')
files = [f for f in os.listdir('.') if f.endswith('.jpeg')]
print(files)
url = "http://localhost/upload/"
for file in files:
    with open(file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})