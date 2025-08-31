# 🧠 Problem Statement

**Leetcode #37 — Hard**

Write a program to solve a Sudoku puzzle by filling the empty cells.

A valid Sudoku solution must satisfy the following rules:

- Each digit `1-9` must occur **exactly once** in each **row**
- Each digit `1-9` must occur **exactly once** in each **column**
- Each digit `1-9` must occur **exactly once** in each of the **nine 3×3 sub-boxes**

> The `'.'` character indicates an empty cell.

---

## 📊 Example

### Example 1  
**Input:**  
```text
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```

Output:
```
[["5","3","4","6","7","8","9","1","2"]
,["6","7","2","1","9","5","3","4","8"]
,["1","9","8","3","4","2","5","6","7"]
,["8","5","9","7","6","1","4","2","3"]
,["4","2","6","8","5","3","7","9","1"]
,["7","1","3","9","2","4","8","5","6"]
,["9","6","1","5","3","7","2","8","4"]
,["2","8","7","4","1","9","6","3","5"]
,["3","4","5","2","8","6","1","7","9"]]
```


📌 Constraints
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit '1' to '9' or '.'
- It is guaranteed that the input board has only one solution

💡 Tags
Backtracking Matrix Constraint Propagation Recursion


