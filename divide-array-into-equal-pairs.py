class Solution(object):
    def divideArray(self, nums):
        count = {}
        if len(nums) % 2 != 0:
            return False
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        for j in count.values():
            if j % 2 != 0:
                return False
        return True
