from nltk.corpus import words
import csv


words_list = words.words()
def charCount(word): 
    dict = {} 
    for i in word: 
        dict[i] = dict.get(i, 0) + 1
    return dict

def possible_words(lwords, charSet): 
    with open('wordgame.csv', mode='w') as csv_file:
        fieldnames = ['count', 'words']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        count = 0
        for item in lwords:
            flag = 0
            if(all(x in charSet for x in list(item))): 
                flag = 1
            if (flag) :
                if len(item) > 2: 
                    count+=1
                    writer.writerow({'count': count, 'words': item})
                    print(item, count) 
            else : 
                continue


if __name__ == "__main__": 
    input = words_list
    question = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
    charSet = sorted(list(question.lower()))
    possible_words(input, charSet)
