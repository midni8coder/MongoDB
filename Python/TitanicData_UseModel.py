import joblib
import pandas as pd


logistic_model = joblib.load('logisticRegression_Titanic.mdl')

titanic_test_data = pd.read_csv('dataframe.csv')
predicted = logistic_model.predict(titanic_test_data)
print(predicted)
