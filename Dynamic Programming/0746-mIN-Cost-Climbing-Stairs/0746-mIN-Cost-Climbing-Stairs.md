# 746. Min Cost Climbing Stairs

**Difficulty:** Easy
**Topics:** Dynamic Programming

You are given an integer array `cost` where `cost[i]` is the cost of the *i-th* step on a staircase. Once you pay the cost, you can either climb **one** or **two** steps.

You can either start from step with index `0`, or step with index `1`.

Return the **minimum cost** to reach the top of the floor.

### Example 1

```
Input: cost = [10, 15, 20]
Output: 15
```

**Explanation:** Start at index `1`, pay 15, and climb two steps to reach the top.

### Example 2

```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
```

### Constraints

* `2 <= cost.length <= 1000`
* `0 <= cost[i] <= 999`

---
