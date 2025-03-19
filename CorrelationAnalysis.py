import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def CorrelationAnalysis(data):

    size = {
    '1-5': 1,
    '6-25': 2,
    '26-100': 3,
    '100-500': 4,
    '500-1000': 5,
    'More than 1000': 6
    }
    leave = {
    'Somewhat easy': 2,
    'Very easy': 1,
    'Somewhat difficult': 3,
    'Very difficult': 4,
    }
    benefits = {
    'No': 0,
    'Yes': 1,
    }
    tech_company = {
    'No': 0,
    'Yes': 1,
    }
    remote_work = {
    'No': 0,
    'Yes': 1,
    }
    data['no_employees'] = data['no_employees'].map(size)
    data['leave'] = data['leave'].map(leave)
    data['benefits'] = data['benefits'].map(benefits)
    data['tech_company'] = data['tech_company'].map(tech_company)
    data['remote_work'] = data['remote_work'].map(remote_work)
    
    correlation_size_leave = np.corrcoef(data['no_employees'], data['leave'])[0, 1]
    correlation_benefits_leave = np.corrcoef(data['benefits'], data['leave'])[0, 1]
    correlation_tech_company_leave = np.corrcoef(data['tech_company'], data['leave'])[0, 1]
    correlation_remote_work_leave = np.corrcoef(data['remote_work'], data['leave'])[0, 1]

    print(f"Correlation between number of employees and leave: {correlation_size_leave}")
    print(f"Correlation between benefits and leave: {correlation_benefits_leave}")
    print(f"Correlation between tech_company and leave: {correlation_tech_company_leave}")
    print(f"Correlation between remote_work and leave: {correlation_remote_work_leave}")