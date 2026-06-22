# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        
        def depth(root: Optional[TreeNode]):
            if not root:
                return 0
            
            l = depth(root.left)
            r = depth(root.right)

            if abs(l - r) > 1:
                self.ans = False

            return max(l, r) + 1
        
        depth(root)
        
        return self.ans

