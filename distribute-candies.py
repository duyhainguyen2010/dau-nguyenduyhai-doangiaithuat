class Solution(object):
    def distributeCandies(self, candyType):

        so_loai_keo = len(set(candyType))  
        so_keo_duoc_an = len(candyType) // 2  

        return min(so_loai_keo, so_keo_duoc_an)
