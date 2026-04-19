class Solution(object):
    def maxProduct(self, nums):
        # 1. Sắp xếp mảng theo thứ tự tăng dần
        nums.sort()
        
        # 2. Hai số lớn nhất sẽ nằm ở cuối mảng (chỉ số n-1 và n-2)
        so_lon_1 = nums[-1]
        so_lon_2 = nums[-2]
        
        # 3. Trả về tích sau khi đã trừ 1 theo yêu cầu đề bài
        return (so_lon_1 - 1) * (so_lon_2 - 1)
