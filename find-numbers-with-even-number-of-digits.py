class Solution(object):
    def findNumbers(self, nums):
        kq = 0
        for i in nums:
            dem = 0
            while(i > 0):
                i = i // 10
                dem += 1
                
            if dem % 2 == 0:
                kq += 1
        return kq

        
