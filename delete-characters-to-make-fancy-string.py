class Solution(object):
    def makeFancyString(self, s):
    
        ket_qua = []
        
        for ky_tu in s:
            if len(ket_qua) >= 2 and ket_qua[-1] == ky_tu and ket_qua[-2] == ky_tu:
                continue
            ket_qua.append(ky_tu)
            
        # Nối danh sách lại thành chuỗi hoàn chỉnh
        return "".join(ket_qua)
