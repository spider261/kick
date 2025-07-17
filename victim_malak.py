import time
import requests
import random

url = "https://kick.com/api/v2/messages/send/16409618"
headers = {
    "Authorization": "Bearer 214176003|8e5NWfg8A3R4XCIdCASqd8Hc0HyTTGCxrNAerKSA",
    "Content-Type": "application/json"
}

emotes = [
    "[emote:3868801:malak01g][emote:3868801:malak01g][emote:3868801:malak01g][emote:3868801:malak01g][emote:3868801:malak01g]",
    "[emote:3868810:malak01we][emote:3868810:malak01we][emote:3868810:malak01we][emote:3868810:malak01we][emote:3868810:malak01we]",
    "[emote:3868782:malak01sh][emote:3868782:malak01sh][emote:3868782:malak01sh][emote:3868782:malak01sh]",
    "[emote:3868787:malak01z][emote:3868787:malak01z][emote:3868787:malak01z][emote:3868787:malak01z]",
    "[emote:3868773:malak01A][emote:3868773:malak01A][emote:3868773:malak01A][emote:3868773:malak01A]",
    "[emote:3868783:malak01f][emote:3868783:malak01f][emote:3868783:malak01f][emote:3868783:malak01f]",
    "[emote:3868793:malak01d][emote:3868793:malak01d][emote:3868793:malak01d][emote:3868793:malak01d]",
    "[emote:3868783:malak01f][emote:3868783:malak01f][emote:3868783:malak01f][emote:3868783:malak01f]",
    "[emote:3868793:malak01d][emote:3868793:malak01d][emote:3868793:malak01d][emote:3868793:malak01d]",
    "[emote:3868775:malak010][emote:3868775:malak010][emote:3868775:malak010][emote:3868775:malak010]",
    "[emote:3868775:malak010][emote:3868775:malak010][emote:3868775:malak010][emote:3868775:malak010]",
    "!points",
    "!xp",
    "!level",
    "سبحان الله وبحمده سبحان الله العظيم",
    "لا اله الا الله وحده لا شريك له له الملك وله الحمد وهو علي كل شئ قدير"
]

for i in range(180):  
    random_emote = random.choice(emotes)
    data = {"content": random_emote, "type": "message"}
    res = requests.post(url, json=data, headers=headers)
    print(f"[{i+1}/180] Sent: {random_emote} | Status: {res.status_code}")
    time.sleep(60)
