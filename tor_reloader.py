# Tor Project Ip Changer For Web Scraping
# written by Kadir Yaren 
# ------------- Description -------------
# use only 60s or more to change your ip otherwise it won't change your ip
# ------------- Usage -------------
# python3 tor_reloader.py
# ------------- Example -------------
# python3 tor_reloader.py
# ------------- Version -------------
# v1.0
# ------------- Changelog -------------
# v1.0
# ------------- License -------------
# MIT License

import os 
import time 
from sys import platform
import requests
from colorama import init
from termcolor import colored


#  be sure your internet service provider supports tor! its impoirtant for this script
# For ubuntu systems do these steps:
# 1. sudo apt install tor
# 2. sudo systemctl start tor.service




def change_ip(reload_time):

    # tor proxy yenilenme aninda istek atmiyor 
    # bu yuzden yenilerken istek atmasin diye 5 saniye bekliyoruz
    # ardindan istek atiyoruz


    if platform == "linux" or platform == "linux2":
        while(True):

            os.system("sudo systemctl  reload tor.service")
            time.sleep(5)
            response = requests.get("http://ip-api.com/json/?fields=61439",proxies=dict(http="socks5://127.0.0.1:9050",https="socks5://127.0.0.1:9050")).json()["query"]
            print(colored(f"Reloaded Tor! Now Your Ip is {response}", 'green', 'on_red'))
        
            time.sleep(reload_time-5)
    elif platform == "darwin":
        # MACOSX
        while(True):
            os.system("brew services reload tor")
            time.sleep(5)
            response = requests.get("http://ip-api.com/json/?fields=61439",proxies=dict(http="socks5://127.0.0.1:9050",https="socks5://127.0.0.1:9050")).json()["query"]
            print(colored(f"Reloaded Tor! Now Your Ip is {response}", 'green', 'on_red'))
       
            time.sleep(reload_time-5)
    else:
        print("Your OS is not supported")
    
    


if __name__=="__main__":
    init() # for colorama
    TIME = 60
    change_ip(TIME)


# ==> Successfully started `tor` (label: homebrew.mxcl.tor)
# Service `tor` already started, use `brew services restart tor` to restart.
# Stopping `tor`... (might take a while)\n
# ==> Successfully stopped `tor` (label: homebrew.mxcl.tor)
# Warning: Service `tor` is not started.
#output = os.popen('brew services start tor').read()

