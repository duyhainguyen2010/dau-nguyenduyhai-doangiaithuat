class Solution(object):
    def searchInsert(self, nums, target):
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            # nếu tìm thấy
            if nums[mid] == target:
                return mid
            
            # nếu target nhỏ hơn
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # nếu không tìm thấy
        return left
