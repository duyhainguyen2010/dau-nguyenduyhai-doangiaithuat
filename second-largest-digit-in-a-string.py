class Solution(object):
    def secondHighest(self, s):
        so = set()
        for i in s:
            if i.isdigit():
                so.add(int(i))
        if len(so) < 2:
            return -1
        so = sorted(so)
        
        return so[-2]
