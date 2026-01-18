1448. Count Good Nodes in Binary Tree

Difficulty: Medium

Problem Statement

Given a binary tree root, a node X in the tree is named good if in the path from the root to node X, there are no nodes with a value greater than X.

In other words, node X is good if its value is greater than or equal to every value on the path from the root to that node (inclusive).

Return the number of good nodes in the binary tree.

Examples

Example 1
Input: root = [3,1,4,3,null,1,5]
Output: 4

Explanation:
Nodes with values 3 (root), 4, 5, and 3 (left child of 1) are good nodes.

Example 2
Input: root = [3,3,null,4,2]
Output: 3

Example 3
Input: root = [1]
Output: 1

Constraints

The number of nodes in the binary tree is in the range [1, 10^5]

-10^4 <= Node.val <= 10^4
