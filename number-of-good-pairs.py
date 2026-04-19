class Solution(object):
    def numIdenticalPairs(self, nums):
   
        so_cap_tot = 0
        

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
    
                if nums[i] == nums[j]:
                    so_cap_tot += 1
        
        return so_cap_tot
