class Solution(object):
    def firstUniqChar(self, s):
        count = {}

        # Bước 1: đếm
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        # Bước 2: tìm ký tự đầu tiên có count = 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
