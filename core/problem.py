class KnapsackProblem:
    def __init__(self, items, capacity):
        self.items = items  # List of tuples (weight, value)
        self.capacity = capacity

    def is_valid(self, solution):
        total_weight = sum(self.items[i][0] for i in solution)
        return total_weight <= self.capacity
