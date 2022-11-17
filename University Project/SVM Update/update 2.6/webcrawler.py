######################################################################################
## this is the py file for web crawler of Websites
## for each university, there is a unique function due to the difference in their url.
######################################################################################


import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import logging
# This is the method used to crawl all the faculty's link from schools' websites
def UR_crawler(root, web):
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all('h4')
    for web in all_web:
        web_url = str(web)[40:] # get the string section from href=
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            if web_url.find('https')== -1:
                web_url = root + web_url
            url_list.append(web_url)
        except:
            pass

    return url_list

def MIT_crawler_p(web):
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all('h3')
    for web in all_web:
        web_url = str(web)[12:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            url_list.append(web_url)
        except:
            pass
    return url_list

def MIT_crawler_h(web):
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find('ul', class_='persongrid-flex').find_all('a')
    for web in all_web:
        web_url = str(web)[8:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            url_list.append(web_url)
        except:
            pass
    return url_list

def UCLA_crawler_P(root, web):
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find('table', class_='table-borderless').find_all('a')
    for web in all_web:
        web_url = str(web)[8:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            if web_url.find('http') == -1:
                web_url = root + web_url
                # this is an unknown bug for prof Levine Alexandar, so we take it out
            if web_url.find('levine') == -1:
                url_list.append(web_url)
        except:
            pass
    return url_list

def UCLA_crawler_H(root, web):
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all("h1")
    for web in all_web:
        web_url = str(web)[8:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            if web_url.find('http')== -1:
                web_url = root + web_url
            url_list.append(web_url)
        except:
            pass
    return url_list
