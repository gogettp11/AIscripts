import random
from numpy import sin

def eval(list):
    val1,val2 = list
    return (val1**2)+sin(val2)

def genrateNewPopulation(limes ,popAmount,
                         bestone, mutation, bests, m_prob, c_prob,features):
    pop = []
    for x in range(popAmount):
        if random.random() < c_prob:
            obj = [random.choice(bestone)[x] for x in range(features)]
        else:
            obj = random.choice(bestone)
        if random.random() < m_prob:
            rand_feature = random.randint(0, features-1)
            obj[rand_feature] = obj[rand_feature] + random.uniform(-mutation, mutation)
            if limes[rand_feature][1] < obj[rand_feature] or obj[rand_feature] < limes[rand_feature][0]:
                obj[rand_feature] = float(random.uniform(limes[rand_feature][0], limes[rand_feature][1]))
        pop.append(obj)
    return pop

def main():

    pop = []
    bests = 3
    bestones = [[0.0 for x in range(2)] for y in range(bests)]
    bestscores = [float("-inf") for x in range(bests)]
    limes = [[-10000, 10000], [-100000, 100000]]
    popAmount = 12
    max_mutation = 10
    generations = 1000
    mutation_prob = 0.9
    crossing_prob = 0.3
    features = len(bestones[0])

    for obj in range(0,popAmount):
        obj = [float(random.uniform(limes[0][0],limes[0][1])),float(random.uniform(limes[1][0],limes[1][1]))]
        pop.append(obj)

    for generation in range(0,generations):
        print("Generation:" + generation.__str__() + "\n" + "Creatures: " + pop.__str__())
        for obj in pop:
            individual = eval(obj)
            for x in range(bests):
                if bestscores[x] < individual:
                    bestscores[x] = individual
                    bestones[x] = obj
                    break
        #generate new generation
        print("best in generation: " + bestones.__str__())
        print("best score: " + bestscores.__str__() + "\n")
        pop = genrateNewPopulation(limes, popAmount, bestones, max_mutation, bests, mutation_prob, crossing_prob,features)


if __name__=="__main__":
    main()

