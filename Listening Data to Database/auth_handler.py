import requests
from random import randint
import urllib
from selenium import webdriver
from listen_auth_localhost import listen_callback
import base64
import time

CLIENT_ID = '';
CLIENT_SECRET = ""
REDIRECT_URI = 'http://127.0.0.1:1111/';
POSSIBLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
SCOPE = 'user-read-recently-played user-top-read';

def generateRandomString(length):
    return "".join(POSSIBLE[randint(0, len(POSSIBLE)-1)] for i in range(length))

def write_to_file(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()

def oauth_user():
    state = generateRandomString(16);
    driver = webdriver.Chrome()
    driver.get('https://accounts.spotify.com/authorize?' +
        urllib.parse.urlencode({
          "response_type": 'code',
          "client_id": CLIENT_ID,
          "scope": SCOPE,
          "redirect_uri": REDIRECT_URI,
          "state": state
    }));
    callback_query = listen_callback()
    if callback_query["state"][0] != state:
        return {"error": "state_mismatch"}
    if "error" in callback_query:
        return {"error": "Unknown error. Try again?"}
    driver.quit()

    body = {
                "grant_type": "authorization_code",
                "code" : callback_query["code"][0],
                "redirect_uri" : REDIRECT_URI,
            }
    headers = {
                "Authorization" : "Basic " + base64.b64encode((CLIENT_ID + ":" + CLIENT_SECRET).encode()).decode("utf-8"),
                "Content-Type" : "application/x-www-form-urlencoded",
            }
    token_req = requests.post("https://accounts.spotify.com/api/token", data = body, headers = headers)
    token_req_json = token_req.json()
    write_to_file("refresh_token.txt", token_req_json["refresh_token"])
    return token_req_json["access_token"]

def auth_refresh_token():
    refresh_token_file = open("refresh_token.txt", "r")
    refresh_token = refresh_token_file.read()
    refresh_token_file.close()
    if not refresh_token:
        return oauth_user()
    body = {
                "grant_type": "refresh_token",
                "refresh_token" : refresh_token,
            }
    headers = {
                "Authorization" : "Basic " + base64.b64encode((CLIENT_ID + ":" + CLIENT_SECRET).encode()).decode("utf-8"),
                "Content-Type" : "application/x-www-form-urlencoded",
            }

    refresh_req = requests.post("https://accounts.spotify.com/api/token", headers = headers, data=body)
    refresh_req_json = refresh_req.json()
    if "refresh_token" in refresh_req_json.keys():
        write_to_file("refresh_token.txt", refresh_req_json["refresh_token"])
    return refresh_req_json["access_token"]

token_cache = {0:""}
def get_token():
    freshest_token_key = max(token_cache, key=token_cache.get)
    if time.time() > freshest_token_key:
        try:
            token = auth_refresh_token()
        except FileNotFoundError:
            token = oauth_user()
        token_cache[int(time.time())+3000] = token
    else:
        token = token_cache[freshest_token_key]
    return token
    
