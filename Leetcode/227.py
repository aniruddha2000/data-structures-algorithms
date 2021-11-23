def solve(s):
    stack, cur, op = [], 0, "+"
    for c in s + "+":
        if c == " ":
            continue
        elif c.isdigit():
            cur = (cur * 10) + int(c)
        else:
            if op == "+":
                stack.append(cur)
            elif op == "-":
                stack.append(-cur)
            elif op == "*":
                stack.append(stack.pop() * cur)
            elif op == "/":
                stack.append(int(stack.pop() / cur))
            cur, op = 0, c
    return sum(stack)


testCase1 = "3+2*2"
testCase2 = " 3/2 "
testCase3 = " 3+5 / 2 "
testCase4 = "10 + 5 - 2"
testCaseses = [testCase1, testCase2, testCase3, testCase4]
for testCase in testCaseses:
    print(testCase + " = " + str(solve(testCase)))
