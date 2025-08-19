# Leetcode 2348: Number of Zero-Filled Subarrays

## 🧠 Problem Statement

Given an integer array `nums`, return the number of **subarrays filled entirely with 0**.

> A subarray is a contiguous non-empty sequence of elements within an array.

---

## 📊 Examples

### Example 1  
**Input:** `nums = [1,3,0,0,2,0,0,4]`  
**Output:** `6`  
**Explanation:**  
- `[0]` occurs 4 times  
- `[0,0]` occurs 2 times  
- No longer zero-filled subarrays exist

---

### Example 2  
**Input:** `nums = [0,0,0,2,0,0]`  
**Output:** `9`  
**Explanation:**  
- `[0]` occurs 5 times  
- `[0,0]` occurs 3 times  
- `[0,0,0]` occurs once

---

### Example 3  
**Input:** `nums = [2,10,2019]`  
**Output:** `0`  
**Explanation:** No zero-filled subarrays exist.

---

## 📌 Constraints

- `1 <= nums.length <= 10⁵`  
- `-10⁹ <= nums[i] <= 10⁹`

---

## 💡 Tags

`Array` `Prefix Sum` `Counting` `Sliding Window`
