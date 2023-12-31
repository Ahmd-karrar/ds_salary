# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 12:05:04 2023

@author: ahmed.abdelmonim
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/ahmed.abdelmonim/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)