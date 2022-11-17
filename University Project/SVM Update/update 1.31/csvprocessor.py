# thisi s the class trying to integrate all the files and put them into dataframe correctly.
import pandas as pd
import numpy as np


def csv_integrate(file_list):
    csv_list = []
    for file in file_list:
        f = pd.read_csv(file, header=0, names=None).transpose()
        f.rename(columns=f.iloc[0], inplace=True)
        f.drop(f.index[0], inplace=True)
        f.rename({"WC": file}, axis='index', inplace=True)
        csv_list.append(f)
    csv_list = pd.concat(csv_list)
    return csv_list


def freq(csv_list):
    # first we get the inverse of relative frequency of one word among all websites
    # course, the more websites containing this word, the less important this word is becoming
    # freq = (overall number of websites)  / (number of websites containing this word + 1) (prevent zero error by +1)
    num_website = len(csv_list)
    freq_among_web_list = []
    for i in range(len(csv_list.columns)):
        num_containing = num_website - csv_list[csv_list.columns[i]].isnull().sum()
        freq_among_web = float(num_website / (num_containing + 1))
        freq_among_web_list.append(freq_among_web)
    #    print('Setting', i, 'column (word) freq to be', freq_among_web)
    csv_list.fillna(float(0), inplace=True)
    # print(csv_list)

    # then we calculate relative frequency of words within one website
    # the more of same word is appearing in this website, the more important this word should be!
    # freq = (abs. freq. of one word) / (max abs. freq. of words)
    # the range of this relative frequency is going to be [0, 1]
    # to make sure both frequencies carry approximately same weight, we standardized the first frequency!
    # The standardization I'm using is that first normalize the data,
    # and then follow by using the min-max normalization.
    max = z_normal(np.max(freq_among_web_list), np.average(freq_among_web_list), np.std(freq_among_web_list))
    min = z_normal(np.min(freq_among_web_list), np.average(freq_among_web_list), np.std(freq_among_web_list))
    stand_freq_list = []
    for freq1 in freq_among_web_list:
        stand_freq1 = (z_normal(freq1, np.average(freq_among_web_list), np.std(freq_among_web_list)) - min)/(max - min)
        stand_freq_list.append(stand_freq1)
    #    print("The standardized frequency is: ", stand_freq1)
    for i in range(len(csv_list)):
        web_row = csv_list.iloc[i]
        max_freq = np.max(web_row)
        for j in range(len(csv_list.columns)):
            # in order to make sure the final relative frequency is similar in scale to our orignial data,
            # multiply 100 for each element.
            csv_list.iloc[i, j] = float((web_row[j] / max_freq) * stand_freq_list[j]) * 100

    return csv_list

# this is the function used to get normalized data!
def z_normal(x, mu, sigma):
    return (x-mu)/sigma


# Here is the function to choose 20 most important / shining words from all the dataset!
# The idea is summing up the weights of each words and make a dictionary
# Sort the dictionary from greatest value to the lowest and get the first 20 items!
# get the 1st element (word) in each tuple in the list to make a new list, and get those columns from the dataset!
def word_choose(csv_file):
    word_list = []
    weight_list = []
    for word in csv_file.columns:
        word_list.append(word)
        weight_list.append(np.sum(csv_file[word]))
    dictionary = {word_list[i]: weight_list[i] for i in range(len(word_list))}
    dictionary = sorted(dictionary.items(), key=lambda item:item[1], reverse=True)
    word_to_use = dictionary[:20]
    word_to_use = [x[0] for x in word_to_use]
    csv_file = csv_file[word_to_use]
    return csv_file






