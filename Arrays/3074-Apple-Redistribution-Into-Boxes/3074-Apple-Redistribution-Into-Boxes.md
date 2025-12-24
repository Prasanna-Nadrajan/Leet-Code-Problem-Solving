# 3074. Apple Redistribution into Boxes

**Difficulty:** Easy

You are given an array `apple` of size `n` and an array `capacity` of size `m`.

There are `n` packs where the `i`th pack contains `apple[i]` apples. There are `m` boxes as well, and the `i`th box has a capacity of `capacity[i]` apples.

Return the **minimum number of boxes** you need to select to redistribute these `n` packs of apples into boxes.

Apples from the same pack can be distributed into different boxes.

### Example 1

```
Input: apple = [1,3,2], capacity = [4,3,1,5,2]
Output: 2
```

### Example 2

```
Input: apple = [5,5,5], capacity = [2,4,2,7]
Output: 4
```

### Constraints

* 1 <= apple.length, capacity.length <= 50
* 1 <= apple[i], capacity[i] <= 50
