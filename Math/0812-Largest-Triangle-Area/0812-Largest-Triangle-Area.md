# 812. Largest Triangle Area

### Problem Description

Given an array of points on the X-Y plane `points` where `points[i] = [x_i, y_i]`, return the area of the largest triangle that can be formed by any three different points. Answers within $10^{-5}$ of the actual answer will be accepted.

### Examples

#### Example 1:
**Input:** `points = [[0,0],[0,1],[1,0],[0,2],[2,0]]`
**Output:** `2.00000`
**Explanation:** The red triangle is the largest.

#### Example 2:
**Input:** `points = [[1,0],[0,0],[0,1]]`
**Output:** `0.50000`

### Constraints:
- `3 <= points.length <= 50`
- `-50 <= x_i, y_i <= 50`
- All the given points are **unique**.
