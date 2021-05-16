#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    
    word =[0,'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve', 'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen','twenty']

    for i in range(1,10):
        word.append('twenty %s'%word[i])
    
    join_word = min_word = ""
    hour_word = word[int(h)]
    
    if m == 00:
        min_word = "o' clock"
        return "%s %s" % (hour_word , min_word)
    elif 1 <= int(m) <= 30:
        join_word = "past"
    elif 30 < int(m) < 60:
        m = 60 - m
        join_word = "to"
        hour_word = word[int(h)+1]
    


    if min_word == "" and not m%15==0 :
        min_word = word[int(m)]
    
    if m == 1:
        min_word = min_word + " minute"
    elif m == 15 or m == 45:
        min_word = "quarter"
    elif m == 30:
        min_word = "half"
    else:
        min_word = min_word +" minutes"
    
    final_string = "%s %s %s" % (min_word,  join_word, hour_word)
    return final_string
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
