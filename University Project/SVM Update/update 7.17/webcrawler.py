######################################################################################
## this is the py file for web crawler of Websites
## for each university, there is a unique function due to the difference in their url.
######################################################################################


import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import logging
import univcombine
# This is the method used to crawl all the faculty's link from schools' websites
def UR_crawler(root, web):
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all('h4')
    for web_1 in all_web:
        if(web == 'https://www.sas.rochester.edu/his/people/faculty/index.html'):
            web_url = str(web_1)[25:] # get the string section from href=
        elif(web == 'https://www.sas.rochester.edu/pas/people/faculty/index.html'):
            web_url = str(web_1)[30:]
        elif(web == 'https://www.cs.rochester.edu/people/index.html'):
            web_url = str(web_1)[40:]
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
def MIT_crawler_CS(web):
    url_list = []
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.63 Safari/537.36'}
        r = requests.get(web, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        all_web = soup.find_all('a', class_='people-index-image')
        for web in all_web:
            web_url = str(web)[54:]
            web_url = web_url.split("\"")
            try:
                web_url = web_url[1]
                url_list.append(web_url)
            except:
                pass
        url_list_new = []
        for url in url_list:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                         'Chrome/51.0.2704.63 Safari/537.36'}
                r = requests.get(url, headers=headers, timeout=30)
                r.raise_for_status()
                r.encoding = r.apparent_encoding
                html = r.text
                soup = BeautifulSoup(html, 'html.parser')
                all_web = soup.find_all(class_='external', target = '_blank')
                for url in all_web:
                    web_url = str(all_web)[31:]
                    web_url = web_url.split("\"")
                    web_url = web_url[1]
                url_list_new.append(web_url)
            except:
                pass

    except:
        pass
    return url_list_new




## useless
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
## useless
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

def UB_crawler(root, web):
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all("a", class_ = 'title')
    for web in all_web:

        web_url = str(web)[22:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            if web_url.find('http')== -1:
                web_url = root + web_url
            url_list.append(web_url)
        except:
            pass
    del url_list[0]
    return url_list

def Harvard_Crawler(web):
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all('h1',class_="node-title",rel="nofollow")
    for web in all_web:
        web_url = str(web)[65:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            url_list.append(web_url)
        except:
            pass
    return url_list

def Harvard_Crawler_cs(root, web):
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all('span', class_ = 'field-content')
    for web in all_web:

        web_url = str(web)[31:]

        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            web_url = root + web_url
            url_list.append(web_url)
        except:
            pass
    url_list_new = []
    for url in url_list:
        try:
            r = requests.get(url, timeout=30)
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            all_web = soup.find_all('div', class_='field-item')
            for url in all_web:

                web_url = str(url)[31:]
                web_url = web_url.split("\"")
                web_url = web_url[1]
                url_list_new.append(web_url)
        except:
            pass



def Van_crawler_P(root, web):
    url_list = []
    isvisited = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all("a", class_='pic')
    for web in all_web:

        web_url = str(web)[20:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            web_url = root + web_url
            if web_url not in isvisited:
                url_list.append(web_url)
                isvisited.append(web_url)
        except:
            pass
    return url_list

def Van_crawler_H(root, web):
    url_list = []
    isvisited = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all("td", class_='biolink', align = 'left')
    for web in all_web:

        web_url = str(web)[33:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            web_url = root + web_url
            if web_url not in isvisited:
                url_list.append(web_url)
                isvisited.append(web_url)
        except:
            pass
    return url_list

def Van_crawler_CS(root, web):
    url_list = []
    isvisited = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find("div", class_='panel-body').find_all('h4')
    for web in all_web:
        web_url = str(web)[12:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            web_url = root + web_url
            if web_url not in isvisited:
                url_list.append(web_url)
                isvisited.append(web_url)
        except:
            pass
    return url_list

def Stan_crawler_P(web):
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all('div', class_="postcard-col2")
    for web in all_web:

        web_url = str(web)[35:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            url_list.append(web_url)
        except:
            pass
    return url_list


def Stan_crawler_H(web):
    root = 'https://history.stanford.edu/'
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all('span', class_="field-content")
    for web in all_web:
        web_url = str(web)[35:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            if web_url != '></span>':
                web_url = root + web_url
                url_list.append(web_url)
        except:
            pass
    return url_list

def Stan_crawler_CS(web):
    url_list = []
    url = requests.get(web)
    html = url.text
    soup = BeautifulSoup(html, 'html.parser')
    all_web = soup.find_all('tr', class_='odd')
    for web in all_web:

        web_url = str(web)[23:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            url_list.append(web_url)
        except:
            pass
    all_web = soup.find_all('tr', class_='even')
    for web in all_web:

        web_url = str(web)[23:]
        web_url = web_url.split("\"")
        try:
            web_url = web_url[1]
            url_list.append(web_url)
        except:
            pass
    return url_list

