# 🧠 Problem Statement

**Leetcode #3021 — Medium**

Alice and Bob are playing a turn-based game on a field with two lanes of flowers between them.

- There are `x` flowers in the first lane and `y` flowers in the second lane.
- Alice always takes the **first turn**.
- On each turn, a player picks **one flower** from **either lane**.
- The player who picks the **last flower** wins the game by capturing their opponent.

🎯 **Goal**:  
Given two integers `n` and `m`, representing the maximum number of flowers in each lane (`x ∈ [1,n]`, `y ∈ [1,m]`), return the **number of valid pairs `(x, y)`** such that **Alice wins** the game.

---

## 📊 Examples

### Example 1  
**Input:** `n = 3`, `m = 2`  
**Output:** `3`  
**Valid pairs:** `(1,2)`, `(2,1)`, `(3,2)`

---

### Example 2  
**Input:** `n = 1`, `m = 1`  
**Output:** `0`  
**Explanation:** No valid pair where Alice wins.

---

## 📌 Constraints

- `1 <= n, m <= 10⁵`

---

## 💡 Tags

`Game Theory` `Math` `Parity` `Simulation`
