# 55. Jump Game

## Problem Description

You are given an integer array `nums`.  
You are initially positioned at the **first index** of the array, and each element in the array represents your **maximum jump length** at that position.

Return **true** if you can reach the **last index**, or **false** otherwise.

---

## Examples

### Example 1:
**Input:**
nums = [2,3,1,1,4]

makefile
Copy code

**Output:**
true

yaml
Copy code

**Explanation:**
Jump 1 step from index 0 to index 1, then jump 3 steps to reach the last index.

---

### Example 2:
**Input:**
nums = [3,2,1,0,4]

makefile
Copy code

**Output:**
false

yaml
Copy code

**Explanation:**
You will always arrive at index 3.  
Its maximum jump length is 0, which makes it impossible to reach the last index.

---

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`
