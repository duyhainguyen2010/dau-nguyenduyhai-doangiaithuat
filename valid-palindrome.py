class Solution(object):
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1

        while i < j:

            while i < j and not (('a' <= s[i] <= 'z') or ('A' <= s[i] <= 'Z') or ('0' <= s[i] <= '9')):
                i += 1

            while i < j and not (('a' <= s[j] <= 'z') or ('A' <= s[j] <= 'Z') or ('0' <= s[j] <= '9')):
                j -= 1

            a = s[i]
            b = s[j]

            if 'A' <= a <= 'Z':
                a = a.lower()

            if 'A' <= b <= 'Z':
                b = b.lower()

            if a != b:
                return False

            i += 1
            j -= 1

        return True
