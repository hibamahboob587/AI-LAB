import random

# Objective function
def fitness_function(x):
    return x**3

# Generate an initial population
def generate_population(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# Selection: Choose two parents based on fitness
def select_parents(population):
    fitness_scores = [fitness_function(ind) for ind in population]
    total_fitness = sum(fitness_scores)
    probabilities = [f / total_fitness for f in fitness_scores]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents

# Crossover: Combine two parents to produce offspring
def crossover(parent1, parent2):
    return (parent1 + parent2) // 2

# Mutation: Apply a small random change
def mutate(individual, mutation_rate, lower_bound, upper_bound):
    if random.random() < mutation_rate:
        individual += random.randint(-1, 1)
        individual = max(min(individual, upper_bound), lower_bound)
    return individual

# Genetic algorithm
def genetic_algorithm(pop_size, generations, mutation_rate, lower_bound, upper_bound):
    # Generate initial population
    population = generate_population(pop_size, lower_bound, upper_bound)
    
    for generation in range(generations):
        # Create a new population
        new_population = []
        
        while len(new_population) < pop_size:
            # Select parents
            parent1, parent2 = select_parents(population)
            
            # Perform crossover
            child = crossover(parent1, parent2)
            
            # Perform mutation
            child = mutate(child, mutation_rate, lower_bound, upper_bound)
            
            # Add child to the new population
            new_population.append(child)
        
        # Update population
        population = new_population
        
        # Print the best solution in the current generation
        best_solution = max(population, key=fitness_function)
        print(f"Generation {generation + 1}: Best Solution = {best_solution}, Fitness = {fitness_function(best_solution)}")
    
    # Return the best solution
    return max(population, key=fitness_function)

# Parameters
POP_SIZE = 20
GENERATIONS = 10
MUTATION_RATE = 0.1
LOWER_BOUND = -10
UPPER_BOUND = 10

# Run the genetic algorithm
best_solution = genetic_algorithm(POP_SIZE, GENERATIONS, MUTATION_RATE, LOWER_BOUND, UPPER_BOUND)
print(f"Best solution found: x = {best_solution}, f(x) = {fitness_function(best_solution)}")
