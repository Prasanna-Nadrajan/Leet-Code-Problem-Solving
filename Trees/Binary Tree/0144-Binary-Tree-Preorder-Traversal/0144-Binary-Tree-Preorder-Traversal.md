## 🌲 Problem: Binary Tree Preorder Traversal (LeetCode #144)

### 📄 Problem Statement
Given the root of a binary tree, return the preorder traversal of its nodes' values.

In preorder traversal, nodes are visited in the order:  
**Root ➝ Left ➝ Right**

---

### 📥 Input
- `root`: TreeNode — the root of a binary tree

---

### 📤 Output
- List of integers representing preorder traversal

---

### 🧪 Examples

**Example 1:**  
Input: `root = [1,null,2,3]`  
Output: `[1,2,3]`

**Example 2:**  
Input: `root = [1,2,3,4,5,null,8,null,null,6,7,9]`  
Output: `[1,2,4,5,6,7,3,8,9]`

**Example 3:**  
Input: `root = []`  
Output: `[]`

**Example 4:**  
Input: `root = [1]`  
Output: `[1]`

---

### 🔒 Constraints
- Number of nodes: [0, 100]
- `-100 <= Node.val <= 100`

---

### 💡 Follow Up
Recursive solution is trivial. Can you do it **iteratively**?
