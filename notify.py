import requests, json, asyncio, time
from discord_webhook import DiscordWebhook
from keyauth import api
import os, hashlib
from datetime import datetime

os.system("cls")









try:
    x = open("webhook.txt",'r')
    x2 = x.read()
    x.close()
    sendwebhook = x2
except:
    x = input("input your webhook -> ")
    x1 = open("webhook.txt",'w')
    x1.write(x)
    x1.close()
    sendwebhook = x

id = input("input user roblox id -> ")
gameid = input("input game id -> ")



onlineurls = []
while True:
    
    
    try:
        fetchthumb = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?size=48x48&format=png&userIds={id}")
        ft = fetchthumb.json()
        ft = ft['data'][0]['imageUrl']
        
        
        allurls = []

        main2 = requests.get(f"https://games.roblox.com/v1/games/{gameid}/servers/Public?sortOrder=Asc&limit=100")
        main = main2.json()['data']

        for i in main:
            t = i['playerTokens']
            store = []
   
            for token in t:
                store.append({ "requestId": f"0:{token}:AvatarHeadshot:48x48:png:regular", "type": "AvatarHeadShot", "targetId": 0, "format": "png", "size": "48x48", "token": token})

            b = requests.post("https://thumbnails.roblox.com/v1/batch",headers={"Content-Type": "application/json"}, data=json.dumps(store))

            b = b.json()

            for i in b['data']:
             allurls.append(i['imageUrl'])

        detected = False

        if ft in allurls:
            detected = True

        if detected == True:
          if id in onlineurls:
            pass
          else:
            onlineurls.append(id)

            webhook = DiscordWebhook(url=sendwebhook, content=f"user -> https://www.roblox.com/users/{id}/profile ] joined the game")
            response = webhook.execute()

        if detected == False:
            if id in onlineurls:
                onlineurls.remove(id)

                webhook = DiscordWebhook(url=sendwebhook, content=f"user -> https://www.roblox.com/users/{id}/profile ] left the game")
                response = webhook.execute()
    except:
        pass
    
