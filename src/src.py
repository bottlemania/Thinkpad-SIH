import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

data = pd.DataFrame(pd.read_csv(r'C:\Users\ackra\Downloads\supermag.csv'))
t=data.shape
print(t)
data.describe()

X = data['MAGON'].values.reshape(-1, 1)  # Reshape X to a 2D array
y = data['MAGLAT'].values.reshape(-1, 1)  # Reshape y to a 2D array

#from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Decision Tree Regression
decision_tree = DecisionTreeRegressor()
decision_tree.fit(X_train, y_train)
y_pred_decision_tree = decision_tree.predict(X_test)

# Random Forest Regression
random_forest = RandomForestRegressor()
random_forest.fit(X_train, y_train)
y_pred_random_forest = random_forest.predict(X_test)

# Support Vector Regression (SVR)
svr = SVR()
svr.fit(X_train, y_train)
y_pred_svr = svr.predict(X_test)

# Gradient Boosting (XGBoost)
xgboost = XGBRegressor()
xgboost.fit(X_train, y_train)
y_pred_xgboost = xgboost.predict(X_test)

# Evaluate the models
def evaluate_model(y_true, y_pred, model_name):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"{model_name} Metrics:")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")
    print(f"R-squared: {r2}")
    

evaluate_model(y_test, y_pred_decision_tree, "Decision Tree")
evaluate_model(y_test, y_pred_random_forest, "Random Forest")
evaluate_model(y_test, y_pred_svr, "SVR")
evaluate_model(y_test, y_pred_xgboost, "XGBoost")