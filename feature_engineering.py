
def create_features(df):
    df['Humidity_Pressure_Ratio']=df['Humidity']/df['Pressure']
    return df
