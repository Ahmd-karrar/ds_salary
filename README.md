# Data Science Salary Estimator: Project Overview
- A data science salary  model was created to help data scientists negotiate their income when they get a job.
- Scraped over 1000 job descriptions from glassdoor using python and selenium
- Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
# Data Cleaning(Data cleaning.py)
- salary parsing numeric data out of salary.
- Company name text only.
- Removed rows without salary
- Parsed rating out of company text
- Made a new column for company state
- Added a column for if the job was at the company’s headquarters
- Transformed founded date into age of company
- Made columns for if different skills were listed in the job description:
Python
R
Excel
AWS
Spark
- Column for simplified job title and Seniority
- Column for description length
# EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.

![sector](https://github.com/Ahmd-karrar/ds_salary/assets/155227956/6aefca44-3cf8-4702-95c8-eb99ba9b49b3)
![newplot (9)](https://github.com/Ahmd-karrar/ds_salary/assets/155227956/a26790ec-5a5f-4c63-9364-b2d9071bf843)
![sp](https://github.com/Ahmd-karrar/ds_salary/assets/155227956/eddf7c6d-00c3-4709-8579-0edccf8e2681)

# Model Building
- choose relevant columns
- deal with categorical variables
- split the data into train and test sets
- Fitting MLR model
- check for multicollinearity using vif function
- calculating Fitted Values and Residuals
- Residuals v/s predicted plot
- Check if distribution of errors "Normal"
- shapiro wilk test 
- calculate RMSE values based on residuals using first principle




