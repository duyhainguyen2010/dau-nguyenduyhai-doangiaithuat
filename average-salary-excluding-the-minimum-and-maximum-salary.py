class Solution(object):
    def average(self, salary):
        # 1. Tìm giá trị nhỏ nhất và lớn nhất
        nho_nhat = min(salary)
        lon_nhat = max(salary)
        
        # 2. Tổng tất cả, trừ đi 1 lần giá trị nhỏ nhất và 1 lần giá trị lớn nhất
        tong = sum(salary) - nho_nhat - lon_nhat
        
        # 3. Số lượng phần tử còn lại là tổng số trừ đi 2
        so_luong = len(salary) - 2
        
        # 4. Trả về kết quả
        return float(tong) / so_luong
