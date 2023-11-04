import pandas as pd
data = pd.read_csv('forbes_2640_billionaires.csv')

data['age'].fillna(data['age'].mean(), inplace=True) 
data = data.dropna()  
data['age'] = data['age'].astype(int)  
data['source'] = data['source'].str.lower()  
selected_columns = ["Self-Made Score","Philanthropy Score","Marital Status","Education","Bachelor","Master","Doctorate","Drop Out"]
data = data.drop(selected_columns, axis=1)  
from scipy import stats
z_scores = stats.zscore(data['net_worth'])
data = data[(abs(z_scores) < 5)]

age_bins = [0, 30, 40, 50, 60, 70, data['age'].max()]
age_labels = ['0-29', '30-39', '40-49', '50-59', '60-69', '70+']
data['age_group'] = pd.cut(data['age'], bins=age_bins, labels=age_labels)
data['have_children'] = data['Children'].apply(lambda x: 1 if x > 0 else 0)
data = pd.get_dummies(data)
data.to_csv('/home/doc-bd-a1/res_dpre.csv', index=False)
