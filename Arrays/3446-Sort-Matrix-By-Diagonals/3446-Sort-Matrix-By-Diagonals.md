## 🧠 Problem Statement

**Leetcode #3446 — Medium**

You are given an `n x n` square matrix of integers `grid`.

🎯 **Goal**:  
Return the matrix such that:
- Diagonals in the **bottom-left triangle** (including the main diagonal) are sorted in **non-increasing order**
- Diagonals in the **top-right triangle** are sorted in **non-decreasing order**

---

## 📊 Examples

### Example 1  
**Input:** `grid = [[1,7,3],[9,8,2],[4,5,6]]`  
**Output:** `[[8,2,3],[9,6,7],[4,5,1]]`  
**Explanation:**  
- Diagonal `[1,8,6]` → `[8,6,1]`  
- Diagonal `[7,2]` → `[2,7]`

---

### Example 2  
**Input:** `grid = [[0,1],[1,2]]`  
**Output:** `[[2,1],[1,0]]`  
**Explanation:**  
- Diagonal `[0,2]` → `[2,0]`

---

### Example 3  
**Input:** `grid = [[1]]`  
**Output:** `[[1]]`  
**Explanation:**  
Single-element diagonals are already sorted.

---

## 📌 Constraints

- `grid.length == grid[i].length == n`  
- `1 <= n <= 10`  
- `-10⁵ <= grid[i][j] <= 10⁵`

---

## 💡 Tags

`Matrix` `Sorting` `Diagonal Traversal` `Simulation`
