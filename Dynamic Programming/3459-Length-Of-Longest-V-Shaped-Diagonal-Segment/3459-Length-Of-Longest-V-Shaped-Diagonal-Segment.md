# 🚀 Day 117: Length of Longest V-Shaped Diagonal Segment

## 🧠 Problem Statement

**Leetcode #3459 — Hard**

You are given a 2D integer matrix `grid` of size `n x m`, where each element is either `0`, `1`, or `2`.

A **V-shaped diagonal segment** is defined as:

- Starts with a `1`
- Follows the infinite alternating sequence: `2, 0, 2, 0, ...`
- Begins in one of the four diagonal directions:
  - Top-left to bottom-right  
  - Bottom-right to top-left  
  - Top-right to bottom-left  
  - Bottom-left to top-right
- May make **at most one clockwise 90° turn** to another diagonal direction while continuing the sequence

🎯 **Goal**:  
Return the **length of the longest V-shaped diagonal segment**.  
If no valid segment exists, return `0`.

---

## 📊 Examples

### Example 1  
**Input:**  
`grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]`  
**Output:** `5`  
**Path:** `(0,2) → (1,3) → (2,4) → turn → (3,3) → (4,2)`

---

### Example 2  
**Input:**  
`grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]`  
**Output:** `4`  
**Path:** `(2,3) → (3,2) → turn → (2,1) → (1,0)`

---

### Example 3  
**Input:**  
`grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]`  
**Output:** `5`  
**Path:** `(0,0) → (1,1) → (2,2) → (3,3) → (4,4)`

---

### Example 4  
**Input:**  
`grid = [[1]]`  
**Output:** `1`  
**Path:** `(0,0)`

---

## 📌 Constraints

- `n == grid.length`  
- `m == grid[i].length`  
- `1 <= n, m <= 500`  
- `grid[i][j]` is either `0`, `1`, or `2`
