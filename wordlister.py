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
        if wordlist.count(newword) == 1 :
            wordlist.remove(newword)
        if word.count(newword) > 1 :
            word.remove(newword)
    wordlist.extend(word) # note that i do not need to wordlist = because extend operation already 
                          # modifies the object and returns nothing
wordlist.sort()
print(wordlist)
