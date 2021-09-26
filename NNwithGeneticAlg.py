from numpy import random
from sys import exit
from numpy import dot
import math
import copy

#input and output may be matrixes or vectors
def train(neuralNetwork, input, output, generations=10, population=10, bests = 4, crossing_prob=0.5,
           mutation_prob=0.5, learning_rate=0.3,function="linear"):

    def mutate(obj):
        for x in range(len(neuralNetwork)):
            for y in range(len(neuralNetwork[x])):
                for z in range(len(neuralNetwork[x][y])):
                    if random.random() < mutation_prob:
                        obj[x][y][z] = obj[x][y][z] + random.uniform(-learning_rate, learning_rate)
        return obj

    def crossing(mother, father):
        for x in range(len(neuralNetwork)):
            for y in range(len(neuralNetwork[x])):
                for z in range(len(neuralNetwork[x][y])):
                    if random.random() < crossing_prob:
                        mother[x][y][z] = father[x][y][z]
        return mother

    def ga(best_nn):
        pop = []
        pop.append(best_nn)
        for x in range(population-1):
            best1 = random.randint(0, bests)
            best2 = random.randint(0, bests)
            obj = copy.deepcopy(bestones[best1])
            obj2 = copy.deepcopy(bestones[best2])
            obj = crossing(obj, obj2)
            obj = mutate(obj)
            pop.append(obj)
        return pop

    pop = [[[[random.uniform(-2, 2) for x in range(len(neuralNetwork[i][j]))]
            for j in range(len(neuralNetwork[i]))] for i in range(len(neuralNetwork))] for a in range(population)]
    bestones = [[[[0.0 for x in range(len(neuralNetwork[i][j]))]
            for j in range(len(neuralNetwork[i]))] for i in range(len(neuralNetwork))] for a in range(bests)]
    bestscores = [float("inf") for x in range(bests)]

    best_score = 0
    for outputx, inputx in zip(output, input):
        best_score += abs((outputx - predict(neuralNetwork, inputx, function)))
    bestscores[0] = best_score
    bestones[0] = neuralNetwork

    print("score at the beggining: " + best_score.__str__())

    for i in range(generations):
        for obj in pop:
            individual = 0
            for outputx, inputx in zip(output, input):
                individual += abs(outputx - predict(obj, inputx,function))
            for x in range(bests):
                if bestscores[x] > individual:
                    bestscores[x] = individual
                    bestones[x] = copy.deepcopy(obj)
                    break
        pop = ga(bestones[0])
    print("score after: " + bestscores[0].__str__())
    return bestones[0]

def predict(neuralNetwork, input,function="linear"):
    for i in range(len(neuralNetwork)):
        input = dot(neuralNetwork[i], Functions.__dict__[function](input))
        input.transpose()
    return input[0]

def initialize(neurons = [2,4,1]):
    nn = ([[[random.uniform(-2, 2) for x in range(neurons[i])]
            for j in range(neurons[i + 1])] for i in range(len(neurons)-1)])
    return nn

class Functions():
    def linear(x, a=1):
        return [i * a for i in x]
    def sigmoid(x):
        return [1 / (1 + math.exp(-x)) for x in x]
    def relu(x):
        return [a * (a > 0) for a in x]

nnx = initialize()
nny = initialize()
print(predict(nnx, [3, 7]))
print(predict(nny, [3, 7]))
nnx = train(nnx, [[2,3],[3,2],[4,1],[5,2],[1,4],[2,3],[7,6],[4,7],[2,3],[3,2],[21,32]],[5,5,5,7,5,5,13,11,5,5,53],crossing_prob=0.5,generations=300,bests=10,population=50)
nny = train(nny, [[2,3],[21,32],[33,17]],[5,53,50],generations=3000,population=20,bests=4,crossing_prob=0.4,mutation_prob=0.4)
print(predict(nnx, [150, 17]))
print(predict(nny, [0, 17]))

exit()