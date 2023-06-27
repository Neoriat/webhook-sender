import requests
import colorama as color
import platform
from os import system
from time import sleep
   
def clear(): # Clear 
    match platform.system():
        case "Windows":
            system("cls")
        case "Linux":
            system("clear")

def is_webhook_url(webhook_url): # Check if the url is valid and a webhook url indeed
    allowed_url = ("https://ptb.discord.com/api/webhooks/" , "https://discord.com/api/webhooks/")

    if webhook_url.startswith(allowed_url):
        return True
    else:
        return False
        
    
def send_message(url , content): # Function for sending a message
    data = {"content":content}
    global response
    response = requests.post(url=url , json=data)

def chat_as_webhook(): # Function for chat
    clear()
    url = input("Enter the webhook url:") # get the webhook
    if is_webhook_url(url): # if it return true
        while True: # continue until message is equal to q or quit
            message = input("Enter your message(Enter 'q' to exit):")
            match message:
                case "q":
                    break
                case _:
                    send_message(url=url , content=message) # sends the messsage to discord
                    

        clear()   
        main() # after the loop ends will return you to the main menu
    else:
        print("Not valid url")
        sleep(2)
        chat_as_webhook() # if the function returned false it will do the function again

def spam_webhook():# Spam the webhook
    clear()
    url = input("Enter the webhook url:") # get the webhook
    if is_webhook_url(url):
        message = input("Enter the message:")
        count = int(input("How many messages you want to send:"))
        
        for num in range(count):
            send_message(url=url , content=message)
        print(color.Fore.GREEN + "Completed")
        sleep(1)
        clear()
        main()
    else:
        clear()  
        spam_webhook()

def send_single_message():
    clear()
    url = input("Enter the webhook url:") # get the webhook
    if is_webhook_url(url): # if it return true
         # continue until message is equal to q 
        message = input("Enter your message:")
        send_message(url=url , content=message) # sends the messsage to discord
        clear()   
        main() # after the loop ends will return you to the main menu
    else:
        print("Not valid url")
        sleep(2)
        send_single_message()

def main():# Main Menu
    print( color.Fore.RED + """

__________________________________________                                   
|                 .                       |
|       _     _ .'|                       |
| /\    \\   //<  |                        |
| `\\  //\\ //  | |                         |
|   \`//  \'/   | | .'''-.         _       |
|    \|   |/    | |/.'''. \      .' |     | 
|     '         |  /    | |     .   | /   |
|               | |     | |   .'.'| |//   |
|               | |     | | .'.'.-'  /    |
|               | '.    | '..'   \_.'     |
|               '---'   '---'             |
|_________________________________________|
|                                         |
|1) Chat as a webhook                     |
|2) Spam a webhook                        |
|3) Send a single message                 |
|                                         |
|_________________________________________|    

    """)
    global option
    option = input( color.Fore.RED + "Choose a option:")
    
    clear()
    match option:
        case "1":
            chat_as_webhook()
            clear()
        case "2":
            spam_webhook()
        case "3":
            send_single_message()
        case _:
            print("Not a valid option")
            sleep(2)
            main()
    
main()
