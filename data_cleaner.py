import pandas as pd

df = pd.read_csv('AAMSS.csv')

def fill_blanks(df):
    df["Other monetary comp"].fillna(0, inplace = True)
    df["Additional context on job title"].fillna('N/A', inplace = True)
    df["Additional context on income"].fillna('N/A', inplace = True)
    df["Currency - other"].fillna('N/A', inplace = True)

    return df

def convert_dtype(df):
    for x in df.index:
        df.loc[x,'Annual salary'] = int(df.loc[x,'Annual salary'].replace(',',''))
    
    df['Annual salary'] = pd.to_numeric(df['Annual salary'])
    
    return df

df = fill_blanks(df)
df = convert_dtype(df)
print(df['Additional context on job title'])
print(df.info())

data = df
