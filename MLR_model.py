# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:27:03 2024

@author: ahmed.abdelmonim
"""

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import statsmodels.formula.api as smf

df = pd.read_csv('eda_data.csv')

# choose relevant columns 
df.columns

df_model = df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue',
               'num_comp','hourly','employer_provided',
             'job_state','same_state','age','python_yn','spark','aws','excel','job_simp','seniority','desc_len']]
#deal with categorical varibules 
df_model[['Size','Type of ownership','Industry','Sector',
'Revenue','job_state','same_state','python_yn', 'spark', 'aws', 'excel',
'job_simp', 'seniority']] =df_model[['Size','Type of ownership','Industry','Sector',
'Revenue','job_state','same_state','python_yn', 'spark', 'aws', 'excel','job_simp', 'seniority']].astype('category')
df_model.info()     
df_model.rename(columns={"Type of ownership": "Type_of_ownership"}, inplace=True)
# train test split 
msk = np.random.rand(len(df_model)) < 0.8
train = df_model[msk]
test =df_model[~msk]

# Fitting MLR model
salary_model = smf.ols('avg_salary~Rating+Size+ Type_of_ownership + Industry + Sector +Revenue  + num_comp +hourly + employer_provided +job_state + same_state + age + python_yn + spark + aws + excel + job_simp + seniority + desc_len ',data= train ).fit()
salary_model.summary()

#check for multicollinearty using vif function
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor
# Break data into left and right hand side ; y and x
y,x = dmatrices('avg_salary~Rating+Size+ Type_of_ownership + Industry + Sector +Revenue  + num_comp +hourly + employer_provided +job_state + same_state + age + python_yn + spark + aws + excel + job_simp + seniority + desc_len ',
      data= train , return_type="dataframe")
vif = pd.Series([variance_inflation_factor(x.values,i)for i  in range(x.shape[1])],index=x.columns)
vif

# is observed that variables seniority and job_state has high vif 
train_1 = train[['avg_salary','Rating','Size','Type_of_ownership','Industry','Sector','Revenue',
               'num_comp','hourly','employer_provided',
             'same_state','age','python_yn','spark','aws','excel','job_simp','desc_len']]
test_1 = test[['avg_salary','Rating','Size','Type_of_ownership','Industry','Sector','Revenue',
               'num_comp','hourly','employer_provided',
             'same_state','age','python_yn','spark','aws','excel','job_simp','desc_len']]

salary_model = smf.ols('avg_salary~Rating+Size+ Type_of_ownership + Industry + Sector +Revenue  + num_comp +hourly + employer_provided + same_state + age + python_yn + spark + aws + excel + job_simp + desc_len ',data= train_1).fit()
salary_model.summary()

y,x = dmatrices('avg_salary~Rating+Size+ Type_of_ownership + Industry + Sector +Revenue  + num_comp +hourly + employer_provided + same_state + age + python_yn + spark + aws + excel + job_simp + desc_len ',data= train_1, return_type="dataframe")
vif = pd.Series([variance_inflation_factor(x.values,i)for i  in range(x.shape[1])],index=x.columns)
vif
#calculating Fitted Values and Residuals
train_1= train_1.assign(pred=pd.Series(salary_model.fittedvalues))
train_1 = train_1.assign(res=pd.Series(salary_model.resid))

#Residuals v/s predicted plot
train_1.plot.scatter(x='pred',y='res')

#It is observed that residuals are randomly distributed and uncorelated with predicted values
#Check if distribution of errors "Normal"
import statsmodels.api as sm
fig = sm.graphics.qqplot(train_1.res,line = '45',fit=True)
#Most of these Points are close to the line except few values indicating no serious deviation from Normality
# shapiro wilk test 
import scipy as sp
sp.stats.shapiro(train_1.res)

#calculate RMSE values based on residuls using first principle 

from math import sqrt 
RMSE = sqrt((train_1['res']**2).mean())
RMSE

test_1 = test_1.assign(pred=pd.Series(salary_model.predict(test_1)))
test_1 = test_1.assign(res = pd.Series(test_1.avg_salary - test_1.pred))

RMSEtest=pd.Series(np.sqrt((test_1.res)**2).mean())

RMSEtest










