import ponssettings
import urllib
from urllib.request import urlopen
import json 

base_url = "https://api-ssl.bitly.com"

def CreteTinyUrl(longurl):
    shorturl = urlopen(base_url + "/v3/shorten?access_token="+ ponssettings.GetBitlyToken() + \
    "&longUrl="+ longurl + "&format=txt")
    print (longurl + "\nvs\n")
    print (shorturl.read())


if __name__ == "__main__":
    longurl = "http://google.co.in"
    CreteTinyUrl(longurl)




