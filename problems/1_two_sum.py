class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            print(lookup)
            if target - num in lookup:
                return [lookup[target-num], i]
            else:
                lookup[num] = i


nums = [2, 7, 11, 15]
target = 13
p1 = Solution()
print(p1.twoSum(nums, target))
