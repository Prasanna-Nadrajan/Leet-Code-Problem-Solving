# 🚀 Day 109: Fruit Into Baskets

## 🧠 Problem Statement

**Leetcode #904 — Medium**

You are visiting a farm with a row of fruit trees represented by an integer array `fruits`, where `fruits[i]` is the type of fruit the `i-th` tree produces.

You have **two baskets**, each can hold **only one type of fruit**, but unlimited quantity.  
Starting from any tree, you must pick **exactly one fruit per tree** while moving to the right.  
You must stop when a fruit cannot fit into either basket.

Return the **maximum number of fruits** you can pick.

---

## 📊 Examples

### Example 1  
**Input:** `fruits = [1,2,1]`  
**Output:** `3` ✅  
**Explanation:** Pick all 3 fruits.

---

### Example 2  
**Input:** `fruits = [0,1,2,2]`  
**Output:** `3` ✅  
**Explanation:** Best pick is from trees [1,2,2].

---

### Example 3  
**Input:** `fruits = [1,2,3,2,2]`  
**Output:** `4` ✅  
**Explanation:** Best pick is from trees [2,3,2,2].

---

## 📌 Constraints

- `1 <= fruits.length <= 10⁵`  
- `0 <= fruits[i] < fruits.length`

---

## 💡 Tags

`Sliding Window` `Greedy` `Hash Map` `Two Pointers`
