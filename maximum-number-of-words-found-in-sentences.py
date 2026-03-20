class Solution(object):
    def mostWordsFound(self, sentences):
        max_ = 0
        for i in sentences:
            doan_van = i.split()
            dem = len(doan_van)
            if max_ < dem:
                max_ = dem
        return max_
