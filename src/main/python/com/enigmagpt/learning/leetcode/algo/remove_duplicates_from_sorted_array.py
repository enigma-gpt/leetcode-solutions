from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        y = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[y] = nums[i+1]
                y += 1
        print(nums)
        return y


print(Solution.removeDuplicates(Solution, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))