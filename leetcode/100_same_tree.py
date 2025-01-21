"""100. Same Tree"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Solution Class"""
    def isSameTree(self, p, q) -> bool:

        """
        This solution recursively, depth first searches each tree and compares the nodes to verify that they meet the requirements to be the same tree. If there is no Node or the node being looked at for each corresponding tree value does not match then false is returned.
        In the worst case the time complexity is O(n) where it is the max number of nodes in the tree when they are the same.

        """
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False

        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)