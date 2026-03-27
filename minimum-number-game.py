class Solution(object):
    def numberGame(self, nums):
        arr = []
        alice = nums[0]
        bob = nums[0]
        for i in range(len(nums) // 2):
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            arr.append(bob)
            arr.append(alice)

        return arr
