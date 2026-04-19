class Solution(object):
    def singleNumber(self, nums):
        result = set()
        for so in nums:
            if so in result:
                result.remove(so)
            else:
                result.add(so)
        return result.pop()
