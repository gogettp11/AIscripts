import random

def eval(list):
    val1,val2 = list
    return (val1**2-val2**2)-(1-val1)**2

def genrateNewPopulation(maxSpan,minSpan,popAmount,bestone,leap):
    pop = []
    minx = bestone[0] - leap
    maxx = bestone[0] + leap
    miny = bestone[1] - leap
    maxy = bestone[1] + leap
    if minx < minSpan:
        minx = minSpan
    if maxx > maxSpan:
        maxx = maxSpan
    if miny < minSpan:
        miny = minSpan
    if maxy > maxSpan:
        maxy = maxSpan
    for obj in range(0,popAmount):
        obj = [random.uniform(minx,maxx),random.uniform(miny,maxy)]
        pop.append(obj)
    return pop

def main():

    pop = []
    bestone = None
    bestscore = float("-inf")
    maxSpan = 20000
    minSpan = -20000
    popAmount = 1
    leap = 1
    generations = 1000000

    for obj in range(0,popAmount):
        obj = [float(random.uniform(minSpan,maxSpan)),float(random.uniform(minSpan,maxSpan))]
        pop.append(obj)

    for generation in range(0,generations):
        print("Generation:" + generation.__str__() + "\n" + "Creatures: " + pop.__str__())
        for obj in pop:
            individual = eval(obj)
            if individual > bestscore:
                bestone = obj
                bestscore = individual
        #generate new generation
        print("best in generation: " + bestone.__str__())
        print("best score: " + bestscore.__str__() + "\n")
        pop = genrateNewPopulation(maxSpan,minSpan,popAmount,bestone,leap)


if __name__=="__main__":
    main()

