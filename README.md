# OneMax with DEAP

This is a small project I made to learn how to use the DEAP library for genetic algorithms. It solves the OneMax problem, which is just trying to evolve a binary list (0s and 1s) into all 1s.

## How it works

Each individual in the population is a list of 0s and 1s. The fitness function just adds up how many 1s are in the list. Over generations, the algorithm selects better individuals, crosses them over, and mutates them until it hopefully gets a perfect one (all 1s).

## Sample Output

Here’s what it looks like after running with IND_SIZE = 500:

Gen 0: Max Fitness = 295.0
Gen 1: Max Fitness = 306.0
Gen 2: Max Fitness = 305.0
...
Gen 72: Max Fitness = 499.0
Gen 73: Max Fitness = 500.0
Gen 74: Max Fitness = 500.0
...
Gen 99: Max Fitness = 500.0
Best individual: [1, 1, 1, ..., 1]
Fitness: 500.0

## Files

- `main.py` – entry point that runs everything
- `config.py` – holds parameters like population size, mutation rate, etc.
- `setup_ga.py` – sets up the DEAP toolbox and individual creation
- `evaluate.py` – defines the fitness function
- `evolution.py` – runs the genetic algorithm loop
- `requirements.txt` – just DEAP for now

## Running it

I used a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

pip install -r requirements.txt
python main.py
