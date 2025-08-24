## 🧠 Problem Statement

**Leetcode #1493 — Medium**

Given a binary array `nums`, you must **delete exactly one element**.

Return the **length of the longest non-empty subarray** that contains **only 1's** in the resulting array.

If no such subarray exists, return `0`.

---

## 📊 Examples

### Example 1  
**Input:** `nums = [1,1,0,1]`  
**Output:** `3`  
**Explanation:** Delete the `0` at index 2 → `[1,1,1]`

---

### Example 2  
**Input:** `nums = [0,1,1,1,0,1,1,0,1]`  
**Output:** `5`  
**Explanation:** Delete the `0` at index 4 → `[1,1,1,1,1]`

---

### Example 3  
**Input:** `nums = [1,1,1]`  
**Output:** `2`  
**Explanation:** Must delete one element → longest subarray is `[1,1]`

---

## 📌 Constraints

- `1 <= nums.length <= 10⁵`  
- `nums[i]` is either `0` or `1`

---

## 💡 Tags

`Sliding Window` `Two Pointers` `Greedy` `Array`
