# 872. Leaf-Similar Trees (Easy)

Consider all the leaves of a binary tree, from left to right order. The values of these leaves form a **leaf value sequence**.

Two binary trees are considered *leaf-similar* if their leaf value sequences are exactly the same.

Given the roots of two binary trees `root1` and `root2`, return `true` if the two trees are leaf-similar, otherwise return `false`.

## Examples

**Input:**
root1 = [3,5,1,6,2,9,8,null,null,7,4]
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]

**Output:** true

**Input:**
root1 = [1,2,3]
root2 = [1,3,2]

**Output:** false

## Constraints

* The number of nodes in each tree is in the range [1, 200]
* Node values are in the range [0, 200]
