class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        dem = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                truoc = (i == 0 or flowerbed[i - 1] == 0)
                sau = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

                if sau and truoc:
                    flowerbed[i] = 1
                    dem += 1

        return dem >= n
        
