#!/usr/bin/env python
from bs4 import BeautifulSoup as bs
import requests
##------------- global constants------------------------
# user string. simply append id to below and GET.
userString = "https://www.yelp.com/user_details?userid="# 
restoString ="https://www.yelp.com/biz/"
#--------------Helper methods ---------------------------
#parse a yelper's profile to look for its reviews on restaurants.
def parseUserHTML(userID):
    url = userString+userID
    r = requests.get(url);
    htmlString = r.text.encode('utf-8');
    soup = bs(htmlString,'html.parser');
    reviews = soup.find_all('div','review')
    print len(reviews)
    ## Todo: what to do here with the soup? We have all the yelper's reviews. 
    # can use to train.

def parseRestaurantHTML(restoName):
    url = restoString+restoName
    r = requests.get(url);
    htmlString = r.text.encode('utf-8');
    soup = bs(htmlString,'html.parser');
    critics = soup.find('ul','ylist ylist-bordered reviews').select(' > li ')
    # critics is all the top recommended (and most relevant by yelp engine?) critic reviews.

## execution code - returns an input output pair:
#parseUserHTML("fMUudVdxRsQn_EiqUcmkmQ")
#parseRestaurantHTML('california-pita-and-grill-los-angeles')
