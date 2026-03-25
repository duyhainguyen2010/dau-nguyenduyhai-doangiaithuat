class Solution(object):
    def mostFrequent(self, nums, key):
        dem = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                dem[nums[i + 1]] = dem.get(nums[i + 1], 0) + 1
        return max(dem, key=dem.get)
