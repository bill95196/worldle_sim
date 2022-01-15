# determine most common locations for each letter

import os
from wordlewords import La as wordlist

wordcount = len(wordlist)
lettercount = {}

for word in wordlist :
    for letter in word:
        if letter in list(lettercount.keys()):
            lettercount[letter] += 1 
        else:
            lettercount[letter] = 1 

letterlist = list(lettercount.keys())
letterlist.sort()
letterlist.pop(0) #it's got '\n' as the first letter
lettersum = sum(list(lettercount.values()))

for letter in letterlist:
    lettercount[letter] = lettercount[letter]/lettersum
print('words analyzed:', wordcount)


letteroptdict = {}
# now to find the optimal locations for each letter:
for letter in letterlist:
    letterwords = []
    optloclist = [0, 0, 0, 0, 0]
    numletterwords = 0
    # get list of all words with letter
    for word in wordlist:
        if letter in word:
            numletterwords +=1  
            optloclist[word.index(letter)] += 1
    optloc = optloclist.index(max(optloclist))+1
    optperclist = [(loc/numletterwords) for loc in optloclist]

    letteroptdict[letter] = [optloclist, optperclist[optloc-1], numletterwords, optloc]
    #print(letter, str(numletterwords), str(optloc), str(optperclist))

# now print letters that have significantly optimal locations:
perclist = [letteroptdict[letter][1] for letter in list(letteroptdict.keys())]
mean = sum(perclist)/len(perclist)
print ("Mean:", mean)

for letter in letterlist:
    if letteroptdict[letter][1] > mean:
        print(letter, letteroptdict[letter][2], letteroptdict[letter][3], letteroptdict[letter][1], letteroptdict[letter][2] * letteroptdict[letter][1])

#for word in wordlist:
    #if word[1] == 'o' and word[4] == 's' and word[2] == 'c':
        #print(word)
