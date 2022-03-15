from datetime import date

custamername=input(" Enter the CustamerName ")
itemslist=[]
pricelist=[]
quntitylist=[]


#print(' chose option ')
#print('1.enter items')
#print('2.exit')


#print("1.rice --- Rs.50/1kg")
#print("2.dal -----Rs.80/1kg") 
#print("3.oil------Rs.110/1li")
#print("4.hairoil--Rs.75/100ml")
#print("5.atta-----Rs.50/1kg")

products={'rice': 50 ,
       'dal': 80 ,
       'oil': 110,
       'hairoil': 75,
       'atta':  50  }


while True:
    print(' _chose option_ ')
    print('0.list of items')
    print('1.enter items')
    print('2.print bill')
    print('3.exit')
    chose=int(input('enter the option :-- '))
    
    
    if chose==0:
        for key, value in products.items():
            print(key, ' : ', value)
            
    elif chose==1:
        a=True
        while a:
            item=input('enter the item :--')
            if item in products:
                quntity=int(input('enter the quntity :--'))
                price=float(products[item]* quntity)
                itemslist.append((item))
                quntitylist.append(quntity)
                pricelist.append(price)
                print('------------if you want exit enter E-------------')
                #if item==a:
                    #break
               # else:
                    #print('not available')
            
            else:
                print('item not available')
                break
                
                
    elif chose==2:
        today = date.today()
        totalamount=sum(pricelist)
        gst=totalamount*(12/100)
        totalandgst=totalamount+gst
        print('  ','-----------------------Super Market-------------------------') 
        print('custamername :',custamername,)
        print('city:Kodad ------------------------------------------------','Date:',today)
        print('product','                     ','quntity','                 ','price')
        print('----------------------------------------------------------------------')
        for i in range(len(itemslist)):
            print(i,'.',itemslist[i],'                      ',quntitylist[i],'                     ',pricelist[i])
        print('-------------------------------  #   -----------------------------')
        print(' amout  :                                                 ',totalamount)
        print('   gst  :                                                 ', gst    )
        print('------------------------------   #    -----------------------------')
        print('                           total amout :                  ',totalandgst)
        print('----------------------------------------------------------------------')
        print('                     ','Thank You Visit Again','                          ')
        
        
        
    elif chose==3:
        break
        
        
    else:
        print('Enter the currect option')