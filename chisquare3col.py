import pandas as pd
import scipy.stats as stats

def chisquare3col(data):
    # Fixed dependent variable
    y = 'leave'
    
    # Ensure the dependent variable exists in the dataset
    if y not in data.columns:
        print(f"Error: Dependent variable '{y}' does not exist in the dataset.")
        return
    
    # Select two independent variables
    # x1 = input('Select your first independent variable (x1): ')
    x1 = 'benefits'
    x2 = input('Select your second independent variable (x2): ')
    
    # Ensure the selected independent variables exist in the dataset
    if x1 not in data.columns or x2 not in data.columns:
        print(f"Error: One or both independent variables '{x1}', '{x2}' do not exist in the dataset.")
        return
    
    # Create a contingency table
    try:
        contingency_table = pd.crosstab(index=data[x1], columns=data[x2], values=data[y], aggfunc='count', dropna=True)
        
        # Perform Chi-Square test
        chi2, p, dof, expected = stats.chi2_contingency(contingency_table.fillna(0))
        
        print(f"Chi-Square statistic: {chi2}")
        print(f"p-value: {p}")
        print(f"Degrees of freedom: {dof}")
        print("Expected frequencies:")
        print(expected)
        
        if p < 0.05:
            print("Reject the null hypothesis: There is a significant association between the variables.")
        else:
            print("Fail to reject the null hypothesis: No significant association between the variables.")
    except Exception as e:
        print(f"Error performing Chi-Square test: {e}")
