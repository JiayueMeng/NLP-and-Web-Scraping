#####################################################################
## wordcounter consists of the original word counter method in the beginning of the project.
## Has been modified to include three more conditions:
## 1) nouns only
## 2) character < 20
## 3) contains no punctuation
#####################################################################

import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import re
import nltk


def counter(web):
    r = requests.get(web)
    soup = BeautifulSoup(r.content, features="lxml")

    text_p = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
    c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))

# We get the words within divs
# findAll(text=True) 会重复
    text_div = (''.join(s.findAll(text=True)) for s in soup.findAll('div'))
    c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))
# rstrip: 删除 string 字符串末尾的指定字符,返回新字符串
# punctuation: 所有符号
# lower: 小写

# We sum the two countesr and get a list with words count from most to less common
    total = c_div + c_p
    L = total.most_common()
    A = []
    B = []

    for i in range(len(L)):
        tokens = nltk.word_tokenize(L[i][0])
        ans = nltk.pos_tag(tokens)
        if ans == []: continue
        else:
            val = ans[0][1]
            if val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP':
              if len(L[i][0]) < 20 and L[i][0] != '':
                 if not if_contain_sign(L[i][0]):
                      A.append(L[i][0])
                      B.append(float(L[i][1]))
                 else: continue
              else: continue
            else:
                continue

# Creating a dictionary from L

# Creating a function to convert two lists to a dictionary
    dictionary = {A[i]: B[i] for i in range(len(A))}
    return dictionary

def if_contain_sign(keyword):
    test_str = re.search(r"\W", keyword)

    if test_str == None:
        return False
    else:
        return True
