class JobSequence:
    def __init__(self, profitDeadline):
        self.profitDeadline = profitDeadline
        self.slots = max([i[1] for i in self.profitDeadline])
        self.jobSequenceList = ["*"] * self.slots

    def solve(self):
        self.profitDeadline.sort(reverse=True)
        for profit, deadline in self.profitDeadline:
            checkTime = deadline - 1
            if "*" in self.jobSequenceList:
                while (
                    self.jobSequenceList[checkTime] != "*" and checkTime > 0
                ):
                    checkTime -= 1
                if self.jobSequenceList[checkTime] == "*":
                    self.jobSequenceList[checkTime] = profit
                else:
                    continue
            else:
                break
        return self.jobSequenceList


# testcase1 = [[50, 2], [15, 1], [10, 2], [25, 1]]
testcase2 = [[20, 2], [15, 2], [10, 1], [5, 3], [1, 3]]
# job1 = JobSequence(testcase1)
# print(job1.solve())
job2 = JobSequence(testcase2)
print(job2.solve())
