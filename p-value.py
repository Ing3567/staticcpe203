import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def p_value(data):

    y = input('Select You y-axis: ')

    while(True):
        if(y.upper()=='X'):
            break
        
        data = pd.crosstab(data['leave'], data[y])

        
        chi2, p, dof, expected = chi2_contingency(data)

        
        print("Chi-Square Value:", chi2)
        print("p-value:", p)
        print("Degrees of Freedom:", dof)
        print("Expected Frequencies Table:")
        print(expected)
        print(f'Exit enter X')