import numpy as np

class PegasosSVM:
    def __init__(self, lambda_param=0.01, max_iter=1000):
        self.lambda_param = lambda_param
        self.max_iter = max_iter
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        y = np.where(y <= 0, -1, 1)

        for t in range(1, self.max_iter + 1):
            idx = np.random.randint(0, n_samples)
            x_i = X[idx]
            y_i = y[idx]

            margin = y_i * (np.dot(x_i, self.weights) + self.bias)
            if margin >= 1:
                self.weights = (1 - 1/t) * self.weights
            else:
                self.weights = (1 - 1/t) * self.weights + self.lambda_param * y_i * x_i
                self.bias += self.lambda_param * y_i
    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return np.sign(linear_output)

if __name__ == "__main__":
    X = np.array([[2, 3], [1, 1], [2, 1], [3, 1]])
    y = np.array([1, -1, -1, 1])  # Labels should be -1 and 1 for SVM
    model = PegasosSVM(lambda_param=0.1, max_iter=1000)
    model.fit(X, y)
    predictions = model.predict(X)
    print("Predictions:", predictions)
    print("Weights:", model.weights)
    print("Bias:", model.bias)