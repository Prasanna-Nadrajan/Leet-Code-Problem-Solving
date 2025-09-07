# 🧠 Problem Statement

**Leetcode #141 — Easy**

Given `head`, the head of a linked list, determine if the linked list contains a **cycle**.

A cycle exists if there is a node in the list that can be reached again by continuously following the `next` pointer.

> Internally, `pos` is used to denote the index of the node that the tail's `next` pointer connects to.  
> Note: `pos` is not passed as a parameter.

🎯 **Goal**:  
Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

---

## 📊 Examples

### Example 1  
**Input:** `head = [3,2,0,-4], pos = 1`  
**Output:** `true`  
**Explanation:** Tail connects to node at index 1 → cycle exists

---

### Example 2  
**Input:** `head = [1,2], pos = 0`  
**Output:** `true`  
**Explanation:** Tail connects to node at index 0 → cycle exists

---

### Example 3  
**Input:** `head = [1], pos = -1`  
**Output:** `false`  
**Explanation:** No cycle in the list

---

## 📌 Constraints

- `0 <= number of nodes <= 10⁴`  
- `-10⁵ <= Node.val <= 10⁵`  
- `pos` is `-1` or a valid index in the linked list

---

## 💡 Tags

`Linked List` `Two Pointers` `Floyd’s Cycle Detection` `Fast and Slow Pointer`
