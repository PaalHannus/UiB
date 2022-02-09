import numpy as np
import matplotlib as plt


class LogReg():
    ''' A simple logistic regression implementation. '''

    def __init__(self, n):
        self.w = np.ones((n))
        self.b = 0
        self.loss = None

    def _cross_entropy_loss(self, Y_pred, Y_true):
        ''' Loss function as described in the lecture slides. '''
        return - (Y_true*(np.log(Y_pred)) + (1-Y_true)*np.log(1-Y_pred))

    def _sigmoid(self, val):
        return 1.0/(1 + np.exp(-val))

    def training_loop(self, training_data, labels, lr=0.01, epochs=1):
        '''
        SGD training loop for updating the weights of the model. Loops over all training examples 1-by-1. Computes
        the prediction, the loss, and finally updates the weights.

        Input:
        - training_data : Training dataset
        - labels : Ground truth labels
        - lr : Learning rate (Defaults to 0.01)
        - epochs : Number of epochs we train the model for. (Defaults to 1)

        Output:
        - Optional list of averaged loss for each epoch.
        '''
        m, n = training_data.shape
        losses = []

        for epoch in range(epochs):
            epoch_loss = 0
            for X, y in zip(training_data, labels):
                pred = self._sigmoid(np.dot(X, self.w) + self.b)
                loss = self._cross_entropy_loss(pred, y)
                epoch_loss += loss

                dw = (pred-y) * X
                db = (pred-y)

                self.w -= lr*dw
                self.b -= lr*db
            losses.append(epoch_loss / m)
        return losses

    def predict(self, X):
        if self.w.shape != X.shape:
            raise AssertionError(
                "ERROR: Input must be of same shape as training data")
        if self.w is None or self.b is None:
            raise AssertionError(
                "ERROR: Tool must first be fit to training data")
        pred = self._sigmoid(np.dot(X, self.w) + self.b)
        return 1 if pred > 0.5 else 0

    def plot_decision_boundary(self, X, y, title):
        x1 = np.array([min(X[:, 0]), max(X[:, 0])])
        m = -self.w[0]/self.w[1]
        c = -self.b/self.w[1]
        x2 = m*x1 + c

        # Plotting
        fig = plt.figure(figsize=(10, 8))
        plt.plot(X[:, 0][y == 0], X[:, 1][y == 0], "g^")
        plt.plot(X[:, 0][y == 1], X[:, 1][y == 1], "bs")
        plt.xlim([-2, 3])
        plt.ylim([-2, 2])
        plt.title(title)
        plt.plot(x1, x2, 'r-')
        plt.show()
