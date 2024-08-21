timeofday = dict()
file = input('Enter file name: ')
try:
    content = open(file)
except:
    print('File not found')
    quit()
for line in content:
    words = line.split()
    if len(line) > 5 and words[0] == 'From' :
        #print(words)
        hour = words[5].split(':')
        #print(hour)
        timeofday[hour[0]] = timeofday.get(hour[0], 0) + 1
slist = sorted([(k,v) for k,v in timeofday.items()])
for k,v in slist :
    print (k,v)