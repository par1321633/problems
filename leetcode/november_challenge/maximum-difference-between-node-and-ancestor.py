"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.


Example 1:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        print(root)
        return self.process_root(root, root_queue=[])

    def process_root(self, root, root_queue):
        if root is None:
            print(root_queue)
            return max(root_queue) - min(root_queue)
            # return max([abs(root.val - val) for val in root_queue])
        root_queue.append(root.val)
        val = max(self.process_root(root.left, root_queue), self.process_root(root.right, root_queue))
        del root_queue[-1]
        return val


if __name__ == '__main__':
    print ("Case 1")
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    sol = Solution().maxAncestorDiff(root)
    print ("Solution : {}".format(sol))

    print ("Case : 2")
    root = TreeNode(2)
    root.right = TreeNode(0)
    root.right.left = TreeNode(1)
    sol = Solution().maxAncestorDiff(root)
    print ("Solution : {]".format(sol))

