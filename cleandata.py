import pandas as pd

def cleanGender(gender):
    if gender in ('M','CIS MALE','MAILE','CIS MALE','MAL','MALE (CIS)','MAKE','MAN','MSLE','MAIL','MALR','CIS MAN'):
        return 'MALE'
    elif gender in ('CIS FEMALE','F','WOMAN','FEMAKE','CIS-FEMALE/FEMME','FEMALE (CIS)','FEMAIL'):
        return 'FEMALE'
    else:
        return gender

def CleanAge(data):
    # คำนวณ IQR (Interquartile Range)
    Q1 = data['Age'].quantile(0.25)  # ควอไทล์ที่ 1 (Q1)
    Q3 = data['Age'].quantile(0.75)  # ควอไทล์ที่ 3 (Q3)
    IQR = Q3 - Q1

    # หาขอบเขตล่างและบน
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # กำจัดค่านอกเกณฑ์
    data = data[(data['Age'] >= lower_bound) & (data['Age'] <= upper_bound)]  # fix this line
    return data

def cleandata(data):
    data['Gender'] = data['Gender'].str.upper()
    data['Gender'] = data['Gender'].str.strip()
    data['Gender'] = data['Gender'].apply(cleanGender)
    data['Age'] = data['Age'].apply(lambda x: abs(x))  # Ensuring positive values for Age
    data = CleanAge(data)
    data = data[(data['Gender'] == 'MALE') | (data['Gender'] == 'FEMALE')]
    return data
