
from data_loader import load_data
from preprocessing import preprocess
from feature_engineering import create_features
from model_training import train_models
from evaluation import evaluate
from report_generator import save_report

df=load_data('../data/sample_weather.csv')
df=preprocess(df)
df=create_features(df)

X=df[['Humidity','WindSpeed','Pressure','Rainfall']]
y=df['Temperature']

models,X_test,y_test=train_models(X,y)
results=evaluate(models,X_test,y_test)

print(results)
save_report(results)
