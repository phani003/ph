import random

def gussno():
    num=random.randint(1,10)
    gusse=()
    for i in range(5):
        gusse=int(input('Enter random 1 to 10 :--'))
        if gusse==num:
            print('your correct')
        else:
            print('Sorry , trai again')
print('you have 5 chances')
gussno()           

            