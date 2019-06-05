import requests
import json

token = "55d87efda345913f136102ce791c622ffe7341c74dcb4790c9d0e463edc831d1"
headers = {"Authorization": token}
r =requests.get('https://api.ciscopark.com/v1/people/me', headers = headers)
r.status_code