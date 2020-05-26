import numpy as np
from numpy import random
from sys import exit

class NeuralNetwork:
    layers = []
    perceptrons_in_layers = []
    depth = 0
    def __init__(self,perceptrons_in_layers=[2,4,3,5,6,2,1], empty = False):
        self.depth = len(perceptrons_in_layers)-1
        self.perceptrons_in_layers = perceptrons_in_layers
        #creating wage matrix
        for i in range(self.depth):
            self.layers.append([[random.uniform(-10,10) for x in range(perceptrons_in_layers[i])]
                                for j in range(perceptrons_in_layers[i+1])])

    def predict(self,input):
        for i in range(self.depth):
            input = np.dot(self.layers[i], self.linear(input))
            input.transpose()
        return input

    def linear(self, x, a=2):
        return [i*a for i in x]

    # input should be input matrix and output should be vector
    def train(self, input, output, generations = 10, bests=4,
              population=10, max_mutation=0.5, mutation_prob=0.5, crossing_prob=0.5):

        pop = [NeuralNetwork(self.perceptrons_in_layers) for x in range(population)]
        bestones = [NeuralNetwork(self.perceptrons_in_layers) for x in range(population)]
        bestscores = [float("inf") for x in range(bests)]

        for i in range(generations):
            for obj in pop:
                individual = 0
                for outputx, inputx in zip(output, input):
                    individual += (outputx - obj.predict(inputx))**2
                for x in range(bests):
                    if bestscores[x] > individual:
                        bestscores[x] = individual
                        bestones[x] = obj
                        break
            pop = self.generateNewPopulation(population)

        self.layers = random.choice(bestones).layers

    def generateNewPopulation(self,population):
        pop = [NeuralNetwork(self.perceptrons_in_layers) for x in range(population)]
        return pop

#end of DNN

print(random.uniform(-2,2))
print(random.uniform(-2,2))
nn = NeuralNetwork([2,4,1])
print(nn.predict([2,2]))
nn.train([[1,2],[2,3],[2,1],[2,2]],[3,5,3,4], generations=10, population=10)
print(nn.predict([2,2]))
print(nn.predict([4,6]))

exit()