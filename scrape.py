def c(link):
    #import requests 
    from urllib.request import Request, urlopen
    import pandas as pd 
    from bs4 import BeautifulSoup 
    import csv
    # link for extract html data 
    def getdata(url): 
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        return webpage

    htmldata = getdata(link) 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    data = '' 
    fdata = ''
    hdata = ''
    for data in soup.find_all("p"): 
        fdata = fdata +" "+ data.get_text()
    for data in soup.find_all("h1"): 
        hdata = hdata +" "+ data.get_text()
    
    return fdata,hdata

