#
# [333] Largest BST Subtree
#
# https://leetcode.com/problems/largest-bst-subtree/description/
#
# algorithms
# Medium (31.95%)
# Total Accepted:	 25.8K
# Total Submissions: 80.9K
# Testcase Example:  '[10,5,15,1,8,null,7]'
#
# Given a binary tree, find the largest subtree which is a Binary Search Tree
# (BST), where largest means subtree with largest number of nodes in it.
#
# Note:
# A subtree must include all of its descendants.
#
# Example:
#
#
# Input: [10,5,15,1,8,null,7]
#
# ⁠  10
# ⁠  / \
# ⁠ 5  15
# ⁠/ \	 \
# 1   8   7
#
# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one.
# ⁠			   The return value is the subtree's size, which is 3.
#
#
# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#	  def __init__(self, x):
#		  self.val = x
#		  self.left = None
#		  self.right = None

class Solution(object):
	def largestBSTSubtree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

