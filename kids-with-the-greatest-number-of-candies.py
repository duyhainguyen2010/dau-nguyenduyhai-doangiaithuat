class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        # Tìm số kẹo lớn nhất hiện có trong danh sách
        max_candies = max(candies)
        
  
        result = []
        

        for so_keo_cua_be in candies:
            if so_keo_cua_be + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result
