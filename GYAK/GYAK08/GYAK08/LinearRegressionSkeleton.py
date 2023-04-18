import numpy as np


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr

    def fit(self, X: np.array, y: np.array):
        self.m = 0
        self.c = 0
        n = float(len(X))

        for i in range(self.epochs):
            y_pred = self.m*X + self.c

            residuals = y - y_pred
            D_m = (-2/n) * sum(X * residuals)
            D_c = (-2/n) * sum(residuals)
            self.m = self.m - self.lr * D_m
            self.c = self.c - self.lr * D_c


    def predict(self, X):
        self.y_pred = []
        for i in X:
            y = self.m * i + self.c
            self.y_pred.append(y)
        self.y_pred = np.asarray(self.y_pred)
        

    def evaluate(self,y_test):
        print("Mean Absolute Error:", np.mean(np.abs(self.y_pred - y_test)))
        print("Mean Squared Error:", np.mean((self.y_pred - y_test)**2))

