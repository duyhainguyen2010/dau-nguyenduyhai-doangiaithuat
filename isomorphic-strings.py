class Solution(object):
    def isIsomorphic(self, s, t):
        # Tạo 2 sổ tay để ghi chép sự tương ứng
        map_s_to_t = {}
        map_t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            # Kiểm tra xem char_s đã được ánh xạ chưa
            if char_s not in map_s_to_t:
                # Nếu chưa, kiểm tra xem char_t đã bị "chiếm dụng" bởi ký tự khác chưa
                if char_t in map_t_to_s:
                    return False
                # Ánh xạ cả 2 chiều
                map_s_to_t[char_s] = char_t
                map_t_to_s[char_t] = char_s
            else:
                # Nếu đã ánh xạ, kiểm tra xem có khớp với cái cũ không
                if map_s_to_t[char_s] != char_t:
                    return False
                    
        return True
