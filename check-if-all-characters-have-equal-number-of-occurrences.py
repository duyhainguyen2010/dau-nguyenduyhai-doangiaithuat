class Solution(object):
    def areOccurrencesEqual(self, s):

        dem = {}

        for i in s:
            if i in dem:
                dem[i] += 1
            else:
                dem[i] = 1

        lan = list(dem.values())

        for i in lan:
            if i != lan[0]:
                return False

        return True
