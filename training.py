import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df=pd.read_csv("height-weight.csv")
x = df[["Weight"]]
y = df["Height"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=42)

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

pipe.fit(x_train, y_train)

y_pred = pipe.predict(x_test)
print("R2 Score:", r2_score(y_test, y_pred))

new_weight = pd.DataFrame([[75]], columns=["Weight"])
prediction = pipe.predict(new_weight)

print("Predicted Height (75kg):", prediction[0])

plt.scatter(x_train, y_train)
X_line = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
plt.plot(X_line, pipe.predict(X_line))
plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("Height vs Weight")
plt.show()

