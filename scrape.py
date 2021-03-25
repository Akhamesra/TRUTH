def c(link):
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup as soup
    import csv
    req = Request(link , headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")

    data = '' 
    fdata = ''
    hdata = ''
    for data in page_soup.find_all("p"): 
        fdata = fdata +" "+ data.get_text()
    for data in page_soup.find_all("h1"): 
        hdata = hdata +" "+ data.get_text()
    
    return fdata,hdata

#print(c("https://zeenews.india.com/buzz/after-woman-accuses-zomato-delivery-guy-of-assault-latter-alleges-she-hit-her-nose-with-her-own-ring-2347297.html"))
