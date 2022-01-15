"""
1. generate a first word from the list(first_）
2. use the judge function to judge wheter each letter is present or absent; and record the data in a list
3. use the history data(output from judge functiom to narraw the position words list. # words_filter 
4. record how many time we can find the answer
"""
# generate a random word from a 2499-word list
import random 
from wordlewords import La as wordlist
from filter import words_filter
from judge import judge
import json

# read first.txt to contruct first_
first_=[]
with open('first.txt','r') as f:
    for line in f:
        first_.append(line.strip('\n'))

        

guess_list = []
record_ = dict()
ana = dict()
for guess in first_:

    for answer in wordlist:        
        
        while guess != answer:
            judge(guess,answer,record_,guess_list)
            first_=words_filter(record_,wordlist)
            guess = random.choice(first_)
            
        judge(guess,answer,record_,guess_list)
                
        ana.setdefault(guess,[])
        time = len(guess_list)
    
        ana[guess].append(time)
            
        guess_list = []
        record_ = dict()
               
        

# write ana into a json file
js = json.dumps(ana)
 
fileObject = open('ana.json', 'w')
fileObject.write(js)
fileObject.close()
