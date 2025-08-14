# 🚀 Day 108: Largest 3-Same-Digit Number in String

## 🧠 Problem Statement

**Leetcode #2264 — Easy**

You are given a string `num` representing a large integer. An integer is considered **good** if it satisfies the following conditions:

- It is a **substring** of `num` with **length 3**.
- It consists of **only one unique digit** (e.g., "111", "000").

Return the **maximum good integer** as a string, or an empty string `""` if no such integer exists.

> 🔹 A substring is a contiguous sequence of characters within a string.  
> 🔹 There may be leading zeroes in `num` or in the good integer.

---

## 📊 Examples

### Example 1
**Input:**  
`num = "6777133339"`  
**Output:**  
`"777"`  
**Explanation:**  
There are two good integers: `"777"` and `"333"`. `"777"` is larger.

---

### Example 2  
**Input:**  
`num = "2300019"`  
**Output:**  
`"000"`  
**Explanation:**  
Only one good integer: `"000"`.

---

### Example 3  
**Input:**  
`num = "42352338"`  
**Output:**  
`""`  
**Explanation:**  
No substring of length 3 has the same digit.

---

## 📌 Constraints

- `3 <= num.length <= 1000`
- `num` consists only of digits (`0-9`)

---

## 💡 Tags

`String` `Sliding Window` `Pattern Matching`
