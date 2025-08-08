# 🍵 808. Soup Servings

## Problem Statement

You have two soups, **A** and **B**, each starting with **n mL**.  
On every turn, one of the following four serving operations is chosen at random, each with probability **0.25**, independent of all previous turns:

1. Pour **100 mL** from type A and **0 mL** from type B  
2. Pour **75 mL** from type A and **25 mL** from type B  
3. Pour **50 mL** from type A and **50 mL** from type B  
4. Pour **25 mL** from type A and **75 mL** from type B  

**Notes:**
- There is no operation that pours **0 mL** from A and **100 mL** from B.
- The amounts from A and B are poured **simultaneously** during the turn.
- If an operation asks you to pour more than you have left of a soup, pour all that remains of that soup.
- The process stops immediately after any turn in which one of the soups is used up.

**Goal:**  
Return the probability that **A is used up before B**, plus **half** the probability that both soups are used up **in the same turn**.

Answers within **10⁻⁵** of the actual answer will be accepted.

---

## Examples

### Example 1:
**Input:**  
n = 50

makefile
Copy
Edit
**Output:**  
0.62500

markdown
Copy
Edit
**Explanation:**  
- Operation 1 or 2 → A becomes empty first.  
- Operation 3 → Both A and B become empty at the same time.  
- Operation 4 → B becomes empty first.  

Total probability:  
0.25 * (1 + 1 + 0.5 + 0) = 0.625

yaml
Copy
Edit

---

### Example 2:
**Input:**  
n = 100

makefile
Copy
Edit
**Output:**  
0.71875

yaml
Copy
Edit
**Explanation:**  
Similar logic applies — summing up probabilities of A being empty first plus half when both empty.

---

## Constraints
- `0 <= n <= 10^9`
