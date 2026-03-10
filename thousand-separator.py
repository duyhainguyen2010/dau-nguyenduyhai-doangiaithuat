class Solution(object):
    def thousandSeparator(self, n):
        chuoi = str(n)
        ket_qua = ""
        dem = 0
        for i in range(len(chuoi) - 1, -1, -1):
            dem += 1
            ket_qua = chuoi[i] + ket_qua
            if dem % 3 == 0 and i != 0:
                ket_qua = "." + ket_qua
            
        return ket_qua
