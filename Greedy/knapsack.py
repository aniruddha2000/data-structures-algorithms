class Knapsack:
    def __init__(self, profit, weight, knapsack_capacity):
        self.profit = profit
        self.weight = weight
        self.knapsack_capacity = knapsack_capacity
        self.current_knapsack = 0
        self.current_profit = 0
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


# profit1 = [25, 24, 15]
# weight1 = [18, 15, 10]
# knapsack_capacity1 = 20
# knapsack = Knapsack(profit1, weight1, knapsack_capacity1)
# print(knapsack.solve())
profit2 = [10, 5, 15, 7, 6, 18, 3]
weight2 = [2, 3, 5, 7, 1, 4, 1]
knapsack_capacity2 = 15
knapsack = Knapsack(profit2, weight2, knapsack_capacity2)
print(knapsack.solve())
