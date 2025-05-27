# Plano de Refatoração

## 1. O que será refatorado
- Extrair a função de fitness e penalização repetidas em cada estratégia para um módulo único (`core/fitness.py`).
- Criar classe abstrata base `MetaHeuristic` em `strategies/base.py`, que encapsula o fluxo genérico de inicialização, avaliação e atualização.
- Separar claramente a modelagem do problema (itens, capacidade) das implementações dos algoritmos.
- Padronizar nomenclaturas usando `snake_case` em todo o código.

## 2. Por que será refatorado
- **Eliminar duplicação**: evita código repetido e facilita manutenções futuras.
- **Reduzir acoplamento**: desacopla lógica de problema de lógica de algoritmos.
- **Aumentar coesão**: cada módulo terá responsabilidade única e bem definida.
- **Facilitar testes**: com estruturas claras, testes automatizados podem ser escritos de forma isolada.

## 3. Técnicas de Refatoração
| Refatoração          | Descrição                                              | Fonte               |
|----------------------|--------------------------------------------------------|---------------------|
| Extract Method       | Extrair lógica de avaliação de solução em método único. | Fowler, cap. 3      |
| Form Template Method | Definir esqueleto de algoritmo em classe base abstrata. | Refactoring Guru    |
| Rename Variable      | Padronizar nomes de variáveis e funções para `snake_case`.| Refactoring Catalog |

## 4. Plano de Ação
1. **Extrair** funções `avaliar_solucao()` e `aplicar_penalizacao()` de cada estratégia para `core/fitness.py`.
2. **Criar** `class MetaHeuristic(ABC)` em `strategies/base.py` com métodos abstratos `initialize()`, `evaluate()`, `update()` e `solve()`.
3. **Refatorar** cada algoritmo (GA, PSO, ACO, Cuckoo) para **herdar** de `MetaHeuristic` e implementar apenas os passos específicos.
4. **Padronizar** nomenclaturas e estilo executando:
   ```bash
   flake8 --max-line-length=88 --select=E,F,W
   pylint strategies/ core/
   ```
5. **Adicionar** testes automatizados em `tests/`, cobrindo casos típicos e extremos:
   - Soluções válidas (sem violar capacidade)
   - Cenários sem itens e capacidade zero
   - Comparação de valores esperados
6. **Gerar** relatório de qualidade antes e depois usando SonarQube e `pytest --cov`.
