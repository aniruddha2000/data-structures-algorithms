class Solution:
    def simplifyPath(self, path: str):
        stack = []
        _list = path.split("/")
        print(_list)
        for i in _list:
            if i == ".." and stack:
                stack.pop()
            elif i != ".." and i != "." and i:
                stack.append(i)
        return "/" + "/".join(stack)


sol = Solution()
print(sol.simplifyPath("/a/./b/../../c/"))
