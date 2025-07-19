## 🔁 Problem: Reverse Bits (LeetCode #190)

### 📄 Problem Statement  
Reverse bits of a given 32-bit unsigned integer.

Note:  
In some programming languages like Java, there's no unsigned integer type. But that doesn't affect the solution, because the internal 32-bit binary representation remains the same (due to 2's complement notation).

---

### 📥 Input  
- `n` (integer): A 32-bit unsigned integer  
  `0 <= n <= 2^31 - 2`  
  (n is guaranteed to be **even**)

---

### 📤 Output  
- An integer: the unsigned 32-bit integer result of reversing the bits of `n`

---

### 🧪 Examples

**Example 1:**  
Input: `n = 43261596`  
Binary: `00000010100101000001111010011100`  
Output: `964176192`  
Binary: `00111001011110000010100101000000`

---

**Example 2:**  
Input: `n = 2147483644`  
Binary: `01111111111111111111111111111100`  
Output: `1073741822`  
Binary: `00111111111111111111111111111110`

---

### 🔒 Constraints  
- `0 <= n <= 2^31 - 2`
- `n` is even

---

### 💡 Hints  
- Bitwise operators are key: `>>`, `<<`, `&`, `|`
- You can reverse bits one by one using a loop that runs 32 times
