def evalRPN(tokens: list) -> int:
    operator = ["+", "-", "*", "/"]
    stack = []
    result = 0
    for item in tokens:
        if item not in operator:
            stack.append(item)
        else:
            second = int(stack.pop())
            first = int(stack.pop())

            if item == "+":
                result = first + second
            if item == "-":
                result = first - second
            if item == "*":
                result = first * second
            if item == "/":
                result = int(first / second)
            stack.append(result)
    return result


testCase1 = ["2", "1", "+", "3", "*"]
print(evalRPN(testCase1))
testCase2 = ["4", "13", "5", "/", "+"]
print(evalRPN(testCase2))
testCase3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(testCase3))
testCase4 = ["0", "3", "/"]
print(evalRPN(testCase4))
