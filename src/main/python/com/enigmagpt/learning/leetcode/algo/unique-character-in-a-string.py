class Solution:
    def firstUniqChar(self, s: str) -> int:

        if len(s) < 2:
            return 0

        m = {}
        i = 0
        for e in s:
            if e not in m:
                m[e] = -1
            else:
                m[e] = i

        i += 1

        i = 0
        for ch in s:
            if ch not in m or m[ch] == -1:
                return i
            i += 1

        return -1


print(Solution.firstUniqChar(Solution, "leetcode"))

print(Solution.firstUniqChar(Solution, "loveleetcode"))
