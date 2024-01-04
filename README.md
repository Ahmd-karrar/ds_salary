# Data Science Salary Estimator: Project Overview
- A data science salary  model was created to help data scientists negotiate their income when they get a job.
- Scraped over 1000 job descriptions from glassdoor using python and selenium
- Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
# Data Cleaning
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
[download](https://github.com/Ahmd-karrar/ds_salary/assets/155227956/0a9c1a98-a775-4bc2-bd1b-82f6faf64721)
