import random
from setup_ga import toolbox
import yaml

import pandas as pd
import matplotlib.pyplot as plt

def load_config():
    with open('config.yml', 'r') as f:
        return yaml.safe_load(f)

def run_evolution():
    config = load_config()
    pop_size = config['POP_SIZE']
    next_gen = config['NGEN']
    crossover_prop = config['CXPB']
    mutation_rate = config['MUTPB']

    

    pop = toolbox.population(n=pop_size)

    for ind in pop:
        ind.fitness.values = toolbox.evaluate(ind)

    gen_data = []
        
    for gen in range(next_gen):

        offspring = toolbox.select(pop, len(pop))

        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < crossover_prop:
                toolbox.mate(child1, child2)
                toolbox.mate(child1, child2)
                del(child1.fitness.values)
                del(child2.fitness.values)
        for mutant in offspring:
            if random.random() < mutation_rate:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        for ind in invalid_ind:
            ind.fitness.values = toolbox.evaluate(ind)
                
        pop[:] = offspring

        fits = [ind.fitness.values[0] for ind in pop]

        max_fit = max(fits)
        avg_fit = sum(fits) / len(fits)
        gen_data.append({"Generation": gen, "Max": max_fit, "Avg": avg_fit})
        print(f"Gen {gen}: Max Fitness = {max(fits)}")


    df = pd.DataFrame(gen_data)
    df.plot(x="Generation", y=["Max","Avg"], title="Fitness Over Generations")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    


