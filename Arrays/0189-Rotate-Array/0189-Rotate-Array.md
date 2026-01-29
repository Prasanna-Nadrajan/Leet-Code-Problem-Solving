# Rotate Array

## Problem Description

Given an integer array `nums`, rotate the array to the **right** by `k` steps, where `k` is non-negative.

---

## Examples

### Example 1:
**Input:**  
nums = [1,2,3,4,5,6,7], k = 3

makefile
Copy code

**Output:**  
[5,6,7,1,2,3,4]

yaml
Copy code

**Explanation:**  
- Rotate 1 step → `[7,1,2,3,4,5,6]`  
- Rotate 2 steps → `[6,7,1,2,3,4,5]`  
- Rotate 3 steps → `[5,6,7,1,2,3,4]`

---

### Example 2:
**Input:**  
nums = [-1,-100,3,99], k = 2

makefile
Copy code

**Output:**  
[3,99,-1,-100]

yaml
Copy code

**Explanation:**  
- Rotate 1 step → `[99,-1,-100,3]`  
- Rotate 2 steps → `[3,99,-1,-100]`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

---

## Follow-Up

- Try to come up with **multiple approaches**
- Can you solve it **in-place** with **O(1)** extra space?
