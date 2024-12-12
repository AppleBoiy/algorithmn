import numpy as np


class PegasosSVM:
    def __init__(self, lambda_param=0.01, max_iter=1000):
        self.lambda_param = lambda_param
        self.max_iter = max_iter
        self.weights = None
        self.intercept = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.intercept = 0
        for t in range(1, self.max_iter + 1):
            idx = np.random.randint(0, n_samples)
            x_i = X[idx]
            y_i = y[idx]
            eta_t = 1 / (self.lambda_param * t)
            margin = y_i * (np.dot(self.weights, x_i) + self.intercept)
            if margin < 1:
                self.weights = (1 - eta_t * self.lambda_param) * self.weights + eta_t * y_i * x_i
                self.intercept = self.intercept + eta_t * y_i
            else:
                self.weights = (1 - eta_t * self.lambda_param) * self.weights
                self.intercept = self.intercept

            self.weights = np.minimum(1, (1 / np.sqrt(self.lambda_param)) / np.linalg.norm(self.weights)) * self.weights

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.intercept
        return np.sign(linear_output)
