#!/usr/bin/python

import re

with open('word.txt', 'r') as f:
    words = f.read()
    word_list = re.findall(r'\b[A-Za-z]+\b', words)
    word_num = len(word_list)
    print "There are %s words in words.txt." % word_num
