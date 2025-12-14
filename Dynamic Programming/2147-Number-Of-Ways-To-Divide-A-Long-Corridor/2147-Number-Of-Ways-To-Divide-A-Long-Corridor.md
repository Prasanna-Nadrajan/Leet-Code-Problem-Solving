# 2147. Number of Ways to Divide a Long Corridor

## Problem Statement

Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string `corridor` of length `n` consisting of characters:

* `'S'` representing a **seat**
* `'P'` representing a **plant**

A room divider is already installed:

* To the **left of index 0**
* To the **right of index n - 1**

You may install additional dividers between positions `i - 1` and `i` (for `1 <= i <= n - 1`), with **at most one divider per position**.

### Objective

Divide the corridor into **non-overlapping sections** such that:

* Each section contains **exactly two seats (`S`)**
* Each section may contain **any number of plants (`P`)**

Two ways of dividing the corridor are considered **different** if there exists at least one position where a divider is placed in one way but not in the other.

Return the **number of valid ways** to divide the corridor. Since the result can be large, return it modulo `10^9 + 7`. If no valid division exists, return `0`.

---

## Examples

### Example 1

**Input:**

```
corridor = "SSPPSPS"
```

**Output:**

```
3
```

**Explanation:**
There are 3 valid ways to place additional dividers such that each section contains exactly two seats.

---

### Example 2

**Input:**

```
corridor = "PPSPSP"
```

**Output:**

```
1
```

**Explanation:**
Only one valid way exists — by not placing any additional dividers. Any divider placement would violate the condition of having exactly two seats per section.

---

### Example 3

**Input:**

```
corridor = "S"
```

**Output:**

```
0
```

**Explanation:**
It is impossible to divide the corridor into sections with exactly two seats.

---

## Constraints

* `1 <= n <= 10^5`
* `corridor[i]` is either `'S'` or `'P'`

---

## Notes

* If the total number of seats is **not even**, there is no valid way to divide the corridor.
* Each valid section must contain **exactly two seats**, regardless of how many plants appear between them.
