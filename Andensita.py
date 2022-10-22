import requests
import threading
import random
import time
import sys
import os
import json

# https://discord.gg/sW3AdNWZNg
# ->  Another tool developed by ssl <- #

class main:

    def __init__(self):
        self.cookies = open('Config//cookies.txt', 'r').read().splitlines()
        self.proxies = open('Config//proxies.txt', 'r').read().splitlines()
        self.joinHeaders = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like GeckoRoblox/WinInetRobloxApp/0.549.0.5490632 (GlobalDist; RobloxDirectDownload)',
            'referer':'https://roblox.com/',
            'origin':'https://roblox.com'
        }


    
    def start_join(self, cookie, placeId):

        with requests.session() as session:

            proxy = random.choice(self.proxies)

            session.proxies = {
                'http':'http://' +proxy,
                'https':'http://'+proxy
            }

            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers = self.joinHeaders

            while True:

                joinGameStandard = session.post(
                    'https://gamejoin.roblox.com/v1/join-game',
                    data = {
                        'placeId':placeId,
                        'gameJoinAttemptId':None
                    }
                )

                print(joinGameStandard.json())

                # if joinGameStandard.json()['joinScriptUrl'] != None:
                #     break
                # elif joinGameStandard.json()['joinScriptUrl'] == None:
                #     continue


if __name__ == '__main__':
    args = sys.argv

    # if the user has ever opened the file and if they have not then they will be opened a discord join link.
    if(json.loads(open('Config//.json','r').read())['ran']!=True):os.system('start,https://discord.gg/sW3AdNWZNg');open('Config//.json','w').write(json.dumps({'ran':True},indent=3));

    dir = args[0]
    placeId = args[1]
    threads = args[2]

    print(f'Dir: [{dir}]\nPlace ID: [{placeId}]\nThreading: [{threads}]\n\n')
    print('-> Another tool developed by ssl, https://discord.gg/sW3AdNWZNg\n\nStarting in 3!')
    time.sleep(3)
    print('Started!')
    main = main()

    def thread(cookie):
        main.start_join(cookie, int(placeId))

        
    for cookie in main.cookies[:int(threads)]:
        print(cookie)
        threading.Thread(target=thread,args=(cookie,)).start()