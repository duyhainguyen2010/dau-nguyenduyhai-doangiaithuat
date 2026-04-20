class Solution(object):
    def countPairs(self, nums, target):
        dem = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    dem += 1
        return dem
