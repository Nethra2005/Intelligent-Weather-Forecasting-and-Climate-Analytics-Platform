
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

def train_models(X,y):
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

    models={
        'LinearRegression':LinearRegression(),
        'DecisionTree':DecisionTreeRegressor(random_state=42),
        'RandomForest':RandomForestRegressor(n_estimators=100,random_state=42)
    }

    trained={}
    for name,model in models.items():
        model.fit(X_train,y_train)
        trained[name]=model

    return trained,X_test,y_test
