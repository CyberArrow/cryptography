import sys

from string import uppercase as uc

enfreq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

ltcount = {'A':0, 
           'B':0, 
           'C':0, 
           'D':0, 
           'E':0,
           'F':0, 
           'G':0, 
           'H':0, 
           'I':0, 
           'J':0, 
           'K':0, 
           'L':0, 
           'M':0, 
           'N':0, 
           'O':0, 
           'P':0, 
           'Q':0, 
           'R':0, 
           'S':0, 
           'T':0, 
           'U':0, 
           'V':0,
           'W':0, 
           'Y':0,
           'X':0, 
           'Z':0}

file = open(sys.argv[1], 'r').read().upper()

for lt in file:
    if lt in uc:
        ltcount[lt] += 1

order = []
score = 0

for word in sorted(ltcount, key=ltcount.get, reverse=True):
    print word, ltcount[word]
    order.append(word)

order = '' .join(order)    

for clt in order[:6]:
    if clt in order[:6]:
        score += 1

for ult in order[-6:]:
    if ult in order[-6:]:
        score += 1

print 'Score', score ,'out of 12',        