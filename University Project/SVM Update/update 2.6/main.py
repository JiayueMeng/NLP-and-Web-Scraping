#####################################################################
## Main class is for implementing all the methods from other py.files!
#####################################################################
import ssl
import webcrawler
import wordcounter
import csvprocessor
ssl._create_default_https_context = ssl._create_unverified_context


## Save the root and web link for later use
ROOT_H = 'https://www.sas.rochester.edu/his/people/faculty/'
WEB_H = "https://www.sas.rochester.edu/his/people/faculty/index.html"

ROOT_P = 'https://www.sas.rochester.edu/pas/people/faculty/'
WEB_P = "https://www.sas.rochester.edu/pas/people/faculty/index.html"

MIT_web_p = 'https://physics.mit.edu/faculty/'
MIT_web_h = 'https://history.mit.edu/people/'

UCLA_ROOT_P = "https://www.pa.ucla.edu/"
UCLA_WEB_P = 'https://www.pa.ucla.edu/faculty.html'

UCLA_ROOT_H = 'https://history.ucla.edu/'
UCLA_WEB_H = 'https://history.ucla.edu/people/faculty'
## crawling history faculty website
# url_list_H = webcrawler.UR_crawler(ROOT_H, WEB_H)
# url_list_H = webcrawler.MIT_crawler_h(MIT_web_h)

url_list_H = webcrawler.UCLA_crawler_H(UCLA_ROOT_H, UCLA_WEB_H)
count = "0"
file_list_H = []
for url in url_list_H:
    new_D = wordcounter.counter(url)
    csvprocessor.convertCSV(new_D, "test" + count + ".csv")
    file_list_H.append("test" + count + '.csv')
    count = int(count)
    count += 1
    count = str(count)

## crawling physics faculty website

# url_list_P = webcrawler.UR_crawler(ROOT_P, WEB_P)
# url_list_P = webcrawler.MIT_crawler_p(MIT_web_p)
url_list_P = webcrawler.UCLA_crawler_P(UCLA_ROOT_P, UCLA_WEB_P)
file_list_P = []

for url in url_list_P:

    new_D = wordcounter.counter(url)
    csvprocessor.convertCSV(new_D, "test" + count + ".csv")
    file_list_P.append("test" + count + '.csv')
    count = int(count)
    count += 1
    count = str(count)

file_list = file_list_H + file_list_P
csv_list = csvprocessor.csv_integrate(file_list)
csv_list_freq = csvprocessor.freq(csv_list)
# csv_list = csvprocessor.freq(csv_list)
words = csvprocessor.word_choose(csv_list_freq)
csvprocessor.convertCSV(csv_list, "test" + ".csv")

# print(csv_list['ny'])

print(words.to_csv())
print(len(file_list_H))

