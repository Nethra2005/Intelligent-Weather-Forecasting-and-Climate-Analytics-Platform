
from sklearn.metrics import mean_absolute_error,r2_score

def evaluate(models,X_test,y_test):
    results={}
    for name,model in models.items():
        pred=model.predict(X_test)
        results[name]={
            'MAE':mean_absolute_error(y_test,pred),
            'R2':r2_score(y_test,pred)
        }
    return results
