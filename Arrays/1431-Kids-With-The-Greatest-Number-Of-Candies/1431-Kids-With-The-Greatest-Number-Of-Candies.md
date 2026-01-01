# 1431. Kids With the Greatest Number of Candies

**Difficulty:** Easy  

There are `n` kids, each having a certain number of candies.  
You are given an integer array `candies`, where `candies[i]` represents the candies owned by the `i`th kid, and an integer `extraCandies`.

For each kid, check whether giving **all** the extraCandies to that kid makes them have the **greatest number of candies** among all kids.

Return a boolean array `result`, where:
- `result[i] = true` if the `i`th kid can have the greatest number of candies
- `result[i] = false` otherwise  

Multiple kids can have the greatest number of candies.

### Example
**Input:**  
`candies = [2,3,5,1,3], extraCandies = 3`

**Output:**  
`[true, true, true, false, true]`

### Constraints
- `2 <= n <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`
