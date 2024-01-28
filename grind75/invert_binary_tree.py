from typing import Optional

class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current:
                current.left, current.right = current.right, current.left
                queue.append(current.left)
                queue.append(current.right)
        return root


solution_instance = Solution()
# Driver code
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

result = solution_instance.invertTree(root)
print(result)
