
def preprocess(df):
    df=df.drop_duplicates()
    return df.fillna(df.mean(numeric_only=True))
