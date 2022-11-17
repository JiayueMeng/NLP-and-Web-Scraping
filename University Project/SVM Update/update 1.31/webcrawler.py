# web crawler for Websites
import re
import urllib.request
import urllib
from collections import deque


# this is the function used to get the title of a html file.
def getTitle(file_content,REX_TITLE):
    linkre = re.search(REX_TITLE, file_content)
    if (linkre):
    #    print('title is：' + linkre.group(1))
        return linkre.group(1)


def cralwer(BASE_URL, REX_TITLE, REX_URL, SUFFIX):
    URL_list = []
#  we need set and queue for crawling
    queue = deque()  # the queue makes sure every URL will be visited
    visited = set()  # the set makes sure each URL is visited once.
#   appending the base URL into the queue.
    queue.append(BASE_URL)
    count = 0

    while queue:
        url = queue.popleft()  # Getting the first member in the queue
        visited |= {url}  # mark as visited
    #    print('Already get : ' + str(count) + '   We are getting <---  ' + url)

        count += 1
    # this method opens a remote url, sending request and getting the result. the returned value is a response object
        urlop = urllib.request.urlopen(url)
    # we will only take care of html links
        if 'html' not in urlop.getheader('Content-Type'):
            continue

    # Avoid program abortion
        try:
            data = urlop.read().decode('utf-8')
         #   title = getTitle(data, REX_TITLE);
        except:
            continue

    # Regular expressions extract all links in the page and then join the queue to be crawled
        linkre = re.compile(REX_URL)
        for sub_link in linkre.findall(data):
            sub_url = BASE_URL + sub_link + SUFFIX;  # combine into the full & useful links.
        # if the url is visited, we will pass
            if sub_url in visited:
                pass
            else:
            # set visited
                visited |= {sub_url}
            # add into the queue for crawling.
                queue.append(sub_url)
            #    print('Adding --->  ' + sub_url)
                URL_list.append(sub_url)
        return URL_list

def check_url(URL_list):
    for mylist in URL_list:
        if if_contain_symbol(mylist):
            URL_list.remove(mylist)
    return URL_list

def if_contain_symbol(keyword):
    symbols = ["<", ">", "=", "#", "@"]
    for symbol in symbols:
        if symbol in keyword:
       #     print('YES!!!')
            return True
    else:
        return False