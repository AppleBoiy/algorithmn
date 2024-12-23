class PQNode:
    def __init__(self, data, priority=0):
        self.data = data
        self.priority = priority
        self.next = None

    def __repr__(self):
        return f"PriorityQueue({self.priority} {self.data})"


class PQ:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def enqueue(self, new):
        # insert new data
        if self.is_empty():
            self.head = new

    def dequeue(self):
        # pop the most priority from queue
        ...

    def top(self):
        return self.head
