class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
 
        so_nhan_vien_dat = 0
        

        for gio_lam_moi_nhan_vien in hours:

            if gio_lam_moi_nhan_vien >= target:
                so_nhan_vien_dat += 1
                
        return so_nhan_vien_dat
