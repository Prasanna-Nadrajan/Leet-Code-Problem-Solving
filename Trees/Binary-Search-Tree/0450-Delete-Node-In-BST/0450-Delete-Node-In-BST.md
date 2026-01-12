450. Delete Node in a BST

Difficulty: Medium

Problem Statement

Given the root of a Binary Search Tree (BST) and a key, delete the node with the given key from the BST.

Return the updated root of the BST.

Deletion involves two main steps:

Search for the node with the given key.

If found, delete the node while maintaining BST properties.

Examples

Example 1
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: One valid BST after deletion is shown above (multiple correct answers are possible).

Example 2
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain the key.

Example 3
Input: root = [], key = 0
Output: []

Constraints

Number of nodes in the tree: [0, 10^4]

-10^5 <= Node.val <= 10^5

Each node has a unique value

The given tree is a valid BST

-10^5 <= key <= 10^5
