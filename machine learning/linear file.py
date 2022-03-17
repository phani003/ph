import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a=int(input('Enter the x value for range :'))
x=[i for i in range(1,a+1)]
y=[]
for j in range(1,a+1):
    g=float(input('Enter the Y_values :'))
    y.append(g)
df=pd.DataFrame()
print('1.M_value===LinearRegression.m()')
print('2.B_value===LinearRegression.b()')
print('3.Y_Predit==LinearRegression.y_pred()')
print('4.Squared_Error==LinearRegression.serror()')
print('5.Grap======LinearRegression.grap()')
print('6.Table=====LinearRegression.table()')
print('7.Above all print at time====LinearRegression.al_in_one()')
print('8.Break')
class LinearRegression:
    def __init__(self,w,e):
        self.a=w
        self.c=e
        df['x']=self.a
        df['y']=self.c   
        df['xy']=df['x']*df['y']
        df['x**2']=df['x']**2
        Ex=df['x'].sum()
        Ey=df['y'].sum()
        Ex2=(Ex)**2
        Ex_Ey=(Ex)*(Ey)
        Exy=df['xy'].sum()
        Ex_2=df['x**2'].sum()
        n=len(df)
        numarater_m=(n*Exy)-(Ex*Ey)
        denominater_m=(n*Ex_2)-(Ex2)
        m=(numarater_m)/(denominater_m)
        b=(Ey-m*Ex)/n
        #y_pred
        y_pred=[round(((m)*i+(b)),2) for i in df['x']]
        #squared error
        squared_error = sum([(y_pred_value - y_org_value) ** 2 for y_pred_value, y_org_value in zip(y_pred, df['y'].values)])
    def m(self):
        Ex=df['x'].sum()
        Ey=df['y'].sum()
        Ex2=(Ex)**2
        Ex_Ey=(Ex)*(Ey)
        Exy=df['xy'].sum()
        Ex_2=df['x**2'].sum()
        n=len(df)
        numarater_m=(n*Exy)-(Ex*Ey)
        denominater_m=(n*Ex_2)-(Ex2)
        m=(numarater_m)/(denominater_m)
        return m
    def b(self):
        Ex=df['x'].sum()
        Ey=df['y'].sum()
        Ex2=(Ex)**2
        Ex_Ey=(Ex)*(Ey)
        Exy=df['xy'].sum()
        Ex_2=df['x**2'].sum()
        n=len(df)
        numarater_m=(n*Exy)-(Ex*Ey)
        denominater_m=(n*Ex_2)-(Ex2)
        m=(numarater_m)/(denominater_m)
        b=(Ey-m*Ex)/n
        return b
    def y_pred(self):
        Ex=df['x'].sum()
        Ey=df['y'].sum()
        Ex2=(Ex)**2
        Ex_Ey=(Ex)*(Ey)
        Exy=df['xy'].sum()
        Ex_2=df['x**2'].sum()
        n=len(df)
        numarater_m=(n*Exy)-(Ex*Ey)
        denominater_m=(n*Ex_2)-(Ex2)
        m=(numarater_m)/(denominater_m)
        b=(Ey-m*Ex)/n
        #y_pred
        y_pred=[round(((m)*i+(b)),2) for i in df['x']]
        return y_pred            
    def serror(self):
        Ex=df['x'].sum()
        Ey=df['y'].sum()
        Ex2=(Ex)**2
        Ex_Ey=(Ex)*(Ey)
        Exy=df['xy'].sum()
        Ex_2=df['x**2'].sum()
        n=len(df)
        numarater_m=(n*Exy)-(Ex*Ey)
        denominater_m=(n*Ex_2)-(Ex2)
        m=(numarater_m)/(denominater_m)
        b=(Ey-m*Ex)/n
        #y_pred
        y_pred=[round(((m)*i+(b)),2) for i in df['x']]
        #squared error
        squared_error = sum([(y_pred_value - y_org_value) ** 2 for y_pred_value, y_org_value in zip(y_pred, df['y'].values)])
        return squared_error
    def grap(self):
        df['x']=self.a
        df['y']=self.c   
        df['xy']=df['x']*df['y']
        df['x**2']=df['x']**2
        Ex=df['x'].sum()
        Ey=df['y'].sum()
        Ex2=(Ex)**2
        Ex_Ey=(Ex)*(Ey)
        Exy=df['xy'].sum()
        Ex_2=df['x**2'].sum()
        n=len(df)
        numarater_m=(n*Exy)-(Ex*Ey)
        denominater_m=(n*Ex_2)-(Ex2)
        m=(numarater_m)/(denominater_m)
        b=(Ey-m*Ex)/n
        #y_pred
        y_pred=[round(((m)*i+(b)),2) for i in df['x']]
        #grap
        plt.figure(figsize=(12,12))
        plt.scatter(x,y,c='red',label='y_original')
        plt.plot(x,y_pred,c='blue',label='y_pred')
        plt.title('Linear Regression',size=32)
        plt.xlabel('X-Original',size=15,c='brown')
        plt.ylabel('Y-Original and Y-pred',size=15,c='brown')
        plt.legend()
        plt.show()
    def table(self):
        df['xy']=df['x']*df['y']
        df['x**2']=df['x']**2
        return df
    def al_in_one(self):
        Ex=df['x'].sum()
        Ey=df['y'].sum()
        Ex2=(Ex)**2
        Ex_Ey=(Ex)*(Ey)
        Exy=df['xy'].sum()
        Ex_2=df['x**2'].sum()
        n=len(df)
        numarater_m=(n*Exy)-(Ex*Ey)
        denominater_m=(n*Ex_2)-(Ex2)
        m=(numarater_m)/(denominater_m)
        b=(Ey-m*Ex)/n
        #y_pred
        y_pred=[round(((m)*i+(b)),2) for i in df['x']]
        #squared error
        squared_error = sum([(y_pred_value - y_org_value) ** 2 for y_pred_value, y_org_value in zip(y_pred, df['y'].values)])
        print('Linear Regression is Y=MX+B ')
        print('<=============================>')
        print(df)
        print('<-------------------------->')
        print('M_value :',m)
        print('<-------------------------->')
        print('B_value :',b)
        print('<-------------------------->')
        print('Squared_Error :',squared_error)
        print('<-------------------------->')
        #grap
        plt.figure(figsize=(12,12))
        plt.scatter(x,y,c='red',label='y_original')
        plt.plot(x,y_pred,c='blue',label='y_pred')
        plt.title('Linear Regression',size=32)
        plt.xlabel('X-Original',size=15,c='brown')
        plt.ylabel('Y-Original and Y-pred',size=15,c='brown')
        plt.legend()
        plt.show()
        
while(1):
    p=int(input('Enter the number for out put :')) 
    if(p==1):
        print('----M_value-----')
        lin=LinearRegression(x,y)
        ma=lin.m()
        print(ma)
    elif(p==2):
        print('----B_value-----')
        lin=LinearRegression(x,y)
        da=lin.b()
        print(da)
    elif(p==3):
        print('----Y_pred-------')
        lin=LinearRegression(x,y)
        y_pred=lin.y_pred()
        print(y_pred)
    elif(p==4):
        print('--Squared_Error--')
        lin=LinearRegression(x,y)
        sq=lin.serror()
        print(sq)
    elif(p==5):
        print('-----Grap-------')
        lin=LinearRegression(x,y)
        gr=lin.grap()
        print(gr)
    elif(p==6):
        print('----Table----')
        lin=LinearRegression(x,y)
        print(df)
    elif(p==7):
        print('-------Al_IN_ONE-----')
        lin=LinearRegression(x,y)
        allinone=lin.grap()
        print(allinone)
    elif(p==8):
        break
    else:
        print('Enter the curret Number')
        
        
        
        
        
       