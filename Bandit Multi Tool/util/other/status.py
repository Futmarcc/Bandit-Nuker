import sys, os, time, requests, random
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class Discord:
    
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "*/*"
        }

    def ChangeStatus(self, status, message):
        jsonData = {
            "status": status,
            "custom_status": {
                "text": message,
        }}
        r = requests.patch("https://discord.com/api/v8/users/@me/settings", headers=self.headers, json=jsonData)
        return r.status_code

def Run(discord, status,):
    discord = discord
    message = random.choice(list(open('messages.txt')))
    message = message.replace('\r', '').replace('\n', '')
    status_code = discord.ChangeStatus(status, message)
    if status_code == 200:
        print("|———————————————————————————————————|")
        print("  Changed your status! ")
        print(f"  Status: {message}")
        print("|———————————————————————————————————|]")
    else:
        print("An error occured. Try again?")

def Main():
    TOKEN = os.environ.get("TOKEN")
    discord = Discord(TOKEN)
    while True:
        Run(discord, "online") # Change circle status | dnd, idle, online
        time.sleep(3)

if __name__ == "__main__":
    Main()
else:
    filename = os.path.basename(sys.argv[0])
    print(f"{filename} is being imported into another module.")