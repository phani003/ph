while(1):
    print('<------------------------------------->')
    print('1.peramid')
    print('2.multification')
    print('3.NAME print in like piramed times')
    print('4.Even or add')
    print('5.PRIME NUMBER')
    print('6.down piramid')
    print('7.factorial')
    print('8.squre shape')
    print('9.Fibonacci Series')
    print('10.Palindrome')
    print('11.Exit program')
    print('<------------------------------------->')
    a=int(input('enter the number :'))
    if a==1:
        print('peramid')
        b=int(input('enter the number for piramid :'))
        for i in range(b):
            for j in range(i-1):
                print('*',end='')
            print('') 
        print('<------------------------------------->')    
    elif a==2:
        print('multification')
        c=int(input('enter the number :'))
        for i in range(11):
            print(c,'x',i,'=',c*i)
        print('<------------------------------------->')    
    elif a==3:
        print('NAME print in like piramed times')
        c=input('enter the name :')
        e=int(input('enter number for print name :'))
        for i in range(e):
            for j in range(i+1):
                print(c,end='')
            print('')  
        print('<------------------------------------->')   
    elif a==4:
        print('Even or add')
        b=int(input('enter the number :'))
        if b%2==0:
            print(b,'- THIS IS EVEN NUMBER')
        else:
            print(b,'- THIS IS ODD NUMBER')
        print('<------------------------------------->')    
    elif a==5:
        print('PRIME NUMBER')
        while(a>1):
            print('if you enter 1 is cala or 2 is break')
            d=int(input('enter the 1 or 2 :'))
            print('<------------------------------------->')
            if d==1:
                b=int(input('enter the calcating number :'))
                if (b==1)or(b==2)or(b==3)or(b==5)or(b==7):
                    print(b,'- prime number')
                    print('<------------------------------------->')
                elif (b%2==0)or(b%3==0)or(b%5==0)or(b%7==0):
                    print(b,'- is not prime number')
                    print('<------------------------------------->')
                else:
                    print(b,'- is prime number')
                    print('<------------------------------------->')
            elif d==2:
                 break
    elif a==6:
        print('down peramid ')
        b=int(input('enter the number for piramid :'))
        for i in range(b):
            for j in range(i+1):
                print('*',end='')
            for k in range(i-2):
                print('\t','*',end='')
            print('') 
        print('<------------------------------------->')   
    elif a==7:
        print('factorial')
        a=int(input('enter the value :'))
        if a==0:
            print(a)
        elif a==1:
            print(1)
        else:
            mult=1
            for i in range(1,a+1):
                mult *=i
            print(a,'factorial is',mult)
        print('<------------------------------------->') 
    elif a==8:
        while a==8:
            print('squre')
            print('Enter the 1 print squre or 2 is break the loop')
            n=int(input('Enter the number 1 or 2 :'))
            print('<------------------------------------->') 
            if n==1:
                b=input('Enter the name :')
                c=int(input('ente the number for squre print :'))
                print('<------------------------------------->') 
                for i in range(c):
                    for j in range(0,c):
                        print(b,end=" ")
                    print('\r')      
            elif n==2:
                break
            print('<------------------------------------->')    
    elif a==9:
        n1=0
        n2=1
        f=[0,1]
        print('Fibonacci Series')
        c=int(input('enter the number :'))
        print('<------------------------------------->')
        for i in range(2,c):
            n3=n1+n2
            n1=n2
            n2=n3
            f.append(n3)
        print(f)
        print('<------------------------------------->')
    elif a==10:
        while(1):
            print('Palindrome')
            print('if you enter 1 cheak for palidrom and 2 is break look')
            s=int(input('Enter the 1 or 2 :'))
            print('<------------------------------------->')
            if s==1:
                n=int(input('Enter the number :'))
                m=n
                rev=0
                while (n !=0):
                    a=n%10
                    rev=rev*10+a
                    n=n//10
                if (m==rev):
                    print(m,'is Palindrome')
                else:
                    print(m,'not Palindrome')
            elif s==2:
                break
            print('<------------------------------------->')    
    elif a==11:
        break
                
                
                