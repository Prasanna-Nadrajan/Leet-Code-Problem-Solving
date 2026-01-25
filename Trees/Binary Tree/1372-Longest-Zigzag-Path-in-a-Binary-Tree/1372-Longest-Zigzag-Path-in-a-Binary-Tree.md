# 1372. Longest ZigZag Path in a Binary Tree

You are given the root of a binary tree.

A **ZigZag path** for a binary tree is defined as follows:

1. Choose any node in the binary tree and a direction (right or left).
2. If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
3. Change the direction from right to left or from left to right.
4. Repeat the above steps until you can no longer move in the tree.

The **ZigZag length** is defined as the number of nodes visited minus one. A single node has a ZigZag length of 0.

Return the **longest ZigZag path** contained in the tree.

---

## Examples

**Example 1**

Input:

```
root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
```

Output:

```
3
```

**Example 2**

Input:

```
root = [1,1,1,null,1,null,null,1,1,null,1]
```

Output:

```
4
```

**Example 3**

Input:

```
root = [1]
```

Output:

```
0
```

---

## Constraints

* The number of nodes in the tree is in the range `[1, 5 * 10^4]`
* `1 <= Node.val <= 100`
