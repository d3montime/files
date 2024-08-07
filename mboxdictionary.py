list = dict()
histo = dict()
inst = dict()
max = 0
maxsender = None
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
            day = words[2]
            list[day] = list.get(day, 0) + 1
            sender = words[1]
            histo[sender] = histo.get(sender, 0) + 1
            if histo[sender] > max :
                max = histo[sender]
                maxsender = sender
            school = sender.split('@')[1]
            inst[school] = inst.get(school, 0) + 1
            

print(list)
print(histo)
print(maxsender, max)
print(inst)