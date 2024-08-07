words = dict()
try:
    file = input('Enter File Name: ')
    hndl = open(file)
except:
    print('File not found')
    quit()
for line in hndl :
    if line.startswith('From') :
        list = line.split()
        if len(list) > 3 :
            list = list[2]
            words[list] = words.get(list, 0)+1


print(words)