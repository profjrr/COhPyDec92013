## Professor Reed demos WEB Page Scraping via Python 3.3 or better
## December 9th, 2013 Demo03 to the Py Ohio Users Group
##
## my thanks to "Greg Reda" for startup code from Python 2.7
## for the "Best of Chicago" url connections and site info
## my thanks to "Christoph Gohlke" for providing Win binaries for lxml install
##
##NOTE:run testBestofChicago() et all.
##
from bs4 import BeautifulSoup
##from urllib2 import urlopen  ## use with 2.7 only!
import urllib.request
##import urllib.parse ## do not use here
from time import sleep # be nice
 
BASE_URL = "http://www.chicagoreader.com"
 
def make_soup(url):
    html = urllib.request.urlopen(url)
    ##    html = urlopen(url).read() ## use with 2.7 only!
    return BeautifulSoup(html, "lxml")
 
def get_category_links(section_url):
    soup = make_soup(section_url)
    boccat = soup.find("dl", "boccat")
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
    return category_links
 
def get_category_winner(category_url):
    soup = make_soup(category_url)
    category = soup.find("h1", "headline").string
    winner = [h2.string for h2 in soup.findAll("h2", "boc1")]
    runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
    return {"category": category,
        "category_url": category_url,
        "winner": winner}
##        "runners_up": runners_up}

fndurl = ("http://www.chicagoreader.com/chicago/"
        "best-of-chicago-2011-food-drink/BestOf?oid=4106228")  
def format_and_print_the_winners(fndurl):
##     food_n_drink = ("http://www.chicagoreader.com/chicago/"
##        "best-of-chicago-2011-food-drink/BestOf?oid=4106228")  
    categories = get_category_links(fndurl)
    for category in categories:
##        print(category)
        winner = get_category_winner(category)
        print(winner)
        print('\n')

def testBestofChicago():
     format_and_print_the_winners(fndurl)
     

