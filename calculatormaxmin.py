tot = 0
cnt = 0
mx = 0
mn = 100000
integer = None 
while True :
    integer = input('Enter number: ')
    try :
        integer = int(integer)
        cnt = cnt + 1
        tot = tot + integer
        if integer > mx : 
            mx = integer
        if integer < mn : 
            mn = integer 
    except :
        if integer == 'done' :
            print(tot, cnt, tot/cnt, mx, mn)
            break
        else :
            print ('Invalid input')