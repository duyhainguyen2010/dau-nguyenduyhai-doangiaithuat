class Solution(object):
    def minDepth(self, root):

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return self.minDepth(root.right) + 1

        if root.right is None:
            return self.minDepth(root.left) + 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left < right:
            return left + 1
        else:
            return right + 1
