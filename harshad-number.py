class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        x = x
        
        so_ban_dau = str(x)
        
        tong = 0
        
        for i in range(len(so_ban_dau)):
            tong += int(so_ban_dau[i])
        
        if x % tong == 0:
            return tong
        
        return -1
