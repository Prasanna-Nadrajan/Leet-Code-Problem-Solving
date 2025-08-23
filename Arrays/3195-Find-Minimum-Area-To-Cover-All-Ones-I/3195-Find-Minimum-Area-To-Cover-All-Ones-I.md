# Leetcode 3195: Find the Minimum Area to Cover All Ones I

## 🧠 Problem Statement

You are given a 2D binary array `grid`.  
Find a rectangle with horizontal and vertical sides that has the **smallest area**, such that **all the 1's** in `grid` lie inside this rectangle.

Return the **minimum possible area** of the rectangle.

---

## 📊 Examples

### Example 1  
**Input:** `grid = [[0,1,0],[1,0,1]]`  
**Output:** `6`  
**Explanation:**  
The smallest rectangle that covers all 1's has a height of 2 and width of 3 → Area = `2 × 3 = 6`

---

### Example 2  
**Input:** `grid = [[1,0],[0,0]]`  
**Output:** `1`  
**Explanation:**  
Only one cell contains a 1 → Area = `1 × 1 = 1`

---

## 📌 Constraints

- `1 <= grid.length, grid[i].length <= 1000`  
- `grid[i][j]` is either `0` or `1`  
- The input is guaranteed to contain **at least one 1**

---

## 💡 Tags

`Matrix` `Geometry` `Bounding Box` `Greedy`
