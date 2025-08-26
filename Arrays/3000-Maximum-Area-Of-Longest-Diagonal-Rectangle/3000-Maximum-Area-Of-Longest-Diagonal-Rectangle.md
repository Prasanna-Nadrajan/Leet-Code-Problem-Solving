## 🧠 Problem Statement

**Leetcode #3000 — Easy**

You are given a 2D 0-indexed integer array `dimensions`.

Each `dimensions[i] = [length, width]` represents a rectangle.

🎯 **Goal**:  
Return the **area** of the rectangle that has the **longest diagonal**.  
If multiple rectangles share the longest diagonal, return the one with the **maximum area**.

> Diagonal length is calculated using the Pythagorean theorem:  
> `diagonal = sqrt(length² + width²)`

---

## 📊 Examples

### Example 1  
**Input:** `dimensions = [[9,3],[8,6]]`  
**Output:** `48`  
**Explanation:**  
- Rectangle 0: Diagonal ≈ 9.487, Area = 27  
- Rectangle 1: Diagonal = 10, Area = 48  
→ Return 48

---

### Example 2  
**Input:** `dimensions = [[3,4],[4,3]]`  
**Output:** `12`  
**Explanation:**  
- Both diagonals = 5  
- Max area = 12

---

## 📌 Constraints

- `1 <= dimensions.length <= 100`  
- `dimensions[i].length == 2`  
- `1 <= dimensions[i][0], dimensions[i][1] <= 100`

---

## 💡 Tags

`Geometry` `Array` `Math` `Greedy`
