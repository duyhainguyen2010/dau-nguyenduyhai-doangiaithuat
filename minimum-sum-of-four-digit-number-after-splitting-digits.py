class Solution(object):
    def minimumSum(self, num):
        chu_so = sorted(str(num))
        return int(chu_so[0] + chu_so[2]) + int(chu_so[1] + chu_so[3])
