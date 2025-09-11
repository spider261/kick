import time
import requests
import random

url = "https://kick.com/api/v2/messages/send/29224752"
headers = {
    "Authorization": "Bearer 206436231|QKzw7hIEv0tBUTl89p1Ugq8kAn6NS1RteXGxfMRj",
    "Content-Type": "application/json"
}

emotes = [
      "[emote:39261:kkHuh]",
    "[emote:4147902:KEKBye]",
    "[emote:37225:KEKLEO]",
    "[emote:37226:KEKW]",
    "[emote:2824545:3mrefr7o]",
    "[emote:37218:Clap]",
    "[emote:37232:PeepoClap]",
    "[emote:2824546:3mrnoata]",
    "[emote:4148128:mericCat]",
    "[emote:4147910:BBoomer]",
    "[emote:2824546:3mrnoata]",
    "[emote:37248:ratJAM]",
    "[emote:37245:peepoDJ]",
    "[emote:39261:kkHuh]",
    "[emote:4147902:KEKBye]",
    "[emote:37225:KEKLEO]",
    "[emote:37226:KEKW]",
    "[emote:2824545:3mrefr7o]",
    "[emote:37218:Clap]",
    "[emote:37232:PeepoClap]",
    "[emote:2824546:3mrnoata]",
    "[emote:4148128:mericCat]",
    "[emote:4147910:BBoomer]",
    "[emote:2824546:3mrnoata]",
    "[emote:37248:ratJAM]",
    "[emote:37245:peepoDJ]",
    "[emote:39261:kkHuh]",
    "[emote:4147902:KEKBye]",
    "[emote:37225:KEKLEO]",
    "[emote:37226:KEKW]",
    "[emote:2824545:3mrefr7o]",
    "[emote:37218:Clap]",
    "[emote:37232:PeepoClap]",
    "[emote:2824546:3mrnoata]",
    "[emote:4148128:mericCat]",
    "[emote:4147910:BBoomer]",
    "[emote:2824546:3mrnoata]",
    "[emote:37248:ratJAM]",
    "[emote:37245:peepoDJ]",
    "!shop",
    "!top",
    "!points"


]

# Calculate the number of iterations needed for 3 hours
# 3 hours = 180 minutes
# Each message is sent every 2 minutes (120 seconds)
# So, total iterations = 180 minutes / 2 minutes/iteration = 90 iterations
num_iterations = 300

# Loop to send messages
for i in range(num_iterations):
    # Randomly select an emote or command from the list
    random_emote = random.choice(emotes)

    # Prepare the data payload for the POST request
    data = {"content": random_emote, "type": "message"}

    # Send the POST request to the Kick.com API
    res = requests.post(url, json=data, headers=headers)

    # Print the status of the sent message
    print(f"[{i+1}/{num_iterations}] Sent: {random_emote} | Status: {res.status_code}")

    # Wait for 120 seconds (2 minutes) before the next iteration
    time.sleep(120)

print("Script finished after 3 hours.")
