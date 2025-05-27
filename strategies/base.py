from abc import ABC, abstractmethod

class MetaHeuristic(ABC):
    def __init__(self, problem, **kwargs):
        self.problem = problem
        self.params = kwargs

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def evaluate(self, population):
        pass

    @abstractmethod
    def update(self, population, fitnesses):
        pass

    def solve(self):
        population = self.initialize()
        for _ in range(self.params.get('generations', 100)):
            fitnesses = [self.evaluate(ind) for ind in population]
            population = self.update(population, fitnesses)
        # Return best solution
        best_idx = max(range(len(population)), key=lambda i: fitnesses[i])
        return population[best_idx], fitnesses[best_idx]
