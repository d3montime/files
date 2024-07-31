fle = input('Enter file name:')
text = open(fle)
sum = 0
cnt = 0
for lne in text :
    if lne.startswith('X-DSPAM-Confidence') is True:
        pos = lne.find(':')
        sum = sum + float(lne[pos + 1:])
        cnt = cnt + 1
print('Average spam confidence:', sum/cnt)
        