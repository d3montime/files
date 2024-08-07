list = dict()
try:
    file = input('Enter File Name: ')
    hndl = open(file)
except:
    print('File not found')
    quit()
for line in hndl :
    if line.startswith('From') :
        words = line.split()
        if len(words) > 3 :
            word = words[2]
            list[word] = list.get(word, 0)+1


print(list)