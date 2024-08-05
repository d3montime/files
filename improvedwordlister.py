try:
    name = input('Enter file name: ')
    file = open(name)
except:
    print('Could not find specified file')
    quit()
wordlist = list()
for line in file:
    word = line.split()
    for newword in word:
        if wordlist.count(newword) < 1 :
            wordlist.append(newword)
wordlist.sort()
print(wordlist)
