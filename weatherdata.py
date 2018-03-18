import urllib
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
from flask import Flask
from tasks import GetAllTasks

app = Flask(__name__)

@app.route("/")
def home():
    weatherdata = GetWeatherData()
    return weatherdata


def GetWeatherData():
    retVal = ""
    url_path = "https://weather.com/en-IN/weather/tenday/l/INTN0282:1:IN"
    htmlfile = urlopen(url_path)
    htmlContent = htmlfile.read()
    htmlsoup = BeautifulSoup(htmlContent, "html.parser")
    
    fulltable = htmlsoup.find_all(class_="twc-table")

    rows = fulltable[0].find_all(class_="clickable closed")
    for row in rows:
        daycols = row.find_all(class_="day-detail clearfix")
        for daycol in daycols:
            retVal += daycol.get_text().strip()
            print (daycol.get_text().strip())
        tempcol = row.find_all(class_="temp")
        for curTemp in tempcol:
            retVal += curTemp.get_text().strip() 
            print (curTemp.get_text().strip())

    return retVal


if __name__ == "__main__":
    print(GetAllTasks())
    app.run(debug=True, port=7777)

