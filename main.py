import os
import random
import httpx
import threading
import time
from colorama import Fore as C

os.system("cls")
print(C.RED + """
    .___                                 
  __| _/______ ____         ____   ____  
 / __ |/  ___// ___\       / ___\ / ___\ 
/ /_/ |\___ \\  \___      / /_/  > /_/  >
\____ /____  >\___  > /\  \___  /\___  / 
     \/    \/     \/  \/ /_____//_____/  

github.com/imvast
""" + C.RESET)

threads = int(input("[?] Threads -> "))
code = input("[?] Code to bot -> ")
proxyless = input("[?] Proxyless (Y/n) -> ")
proxies = None
if proxyless.lower() == "n":
    proxys = open('proxies.txt', 'r').read().splitlines()


class stats:
    hits = 0
    failed = 0
    start = time.time()


def TitleThread():
    while True:
        os.system(f"title dsc.gg clicker ~ Hits: {stats.hits} ^| Failed {stats.failed} ^| Threads: {threading.active_count()} ^| Elapsed: {round(time.time() - stats.start, 1)}")
        time.sleep(0.1)

def click():
    try:
        proxies = None
        if proxyless.lower() == "n":
            proxy = random.choice(proxys)
            proxies = {'http://': f'http://{proxy}', 'https://': f'http://{proxy}'}
            

        headers = {
            'authority': 'r.dsc.gg',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.7',
            'cookie': 'clicked_tags=dsc.gg',
            'dnt': '1',
            'sec-ch-ua': '^\\^Not?A_Brand^\\^;v=^\\^8^\\^, ^\\^Chromium^\\^;v=^\\^108^\\^, ^\\^Brave^\\^;v=^\\^108^\\^',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '^\\^Windows^\\^',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }

        r = httpx.get(f"https://r.dsc.gg/{code}", headers=headers, proxies=proxies, timeout=30)
        if r.status_code in (200, 302):
            stats.hits += 1
        else:
            #print(r.status_code)
            stats.failed += 1
    except KeyboardInterrupt: os._exit(0)
    except Exception as e:
        #print(e)
        stats.failed += 1



threading.Thread(target=TitleThread).start()
try:
    while True:
        if threading.active_count() < threads:
            threading.Thread(target=click).start()
except KeyboardInterrupt: os._exit(0)