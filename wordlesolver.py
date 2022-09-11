
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

allwords = sorted(awd.items(), key=lambda x: x[1], reverse=True)
    
l1 = {}
openC = open("mcw.txt")
for line in openC:
    word = line.strip()
    value = 0
    s = ''
    for letter in word:
        if letter in s:
            value += rankings[letter]/4
        elif letter not in s and letter != "'":
            value += rankings[letter]
        s += letter
    l1[word] = value

commonwords = sorted(l1.items(), key=lambda x: x[1], reverse=True)

numG = 0
# print(commonwords)

while numG != 6:
    numG += 1
    #print(len(allwords))
    #print(len(commonwords))

    
    # guess = list(allwords.keys())[0]
    if len(allwords) < 250 and 0 < len(commonwords) < 125:
        guess = commonwords[0][0]
    else:
        guess = allwords[0][0]

    
    print(f"you should guess {guess}")
    # print(allwords)

    # print(allwords[guess])
        
    result = input("Please enter what wordle responded. enter a five letter string with b for a black tile, y for a yellow tile, and g for a green tile: ")
    
    for i in range(len(result)):
        temp = []
        temp2 = []
        if result[i] == 'b':
            for w in allwords:
                if guess[i] not in w[0]:
                    temp.append(w)
            for w1 in commonwords:
                if guess[i] not in w1[0]:
                    temp2.append(w1)
        elif result[i] == 'y':
            for w in allwords:
                if guess[i] in w[0]:
                    temp.append(w)
            for w1 in commonwords:
                if guess[i] in w1[0]:
                    temp2.append(w1)
        elif result[i] == 'g':
            for w in allwords:
                if guess[i] == w[0][i]:
                    temp.append(w)
            for w1 in commonwords:
                if guess[i] == w1[0][i]:
                    temp2.append(w1)
        allwords = temp
        commonwords = temp2
    if result == 'ggggg':
        print(f"Yay! well done, we guessed the word in {numG} guesses")
        break
