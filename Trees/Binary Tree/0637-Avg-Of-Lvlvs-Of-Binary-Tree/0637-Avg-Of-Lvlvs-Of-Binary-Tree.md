# 637. Average of Levels in Binary Tree

**Difficulty:** Easy  
**Platform:** LeetCode  

## Problem Statement

Given the root of a binary tree, return the **average value of the nodes on each level** in the form of an array.

Answers within `10^-5` of the actual answer will be accepted.

## Examples

### Example 1
**Input:**  
root = [3,9,20,null,null,15,7]

**Output:**  
[3.00000,14.50000,11.00000]

**Explanation:**  
- Level 0 → Average = 3  
- Level 1 → Average = (9 + 20) / 2 = 14.5  
- Level 2 → Average = (15 + 7) / 2 = 11  

Hence return `[3, 14.5, 11]`.

---

### Example 2
**Input:**  
root = [3,9,20,15,7]

**Output:**  
[3.00000,14.50000,11.00000]

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`
- `-2^31 <= Node.val <= 2^31 - 1`
