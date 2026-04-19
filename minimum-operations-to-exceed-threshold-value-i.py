class Solution(object):
    def minOperations(self, nums, k):
        # Biến đếm số lần thao tác
        so_lan_thao_tac = 0
        
        # Duyệt qua từng số trong mảng
        for so in nums:
            # Nếu số đó nhỏ hơn k, ta cần xóa nó (1 thao tác)
            if so < k:
                so_lan_thao_tac += 1
                
        return so_lan_thao_tac
