class Solution(object):
    def findClosestNumber(self, nums):
        kq = nums[0]
        min = abs(nums[0])

        for i in range(len(nums)):
            test = abs(nums[i])

            if test < min or (test == min and nums[i] > kq):
                min = test
                kq = nums[i]

        return kq
