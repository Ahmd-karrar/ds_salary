# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:24:37 2023

@author: ahmed.abdelmonim
"""

import pandas as pd 
df =pd.read_csv('C:/Users/ahmed.abdelmonim/Documents/ds_salary_proj/glassdoor_jobs.csv')

#salary parsing
df.columns
df['hourly'] = df['Salary Estimate'].apply(lambda x:1 if 'per hour' in x.lower()else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x:1 if 'employer provided salary:' in x.lower()else 0)

df= df[df['Salary Estimate']!= '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K' ,'').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2
