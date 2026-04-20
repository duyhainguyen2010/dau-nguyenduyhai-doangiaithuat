class Solution(object):
    def truncateSentence(self, s, k):
        # Tạo một biến đếm số từ đã tìm thấy
        dem = 0
        
        for i in range(len(s)):
            # Nếu gặp dấu cách, nghĩa là hết 1 từ
            if s[i] == " ":
                dem += 1
            
            # Nếu đã đếm đủ k từ, thì lấy toàn bộ chuỗi từ đầu đến chỗ này
            if dem == k:
                return s[:i]
        
        return s
