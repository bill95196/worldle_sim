"""
judge function 
"""

record_ = dict()

def judge(guess,ans,record_,guess_list):
    guess_list.append(guess)
    
    # judge if each letter in guess word is present in answer word
    for i in range(len(ans)):
        if guess[i] != ans[i]:
            if guess[i] in ans:
                print(guess[i], " is present, but not No.",i+1)
                record_.setdefault(guess[i],[])
                if "no"+" "+"No."+str(i+1) not in record_[guess[i]]:
                    record_[guess[i]].append("no"+" "+"No."+str(i+1))               
            else: 
                print(guess[i], " is absent")
                record_[guess[i]] = "absent"
        else:
            print("The no.%d is %s" %(i+1, guess[i]))
            record_.setdefault(guess[i],[])
            if i+1 not in record_[guess[i]]:
                record_[guess[i]].append(i+1)

    print("The record is:", record_)
    print("my guess words are", guess_list)
    if guess == ans:
        time = len(guess_list)
        print("congulation! The attempt time is",time)

   
    return record_
