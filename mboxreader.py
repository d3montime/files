try:
    file = input('Enter File Name: ')
except:
    print('Invalid File Name')
    quit()
content = open(file)
count = 0
for line in content :
    if line.startswith('From') :
        line.split()
        name = line[1]
        print(name)
        count = count + 1
print('There were', count, 'lines in the file with From as the first word')
