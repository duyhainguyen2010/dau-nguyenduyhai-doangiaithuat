class Solution(object):
    def countSegments(self, s):

        dem = 0

        for i in range(len(s)):

            if s[i] != ' ':

                if i == 0 or s[i - 1] == ' ':
                    dem += 1

        return dem
