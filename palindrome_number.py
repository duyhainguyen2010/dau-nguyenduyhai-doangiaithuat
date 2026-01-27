class Solution(object):
    def isPalindrome(self, x):
        chuoi = str(x)
        chuoi_nguoc = chuoi[::-1]
        return chuoi == chuoi_nguoc
        
