class Solution(object):
    def isThree(self, n):
        dem = 0
        for i in range(1, n+1):
            if n % i == 0:
                dem += 1
            if dem >= 4:
                return False
        if dem == 3:
            return True
        else:
            return False
