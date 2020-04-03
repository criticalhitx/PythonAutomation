import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math

dataset = pd.read_csv("D:\\Python\\Machine Learning\\01 Linear Reg\\mycsv.csv")
size = dataset['sizeList']
price = dataset['priceList']

x = np.array(size).reshape(-1,1)
y = np.array(price).reshape(-1,1)

print(x)

# Fit the model. Gradient Decent make optimization problem
model = LinearRegression()
model.fit(x, y)

#MSE and R vlaue

regression_model_mse = mean_squared_error(x, y)
print("MSE : ", math.sqrt(regression_model_mse))
print("R squared value : ", model.score(x,y))

# y = b0+b1x
#b0
print("b0 : ",model.intercept_[0])

#b1
print("b1 : ",model.coef_[0])

plt.scatter(x, y, color='green')
plt.plot(x, model.predict(x), color = 'black')
plt.title("Linear Regression")
plt.xlabel("Land Size")
plt.ylabel("Price")
plt.show()

print("Prediction by the model: ", model.predict([[50]]))

