# his challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.

# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.

# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s. Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and tell us your conclusion :).
import random   
class Gene:
    def __init__(self, value):
        self.value = value

    def mutate(self):
        self.value = 1 - self.value  # Flip the gene (0 to 1 or 1 to 0) 

class Chromosome:
    def __init__(self, genes):
        self.genes = genes

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:  # 50% chance to mutate each gene
                gene.mutate()                                   
class DNA:
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:  # 50% chance to mutate each chromosome
                chromosome.mutate()     
class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment

    def mutate(self):
        if random.random() < self.environment:  # Probability to mutate based on the environment
            self.dna.mutate()       
def is_perfect_dna(dna):
    for chromosome in dna.chromosomes:
        for gene in chromosome.genes:
            if gene.value == 0:
                return False
    return True
def simulate_evolution(environment):
    # Create an initial random DNA
    chromosomes = [Chromosome([Gene(random.randint(0, 1)) for _ in range(10)]) for _ in range(10)]
    dna = DNA(chromosomes)
    organism = Organism(dna, environment)

    generations = 0
    while not is_perfect_dna(organism.dna):
        organism.mutate()
        generations += 1

    return generations                                          
# Simulate the evolution with a given environment mutation probability
environment_mutation_probability = 0.1  # Example: 10% chance to mutate     
generations_needed = simulate_evolution(environment_mutation_probability)
print(f"Number of generations needed to reach perfect DNA: {generations_needed}")   
        

