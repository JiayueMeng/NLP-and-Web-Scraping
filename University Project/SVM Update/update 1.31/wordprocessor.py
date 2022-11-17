# distinguish nouns from words
import nltk
import csv
import re

#nltk.download()
def processor(dictionary):

# taking input words in a list
    ans = nltk.pos_tag(dictionary.keys())

# save the nouns
# save nouns word count respectively
    N = []
    NC = []

# ans returns a list of tuple
    for i in range(len(dictionary.key)):
        text = ans[i][0]
        val = ans[i][1]
        if (val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP'):
        #   print(text, " is a noun.")
            N.append(text)

    for i in range(len(N)):
        count = dictionary.get(N[i])
        NC.append(count)

# form new noun Dictionary
    new_D = {N[i]: floatNC[i] for i in range(len(N))}
    return new_D


def if_contain_sign(keyword):
    test_str = re.search(r"\W", keyword)

    if test_str == None:
        return False
    else:
        return True

# transfer the right dictionary to csv file for later use
header = ["Noun", "WC"]
def convertCSV(new_D, string):
    with open(string, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)  # write header in first row
        for row in new_D.items():
            writer.writerow(row)  # write each word respectively

