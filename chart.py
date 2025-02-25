import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def chart(data):
    # Arrays for storing columns based on their type
    int_columns = []
    object_columns = []
    bool_columns = []

    # Separate columns based on data type
    for column in data.columns:
        if pd.api.types.is_integer_dtype(data[column]):
            int_columns.append(column)
        elif pd.api.types.is_bool_dtype(data[column]):
            bool_columns.append(column)
        elif pd.api.types.is_object_dtype(data[column]):
            object_columns.append(column)

    while True:
        typechart = input(f'Select your chart (bar,box): ').lower()

        if typechart == 'bar':
            # Bar chart requires x-axis categorical and y-axis numerical
            x = input(f'Select your x-axis (categorical from {object_columns}): ')
            
            if x in data.columns:
                sns.displot(x=x, data=data,kde=True,hue="Gender")
                plt.show()
            else:
                print("Invalid column selection! Please check if the column names exist.")
            break
        elif typechart == 'box':
            # Box plot typically uses categorical x-axis and numerical y-axis
            x = input(f'Select your x-axis (categorical from {object_columns}): ')
            y = input(f'Select your y-axis (numerical from {int_columns}): ')

            if x in data.columns and y in data.columns:
                sns.boxplot(x=x, y=y, data=data)
                plt.show()
            else:
                print("Invalid column selection! Please check if the column names exist.")
            break

        else:
            print("Invalid chart type selected! Please try again.")

