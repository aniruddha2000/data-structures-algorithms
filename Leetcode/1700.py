# Number of Students Unable to Eat Lunch
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while any(item in students for item in sandwiches):
            print(students, sandwiches)
            for sandwich in sandwiches:
                if students[0] != sandwich:
                    tmp = students.pop(0)
                    students.append(tmp)
                else:
                    students.pop(0)
                    sandwiches.pop(0)
        return len(students)


sol = Solution()
students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(sol.countStudents(students, sandwiches))
