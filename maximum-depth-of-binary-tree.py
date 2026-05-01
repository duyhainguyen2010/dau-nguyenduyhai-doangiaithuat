class Solution(object):
    def maxDepth(self, root):
        
        def dfs(node):
            if node is None:
                return 0
            
            # Tính độ sâu bên trái
            depth_left = dfs(node.left)
            
            # Tính độ sâu bên phải
            depth_right = dfs(node.right)
            
            # Lấy bên sâu hơn + 1 (node hiện tại)
            depth_current = max(depth_left, depth_right) + 1
            
            return depth_current
        
        return dfs(root)
