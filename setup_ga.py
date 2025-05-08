from deap import base, creator, tools
from evaluate import eval_onemax
import random
import yaml

def load_config():
    with open('config.yml', 'r') as f:
        return yaml.safe_load(f)
    
config = load_config()
# Define the fitness function type — here we're maximizing a single objective.
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# Define the individual class — it's a list with an attached fitness attribute of type FitnessMax.
creator.create("Individual", list, fitness=creator.FitnessMax)

# Initialize the DEAP toolbox to hold evolutionary operators and constructors.
toolbox = base.Toolbox()

# Register a gene generator — returns a random 0 or 1 (i.e., binary gene).
toolbox.register("attr_bool", random.randint, 0, 1)

# Register how to initialize an individual:
# Use attr_bool repeatedly to fill a list of length IND_SIZE, wrapped as an Individual.
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, config['IND_SIZE'])

# Register how to initialize a population:
# A population is simply a list of individuals.
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", eval_onemax)

#pick 3 individuals at random → keep the one with the best fitness.
toolbox.register("select", tools.selTournament, tournsize = 3)

#swaps slices of their gene lists

toolbox.register("mate", tools.cxTwoPoint)

toolbox.register("mutate", tools.mutFlipBit, indpb=.01)