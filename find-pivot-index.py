class Solution(object):
    def pivotIndex(self, nums):
        tong = sum(nums)
        truoc = 0
        for i in range(len(nums)):
            sau = tong - truoc - nums[i]
            if truoc == sau:
                return i
            truoc += nums[i]
        return -1
