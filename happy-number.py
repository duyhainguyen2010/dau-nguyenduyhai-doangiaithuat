class Solution(object):
    def isHappy(self, n):
        # Đây là cuốn sổ tay để ghi lại những số đã qua
        result = set()
        
        # Chừng nào chưa tới số 1 và số đó chưa từng xuất hiện
        while n != 1 and n not in result:
            # Ghi số hiện tại vào sổ tay
            result.add(n)
            
            # Tính tổng bình phương các chữ số
            tong = 0
            while n > 0:
                chu_so = n % 10          # Lấy số cuối (ví dụ 19 -> lấy 9)
                tong += chu_so * chu_so  # Bình phương rồi cộng vào tổng
                n = n // 10              # Bỏ số cuối (ví dụ 19 -> còn 1)
            
            # Gán tổng vừa tính được cho n để nhảy sang bước tiếp theo
            n = tong
            
        # Nếu n bằng 1 thì là Happy, còn không thì ngược lại
        return n == 1
