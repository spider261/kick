import time
import requests
import random

url = "https://kick.com/api/v2/messages/send/16409618"
headers = {
    "Authorization": "Bearer 206436231|QKzw7hIEv0tBUTl89p1Ugq8kAn6NS1RteXGxfMRj",
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
    "!level"
]

for i in range(720):  
    random_emote = random.choice(emotes)
    data = {"content": random_emote, "type": "message"}
    res = requests.post(url, json=data, headers=headers)
    print(f"[{i+1}/180] Sent: {random_emote} | Status: {res.status_code}")
    time.sleep(6)
