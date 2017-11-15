import sys
import re
import operator

###### initialize variables
# text to be parsed, encoded in UTF-8
whole_text = open('text.txt', encoding='utf-8').readlines()
# stores the count for each word
dictionary = {}

# helper to delete characters not in UTF-8
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), '')

# for each line in the text
for line in whole_text:
    # for each 'word' in the text
    for word in line.split():
        # delete unknown characters, e.g. emoticons
        word = word.translate(non_bmp_map)

        # don't count datestamps
        if re.match(r'\d+/\d+/\d', word):
            continue

        # don't count timestamps
        if re.match(r'\d\d+:+\d\d', word):
            continue

        # don't count <Media ommited>
        # it's actually nice to know how many files (pics etc.) have been sent
        #if re.match(r'[omitted>|<Media]', word):
        #    continue

        # delete signs
        word = re.sub(r'[!.:?,\-\*]', '', word)

        # skip empty string
        if word == '':
            continue

        # nouns are often written in lower case
        # set everthing to lower case as to not count two different instances
        word = word.lower()
        
        
        if dictionary.get(word, 0):
            # increase the word count by 1
            dictionary[word] += 1
        else:
            # start listing the word in the dictionary
            dictionary[word] = 1

# print result from starting with the most counted word
[print(k, dictionary[k]) for k in sorted(dictionary, key=dictionary.get, reverse=True) if dictionary[k] > 20]
