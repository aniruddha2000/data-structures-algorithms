def removeDuplicateLetters(s: str) -> str:
    freqMap = {}
    stack = []
    visited = set()
    for c in s:
        if c not in freqMap:
            freqMap[c] = 1
        else:
            freqMap[c] += 1
    for c in s:
        if c not in visited:
            while stack and stack[-1] > c and freqMap[stack[-1]]:
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        freqMap[c] -= 1
    return "".join(stack)


testcase1 = "cbacdcbc"
print(removeDuplicateLetters(testcase1))
