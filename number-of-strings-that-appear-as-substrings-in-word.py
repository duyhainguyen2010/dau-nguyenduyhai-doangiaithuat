class Solution(object):
    def numOfStrings(self, patterns, word):
        dem = 0
        for i in range(len(patterns)):
            if patterns[i] in word:
                dem += 1
        return dem
