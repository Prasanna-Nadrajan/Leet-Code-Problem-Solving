# 🧠 Problem Statement

**Leetcode #1792 — Medium**

You are given a 2D integer array `classes`, where each `classes[i] = [passi, totali]` represents a class with `totali` total students, of which `passi` will pass the exam.

You are also given an integer `extraStudents`, representing brilliant students who are guaranteed to pass any class they are assigned to.

🎯 **Goal**:  
Assign each of the `extraStudents` to a class in a way that **maximizes the average pass ratio** across all classes.

### 📐 Definitions:
- **Pass ratio of a class** = `passi / totali`
- **Average pass ratio** = Sum of all class pass ratios / Number of classes

> ✅ Return the **maximum possible average pass ratio** after assigning all extra students.  
> Answers within `10⁻⁵` of the actual answer are accepted.

---

## 📊 Examples

### Example 1  
**Input:** `classes = [[1,2],[3,5],[2,2]], extraStudents = 2`  
**Output:** `0.78333`  
**Explanation:** Assign both extra students to the first class →  
New ratios: `3/4`, `3/5`, `2/2` → Average = `(0.75 + 0.6 + 1.0)/3 = 0.78333`

---

### Example 2  
**Input:** `classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4`  
**Output:** `0.53485`

---

## 📌 Constraints

- `1 <= classes.length <= 10⁵`  
- `classes[i].length == 2`  
- `1 <= passi <= totali <= 10⁵`  
- `1 <= extraStudents <= 10⁵`

---

## 💡 Tags

`Greedy` `Heap` `Priority Queue` `Optimization` `Math`
