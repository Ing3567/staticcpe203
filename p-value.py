import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def p_value(data):

    y = input('Select You y-axis: ')
        
    data = np.array([[20, 30, 50],
                    [40, 10, 50]])

    
    chi2, p, dof, expected = chi2_contingency(data)

    
    print("Chi-Square Value:", chi2)
    print("p-value:", p)
    print("Degrees of Freedom:", dof)
    print("Expected Frequencies Table:")
    print(expected)