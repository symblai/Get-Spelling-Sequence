import requests
import os
import json
import uuid
from datetime import datetime
from os.path import join, dirname
from dotenv import load_dotenv
import re


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
conversationId = "<Add Your Symbl ConversationId>"

def getWordLevelMessage(conversationId,token):
    url = "https://api.symbl.ai/v1/conversations/{0}/messages?verbose=true".format(conversationId)
    
    payload = ""
    headers = {
    'x-api-key':accessToken,
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return(response.json())



#Generate Symbl Token
def getAuthKey():
    url = "https://api.symbl.ai/oauth2/token:generate"
    payload = json.dumps({
    "type": "application",
            "appId": os.environ.get("APP_ID"),# appId
            "appSecret": os.environ.get("APP_SECRET"),  # appSecretId
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return(response.json())

def getSpellingSequense(wordLevelmessages):
    for item in wordLevelmessages["messages"]:
        prev = 0
        for words in item["words"]:
            s = re.sub(r'[^\w\s]','',words["word"]).lower()
            # Spelling is <letter> "like" <word>
            if s.lower() == "like":
                prev = 2
            # Spelling is <letter> "like a" <word>
            elif prev == 2 and words["word"] == "a":
                prev = 2    
            elif words["word"] == "as":
                prev = 1
            # Spelling is <letter> "as a" <word>
            elif prev == 1 and words["word"] == "a":
                prev = 2           
            # Spelling is <letter> "as in" <word>
            elif prev == 1 and words["word"] == "in":
                prev = 2
            # print the spelled letter
            elif prev == 2:
                print(words["word"][0].lower())
                prev = 0
            else:
                prev = 0

accessToken = getAuthKey()["accessToken"]
wordLevelmessages = getWordLevelMessage(conversationId,accessToken)
getSpellingSequense(wordLevelmessages)
