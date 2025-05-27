import pytest
from core.problem import KnapsackProblem
from strategies.genetic import GeneticAlgorithm

@pytest.fixture
def problema_pequeno():
    itens = [(2,3), (3,4), (4,5)]
    capacidade = 5
    return KnapsackProblem(itens, capacidade)

def test_genetic_retorna_solucao_valida(problema_pequeno):
    ga = GeneticAlgorithm(problema_pequeno, pop_size=20, generations=50, mutation_rate=0.1)
    solucao, valor = ga.solve()
    peso_total = sum(problema_pequeno.items[i][0] for i in solucao)
    assert peso_total <= problema_pequeno.capacity
