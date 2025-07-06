# 🚫 Day 91 – Remove Unwanted Values: Array Cleanup In-Place! 🧹🧩

Today’s LeetCode challenge focused on removing all instances of a value from an array, in-place, without allocating extra space.  
It wasn't just about deleting — it was about rebuilding the array smartly 🔁.

---

## 🔍 Challenge: Remove Element (LeetCode #27)

### 📄 Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**.  
The order of the elements may be changed.  
Then return the number of elements in `nums` which are **not equal to `val`**.

Let `k` be the number of elements in `nums` that are not equal to `val`.

You must do the following:

- Modify the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`.
- The remaining elements of `nums` beyond index `k` do not matter.
- Return `k`.

---

### 📥 Examples

#### Example 1:

    Input: nums = [3,2,2,3], val = 3  
    Output: 2, nums = [2,2,_,_]

Explanation: Return `k = 2`, and the first two elements of `nums` should be `2`.  
It does not matter what you leave beyond the returned `k`.

---

#### Example 2:

    Input: nums = [0,1,2,2,3,0,4,2], val = 2  
    Output: 5, nums = [0,1,4,0,3,_,_,_]

Explanation: Return `k = 5`. The first five elements of `nums` can be any order of `[0,1,4,0,3]`.

---

### ✅ Constraints

- `0 <= nums.length <= 100`  
- `0 <= nums[i] <= 50`  
- `0 <= val <= 100`

---

## ✅ Key Learnings

- 🔄 Used two-pointer strategy to overwrite unwanted values  
- ⚡ Practiced writing memory-efficient, in-place logic  
- 🧠 Improved skills in index management and selective overwrites

📂 **Category**: Arrays  
💡 **Skills Applied**: In-place updates, loop control, value matching

---

## ✨ Reflection

This challenge reminds us that performance isn't always about speed — sometimes it's about space and how cleanly we can transform data without allocating more.  
**Day 91**: still solving, still growing! 🚀

#100DaysOfCode #Day91 #LeetCode #Arrays #RemoveElement #InPlace #DSA #Python #CodingJourney
