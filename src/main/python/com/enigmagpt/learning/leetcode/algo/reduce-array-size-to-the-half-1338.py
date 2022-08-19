from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:

        arr.sort()
        sums = []
        prev_elem = 0
        for elem in arr:
            if len(sums) > 0 and elem == prev_elem:
                sums[-1] = sums[-1] + 1
            else:
                sums.append(1)
            prev_elem = elem

        sums.sort(reverse=True)

        print(sums)

        for i in range(0, len(sums)):
            summ=0
            for ii in range(0, i+1):
                print("i= ", i)
                summ += sums[ii]
                if summ >= int(len(arr)/2):
                    return i+1
            print("summ= ", summ)

        return -1

    def minSetSizeTheBest(self, arr: list[int]) -> int:
        cnt = Counter(arr)
        frequencies = list(cnt.values())
        frequencies.sort()

        ans, removed, half = 0, 0, len(arr) // 2
        while removed < half:
            ans += 1
            removed += frequencies.pop()
        return ans


#print(Solution.minSetSize(Solution, [3,3,3,3,5,5,5,2,2,7]))

#print(Solution.minSetSize(Solution, [1, 9]))

print(Solution.minSetSize(Solution, [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))



