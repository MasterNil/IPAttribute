import json
from virus_total_apis import PublicApi as VirusTotalPublicApi
from Config import env
#  query from VirusTotal

VT_API_KEY = ["vt_api_key"]

vt = VirusTotalPublicApi(VT_API_KEY)

def getIPAttribute(ip):
    r = vt.get_ip_report(ip)
    print(json.dumps(r, sort_keys=False, indent=4))


if __name__=="__main__":
    getIPAttribute("202.112.238.164")