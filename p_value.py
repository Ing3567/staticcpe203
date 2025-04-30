import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def p_value(data):

    y = input('Select You y-axis: ')

    data = pd.crosstab(data['leave'], data[y])
  
    chi2, p, dof, expected = chi2_contingency(data)

    print(data)
    print("Chi-Square Value:", chi2)
    print("p-value:", p)
    print("Degrees of Freedom:", dof)
    print("Expected Frequencies Table:")
    print(expected)
    if p < 0.05:
        print("Reject the null hypothesis: There is a significant association between the variables.")
    else:
        print("Fail to reject the null hypothesis: No significant association between the variables.")
    return p