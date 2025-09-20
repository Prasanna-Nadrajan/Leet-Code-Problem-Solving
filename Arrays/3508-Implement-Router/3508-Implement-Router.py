from collections import deque, defaultdict
from typing import List
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.MAX = memoryLimit
        self.ds = deque()
        self.packet_set = set()
        self.dest_to_timestamps = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False

        if len(self.ds) == self.MAX:
            old = self.ds.popleft()
            self.packet_set.discard(old)
            _, old_dest, old_ts = old
            idx = bisect.bisect_left(self.dest_to_timestamps[old_dest], old_ts)
            if idx < len(self.dest_to_timestamps[old_dest]) and self.dest_to_timestamps[old_dest][idx] == old_ts:
                self.dest_to_timestamps[old_dest].pop(idx)

        self.ds.append(packet)
        self.packet_set.add(packet)
        bisect.insort(self.dest_to_timestamps[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.ds:
            return []
        packet = self.ds.popleft()
        self.packet_set.discard(packet)

        _, dest, ts = packet
        idx = bisect.bisect_left(self.dest_to_timestamps[dest], ts)
        if idx < len(self.dest_to_timestamps[dest]) and self.dest_to_timestamps[dest][idx] == ts:
            self.dest_to_timestamps[dest].pop(idx)

        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ts_list = self.dest_to_timestamps[destination]
        left = bisect.bisect_left(ts_list, startTime)
        right = bisect.bisect_right(ts_list, endTime)
        return right - left
