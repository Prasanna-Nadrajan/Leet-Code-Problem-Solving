# 🧠 Problem Statement

**Leetcode #36 — Medium**

Determine if a `9 x 9` Sudoku board is **valid**.  
Only the **filled cells** need to be validated according to the following rules:

### ✅ Rules:
- Each **row** must contain the digits `1-9` **without repetition**
- Each **column** must contain the digits `1-9` **without repetition**
- Each of the **nine 3 x 3 sub-boxes** must contain the digits `1-9` **without repetition**

> ⚠️ Note:  
> A valid Sudoku board may not be **solvable**, but it must follow the rules above for the filled cells.

---

## 📊 Examples

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
Output: true
```
Example 2
Input:
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```

Output: false
Explanation: Two 8s in the top-left 3x3 box violate the rule.

📌 Constraints
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit '1' to '9' or '.'
