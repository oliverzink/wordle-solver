

import random 

awd = {}
rankings = {'e': 11.1607, 'a': 8.4966, 'r': 7.5809, 'i': 7.5448, 'o': 7.1635, 't': 6.9509, 'n': 6.6544, 's': 5.7351, 'l': 5.4893, 'c': 4.5388, 'u': 3.6308, 'd': 3.3844, 'p': 3.1671, 'm': 3.0129, 'h': 3.0034, 'g': 2.4705, 'b': 2.0720, 'f': 1.8121, 'y': 1.7779, 'w': 1.2899, 'k': 1.1016, 'v': 1.0074, 'x': 0.2902, 'z': 0.2722, 'j': 0.1965, 'q': 0.1962}

openW = open("wordlewords.txt", "r")
for line in openW:
    word = line.strip()
    value = 0
    s = ''
    for letter in word:
        if letter in s:
            value += rankings[letter]/4
        else:
            value += rankings[letter]
        s += letter
    awd[word] = value



numSim = int(input("Enter the number of times it should run: "))
total = 0
for i in range(numSim):
    
    
    allwords = sorted(awd.items(), key=lambda x: x[1], reverse=True)
    
    wIdx = random.randint(0, len(allwords))
    wordle = allwords[wIdx][0]    
    numG = 0
    
    while numG != 6:
        numG += 1
    
        guess = allwords[0][0]
    
        result = ''
        for i in range(len(guess)):
            if guess[i] not in wordle:
                result += 'b'
            elif guess[i] == wordle[i]:
                result += 'g'
            elif guess[i] in wordle:
                result += 'y'
        for i in range(len(result)):
            temp = []
            if result[i] == 'b':
                for w in allwords:
                    if guess[i] not in w[0]:
                        temp.append(w)
            elif result[i] == 'y':
                for w in allwords:
                    if guess[i] in w[0]:
                        temp.append(w)
            elif result[i] == 'g':
                for w in allwords:
                    if guess[i] == w[0][i]:
                        temp.append(w)
            allwords = temp
        if result == 'ggggg':
            total += numG
            break

avg = total/numSim

print(f"Average number of guesses {avg}")
        
