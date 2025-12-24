# 334. Increasing Triplet Subsequence

**Difficulty:** Medium

Given an integer array `nums`, return `true` if there exist indices `(i, j, k)` such that:

* `i < j < k`
* `nums[i] < nums[j] < nums[k]`

Otherwise, return `false`.

### Example 1

```
Input: nums = [1,2,3,4,5]
Output: true
```

### Example 2

```
Input: nums = [5,4,3,2,1]
Output: false
```

### Example 3

```
Input: nums = [2,1,5,0,4,6]
Output: true
```

### Constraints

* 1 <= nums.length <= 5 * 10^5
* -2^31 <= nums[i] <= 2^31 - 1
