import pprint
from numpy import random
import numpy as np


class NeuralNetwork:
    layers = []
    depth = 0
    def __init__(self,perceptrons_in_layers=[3,4,1]):
        self.depth = len(perceptrons_in_layers)
        for i in range(len(perceptrons_in_layers)-1):
            self.layers.append([[random.uniform(-2,2) for x in range(perceptrons_in_layers[i])]
                                for j in range(perceptrons_in_layers[i+1])])


    def predict(self,input):
        for i in range(self.depth-1):
            input = np.dot(self.layers[i], self.linear(input))
            input.transpose()
        return input

    def linear(self,x,a=2):
        return [i*a for i in x]

    def train(self,input,output,iter):
        pass


nn = NeuralNetwork()
print(nn.layers)
print(nn.predict([2,3,4]))
