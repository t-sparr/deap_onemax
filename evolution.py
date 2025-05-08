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
    array_size = config['IND_SIZE']
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

        fits = [ind.fitness.values[0] for ind in pop]
        max_fit = max(fits)
        avg_fit = sum(fits) / len(fits)

        gen_data.append({
            "Generation": gen,
            "Max": max_fit,
            "Avg": avg_fit
        })

        print(f"Gen {gen}: Max Fitness = {max_fit}")


    df = pd.DataFrame(gen_data)
    df["Max"] = df["Max"] / array_size * 100
    df["Avg"] = df["Avg"] / array_size * 100
  
    

    plt.rcParams.update({
        "figure.facecolor": "#2b2d31",
        "axes.facecolor": "#2b2d31",
        "axes.edgecolor": "#cccccc",
        "axes.labelcolor": "#ffffff",
        "xtick.color": "#cccccc",
        "ytick.color": "#cccccc",
        "text.color": "#ffffff",
        "legend.edgecolor": "#2b2d31",
        "axes.titleweight": "bold"
    })


    plt.figure(figsize=(10, 6))

    plt.plot(df["Generation"], df["Max"], label="Max Fitness", linewidth=2, color="#2a66d5")
    plt.plot(df["Generation"], df["Avg"], label="Average Fitness", linestyle="--", linewidth=2, color="#b34c7e")

    plt.title("Genetic Algorithm Performance", fontsize=14)
    plt.xlabel("Generation", fontsize=12)
    plt.ylabel("Accuracy (%)", fontsize=12)
    plt.ylim(50, 100)  # adjust to zoom in nicely
    

    info_text = (
        f"Indvidual Size: {array_size}   POP_SIZE: {pop_size}   Number of Generations: {next_gen}  "
        f"\nCrossover Rate: {int(crossover_prop*100)}%  Mutation Rate: {int(mutation_rate*100) }%"
    )

    plt.annotate(
    info_text,
    xy=(0.5, -0.18),
    xycoords='axes fraction',
    ha='center',
    fontsize=10,
    fontfamily='monospace',
    fontweight='light',
    color='#bbbbbb',
    bbox=dict(facecolor='#1e1e1e', edgecolor='none', boxstyle='round,pad=0.4', alpha=0.8)
    )
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.legend()

    plt.tight_layout()
    plt.show()

    


