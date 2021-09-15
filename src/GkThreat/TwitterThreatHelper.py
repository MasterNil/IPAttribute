import nest_asyncio
nest_asyncio.apply()

import twint
import time

Fresh_Limit = 10
Fresh_Gap = 86400

def getSearchTime():
    t_format = "%Y-%m-%d %H:%M:%S"
    st= time.localtime(time.time()-Fresh_Gap)
    time_str = time.strftime(t_format,st)
    return time_str

def getBaseConfig():
    config = twint.Config()
    config.Limit = Fresh_Limit
    config.Since = getSearchTime()
    config.Store_csv = True
    return config

def searchByContent(content,out_dir="./"):
    config = getBaseConfig()
    config.Search = content
    config.Output = f"{out_dir}/{content}.csv"
    twint.run.Search(config)

def searchByUser(username,out_dir):
    config = getBaseConfig()
    config.Username = username
    config.Output = f"{out_dir}/{username}.csv"
    twint.run.Search(config)


if __name__=="__main__":
    searchByContent("APT29")