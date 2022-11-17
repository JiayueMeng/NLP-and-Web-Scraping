#####################################################################
## Main class is for implementing all the methods from other py.files!
#####################################################################
import ssl

import univcombine
import webcrawler
import wordcounter
import csvprocessor
ssl._create_default_https_context = ssl._create_unverified_context

## Save the root and web link for later use
ROOT_H = 'https://www.sas.rochester.edu/his/people/faculty/'
WEB_H = "https://www.sas.rochester.edu/his/people/faculty/index.html"
ROOT_P = 'https://www.sas.rochester.edu/pas/people/faculty/'
WEB_P = "https://www.sas.rochester.edu/pas/people/faculty/index.html"
WEB_CS = 'https://www.cs.rochester.edu/people/index.html'
ROOT_CS = 'https://www.cs.rochester.edu/people/'

MIT_web_p = 'https://physics.mit.edu/faculty/'
MIT_web_h = 'https://history.mit.edu/people/'
MIT_web_CS = 'https://www.eecs.mit.edu/role/faculty-cs/'
MIT_ROOT_CS = 'https://www.csail.mit.edu/'

Stan_WEB_P = 'https://physics.stanford.edu/people/faculty'
Stan_WEB_H = 'https://history.stanford.edu/people/faculty'
Stan_WEB_CS = 'https://cs.stanford.edu/directory/faculty'

UB_ROOT = "http://arts-sciences.buffalo.edu/"
UB_WEB_P = 'http://arts-sciences.buffalo.edu/physics/faculty/faculty-directory.html'
UB_WEB_H = 'http://arts-sciences.buffalo.edu/history/faculty/faculty-directory.html'
UB_WEB_CS = 'http://engineering.buffalo.edu/computer-science-engineering/people/faculty-directory.html'
UB_ROOT_CS = 'http://engineering.buffalo.edu/'

Har_WEB_P = 'https://www.physics.harvard.edu/people/faculty'
Har_WEB_H = 'https://history.fas.harvard.edu/people/faculty_alpha'
Har_WEB_CS = 'https://www.seas.harvard.edu/computer-science/faculty-research'
Har_ROOT_CS = 'https://www.seas.harvard.edu/'

Van_WEB_P = 'https://as.vanderbilt.edu/physics/people/index.php?group=faculty'
Van_WEB_H = 'https://as.vanderbilt.edu/history/people/index.php?group=primary-and-joint-appointments'
Van_ROOT = 'https://as.vanderbilt.edu/'
Van_ROOT_CS = 'https://engineering.vanderbilt.edu/'
Van_WEB_CS = 'https://engineering.vanderbilt.edu/people/cs'

## crawling history faculty website

# url_list_H = webcrawler.UR_crawler(ROOT_H, WEB_H)
# url_list_H = webcrawler.MIT_crawler_h(MIT_web_h)
# url_list_H = webcrawler.Har_crawler_H(Har_WEB_H)
# url_list_H = webcrawler.UB_crawler(UB_ROOT, UB_WEB_H)
# url_list_H = webcrawler.Stan_crawler_H(Stan_WEB_H)
url_list_H = webcrawler.Van_crawler_H(Van_ROOT, Van_WEB_H)

count = "0"
file_list_H = []

for url in url_list_H:
    new_D = wordcounter.counter(url)
    if len(new_D) == 0:
        continue
    else:
        csvprocessor.convertCSV(new_D, "HIS VA test " + count + ".csv")
        file_list_H.append("HIS VA test" + count + '.csv')
        count = int(count)
        count += 1
        count = str(count)

## crawling physics faculty website

# url_list_P = webcrawler.UR_crawler(ROOT_P, WEB_P)
# url_list_P = webcrawler.MIT_crawler_p(MIT_web_p)
# url_list_P = webcrawler.Stan_crawler_P(Stan_WEB_P)
# url_list_P = webcrawler.UB_crawler(UB_ROOT, UB_WEB_P)
# url_list_P = webcrawler.Harvard_Crawler(Har_WEB_P)
url_list_P = webcrawler.Van_crawler_P(Van_ROOT, Van_WEB_P)
file_list_P = []

for url in url_list_P:
    new_D = wordcounter.counter(url)
    if len(new_D) == 0:
        continue
    else:

        csvprocessor.convertCSV(new_D, "PHY VA test" + count + ".csv")
        file_list_P.append("PHY ST test" + count + '.csv')
        count = int(count)
        count += 1
        count = str(count)
        
url_list_CS = webcrawler.Van_crawler_CS(Van_ROOT_CS, Van_WEB_CS)
# url_list_CS = webcrawler.UR_crawler(ROOT_CS, WEB_CS)
# url_list_CS = webcrawler.UB_crawler(UB_ROOT_CS, UB_WEB_CS)
# url_list_CS = webcrawler.MIT_crawler_CS(MIT_web_CS)
# url_list_CS = webcrawler.Stan_crawler_CS(Stan_WEB_CS)
file_list_CS = []
for url in url_list_CS:
    new_D = wordcounter.counter(url)
    if len(new_D) == 0:
        continue
    else:
        csvprocessor.convertCSV(new_D, "CS VA test" + count + ".csv")
        file_list_CS.append("CS VA test" + count + '.csv')
        count = int(count)
        count += 1
        count = str(count)

#file_list = file_list_H + file_list_P + file_list_CS

#csv_list = csvprocessor.csv_integrate(file_list)
#csv_list_freq = csvprocessor.freq(csv_list)

#words = csvprocessor.word_choose(csv_list_freq)
#csvprocessor.convertCSV(csv_list, "test" + ".csv")

# print(csv_list['ny'])
# print(words.to_csv())
print(len(file_list_H))
print(len(file_list_P))
'''

list_csv = univcombine.read_all_csv(1, 2)
print(list_csv)
csv_list = csvprocessor.csv_integrate(list_csv)
csv_list_freq = csvprocessor.freq(csv_list)
words = csvprocessor.word_choose(csv_list_freq)
csvprocessor.convertCSV(csv_list, "test2UnivUR+UB" + ".csv")
print(words.to_csv())

'''