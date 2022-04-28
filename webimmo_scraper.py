# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 10:11:27 2022

This program will scrape the website 'immoweb.be'
The program will first filter out the url links to the houses.
(aprox. 10000 urls)

The second part will go trouhg these links and will download the data
related to every house.

Using Soup we can import the data in a json object.

After removing the duplicates the data is then storen in a csv file.

The csv file still needs some cleaning up.
We use Excel for removing bad entries and filling empty fields aswell as
changing the yes/no fields to a 1/0 value.

@authors: Group Mousumi/Anzeem/Mohammed
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import json
from time import sleep
from random import randrange
import pandas as pd


#every webpage gives 31 links to houses
MAXPAGE=333
home_links=[]
for loop in range (1,MAXPAGE):

    #select just one page containing 31 links to houses
    url="https://www.immoweb.be/en/search/house/for-sale?countries=BE&page="+str(loop)

    # The selenium.webdriver module provides all the implementations of WebDriver
    # Firefox has to be installed on your system
    # Here, we create instance of Firefox WebDriver.
    driver = webdriver.Firefox()
    # The driver.get method will lead to a page given by the URL. WebDriver will wait until the page is fully
    driver.get(url)
    #simulate human 
    rnd=randrange(1,2)
    sleep(rnd)
    page=driver.page_source
    driver.close()
    
    soup = BeautifulSoup(page, "html.parser")
    soup.prettify()

    #get all url links out of soup
    links = []
    for elem in soup.find_all("a"):
        links.append(elem.get("href"))
    
    #save only the url links we need
    for elem in links:
        if type(elem) == str:
            if "https://www.immoweb.be/en/classified" in elem :
                home_links.append(elem)
              
               
#remove duplicate url links
mycleanlist = list(dict.fromkeys(home_links))

       
#write the url links to a file 
with open("home_links.txt","a+") as fp:
    for url in mycleanlist:
        fp.write(url+"\n")
    fp.close()  


# This part will get all the data of the houses
# and will save it as a csv file
# it uses the urls from file 'home_links.txt'

firsttime=True
with open("home_links.txt","r") as fz:
    
    for url in fz:
        
        # get webpage of a house
        driver = webdriver.Firefox()
        driver.get(url)
        
        #simulate a human
        rnd=randrange(1,3)
        sleep(rnd)
        page=driver.page_source
        driver.close()
        
        soup = BeautifulSoup(page, "lxml")
        soup.prettify()
        
        # Here we create a string that can be cast to json object
        # it will contain all the data of a house
        homeinfo=''
        for elem in soup.find_all("script"):
            if 'window.dataLayer' in elem.text:
                homeinfo+=elem.text
                
        #convert string to json object
        homeinfo=homeinfo[34::]
        homeinfo=homeinfo.replace('\n','')
        homeinfo=homeinfo.replace('];','')
        js_obj = json.loads(homeinfo)
    
    
        #prepare a dataframe object using the json data object of a house
        df = pd.DataFrame.from_dict(pd.json_normalize(js_obj), orient='columns')
        
        # Append the dataframe objects to our deliverable file
        # The first time also put a header
        if  firsttime:
            df.to_csv("data_homes.csv", mode='a', header=True)
            firsttime = False
        else:
            df.to_csv("data_homes.csv", mode='a', header=False)

