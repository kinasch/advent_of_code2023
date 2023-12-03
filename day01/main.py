import re


f = open("./input", "r")
lines = f.read().split('\n')

sum = 0
number_words_to_numbers = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

for line in lines:
    curLineDic = {}
    for key in number_words_to_numbers.keys():
        startIndex = 0
        while line.find(key,startIndex) > -1:
            curIndex = line.find(key,startIndex)
            startIndex = curIndex+1
            curLineDic[curIndex] = number_words_to_numbers[key]
    curLineDic = dict(sorted(curLineDic.items()))

    sum += int(str(curLineDic[list(curLineDic.keys())[0]])+str(curLineDic[list(curLineDic.keys())[-1]]))

print(sum)