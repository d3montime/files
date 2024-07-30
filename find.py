str = 'X-DSPAM-Confidence: 0.8475 Confidence Confidence Confidence Confidenc'
pos = str.find(':')
#print(float(str[pos+1:]))
print(str.replace('Confidence', 'Anxiety'))