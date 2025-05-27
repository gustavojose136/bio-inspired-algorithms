import random
from core.fitness import evaluate_solution
from strategies.base import MetaHeuristic

class GeneticAlgorithm(MetaHeuristic):
    def initialize(self):
        pop_size = self.params.get('pop_size', 50)
        num_items = len(self.problem.items)
        return [[random.randint(0, 1) for _ in range(num_items)] for _ in range(pop_size)]

    def evaluate(self, individual):
        # Individual is binary list; indices with 1 are selected
        solution = [i for i, bit in enumerate(individual) if bit]
        return evaluate_solution(self.problem, solution)

    def update(self, population, fitnesses):
        pop_size = len(population)
        # Tournament selection
        def select():
            i, j = random.sample(range(pop_size), 2)
            return population[i] if fitnesses[i] > fitnesses[j] else population[j]
        # Crossover and mutation
        new_pop = []
        for _ in range(pop_size // 2):
            p1, p2 = select(), select()
            point = random.randint(1, len(p1)-1)
            c1 = p1[:point] + p2[point:]
            c2 = p2[:point] + p1[point:]
            # Mutation
            for c in (c1, c2):
                if random.random() < self.params.get('mutation_rate', 0.01):
                    idx = random.randrange(len(c))
                    c[idx] = 1 - c[idx]
                new_pop.append(c)
        return new_pop
