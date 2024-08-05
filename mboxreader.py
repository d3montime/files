try:
    file = input('Enter File Name: ')
    content = open(file)
except:
    print('Invalid File Name')
    quit()
count = 0
for line in content :
    if line.startswith('From:') :
        word = line.split()
        name = word[1]
        print(name)
        count = count + 1
print('There were', count, 'lines in the file with From as the first word')
