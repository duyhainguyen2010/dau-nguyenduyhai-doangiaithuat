class Solution(object):
    def sumOfUnique(self, nums):
        tong = 0

        for i in nums:
            if nums.count(i) == 1: # ham count dem so lan i xuat hien trong 1 list
                tong += i

        return tong
