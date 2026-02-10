# 2130. Maximum Twin Sum of a Linked List

**Difficulty:** Medium  
**Platform:** LeetCode  

## Problem Statement

In a linked list of size `n`, where `n` is even, the `i`th node (0-indexed) is the **twin** of the `(n - 1 - i)`th node, for  
`0 <= i <= (n / 2) - 1`.

The **twin sum** is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the **maximum twin sum** of the linked list.

## Examples

### Example 1
**Input:**  
head = [5,4,2,1]  

**Output:**  
6  

**Explanation:**  
- Node 0 and Node 3 → 5 + 1 = 6  
- Node 1 and Node 2 → 4 + 2 = 6  
Maximum twin sum = 6.

### Example 2
**Input:**  
head = [4,2,2,3]  

**Output:**  
7  

**Explanation:**  
- Node 0 and Node 3 → 4 + 3 = 7  
- Node 1 and Node 2 → 2 + 2 = 4  
Maximum twin sum = 7.

### Example 3
**Input:**  
head = [1,100000]  

**Output:**  
100001  

**Explanation:**  
Only one twin pair exists → 1 + 100000 = 100001.

## Constraints

- The number of nodes in the list is an even integer in the range `[2, 10⁵]`
- `1 <= Node.val <= 10⁵`
