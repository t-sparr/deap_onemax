import random
from setup_ga import toolbox
from config import POP_SIZE, NGEN, CXPB, MUTPB

def run_evolution():

    pop = toolbox.population(n=POP_SIZE)

    for ind in pop:
        ind.fitness.values = toolbox.evaluate(ind)
        
    for gen in range(NGEN):

        offspring = toolbox.select(pop, len(pop))

        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                toolbox.mate(child1, child2)
                del(child1.fitness.values)
                del(child2.fitness.values)
        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        for ind in invalid_ind:
            ind.fitness.values = toolbox.evaluate(ind)
                
        pop[:] = offspring

        fits = [ind.fitness.values[0] for ind in pop]
        print(f"Gen {gen}: Max Fitness = {max(fits)}")

    best = toolbox.select(pop, 1)[0]
    print("Best individual:", best)
    print("Fitness:", best.fitness.values[0])