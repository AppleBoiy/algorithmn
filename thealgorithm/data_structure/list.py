from .node import ListNode

class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        if self.size == 0:
            return '[]'
        else:
            result = '['
            current = self.head
            while current.next is not None:
                result += str(current.val) + ', '
                current = current.next
            result += str(current.val) + ']'
            return result

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range')
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range')
        current = self.head
        for i in range(index):
            current = current.next
        current.val = value

    def __delitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range')
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        current.next = current.next.next
        self.size -= 1

    def append(self, x):
        new_node = ListNode(x)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, index, x):
        if index < 0 or index > self.size:
            raise IndexError('Index out of range')
        new_node = ListNode(x)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def remove(self, x):
        current = self.head
        if current.val == x:
            self.head = current.next
            self.size -= 1
            return
        while current.next is not None:
            if current.next.val == x:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
        raise ValueError('Value not found in the list')

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def index(self, x):
        current = self.head
        for i in range(self.size):
            if current.val == x:
                return i
            current = current.next
        raise ValueError('Value not found in the list')

    def count(self, x):
        current = self.head
        count = 0
        while current is not None:
            if current.val == x:
                count += 1
            current = current.next
        return count

    def extend(self, other):
        self.tail.next = other.head
        self.tail = other.tail
        self.size += other.size

    def pop(self, index=None):
        if index is None:
            index = self.size - 1
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range')
        if index == 0:
            value = self.head.val
            self.head = self.head.next
            self.size -= 1
            return value
        current = self.head
        for i in range(index - 1):
            current = current.next
        value = current.next.val
        current.next = current.next.next
        self.size -= 1
        return value

    def copy(self):
        new_list = SingleLinkList()
        current = self.head
        while current is not None:
            new_list.append(current.val)
            current = current.next
        return new_list

    def __add__(self, other):
        new_list = self.copy()
        new_list.extend(other)
        return new_list

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        if self.size != other.size:
            return False
        current1 = self.head
        current2 = other.head
        while current1 is not None:
            if current1.val != current2.val:
                return False
            current1 = current1.next
            current2 = current2.next
        return True

    def __ne__(self, other):
        return not self == other

    def __contains__(self, x):
        current = self.head
        while current is not None:
            if current.val == x:
                return True
            current = current.next
        return False

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.val
        self.current = self.current.next
        return value

    def __reversed__(self):
        return self[::-1]

    def __bool__(self):
        return self.size > 0

    @classmethod
    def from_iterable(cls, iterable):
        new_list = cls()
        for x in iterable:
            new_list.append(x)
        return new_list

    def to_list(self):
        return [x for x in self]

class DoubleLinkList(SingleLinkList):
    def __init__(self):
        super().__init__()

    def append(self, x):
        new_node = ListNode(x)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def insert(self, index, x):
        if index < 0 or index > self.size:
            raise IndexError('Index out of range')
        new_node = ListNode(x)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
        self.size += 1

    def remove(self, x):
        current = self.head
        if current.val == x:
            self.head = current.next
            self.head.prev = None
            self.size -= 1
            return
        while current.next is not None:
            if current.next.val == x:
                current.next = current.next.next
                if current.next is not None:
                    current.next.prev = current
                self.size -= 1
                return
            current = current.next
        raise ValueError('Value not found in the list')

    def reverse(self):
        current = self.head
        self.head, self.tail = self.tail, self.head
        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev

    def pop(self, index=None):
        if index is None:
            index = self.size - 1
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range')
        if index == 0:
            value = self.head.val
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            self.size -= 1
            return value
        current = self.head
        for i in range(index - 1):
            current = current.next
        value = current.next.val
        current.next = current.next.next
        if current.next is not None:
            current.next.prev = current
        self.size -= 1
        return value

    def copy(self):
        new_list = DoubleLinkList()
        current = self.head
        while current is not None:
            new_list.append(current.val)
            current = current.next
        return new_list

    def __reversed__(self):
        return self[::-1]

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.val
        self.current = self.current.next
        return value
