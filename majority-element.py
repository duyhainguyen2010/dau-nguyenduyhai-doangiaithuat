class Solution(object):
    def majorityElement(self, nums):
        kq = 0
        dem = 0
        
        for so in nums:
            if dem == 0:
                kq = so
            
            if so == kq:
                dem += 1
            else:
                dem -= 1
                
        return kq
