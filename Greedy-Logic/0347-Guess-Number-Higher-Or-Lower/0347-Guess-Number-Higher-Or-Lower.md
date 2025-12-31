# 374. Guess Number Higher or Lower

**Difficulty:** Easy  

You are playing a guessing game where a number is picked between `1` and `n`.  
Your task is to guess the picked number using a predefined API:

`int guess(int num)`

### API Behavior
- Returns `-1` if `num` is higher than the picked number  
- Returns `1` if `num` is lower than the picked number  
- Returns `0` if `num` is equal to the picked number  

### Objective
Return the number that was picked.

### Constraints
- `1 <= n <= 2^31 - 1`

### Hint
Use a **binary search strategy** to minimize the number of guesses.
