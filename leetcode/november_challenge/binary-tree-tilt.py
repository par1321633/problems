"""
https://leetcode.com/problems/binary-tree-tilt/

Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

Input: root = [1,2,3]
Output: 1
Explanation:
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tile of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
Sum of every tilt : 0 + 0 + 1 = 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        out = []
        self.process_root(root, 0, 0, out)
        return sum(out)

    def process_root(self, root, left, right, out):
        if root is None:
            # print ("ROOT NONE")
            return 0
        if root.left is None and root.right is None:
            return root.val
        l, r = self.process_root(root.left, left, right, out), self.process_root(root.right, left, right, out)
        left = left + l
        right = right + r
        print(root.val)
        print(l, r, abs(left - right))
        out.append(abs(left - right))
        return left + right + root.val

    def traverse_tree(self, root: TreeNode):
        if root is not None:
            print(root.val, end='->')
            self.traverse_tree(root.left)
            self.traverse_tree(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print ("Case 1")
    Solution().traverse_tree(root)
    sol = Solution().findTilt(root)
    print("Solution : {}".format(sol))

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(9)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    print ("Case 2")
    Solution().traverse_tree(root)
    sol = Solution().findTilt(root)
    print("Solution : {}".format(sol))

    root = TreeNode(21)
    root.left = TreeNode(7)
    root.right = TreeNode(14)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(2)
    print("Case 3")
    Solution().traverse_tree(root)
    sol = Solution().findTilt(root)
    print ("Solution : {}".format(sol))