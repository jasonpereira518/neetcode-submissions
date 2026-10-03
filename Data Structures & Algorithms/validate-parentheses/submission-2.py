class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack = []

        for string in s:
            if string in par:
                if stack and stack[-1] == par[string]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(string)
        if stack:
            return False
        return True