class Solution(object):
    def checkRecord(self, s):

        demA = 0

        for i in range(len(s)):

            if s[i] == "A":
                demA += 1

        if demA < 2 and "LLL" not in s:
            return True
        else:
            return False
