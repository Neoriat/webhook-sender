
import requests
import colorama as color

# Get the webhook url from the user
webhook_url = input(color.Fore.CYAN + "Enter the webhook url:")
#Get the message from the user

if "https://discord.com/api/webhooks/" not in webhook_url:
    color.Fore.RED
    raise Exception("Not a valid url")
    

while True:
    message = input(color.Fore.CYAN + "What message do you want to send:")

    data = {"content": message} # The message


    def send_message(url , message): #sends the message
        response = requests.post(url , json=message)
    try:
        send_message(webhook_url , data) #send message
        print(color.Fore.YELLOW + "Sending...")
        print(color.Fore.RESET)
    except:
        print(color.Fore.RED + "something went wrong")
        print(color.Fore.RESET) 
        
    else:
        print(color.Fore.GREEN + "You message was sent")
        print(color.Fore.RESET) 
    
        
