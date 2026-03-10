class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr = []
        for i in range(len(nums)):
            dem = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    dem += 1
            arr.append(dem)
        return arr
