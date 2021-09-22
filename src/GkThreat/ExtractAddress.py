import sys
sys.path.append("./")

from GkThreat.CollectFresh import base_dir
from GkThreat.CollectThreatContent import fetchContent

import pandas as pd
import os
from multiprocessing import Pool

def loadFiles():
    files = []
    for root,sub,names in os.walk(base_dir):
        for name in names:
            if not name.endswith("csv"):
                continue
            filename = os.path.join(root,name)
            files.append(filename)
    return files


def loadCsvFile(filename):
    df = pd.read_csv(filename)
    result = []
    for content in df["tweet"]:
        result += fetchContent(content)
    return result


def run():
    files = loadFiles()
    p = Pool(10)
    result = [] 
    result_list = p.map(loadCsvFile,files)
    for r_list in result_list:
        result += r_list
    df = pd.DataFrame(result).drop_duplicates()
    df.to_csv("tmp/threat_twitter.csv")

if __name__=="__main__":
    run()