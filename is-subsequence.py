class Solution(object):
    def isSubsequence(self, s, t):
        y = 0
        for i in range(len(t)):
            if y < len(s) and s[y] == t[i]:
                y += 1
        return y == len(s)
