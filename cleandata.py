import pandas as pd

def cleanGender(gender):
    if gender in ('M','CIS MALE','MAILE','CIS MALE','MAL','MALE (CIS)','MAKE','MAN','MSLE','MAIL','MALR','CIS MAN'):
        return 'MALE'
    elif gender in ('CIS FEMALE','F','WOMAN','FEMAKE','CIS-FEMALE/FEMME','FEMALE (CIS)','FEMAIL'):
        return 'FEMALE'
    else:
        return gender
    

def CleanAge(data):
    data = data[(data['Age'] >= 0) & (data['Age'] <= 100)]  # fix this line
    return data

def cleandata(data):
    data['Gender'] = data['Gender'].str.upper()
    data['Gender'] = data['Gender'].str.strip()
    data['Gender'] = data['Gender'].apply(cleanGender)
    data['Age'] = data['Age'].apply(lambda x: abs(x))  # Ensuring positive values for Age
    data = CleanAge(data)
    data = data[(data['Gender'] == 'MALE') | (data['Gender'] == 'FEMALE')]
    data = data[(data['leave'] != 'Don\'t know')]
    return data