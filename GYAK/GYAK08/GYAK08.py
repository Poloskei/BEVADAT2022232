import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

df['target'] = iris.target
X = df['petal length (cm)'].values
y = df['petal width (cm)'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from LinearRegressionSkeleton import LinearRegression

LinReg = LinearRegression(epochs=1000,lr=0.0001)
LinReg.fit(X_train,y_train)
y_pred = LinReg.predict(X_test)

#print(accuracy_score(y_test,y_pred))
LinReg.evaluate(y_pred,y_test)