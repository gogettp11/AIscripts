from numpy import random
from sys import exit
from numpy import dot

#input and output may be matrixes or vectors
def train(neuralNetwork, input, output, generations=10, population=10, bests = 4, crossing_prob=0.5,
           mutation_prob=0.5, learning_rate=0.3):
    def mutate(obj):
        for x in range(len(neuralNetwork)):
            for y in range(len(neuralNetwork[x])):
                for z in range(len(neuralNetwork[x][y])):
                    obj[x][y][z] = obj[x][y][z] + random.uniform(-learning_rate, learning_rate)
    def ga():
        pop = []
        for x in range(population):
            best1 = random.randint(0, bests)
            best2 = random.randint(0, bests)
            obj = []
            if random.random() < crossing_prob:
                for i in range(len(neuralNetwork)):
                    if i%2:
                        obj.append(bestones[best1][i])
                    else:
                        obj.append(bestones[best2][i])
            else:
                obj = bestones[best1]
            if random.random() < mutation_prob:
                mutate(obj)
            pop.append(obj)
        return pop

    print("before:" + neuralNetwork.__str__())

    pop = [[[[random.uniform(-2, 2) for x in range(len(neuralNetwork[i][j]))]
            for j in range(len(neuralNetwork[i]))] for i in range(len(neuralNetwork))] for a in range(population)]
    bestones = [[[[random.uniform(-2, 2) for x in range(len(neuralNetwork[i][j]))]
            for j in range(len(neuralNetwork[i]))] for i in range(len(neuralNetwork))] for a in range(population)]
    bestscores = [float("inf") for x in range(bests)]

    for i in range(generations):
        for obj in pop:
            individual = 0
            for outputx, inputx in zip(output, input):
                individual += (outputx - predict(obj, inputx)) ** 2
            for x in range(bests):
                if bestscores[x] > individual:
                    bestscores[x] = individual
                    bestones[x] = obj
                    break
        pop = ga()
    best_nn = bestones[bests-1]
    print("after:" + best_nn.__str__())
    return best_nn

def linear(x, a=2):
    return [i * a for i in x]
def predict(neuralNetwork, input):
    for i in range(len(neuralNetwork)):
        input = dot(neuralNetwork[i], linear(input))
        input.transpose()
    return input
def initialize(neurons = [2,4,1]):
    nn = ([[[random.uniform(-2, 2) for x in range(neurons[i])]
            for j in range(neurons[i + 1])] for i in range(len(neurons)-1)])
    return nn

nnx = initialize()
nny = initialize()
print(nnx)
print(nny)
print(predict(nnx, [5, 3]))
print(predict(nny, [5, 3]))
nnx = train(neuralNetwork=nnx, input=[[1,2],[2,3],[4,3],[3,2]], output=[3,5,7,5], learning_rate=1, population=100,generations=100,bests=15)
nny = train(nny, [[1,2],[2,3],[4,3],[3,2]], [3,5,7,5], learning_rate=0.5, population=20,generations=100,bests=7, crossing_prob=0.2)
print(predict(nnx, [5, 3]))
print(predict(nny, [5, 3]))

exit()