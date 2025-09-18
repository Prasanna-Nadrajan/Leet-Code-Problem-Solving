from sortedcontainers import SortedList

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.sorted_tasks = SortedList()
        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (userId, priority)
            self.sorted_tasks.add((-priority, -taskId, userId, taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        self.sorted_tasks.add((-priority, -taskId, userId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, oldPriority = self.task_map[taskId]
        self.sorted_tasks.discard((-oldPriority, -taskId, userId, taskId))
        self.task_map[taskId] = (userId, newPriority)
        self.sorted_tasks.add((-newPriority, -taskId, userId, taskId))

    def rmv(self, taskId: int) -> None:
        userId, priority = self.task_map.pop(taskId)
        self.sorted_tasks.discard((-priority, -taskId, userId, taskId))

    def execTop(self) -> int:
        if not self.sorted_tasks:
            return -1
        _, _, userId, taskId = self.sorted_tasks.pop(0)
        self.task_map.pop(taskId)
        return userId

        
