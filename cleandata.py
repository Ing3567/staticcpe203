import pandas as pd

def cleanGender(gender):
    if gender in ('M','CIS MALE','MAILE','CIS MALE','MAL','MALE (CIS)','MAKE','MAN','MSLE','MAIL','MALR','CIS MAN'):
        return 'MALE'
    elif gender in ('CIS FEMALE','F','WOMAN','FEMAKE','CIS-FEMALE/FEMME','FEMALE (CIS)','FEMAIL'):
        return 'FEMALE'
    else:
        return gender
    

def CleanAge(data):
    # กรองค่าที่อยู่ระหว่าง 0 และ 100 ก่อน
    data = data[(data['Age'] >= 0) & (data['Age'] <= 100)]
    
    # คำนวณ quartiles
    Q1 = data['Age'].quantile(0.25)
    Q3 = data['Age'].quantile(0.75)
    
    # คำนวณ Interquartile Range (IQR)
    IQR = Q3 - Q1
    
    # คำนวณค่า outliers (1.5 เท่าของ IQR)
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # กำจัดค่า outliers
    data = data[(data['Age'] >= lower_bound) & (data['Age'] <= upper_bound)]
    
    return data

def cleandata(data):
    data['Gender'] = data['Gender'].str.upper()
    data['Gender'] = data['Gender'].str.strip()
    data['Gender'] = data['Gender'].apply(cleanGender)
    data['Age'] = data['Age'].apply(lambda x: abs(x))  # Ensuring positive values for Age
    data = CleanAge(data)
    data = data[(data['Gender'] == 'MALE') | (data['Gender'] == 'FEMALE')]
    data = data[(data['leave'] != 'Don\'t know')]
    data = data[(data['benefits'] != 'Don\'t know')]
    return data