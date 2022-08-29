class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        a = dict()

        for i in range(0, len(nums)):
            num = nums[i]
            if num < target:
                a[num] = i

        for i in range(0, len(nums)):
            num = nums[i]
            if target - num in a:
                return [i, a[target - num]]

        return [0, 0]


print(Solution.twoSum(Solution, [2,7,11,15], 9))