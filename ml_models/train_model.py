import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
data = {
    'credit_score': [750, 600, 720, 500, 680, 800, 550, 710],
    'annual_income': [800000, 300000, 600000, 200000, 500000, 1000000, 250000, 700000],
    'loan_amount': [300000, 500000, 400000, 600000, 350000, 450000, 550000, 250000],
    'approved': [1, 0, 1, 0, 1, 1, 0, 1]
}
df=pd.DataFrame(data)
X=df[['credit_score','annual_income','loan_amount']]
y=df[['approved']]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=RandomForestClassifier()
model.fit(X_train,y_train)
joblib.dump(model,'ml_models/loan_model.pkl')
print("Model Trained Successfully")
