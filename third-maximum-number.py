class Solution(object):
    def thirdMax(self, nums):

        danh_sach_so = sorted(set(nums), reverse=True)
        

        if len(danh_sach_so) >= 3:
            return danh_sach_so[2]
        else:
            return danh_sach_so[0]
