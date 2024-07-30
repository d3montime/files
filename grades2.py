def computegrade(score) : 
    if 1.0 >= score >= 0.9 :
        return 'A'
    elif 0.9 > score >= 0.8 :
        return 'B'
    elif 0.8 > score >= 0.7 :
        return 'C'
    elif 0.7 > score >= 0.6 :
        return 'D'
    elif score < 0.6 :
        return 'F'
    else:
        return 'Bad score'

try : 
    print(computegrade(float(input('Enter score: '))))
except:
    print('Bad score')

#Since I am putting the entire function into try there can be other parts of the function 
# (that is not float) that may fail which will lead into except

#Also note that I need both the else and the except for bad score because the float can fail 
# but the score entered can also be out of set range 