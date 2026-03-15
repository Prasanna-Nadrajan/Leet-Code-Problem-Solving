# The Grid Search

**Platform:** HackerRank  
**Difficulty:** Medium  

## Problem Statement

Given a grid of digits represented as an array of strings, determine whether a **pattern grid** exists inside the larger grid.

Each string in the arrays represents a row in the grid.

The task is to check whether the smaller pattern appears **exactly** within the larger grid, maintaining the same **row order and column alignment**.

If the pattern exists inside the grid, return **"YES"**. Otherwise, return **"NO"**.

---

## Function Description

Complete the function:


gridSearch(G, P)


### Parameters

- `string G[R]` : the grid to search
- `string P[r]` : the pattern to search

### Returns

- `string` : `"YES"` if the pattern exists in the grid, otherwise `"NO"`

---

## Input Format

1. The first line contains an integer `t`, the number of test cases.

For each test case:

- The first line contains two integers `R` and `C`
  - `R` = number of rows in the grid
  - `C` = length of each row

- The next `R` lines contain strings representing the grid.

- The next line contains two integers `r` and `c`
  - `r` = number of rows in the pattern
  - `c` = length of each pattern row

- The next `r` lines contain strings representing the pattern.

---

## Example

### Grid


1234567890
0987654321
1111111111
1111111111
2222222222


### Pattern


876543
111111
111111


### Output


YES


**Explanation**

The pattern begins at the **second row and third column** of the grid and continues for the next rows, forming an exact match.

---

## Sample Input


2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99


---

## Sample Output


YES
NO


---

## Key Idea

To solve the problem:

1. Traverse each row of the grid.
2. Look for occurrences of the first row of the pattern.
3. Once found, check the subsequent rows to see if the full pattern matches.
4. If all rows match consecutively, return **YES**.

Otherwise return **NO**.

---

## Concepts Practiced

- Matrix / Grid traversal
- Pattern matching
- String comparison
- Nested iteration
