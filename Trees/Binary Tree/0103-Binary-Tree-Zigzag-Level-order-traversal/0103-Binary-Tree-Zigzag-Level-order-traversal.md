# 103. Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium  
**Platform:** LeetCode  

## Problem Statement

Given the root of a binary tree, return the **zigzag level order traversal** of its nodes' values.

(Level order traversal alternating between **left to right** and **right to left** for each level.)

## Examples

### Example 1
**Input:**  
root = [3,9,20,null,null,15,7]

**Output:**  
[[3],[20,9],[15,7]]

### Example 2
**Input:**  
root = [1]

**Output:**  
[[1]]

### Example 3
**Input:**  
root = []

**Output:**  
[]

## Constraints

- The number of nodes in the tree is in the range `[0, 2000]`
- `-100 <= Node.val <= 100`
