# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode):
        vals = self._get_ordered_list(root)
        return vals

    def _get_ordered_list(self, node):
        if not node.left and not node.right:
            return [node.val]

        if node.left:
            vals = self._get_ordered_list(node.left)
            vals.append(node.val)
            return vals

        if node.right:
            vals = self._get_ordered_list(node.right)
            vals = [node.val] + vals
            return vals