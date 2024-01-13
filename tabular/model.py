# Import libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
import pandas as pd
import pickle


# Load the Iris dataset
diabetes = load_diabetes()

# Access the data and target variables
X = diabetes.data  # Features (sepal length, sepal width, petal length, petal width)
y = diabetes.target  # Target variable (species: setosa, versicolor, virginica)


# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Model is now trained and can be used for predictions
with open('model/model.pkl', 'wb') as file:
    pickle.dump(model, file)