"""
1. generate a first word from the list(first_）
2. use the judge function to judge wheter each letter is present or absent; and record the data in a list
3. use the history data(output from judge functiom to narraw the position words list. # words_filter
4. record how many time we can find the answer
"""


# score function ---------------------------------------- Kanwal
def bestguess(wordlist, wordscore):
    maxword = wordlist[0]
    maxscore = wordscore[maxword]
    for word in wordlist:
        if wordscore[word] > maxscore:
            maxscore = wordscore[word]
            maxword = word
    return maxword


# -------------------------------------------------------- Kanwal

# score function using letters --------------------------- Kanwal
def bestguesswletter(wordlist, locs, unused, wordscore, letterloc):
    # locs is a list like [2,3] that says the indexes (starting at 0) of the
    # locations that are not certain. For example, if we know the word is G_ESS,
    # then loc = [1]
    # I wasn't sure how you were storing letters that hadn't been guessed yet,
    # or so I am representing it as the list unused

    # find highest probability letter + location
    maxloc = locs[0]
    maxletter = unused[0]
    maxletscore = letterloc[maxloc][maxletter]
    for i in locs:
        for letter in unused:
            if letterloc[i][letter] > maxletscore:
                maxloc = i
                maxletter = letter
                maxletscore = letterloc[i][letter]

    bestwords = []
    for word in wordlist:
        if word[maxloc] == maxletter:
            bestwords.append(word)

    if len(bestwords) > 0:
        maxword = bestguess(bestwords, wordscore)
    else:
        maxword = bestguess(wordlist, wordscore)

    return maxword


# -------------------------------------------------------- Kanwal

def find_locs(record_):
    locs_op = []
    for element in list(record_.values()):
        if type(element) is list:
            for i in element:
                if type(i) is int:
                    locs_op.append(i-1)
    locs = list(set(list(range(5))).difference(set(locs_op)))
    return locs


# generate a random word from the word list
from wordlewords import La as wordlist
from filter import words_filter
from judge import judge
import json

# read first.txt to contruct first_
first_ = []
with open('first.txt', 'r') as f:
    for line in f:
        first_.append(line.strip('\n'))

first_ = first_[350:]

# additional loop to create simple score dictionary ----- Kanwal
lettercount = {}
wordscore = {}
for word in wordlist:
    for letter in word:
        if letter in list(lettercount.keys()):
            lettercount[letter] += 1
        else:
            lettercount[letter] = 1
lettersum = sum(list(lettercount.values()))

for letter in list(lettercount.keys()):
    lettercount[letter] = lettercount[letter] / lettersum

for word in wordlist:
    wordscore[word] = 0
    for letter in word:
        wordscore[word] = wordscore[word] + lettercount[letter]
# -------------------------------------------------------- Kanwal

# what if we also weighted letters based on posiiton? ---- Kanwal
letterloc = [{}] * 5
for word in wordlist:
    for i in range(len(word)):
        letter = word[i]
        if letter in list(letterloc[i].keys()):
            letterloc[i][letter] += 1
        else:
            letterloc[i][letter] = 1
# -------------------------------------------------------- Kanwal

letter26 = []                      #letter26 consists all letters. use it to construct the unused
for i in range(ord('a'),ord('z')+1):
    letter26.append(chr(i))

guess_list = []
record_ = dict()
ana = dict()
for guess1 in first_:

    for answer in wordlist:

        guess = guess1
        while guess != answer:
            judge(guess, answer, record_, guess_list)
            first_ = words_filter(record_, wordlist)
            unused = list(set(letter26).difference(set(list(record_.keys()))))
            locs = find_locs(record_)

            guess = bestguesswletter(first_, locs, unused, wordscore, letterloc)

        judge(guess, answer, record_, guess_list)

        ana.setdefault(guess1, [])
        time = len(guess_list)

        ana[guess1].append(time)

        guess_list = []
        record_ = dict()

        
 
# write ana into a json file
js = json.dumps(ana)

fileObject = open('ana750_.json', 'w')
fileObject.write(js)
fileObject.close()