import ssl
import webcrawler
import wordcounter
import wordprocessor
import csvprocessor
ssl._create_default_https_context = ssl._create_unverified_context


# Save suffix for later use
SUFFIX = '.html'
# Save the expression for web's title
REX_TITLE = r'<title>(.*?)</title>'
# Save the expression for website
REX_URL = r'/pas/people/faculty/(.+?)/index.html'
# Save the base URL to work with
BASE_URL = 'https://www.sas.rochester.edu/pas/people/faculty/index.html'
# Create a location for saving all URLs


def get_baseurl(): return BASE_URL
def get_rexurl(): return REX_URL
def get_suffix(): return SUFFIX
def get_rextitle(): return REX_TITLE


#URL_list = webcrawler.cralwer(BASE_URL, REX_TITLE, REX_URL, SUFFIX)
#URL_list1 = webcrawler.check_url(URL_list)

count = "9"
#for mylist in URL_list1:
#    print(mylist)
new_D = wordcounter.counter("https://www.sas.rochester.edu/his/people/faculty/devoe-harry/index.html")
wordprocessor.convertCSV(new_D, "test" + count + ".csv")
#file_list.append("test" + count + '.csv')
#    count = int(count)
#    count += 1
#   count = str(count)

file_list = ['test0.csv', 'test1.csv', 'test2.csv', 'test3.csv', 'test4.csv', 'test5.csv', 'test6.csv',
             'test7.csv', 'test8.csv', 'test9.csv']
csv_list = csvprocessor.csv_integrate(file_list)
csv_list = csvprocessor.freq(csv_list)
words = csvprocessor.word_choose(csv_list)
#wordprocessor.convertCSV(csv_list, "test" + ".csv")
print(words)
wordprocessor.convertCSV(words, 'smalltest.csv')




