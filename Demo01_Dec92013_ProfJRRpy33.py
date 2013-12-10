##Demo Program Scraping URL's from web pages-- Professor Reed -- Monday Dec. 9th, 2013
##Modified (12/10/2013) for Python 3.3
####requires special install of requests
##==>see: http://docs.python-requests.org/en/latest/user/install/#install for complete details

##Demo01 -- CohPY -- Meeting
##NOW: setup for Python 3.3 (as of Dec. 10th, 2013)
##
##NOTE: run testURLscraper()
##
from bs4 import BeautifulSoup
import requests

def get_my_urls(url): 
    r  = requests.get("http://" +url) 
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        print(link.get('href'))

def testURLscraper():
## uncomment next statement for live input test    
##    url = raw_input("Enter a website to extract the URL's from: ")
    print('USCG Radio Club:')
    url = 'www.w5cgc.org'
    get_my_urls(url)
    print('### end of scrapes from USCG Club Radio Pages ###')
    print('____________________________________________')
    print('Yahoo S&P:')
    url = 'finance.yahoo.com/q?s=^gspc'
    get_my_urls(url)
    print('### end of scrapes from Yahoo Finance Pages ###')
    print('__________________________________________')
    url ='www.chicagoreader.com'
    get_my_urls(url)
    print('### end of scrapes from Chicago Reader Pages ###')
    print('___________________________________________')
    print
    print('end of report')
    
    
    


