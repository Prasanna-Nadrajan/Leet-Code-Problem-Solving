# 2095. Delete the Middle Node of a Linked List

## Problem Statement

You are given the `head` of a singly linked list. Your task is to **delete the middle node** and return the head of the modified linked list.

The middle node of a linked list of size `n` is defined as the `⌊n / 2⌋`th node (0-based indexing), where `⌊x⌋` represents the floor value of `x`.

If the list contains only one node, the result after deletion should be an empty list.

---

## Examples

**Example 1:**

Input: `head = [1,3,4,7,1,2,6]`

Output: `[1,3,4,1,2,6]`

**Example 2:**

Input: `head = [1,2,3,4]`

Output: `[1,2,4]`

**Example 3:**

Input: `head = [2,1]`

Output: `[2]`

---

## Constraints

* Number of nodes is in the range `[1, 10^5]`
* `1 <= Node.val <= 10^5`
