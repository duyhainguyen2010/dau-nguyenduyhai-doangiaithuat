class Solution(object):
    def maxDistance(self, colors):
        lon_nhat = 0
        for i in range(len(colors)):
            for j in range(len(colors) - 1, -1, -1):
                if colors[i] != colors[j]:
                    tam = j - i
                    if lon_nhat < tam:
                        lon_nhat = tam
        return lon_nhat
