# 🧠 Problem Statement

**Leetcode #2197 — Hard**

You are given an array of integers `nums`. Perform the following steps repeatedly:

1. Find any two **adjacent non-coprime** numbers in `nums`  
  (i.e., `GCD(x, y) > 1`)
2. Replace them with their **LCM (Least Common Multiple)**
3. Continue until no adjacent non-coprime pairs remain

🎯 **Goal**:  
Return the final modified array.  
It is guaranteed that **any order of replacement** will lead to the **same result**.

---

## 📊 Examples

### Example 1  
**Input:** `nums = [6,4,3,2,7,6,2]`  
**Output:** `[12,7,6]`  
**Explanation:**  
- (6,4) → 12  
- (12,3) → 12  
- (12,2) → 12  
- (6,2) → 6  
→ Final array: `[12,7,6]`

---

### Example 2  
**Input:** `nums = [2,2,1,1,3,3,3]`  
**Output:** `[2,1,1,3]`  
**Explanation:**  
- (3,3) → 3  
- (3,3) → 3  
- (2,2) → 2  
→ Final array: `[2,1,1,3]`

---

## 📌 Constraints

- `1 <= nums.length <= 10⁵`  
- `1 <= nums[i] <= 10⁵`  
- Final array values ≤ `10⁸`

---

## 💡 Tags

`Math` `Stack` `GCD` `LCM` `Simulation` `Greedy`
