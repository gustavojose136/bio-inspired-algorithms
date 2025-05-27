import sys
from core.problem import KnapsackProblem
from strategies.genetic import GeneticAlgorithm

def main():
    # Example usage
    items = [(2,3), (3,4), (4,5), (5,8)]
    capacity = 10
    problem = KnapsackProblem(items, capacity)
    ga = GeneticAlgorithm(problem, pop_size=100, generations=200, mutation_rate=0.05)
    solution, value = ga.solve()
    print(f"Melhor solução: {solution}, valor: {value}")

if __name__ == '__main__':
    main()
