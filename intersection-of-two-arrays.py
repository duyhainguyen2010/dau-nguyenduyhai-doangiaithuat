class Solution(object):
    def intersection(self, nums1, nums2):
        tap_hop_1 = set(nums1)
      
        result = set()
        
        for so in nums2:
 
            if so in tap_hop_1:
                result.add(so)
                
      
        return list(result)
