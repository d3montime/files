try: 
    hrs = float(input('Enter Hours: '))
    rte = float(input('Enter Rate: '))
except:
    # This is completely unecessary. If you use except: it will skip try and continue.
    #  If the intention was to quit after an error, using quit() would not necessitate lines 7-9
    hrs = "e"
    rte = "e"
if hrs == "e" or rte == "e" :
    print('Error, please enter numeric input')
    quit()
pay = round(hrs * rte, 2)
if hrs > 40 : 
    pay = round(40 * rte + (hrs - 40) * 1.5 * rte, 2)
print('Pay: ', pay)
