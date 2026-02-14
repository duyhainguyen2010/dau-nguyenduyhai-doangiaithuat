class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        dem = 0
        max_dem = 0
        
        for so in nums:
            if so == 1:
                dem += 1
                if dem > max_dem:
                    max_dem = dem
            else:
                dem = 0
                
        return max_dem
