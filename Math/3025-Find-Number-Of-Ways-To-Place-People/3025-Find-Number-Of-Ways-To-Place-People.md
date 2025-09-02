# 🧠 Problem Statement

**Leetcode #3025 — Medium**

You are given a 2D array `points` of size `n x 2`, where each `points[i] = [xi, yi]` represents a point on a 2D plane.

🎯 **Goal**:  
Count the number of valid pairs of points `(A, B)` such that:
- Point `A` is on the **upper left side** of point `B`  
  (i.e., `A.x < B.x` and `A.y > B.y`)
- There are **no other points** inside the rectangle (or line) formed by `A` and `B`, including the border

Return the total number of such valid pairs.

---

## 📊 Examples

### Example 1  
**Input:** `points = [[1,1],[2,2],[3,3]]`  
**Output:** `0`  
**Explanation:** No valid `(A, B)` pairs satisfy the condition.

---

### Example 2  
**Input:** `points = [[6,2],[4,4],[2,6]]`  
**Output:** `2`  
**Explanation:**  
- Valid pairs: `(points[1], points[0])`, `(points[2], points[1])`  
- `(points[2], points[0])` is invalid due to a third point inside the rectangle

---

### Example 3  
**Input:** `points = [[3,1],[1,3],[1,1]]`  
**Output:** `2`  
**Explanation:**  
- Valid pairs: `(points[2], points[0])`, `(points[1], points[2])`  
- `(points[1], points[0])` is invalid due to a point on the border

---

## 📌 Constraints

- `2 <= n <= 50`  
- `points[i].length == 2`  
- `0 <= points[i][0], points[i][1] <= 50`  
- All points are **distinct**

---

## 💡 Tags

`Geometry` `Brute Force` `2D Grid` `Simulation` `Spatial Reasoning`
