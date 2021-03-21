def c(link):
    import requests 
    import pandas as pd 
    from bs4 import BeautifulSoup 
    import csv
    # link for extract html data 
    def getdata(url): 
        r = requests.get(url) 
        return r.text 

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


#test = c("https://zeenews.india.com/cricket/live-updates/india-vs-england-5th-t20i-live-cricket-score-2349176")
#print(test)