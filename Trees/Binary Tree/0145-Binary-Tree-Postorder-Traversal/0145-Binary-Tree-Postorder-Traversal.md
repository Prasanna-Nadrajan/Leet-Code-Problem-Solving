## 🌳 Problem: Binary Tree Postorder Traversal (LeetCode #145)

### 📄 Problem Statement
Given the root of a binary tree, return the postorder traversal of its nodes' values.

In postorder traversal, nodes are visited in the order:  
**Left ➝ Right ➝ Root**

---

### 📥 Input
- `root`: TreeNode — the root of a binary tree

---

### 📤 Output
- List of integers representing postorder traversal

---

### 🧪 Examples

**Example 1:**  
Input: `root = [1,null,2,3]`  
Output: `[3,2,1]`

**Example 2:**  
Input: `root = [1,2,3,4,5,null,8,null,null,6,7,9]`  
Output: `[4,6,7,5,2,9,8,3,1]`

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
