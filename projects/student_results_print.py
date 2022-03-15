def studentmarks():
    student=[]
    totalmarks=[]
    percen=[]
    telugu=[]
    hindi=[]
    english=[]
    maths=[]
    social=[]
    science=[]
    a=int(input('How many student marks cala :--')) 
    
    for i in range(a):
        studentname=input('Enter the student name:--')
        telugumarks=float(input('Enter the telugu:--'))
        hindimarks=float(input('Enter the Hindi:--'))
        englishmarks=float(input('Enter the English:--'))
        mathsmarks=float(input('Enter the Maths:--'))
        socialmarks=float(input('Enter the Social:--'))
        sciencemarks=float(input('Enter the Science:--'))
        print('----------------------------------------')
        #calacalation part
        total=telugumarks+hindimarks+englishmarks+mathsmarks+socialmarks+sciencemarks
        avarage=total/6
        per=total*(100/600)
        #data storage in list
        student.append(studentname)
        telugu.append(telugumarks)
        hindi.append(hindimarks)
        english.append(englishmarks)
        maths.append(mathsmarks)
        social.append(socialmarks)
        science.append(sciencemarks)
        totalmarks.append(total)
        percen.append(per)

    
    print('------------------------------------------------------------------------------------------------')
    print('                                          ','student Marks sheet','                                          ')
    print('------------------------------------------------------------------------------------------------')
    print('------------------------------------------------------------------------------------------------')
    print('s.no| Name          | Telugu | Hindi| English |  Maths  | Social | Science | Total.marks | percentage')                
    print('------------------------------------------------------------------------------------------------')
    for j in range(len(student)):
        print(j+1  ,'|',student[j],'       |',telugu[j],'  |',hindi[j],'|',english[j],'   |',maths[j],'   |',social[j],'  |',science[j],'   |',totalmarks[j],'      |',percen[j])
    print('------------------------------------------------------------------------------------------------')
    print('------------------------------------------------------------------------------------------------')
    


studentmarks()
