"""
The words filter:
There are two inputs: dic and lis
dic consists recorded information; its format is like {'a': 'absent', 'r': 'absent', 'o': 'absent', 's': ['no No.4', 'no No.3'], 'e': 'absent', 'b': 'absent', 'u': 'absent', 't': ['no No.4'], 'y': 'absent'}
lis is the Wordle words list.
There are an output variable: pos;
pos is a list that consists of the possible words that fit the position
"""
# words filter 
def words_filter(dic,lis):
    pos=[]
    for word in lis:
        exitFlag1 = False
        exitFlag2 = False
        exitFlag3 = False
        exitFlag4 = False
        exitFlag5 = False
        exitFlag6 = False
        exitFlag7 = False
        exitFlag8 = False
        exitFlag9 = False
        exitFlag10 = False
        exitFlag11 = False    
        for letter in dic:
            if dic[letter] == "absent":
                if letter in word:
                    exitFlag1 = True
                    break
            else:
                if 1 in dic[letter]:
                    if word[0] != letter:
                        exitFlag2 = True
                        break
                    
                if 2 in dic[letter]:
                    if word[1] != letter:
                        exitFlag3 = True
                        break
                
                if 3 in dic[letter]:
                    if word[2] != letter:
                        exitFlag4 = True
                        break               

                
                if 4 in dic[letter]:
                    if word[3] != letter:
                        exitFlag5 = True
                        break

             
                if 5 in dic[letter]:
                    if word[4] != letter:
                        exitFlag6 = True
                        break                

                if "no No.1" in dic[letter]:
                    if word[0] == letter or letter not in word:
                        exitFlag7 = True
                        break                

                if "no No.2" in dic[letter]:
                    if word[1] == letter or letter not in word:
                        exitFlag8 = True
                        break

                if "no No.3" in dic[letter]:
                    if word[2] == letter or letter not in word:
                        exitFlag9 = True
                        break                

                if "no No.4" in dic[letter]:
                    if word[3] == letter or letter not in word:
                        exitFlag10 = True
                        break
                if "no No.5" in dic[letter]:
                    if word[4] == letter or letter not in word:
                        exitFlag11 = True
                        break
        if exitFlag1 or exitFlag2 or exitFlag3 or exitFlag4 or exitFlag5 or exitFlag6 or exitFlag7 or exitFlag8 or exitFlag9 or exitFlag10 or exitFlag11:
            continue
        pos.append(word)
        
    return pos