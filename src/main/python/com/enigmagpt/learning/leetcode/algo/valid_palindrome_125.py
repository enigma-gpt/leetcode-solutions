import re


class Solution:

    def isPalindrome(self, s: str) -> bool:

        if len(s) < 2:
            return True

        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        reversed = s[::-1]

        print(s)

        return reversed == s


print(Solution.isPalindrome(Solution, "_aSd-d#sA@!"))

print(Solution.isPalindrome(Solution, "@"))

print(Solution.isPalindrome(Solution, ""))
