class RecentCounter:

    def __init__(self):
        self.counter=[]

    def ping(self, t: int) -> int:
        counter=self.counter
        counter.append(t)
        while(counter and (t-3000) > counter[0]):
            counter.pop(0)
        return len(counter)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
