from core.fitness import evaluate_solution
from strategies.base import MetaHeuristic

class Cuckoo(MetaHeuristic):
    def initialize(self):
        raise NotImplementedError("Cuckoo not yet implemented")

    def evaluate(self, individual):
        raise NotImplementedError("Cuckoo not yet implemented")

    def update(self, population, fitnesses):
        raise NotImplementedError("Cuckoo not yet implemented")
