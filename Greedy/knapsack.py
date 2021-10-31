class Knapsack:
    def __init__(self):
        self.knapsack_capacity = 20
        self.current_knapsack = 0
        self.current_profit = 0
        self.profit = [25, 24, 15]
        self.weight = [18, 15, 10]
        self.profit_per_weight = []

    def solve(self):
        for i, (p, w) in enumerate(zip(self.profit, self.weight)):
            self.profit_per_weight.append([(p / w), i])

        self.profit_per_weight.sort(reverse=True)

        for wi, i in self.profit_per_weight:
            if self.remain_knapsack_capacity() > 0 and (
                self.weight[i] <= self.remain_knapsack_capacity()
            ):
                self.current_profit += self.profit[i]
                self.current_knapsack += self.weight[i]
            elif self.remain_knapsack_capacity() > 0:
                self.current_profit += (
                    self.remain_knapsack_capacity() / self.weight[i]
                ) * self.profit[i]
                self.current_knapsack += (
                    self.weight[i] - self.remain_knapsack_capacity()
                )
            else:
                break

        return self.current_profit

    def remain_knapsack_capacity(self):
        return self.knapsack_capacity - self.current_knapsack


knapsack = Knapsack()
print(knapsack.solve())
