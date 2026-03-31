class Solution(object):
    def guessNumber(self, n):

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 1:
                left = mid + 1
