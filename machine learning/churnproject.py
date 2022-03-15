#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("D:\\projects\\capstone projct\\Capstone-project-2 (1) (1)\\Dataset\\Dataset\\customer_churn.csv")


# In[77]:


data.count()


# In[6]:


data.isnull().sum()


# In[7]:


data.dtypes


# In[11]:


data[['SeniorCitizen','PaymentMethod']].value_counts()


# # a.Extract the 5th column & store it in ‘customer_5’

# In[42]:


customer_5=data.iloc[:,[4]]


# In[43]:


customer_5.head()


# # b.Extract the 15th column & store it in ‘customer_15’

# In[44]:


customer_15=data.iloc[:,[14]]


# In[45]:


customer_15.head()


# # c.Extract all the male senior citizens whose Payment Method is Electronic check & store the result in ‘senior_male_electronic’

# In[65]:


data[['gender','SeniorCitizen','PaymentMethod']].value_counts()


# In[32]:


data[['gender','SeniorCitizen','PaymentMethod']].head()


# In[47]:


senior_male_electronic=data[(data['gender']=='Male') & (data['SeniorCitizen']==1) & (data['PaymentMethod']=='Electronic check')]


# In[49]:


senior_male_electronic.head()


# # d.	Extract all those customers whose tenure is greater than 70 months or their Monthly charges is more than 100 & store the result in ‘customer_total_tenure’

# In[64]:


data[['tenure','MonthlyCharges']].value_counts()


# In[53]:


customer_total_tenure=data[(data['tenure']>70) | (data['MonthlyCharges']>100)]


# In[54]:


customer_total_tenure.head()


# # e.	Extract all the customers whose Contract is of two years, payment method is Mailed check & the value of Churn is ‘Yes’ & store the result in ‘two_mail_yes’

# In[59]:


data[['Contract','PaymentMethod','Churn']].value_counts()


# In[ ]:





# In[62]:


two_mail_yes=data[(data['Contract']=='Two year') &(data['PaymentMethod']=='Mailed check') &(data['Churn']=='Yes')]


# In[63]:


two_mail_yes.head()


# # f.	Extract 333 random records from the customer_churn dataframe & store the result in ‘customer_333’

# In[66]:


import random


# In[74]:


da=random.randint(0,33)


# In[75]:


da


# In[90]:


for i in range(0,333):
    da=random.randint(0,7043)
    m=data.iloc[[da],:]
    print(m)    


# In[82]:


data.iloc[[2],:]


# In[94]:


data.sample()


# In[95]:


customer_333=data.sample(n=333)


# In[96]:


customer_333


# # g.	Get the count of different levels from the ‘Churn’ column

# In[97]:


data['Churn'].value_counts()


# In[98]:


data.head()


# In[99]:


data.count()


# # B)	Data Visualization:
#       a.	Build a bar-plot for the ’InternetService’ column:
#           i.	Set x-axis label to ‘Categories of Internet Service’
#           ii.	Set y-axis label to ‘Count of Categories’
#           iii.	Set the title of plot to be ‘Distribution of Internet Service’
#           iv.	Set the color of the bars to be ‘orange’
# 

# In[248]:


x=data['InternetService'].value_counts().keys().tolist()


# In[249]:


y=data['InternetService'].value_counts()


# In[252]:


plt.figure(figsize=(10,10))
plt.bar(x,y,color='orange')
plt.xlabel('Categories of Internet Service',size=20)
plt.ylabel('Count of Categories',size=20)
plt.title('Distribution of Internet Service',size=32,color='gold')


# # b.	Build a histogram for the ‘tenure’ column:
#        i.	Set the number of bins to be 30
#        ii.	Set the color of the bins  to be ‘green’
#        iii.	Assign the title ‘Distribution of tenure’
# 

# In[126]:


plt.figure(figsize=(10,10))
plt.hist(data['tenure'],color='green',bins=30)
plt.title('Distribution of tenure',size=32)


# # c.	Build a scatter-plot between ‘MonthlyCharges’ & ‘tenure’. Map ‘MonthlyCharges’ to the y-axis & ‘tenure’ to the ‘x-axis’:
#     i.	Assign the points a color of ‘brown’
#     ii.	Set the x-axis label to ‘Tenure of customer’
#     iii.	Set the y-axis label to ‘Monthly Charges of customer’
#     iv.	Set the title to ‘Tenure vs Monthly Charges’
# 

# In[245]:


plt.figure(figsize=(10,10))
plt.scatter(data['tenure'],data['MonthlyCharges'],color='brown')
plt.xlabel('Tenure of customer',size=15,color='red')
plt.ylabel('Monthly Charges of customer',size=15,color='orange')
plt.title('Tenure vs Monthly Charges',size=32,color='gold')


# # d.	Build a box-plot between ‘tenure’ & ‘Contract’. Map ‘tenure’ on the y-axis & ‘Contract’ on the x-axis. 

# In[152]:



data.boxplot(column='tenure',by=['Contract'],figsize=(10,10))
plt.title('tenure’ & ‘Contract',size=32,color='brown')
plt.xlabel('Contract',size=15,color='red')
plt.ylabel('tenure',size=15,color='blue')


# # C)	Linear Regression:
#   a.	Build a simple linear model where dependent variable is ‘MonthlyCharges’ and independent variable is ‘tenure’
#      i.	Divide the dataset into train and test sets in 70:30 ratio. 
#      ii.	Build the model on train set and predict the values on test set
#      iii.	After predicting the values, find the root mean square error
#      iv.	Find out the error in prediction & store the result in ‘error’
#      v.	Find the root mean square error
# 

# In[196]:


x=data['tenure'] #independent
y=data['MonthlyCharges'] #dependent


# In[182]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# In[157]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.30)


# In[161]:


x_train=pd.DataFrame(x_train)


# In[164]:


x_test=pd.DataFrame(x_test)


# In[159]:


linear=LinearRegression()


# In[162]:


linear.fit(x_train,y_train)


# In[165]:


y_predict=linear.predict(x_test)


# In[168]:


msr=mean_squared_error(y_test,y_predict)


# In[169]:


Rootmsr=np.sqrt(msr)


# In[177]:


from sklearn.linear_model import Lasso


# In[178]:


model1=Lasso()


# In[ ]:





# In[174]:


print('mean_squared_error           :',msr)
print('Root of mean_squared_error   :',Rootmsr)


# # D)	Logistic Regression:
# a.	Build a simple logistic regression model where dependent variable is ‘Churn’ & independent variable is ‘MonthlyCharges’
# i.	Divide the dataset in 65:35 ratio
# ii.	Build the model on train set and predict the values on test set
# iii.	Build the confusion matric and get the accuracy score
# 

# In[183]:


x=pd.DataFrame(data['MonthlyCharges'])
y=data['Churn']


# In[188]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[189]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.35)
logistic=LogisticRegression()


# In[191]:


logistic.fit(x_train,y_train)


# In[192]:


y_predict=logistic.predict(x_test)


# In[193]:


score=accuracy_score(y_predict,y_test)


# In[195]:


print('Accuracy score :',score)


# # b.	Build a multiple logistic regression model where dependent variable is ‘Churn’ & independent variables are ‘tenure’ & ‘MonthlyCharges’
# i.	Divide the dataset in 80:20 ratio
# ii.	Build the model on train set and predict the values on test set
# iii.	Build the confusion matrix and get the accuracy score
# 

# In[199]:


x=pd.DataFrame(data[['tenure','MonthlyCharges']])
y=data['Churn']


# In[204]:


x.head()


# In[216]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


# In[201]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20)
logistic=LogisticRegression()


# In[205]:


x_train.head()


# In[202]:


logistic.fit(x_train,y_train)


# In[209]:


y_predict=logistic.predict(x_test)


# In[210]:


con_matrix=confusion_matrix(y_predict,y_test)


# In[211]:


accu=accuracy_score(y_predict,y_test)


# In[221]:


print('confusion_matrix :')
print(con_matrix)
print('---------------------------------')
print('accuracy_score   :',accu)
print('---------------------------------')
print('classification_report')
print(classification_report(y_predict,y_test))


# # E)	Decision Tree:
# a.	Build a decision tree model where dependent variable is ‘Churn’ & independent variable is ‘tenure’
# i.	Divide the dataset in 80:20 ratio
# ii.	Build the model on train set and predict the values on test set
# iii.Build the confusion matrix and calculate the accuracy

# In[222]:


x=pd.DataFrame(data['tenure'])
y=data['Churn']


# In[223]:


x.head()


# In[225]:


from sklearn.tree import DecisionTreeClassifier  


# In[226]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20)


# In[227]:


x_train.head()


# In[228]:


d_tree=DecisionTreeClassifier()  


# In[229]:


d_tree.fit(x_train,y_train)


# In[230]:


y_predict=d_tree.predict(x_test)


# In[231]:


con_matrix_tree=confusion_matrix(y_predict,y_test)
acc_tree=accuracy_score(y_predict,y_test)


# In[232]:


print('confusion_matrix :')
print(con_matrix_tree)
print('---------------------------------')
print('accuracy_score   :',acc_tree)
print('---------------------------------')
print('classification_report')
print(classification_report(y_predict,y_test))


# # F)	Random Forest:
# a.	Build a Random Forest model where dependent variable is ‘Churn’ & independent variables are ‘tenure’ and ‘MonthlyCharges’
# i.	Divide the dataset in 70:30 ratio
# ii.	Build the model on train set and predict the values on test set
# iii.	Build the confusion matrix and calculate the accuracy
# 

# In[233]:


x=data[['tenure','MonthlyCharges']]
y=data['Churn']


# In[236]:


x.head()


# In[237]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20)


# In[238]:


from sklearn.ensemble import RandomForestClassifier
r_tree=RandomForestClassifier(n_estimators=100)
r_tree.fit(x_train,y_train)


# In[240]:


y_predict=r_tree.predict(x_test)


# In[241]:


con_matrix_r_tree=confusion_matrix(y_predict,y_test)
acc_r_tree=accuracy_score(y_predict,y_test)


# In[242]:


print('confusion_matrix :')
print(con_matrix_r_tree)
print('---------------------------------')
print('accuracy_score   :',acc_r_tree)
print('---------------------------------')
print('classification_report')
print(classification_report(y_predict,y_test))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




