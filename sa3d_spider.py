import time
import requests
import random

url = "https://kick.com/api/v2/messages/send/15423903"
headers = {
    "Authorization": "Bearer 207575384|VM2TjP93pkyfOxxlZb9zeKt5eNRRHtj5qeooggnC",
    "Content-Type": "application/json"
}

emotes = [
    "[emote:2728414:sa3dolaEZ]",
    "[emote:2728417:sa3dolaHEHE]",
    "[emote:2728420:sa3dolaPERFECTO]",
    "[emote:2728416:sa3dolaRokba]",
    "[emote:2728422:sa3dolaZ3eem]",
    "[emote:37218:Clap]",
    "[emote:37232:PeepoClap]",
    "[emote:2728418:sa3dolaCLOWN]",
    "!shop",
    "!top",
    "!points"

   
]

# Calculate the number of iterations needed for 3 hours
# 3 hours = 180 minutes
# Each message is sent every 2 minutes (120 seconds)
# So, total iterations = 180 minutes / 2 minutes/iteration = 90 iterations
num_iterations = 120

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
