import numpy as np
import matplotlib.pyplot as plt


class FeedforwardNN():
    def __init__(self, structure):
        self._layers, self.act = list(zip(*structure))
        self._params = {}
        self.grad = {}
        self.a_dict = {
            "relu": self.relu,
            "sigmoid": self.sigmoid,
        }
        self.d_dict = {
            "relu": self.d_relu,
            "sigmoid": self.d_sigmoid
        }
        self.__init_weights()

    def __init_weights(self):
        self._params['W'] = {}
        self._params['B'] = {}
        for layer in (range(1, len(self._layers))):
            self._params['W'][layer] = np.random.rand(
                self._layers[layer], self._layers[layer-1])
            self._params['B'][layer] = np.random.rand(self._layers[layer], 1)

    def sigmoid(self, val):
        return 1.0/(1 + np.exp(-val))

    def d_sigmoid(self, val):
        return np.exp(-val) / (np.exp(-val)+1)**2

    def relu(self, val):
        return np.where(val > 0, val, 0)

    def d_relu(self, val):
        return np.where(val > 0, 1, 0)

    def softmax(self, val):
        exps = np.exp(val - val.max())
        return exps / np.sum(exps, axis=0)

    def d_softmax(self, val):
        exps = np.exp(val - val.max())
        return exps / np.sum(exps, axis=0) * (1 - exps / np.sum(exps, axis=0))

    def cross_entropy(self, predictions, targets, epsilon=1e-9):
        predictions = np.clip(predictions.squeeze(), epsilon, 1. - epsilon)

        N = predictions.shape[0]
        ce = -np.sum(targets*np.log(predictions))/N
        return ce

    def predict(self, X):
        '''
        The predict function.
        Input: 
        - X 
        Output:
        - Predicted class in the form of a softmax
        '''
        A = X.T
        for layer in range(1, len(self._layers)-1):
            Z = np.dot(self._params['W'][layer], A) + self._params['B'][layer]
            A = self.a_dict[self.act[layer]](Z)
        Z = np.dot(self._params['W'][len(self._layers)-1],
                   A) + self._params['B'][len(self._layers)-1]
        A = self.softmax(Z)
        return A

    def forward(self, X):
        '''
        Forward propagation. Loops through all layers and calculates activations of each layer. The values are stored in 
        a variable called grad
        '''
        grad = {
            'A': {},
            'Z': {},
        }
        A = X.T
        grad['A'][0] = A

        for layer in range(1, len(self._layers)-1):
            Z = np.dot(self._params['W'][layer], A) + self._params['B'][layer]
            # print(self._params['W'][layer].shape)
            #A = self.sigmoid(Z)
            A = self.a_dict[self.act[layer]](Z)
            grad['A'][layer] = A
            grad['Z'][layer] = Z

        Z = np.dot(self._params['W'][len(self._layers)-1],
                   A) + self._params['B'][len(self._layers)-1]
        A = self.softmax(Z)

        grad["A"][len(self._layers) - 1] = A
        grad["Z"][len(self._layers) - 1] = Z
        self.grad = grad

        return A

    def backwards(self, y_true):
        '''
        Backwards propagation. Loops through the layers in a reversed order and calculates the gradients of each layer.
        The gradients are stores in a dictionary. In the last network layer the ground truth and the prediction are
        compared.

        Input:
        - y_true: ground truth
        '''
        n_layers = len(self._layers)
        W = self._params['W']
        B = self._params['B']
        grad = self.grad

        gradients = {
            'Z': {},
            'W': {},
            'b': {}
        }
        for layer in reversed(range(1, n_layers)):
            if layer == n_layers-1:
                dZ = grad['A'][n_layers-1].reshape(
                    grad['Z'][n_layers-1].shape) - y_true.reshape(grad['Z'][n_layers-1].shape)
            else:
                dZ = np.dot(W[layer+1].T, dZ) * \
                    self.d_dict[self.act[layer]](grad['Z'][layer])

            dW = np.dot(dZ, grad['A'][layer-1].T)
            db = dZ

            gradients['Z'][layer] = dZ
            gradients['W'][layer] = dW
            gradients['b'][layer] = db
        self.gradients = gradients
        return gradients

    def optimize(self, lr):
        '''
        Loops over the layers of the network and updates the weights and biases in each layer based on gradients
        from backprop and learning rate.

        Input:
        - lr : learning rate
        '''
        for layer in range(1, len(self._layers)):
            before = self._params['W'][layer].copy()
            self._params['W'][layer] -= lr * self.gradients['W'][layer]
            self._params['B'][layer] -= lr * self.gradients['b'][layer]

    def reset_gradients(self):
        '''
        Simply resets the gradients of the model
        '''
        self.gradients = {}

    def train(self, data, labels, n_epochs, lr=0.01):
        '''
        Neural network training procedure. Will loop over the training data for n_epochs times. For each training
        example it will update the weights based on the gradients from backprop and the learning rate. 
        Additionally we keep the loss during all epochs for visualisation purposes.

        Input:
        - data
        - labels
        - n_epochs : number of training epochs
        - lr : learning rate (default = 0.01)

        Output:
        - A list containing the averaged error for each epoch
        '''
        error = []
        for epoch in range(n_epochs):
            epoch_loss = 0
            for x, y in zip(data, labels):

                pred = self.forward(x)
                epoch_loss = epoch_loss + self.cross_entropy(pred, y)
                self.backwards(y)
                self.optimize(lr)

            error.append(epoch_loss / len(labels))
        return error
