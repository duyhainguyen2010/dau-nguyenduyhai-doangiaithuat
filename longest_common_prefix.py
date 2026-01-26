class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]   # lấy chuỗi đầu tiên
        
        for i in range(len(prefix)):
            for s in strs:
                if i >= len(s) or s[i] != prefix[i]:
                    return prefix[:i]
        
        return prefix
