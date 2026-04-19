class Solution(object):
    def sortedSquares(self, nums):
        
        ket_qua = []
        

        for so in nums:
            binh_phuong = so * so
            ket_qua.append(binh_phuong)
        
  
        ket_qua.sort()
        
        return ket_qua
