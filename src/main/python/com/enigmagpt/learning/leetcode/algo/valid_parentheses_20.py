class Solution:
    def isValid(self, s: str) -> bool:

        m = {'(': ')',
             '[': ']',
             '{': '}'}

        stack = []

        for symbol in s:
            if symbol in m.keys():
                stack.append(symbol)
            elif not stack or m[stack.pop()] != symbol:
                return False

        return stack == []


print(Solution.isValid(Solution, "()[]{}"))
