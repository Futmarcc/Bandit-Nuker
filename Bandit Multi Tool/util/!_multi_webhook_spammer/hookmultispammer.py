import requests
import os.path
import os
import time
import colorama
from colorama import Fore, init, Back, Style

os.system("title     Webhook Multi Spammer     $     Marcc#6666")

def hook():
	try:
		if os.path.exists('./webhooks.txt') == True:
			if os.stat("webhooks.txt").st_size == 0:
				print(f"\n{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} webhooks.txt not found!")
			else:
				content = input(f'{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Webhook Messages: ')
				while True:
					for line in open('webhooks.txt'):
						line = line.strip()
						req = requests.post(
							line,
							json = {
								"content": content
							}
						)
						statusCode = str(req.status_code)
						if statusCode.startswith('2') == True:
							print(f'{Fore.RED}[{Fore.RESET}' + str(req.status_code) + f'{Fore.RED}]{Fore.RESET}' + ' Message successfully sent.')
						elif statusCode.startswith('4') == True:
							if statusCode == '429':
								retry = int(req.headers['retry-after']) / int(1000)
								print(f'\n{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} Ratelimited next try in ' + str(retry) + ' seconds.\n')
								time.sleep(retry)
							else:
								print('[' + str(req.status_code) + ']' + ' Message not sent.')
		elif os.path.exists('./webhooks.txt') == False:
			print(f'\n{Fore.RED}[{Fore.RED}?{Fore.RED}]{Fore.RESET} webhooks.txt not found!')
	except KeyboardInterrupt:
		print('\nExiting...')
		exit()

hook()