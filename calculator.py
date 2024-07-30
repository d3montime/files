tot = 0
cnt = 0
avg = None # not required because avg has equivalence before print in the if statement
integer = None 
while integer != 'done' :
    integer = input('Enter number: ')
    try :
        integer = int(integer)
        cnt = cnt + 1
    except :
        # print('Hi')
        if integer == 'done' :
            # print('Bye')
            avg = tot / cnt
            print(tot, cnt, avg)
            break
        else :
            print ('Invalid input')
            integer = 0
    tot = tot + integer

    # prints in this code used to determine what part of the loop was not working as intended/skipped
    # also note that while True leads to a infinite loop. Could have used this conditional in this case