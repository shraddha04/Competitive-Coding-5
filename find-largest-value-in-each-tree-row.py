# Time Complexity : O(n) - n is the number of nodes in tree
# Space Complexity : O(n) - n is the number of nodes in tree, this is the queue
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

"""

Do BFS and track the max element at each level and add it to the result array

"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        result = []

        if not root:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            maxNumber = float("-inf")
            for i in range(0, size):
                node = queue.popleft()
                if node.val > maxNumber:
                    maxNumber = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(maxNumber)

        return result









