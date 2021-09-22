import re

def fetchIpV4(content):
    pattern = re.compile('(?:[0-9]{1,3}\[?\.\]?){3}[0-9]{1,3}')
    p_val = pattern.findall(content)
    return p_val

def fetchDomain(content):
    pattern = re.compile("hxxps://.{1,30}\.[a-z]{2,5}")
    p_val = pattern.findall(content)
    return p_val


def fetchContent(content):
    ips = set()
    domains = set()
    result = []
    for ip_raw in fetchIpV4(content):
        ip = ip_raw.replace("[","").replace("]","")
        ips.add(ip)
    for domain_raw in fetchDomain(content):
        domain = domain_raw.split("://")[-1]
        domain = domain.replace("[.]",".")
        domains.add(domain)
    for ip in ips:
        result.append({"address":ip,"type":"ip"})
    for domain in domains:
        result.append({"address":domain,"type":"domain"})
    return result

def test():
    c = '🎣Massive NTTdocomo #Phishing Attacks on .xyz Domain. ⚠️ hxxps://www[.]docomo[a-z].xyz/  [‼️] need UserAgent=(iPhone|Android) &amp; SrcIP=JP🇯🇵 IP: 154.82.111[.]29 CloudInnovation🇸🇨🇲🇺 #AfriNIC  Registrar:hkdns 环球万维🇭🇰 Brand: NTTドコモ, Japan🇯🇵 Domain, IoCs:  https://t.co/eYyoNc0uhs  https://t.co/KvGwv5qDfd'
    fetchContent(c)

if __name__=="__main__":
    test()
