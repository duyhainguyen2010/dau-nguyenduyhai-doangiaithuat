class Solution(object):
    def prefixCount(self, words, pref):
        dem = 0
        for i in range(len(words)):
            if words[i].startswith(pref):
                dem += 1
                
        return dem
