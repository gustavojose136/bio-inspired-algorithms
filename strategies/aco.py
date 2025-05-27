from core.fitness import evaluate_solution
from strategies.base import MetaHeuristic

class ACO(MetaHeuristic):
    def initialize(self):
        raise NotImplementedError("ACO not yet implemented")

    def evaluate(self, individual):
        raise NotImplementedError("ACO not yet implemented")

    def update(self, population, fitnesses):
        raise NotImplementedError("ACO not yet implemented")
