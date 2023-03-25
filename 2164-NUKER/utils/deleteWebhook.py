import requests
from utils.common import *

def deleteWebhook(url):
    set_console_title("2164 V1 | Made by .gg/2164 | Delete Webhook")
    requests.delete(url)
    print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}C{Fore.WHITE}] Deleted Webhook")
    sleep(1)