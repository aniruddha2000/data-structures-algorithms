def isValidSerialization(preorder: str) -> bool:
    stack = []
    preorder = preorder.split(",")
    for i in range(len(preorder)):
        stack.append(preorder[i])
        while (
            len(stack) >= 3
            and stack[len(stack) - 1] == "#"
            and stack[len(stack) - 2] == "#"
            and stack[len(stack) - 3] != "#"
        ):
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append("#")

    if len(stack) == 1 and stack[0] == "#":
        return "True"
    else:
        return "False"


testCase1 = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(isValidSerialization(testCase1))
testCase2 = "1,#"
print(isValidSerialization(testCase2))
testCase3 = "9,#,#,1"
print(isValidSerialization(testCase3))
testCase4 = "1,#,#"
print(isValidSerialization(testCase4))
