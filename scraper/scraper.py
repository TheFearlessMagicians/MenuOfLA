#!/usr/bin/env python
from bs4 import BeautifulSoup as bs
import requests
##------------- global constants------------------------
# user string. simply append id to below and GET.
userString = "https://www.yelp.com/user_details?userid="# 


#--------------Helper methods ---------------------------
#parse a yelper's profile to look for its reviews on restaurants.
def parseUserHTML(userID):
    url = userString+userID
    r = requests.get(url);
    htmlString = r.text.encode('utf-8');
    soup = bs(htmlString,'html.parser');
    ## Todo: what to do here with the soup? We have all the yelper's reviews. 
    # can use to train.


## execution code - returns an input output pair:

