class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dem = {}

        for ch in magazine:
            if ch in dem:
                dem[ch] += 1
            else:
                dem[ch] = 1

        for ch in ransomNote:
            if ch not in dem or dem[ch] == 0:
                return False
            dem[ch] -= 1

        return True
