
import requests
import colorama as color
import json
from time import sleep
from sys import exit

# Get the webhook url from the user
with open("config.json" ,"r" ) as f:
    
    config = json.load(f)
if config["url"] == "None":
    webhook_url = input(color.Fore.CYAN + "Enter the webhook url:")
else:
    webhook_url = config["url"]


#Get the message from the user
allowed_url = ["https://ptb.discord.com/api/webhooks/" , "https://discord.com/api/webhooks/" ]

if webhook_url not in webhook_url :
    color.Fore.RED
    raise Exception("Not a valid url")
    

def send_message(url , message): #sends the message
    
    try:
        response = requests.post(url , json=message) #send message
        print(color.Fore.YELLOW + "Sending...")
        sleep(1)
        print(color.Fore.RESET)
    except:
        print(color.Fore.RED + "something went wrong")
        print(color.Fore.RESET) 
        exit()
        
    else:
        print(color.Fore.GREEN + "You message was sent")
        print(color.Fore.RESET) 

count = config["times_to_send"]

if count <= 0:
    raise Exception("No zero or minus numbers allowed")
    
    

for num in range(0 , count):

    if config["message"] == "None":
        message = input(color.Fore.CYAN + "What message do you want to send:")
    else:
        message = config["message"]
    
    data = {"content": message} # The message


    send_message(webhook_url , data)





   

    
        
