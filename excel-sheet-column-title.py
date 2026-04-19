class Solution(object):
    def convertToTitle(self, n):
        bang = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ket_qua = ""

        while n > 0:
            n -= 1  

            phan_du = n % 26
            ky_tu = bang[phan_du]   

            ket_qua = ky_tu + ket_qua

            n = n // 26

        return ket_qua
