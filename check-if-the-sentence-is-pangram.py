class Solution(object):
    def checkIfPangram(self, sentence):
        # 1. Chuyển chuỗi thành một tập hợp (set) để loại bỏ các chữ cái trùng lặp
        cac_chu_cai = set(sentence)
        
        # 2. Kiểm tra xem số lượng phần tử trong tập hợp có bằng 26 không
        if len(cac_chu_cai) == 26:
            return True
        else:
            return False
