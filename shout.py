count = 0
try : 
    file = input('Enter file name: ')
except:
    print('Could not find specified file')
    quit()
content = open(file)
for line in content :
    count = count + 1
    if count == 6 :
        break
    line = line.rstrip()
    print(line.upper())

# note that where the if conditional is placed and where the count variable is modified determines
# how many lines are printed. 