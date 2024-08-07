sender = dict()
try:
    file = input('Enter file name: ')
    content = open(file)
except:
    print('Failed to find file')
    quit()
for line in content :
    words = line.split()
    if len(words) > 3 and words[0] == 'From' :
        sender[words[1]] = sender.get(words[1], 0) + 1
slist = sorted([(v,k) for k,v in sender.items()], reverse= True)
print(slist)
for v,k in slist[0] :
    print(k,v)



