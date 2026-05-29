
import pandas as pd

def save_report(results,path='model_report.csv'):
    pd.DataFrame(results).T.to_csv(path)
