from core.problem import KnapsackProblem

def evaluate_solution(problem: KnapsackProblem, solution):
    # Sum values and apply penalty if overweight
    total_weight = sum(problem.items[i][0] for i in solution)
    total_value = sum(problem.items[i][1] for i in solution)
    if total_weight > problem.capacity:
        total_value -= penalty(problem, total_weight)
    return total_value

def penalty(problem: KnapsackProblem, total_weight):
    # Linear penalty: excess weight * average item value
    excess = total_weight - problem.capacity
    avg_value = sum(v for _, v in problem.items) / len(problem.items)
    return excess * avg_value
