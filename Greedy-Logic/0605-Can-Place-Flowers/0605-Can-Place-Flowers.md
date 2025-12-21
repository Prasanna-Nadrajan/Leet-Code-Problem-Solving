# 605. Can Place Flowers

## Problem Statement

You are given a long flowerbed represented as an integer array `flowerbed`, where:

* `0` means the plot is empty
* `1` means the plot already has a flower

Flowers **cannot be planted in adjacent plots**.

You are also given an integer `n`, representing the number of new flowers you want to plant.

Return `true` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule. Otherwise, return `false`.

---

## Examples

### Example 1

**Input:**

```
flowerbed = [1,0,0,0,1], n = 1
```

**Output:**

```
true
```

---

### Example 2

**Input:**

```
flowerbed = [1,0,0,0,1], n = 2
```

**Output:**

```
false
```

---

## Constraints

* `1 <= flowerbed.length <= 2 * 10^4`
* `flowerbed[i]` is either `0` or `1`
* There are no two adjacent flowers in the initial flowerbed
* `0 <= n <= flowerbed.length`
