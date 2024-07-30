def computepay(hrs, rte):
    if hrs > 40 :
        pay = round(40 * rte + (hrs - 40) * 1.5 * rte, 2)
    else:
        pay = round(hrs * rte, 2)
    return pay
try:
    print("Pay:", computepay(float(input('Enter Hours: ')), float(input('Enter Rate: '))))
except:
    print('Error, please enter numeric input')
    quit()
    #Since I am putting the entire function into try there can be other parts of the function 
# (that is not float) that may fail which will lead into except