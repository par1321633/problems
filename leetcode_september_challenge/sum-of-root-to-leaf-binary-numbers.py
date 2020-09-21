
"""
You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


"""

#!/usr/bin/env python
# -*- coding: utf-8
__author__ = "Parkash Sharma"



# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        val = 0
        return self.PreorderTraverseSum(root, val)

    def PreorderTraverseSum(self, root, val=None):
        if root is None:
            return 0
        print(root.val)
        if val is None:
            val = '{}'.format(root.val)
        else:
            val = "{}{}".format(val, root.val)
        if root.left is None and root.right is None:
            return int(val, 2)
        return self.PreorderTraverseSum(root.left, val) + self.PreorderTraverseSum(root.right, val)


if __name__ == '__main__':
    print ("Running Sum to Leaf Binary Number")
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    print (Solution().sumRootToLeaf(root))