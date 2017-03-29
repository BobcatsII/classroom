import random
times = 0
total = 0
while True:
    choise = input('1.begin,2.close\n')
    if choise == 1:
        total += 1
        num = random.randint(1,50)
        while True:
            gue = int(input("please guess my input:"))
            times += 1
            if gue > num:
                print "too big"
            elif gue < num:
                print "too small"
            else:
                print "good , u guess right"
                break
        print "total guess number of %s round, you guess number of %s times, you guess right %s " %(total, times, float(total)/times)
    elif choise == 2:
        break
    else:
        print "please input right num"