class Solution(object):
    def runningSum(self, nums):
        cong_don = 0
        kq = []
        for i in range(len(nums)):
            cong_don += nums[i]
            kq.append(cong_don)
        return kq
