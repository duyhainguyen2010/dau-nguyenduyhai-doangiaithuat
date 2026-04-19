class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        # Biến đếm tổng số lần đã giảm hiệu năng
        da_giam = 0
        # Biến đếm số thiết bị được kiểm thử thành công
        so_thiet_bi_dat = 0
        
        for pin in batteryPercentages:
            # Kiểm tra hiệu năng thực tế của thiết bị
            if pin - da_giam > 0:
                # Nếu còn hiệu năng, thiết bị được kiểm thử
                so_thiet_bi_dat += 1
                # Các thiết bị sau đó sẽ bị giảm thêm 1 đơn vị
                da_giam += 1
                
        return so_thiet_bi_dat
