# 🧠 Problem Statement

**Leetcode #3408 — Medium**

You are building a **task management system** that allows users to manage tasks, each associated with a **priority**.

### 🛠️ Implement the `TaskManager` class:

#### Initialization:
TaskManager(vector<vector<int>>& tasks)


- Initializes the system with a list of [userId, taskId, priority] triples.
Methods:
- void add(int userId, int taskId, int priority)
Adds a task for the user. taskId is guaranteed to be unique.
- void edit(int taskId, int newPriority)
Updates the priority of an existing task.
- void rmv(int taskId)
Removes the task from the system.
- int execTop()
Executes the task with the highest priority.
If multiple tasks share the same priority, choose the one with the highest taskId.
Returns the userId of the executed task.
If no tasks are available, return -1.

📊 Example
Input:
["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
[[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]

Output:
[null, null, null, 3, null, null, 5]



📌 Constraints
- 1 <= tasks.length <= 10⁵
- 0 <= userId, taskId <= 10⁵
- 0 <= priority, newPriority <= 10⁹
- At most 2 × 10⁵ method calls
- All taskIds are valid and unique


💡 This problem w

