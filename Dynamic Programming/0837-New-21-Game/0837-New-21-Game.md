
## 🧠 Problem Statement

**Leetcode #837 — Medium**

Alice plays a game inspired by the card game "21":

- She starts with **0 points**.
- While her score is **less than `k`**, she draws numbers randomly from the range `[1, maxPts]`.
- Each draw is **independent** and **uniformly distributed**.
- She **stops drawing** once her score reaches **`k` or more**.

🔍 **Goal**:  
Return the **probability** that Alice ends up with **`n` or fewer points**.

> Answers within `10⁻⁵` of the actual value are considered correct.

---

## 📊 Examples

### Example 1  
**Input:** `n = 10`, `k = 1`, `maxPts = 10`  
**Output:** `1.00000` ✅  
**Explanation:** Alice draws once and always ends with ≤ 10.

---

### Example 2  
**Input:** `n = 6`, `k = 1`, `maxPts = 10`  
**Output:** `0.60000` ✅  
**Explanation:** Alice draws once. 6 out of 10 outcomes are ≤ 6.

---

### Example 3  
**Input:** `n = 21`, `k = 17`, `maxPts = 10`  
**Output:** `0.73278` ✅

---

## 📌 Constraints

- `0 <= k <= n <= 10⁴`  
- `1 <= maxPts <= 10⁴`

---

## 💡 Tags

`Dynamic Programming` `Probability` `Sliding Window`
