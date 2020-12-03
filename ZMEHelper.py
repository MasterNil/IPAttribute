import requests
import json
import time
from Config import env

ZME_key = env["zme_key"]
headers = {"Authorization":ZME_key}

def sendData(query_data):
    url = "https://api.zoomeye.org/host/search?query=%s"%query_data
    print(url)
    r = requests.get(url,headers=headers)
    r_json = r.json()
    return r_json


def run():
    ip_list = [x.strip() for x in open("Data/client.txt").readlines()]
    for ip in ip_list:
        r_json = sendData("ip:%s"%ip)
        json.dump(r_json,open("Data/zoomeye/%s.json"%ip,"w+"))
        time.sleep(15)

if __name__=="__main__":
    run()
    