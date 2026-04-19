class Solution(object):
    def maximumWealth(self, accounts):
        # Biến để lưu giá trị lớn nhất tìm được
        maxx = 0
        
        # Duyệt qua từng khách hàng (mỗi khách hàng là một danh sách các ngân hàng)
        for customer in accounts:
            # Tính tổng số tiền của khách hàng hiện tại
            tong_tien_khach_hang = sum(customer)
            
            # Nếu tổng tiền này lớn hơn max_wealth thì cập nhật lại
            if tong_tien_khach_hang > maxx:
                maxx = tong_tien_khach_hang
                
        return maxx
