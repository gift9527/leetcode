class LinkNode(object):
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRU_CACHE(object):
    def __init__(self, capacity):
        self.key_dict = {}
        self.head = LinkNode(0, 0)
        self.tail = LinkNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key):
        if key in self.key_dict:
            n = self.key_dict[key]
            self.remove(n)
            self.add_back(n)
            return n.val
        return -1


    def set(self, key, value):
        if key in self.key_dict:
            self.remove(self.key_dict[key])
        n = LinkNode(key,value)
        self.add_back(n)
        self.key_dict[key] = n

        if len(self.key_dict) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.key_dict[n.key]


    def remove(self,node):
        p = node.prev
        q = node.next
        p.next = q
        q.prev = p


    def add_back(self,node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail