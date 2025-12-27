# 700. Search in a Binary Search Tree

## Problem Statement

You are given the root of a **Binary Search Tree (BST)** and an integer `val`.

Your task is to find the node in the BST such that the node’s value is equal to `val` and return the **subtree rooted at that node**. If such a node does not exist, return `null`.

A Binary Search Tree follows the rule:

* Left subtree values < node value
* Right subtree values > node value

---

## Examples

**Example 1:**

Input: `root = [4,2,7,1,3], val = 2`

Output: `[2,1,3]`

**Example 2:**

Input: `root = [4,2,7,1,3], val = 5`

Output: `[]`

---

## Constraints

* Number of nodes in the tree is in the range `[1, 5000]`
* `1 <= Node.val <= 10^7`
* `root` is a valid Binary Search Tree
* `1 <= val <= 10^7`
