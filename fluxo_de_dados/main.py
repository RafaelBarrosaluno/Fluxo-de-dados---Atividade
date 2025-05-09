import pandas as pd
from sqlalchemy import create_engine

# Nome: Rafael Luis da Silva Barros
# RA: 28320078

# EXTRACT
url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
df = pd.read_csv(url)
# print(df.head())

# TRANSFORM
df = df[df ['Country']=='Brazil'].dropna()
df ['Total Cases'] = df ['Confirmed'].cumsum()
print(df.head())

# LOAD
engine = create_engine('sqlite:///covid_data.sqlite')
df.to_sql('brasil_covid', engine, if_exists='replace', index=False)
