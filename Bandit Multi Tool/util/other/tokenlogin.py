import os, sys, ctypes, time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import colorama
from colorama import Fore, init, Back, Style

os.system("title     Token Login     $     Marcc#6666")

token = input(f'{Fore.RED}[{Fore.GREEN}-->{Fore.RED}]{Fore.RESET} Discord Token: ')
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://discord.com/login')
js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
driver.execute_script(js + f'login("{token}")')