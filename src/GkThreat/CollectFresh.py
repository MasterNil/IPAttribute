import sys
sys.path.append("./")

from GkThreat.TwitterThreatHelper import searchByContent,searchByUser

import json
import time
import os

def checkAndCreateDir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)

def getTwitterOutdir():
    time_key = str(int(time.time()/3600))
    base_dir = "./twitter"
    checkAndCreateDir(base_dir)
    out_dir = os.path.join(base_dir,time_key)
    checkAndCreateDir(out_dir)
    return out_dir

def searchTwitter():
    conf = json.load(open("GkThreat/twitter_config.json"))
    out_dir = getTwitterOutdir()
    for c in conf["content"]:
        searchByContent(c,out_dir)
    for u in conf["user"]:
        searchByUser(u,out_dir)
    

def run():
    searchTwitter()

if __name__=="__main__":
    run()