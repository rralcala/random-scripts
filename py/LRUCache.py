
class ListNode(object):
    def __init__(self, key, data, prev, next):
        self.data = data
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.index = {}

    def append(self, new_node):
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            new_node.next.prev = new_node
            self.head = new_node
        return new_node

    def remove_node(self, node):
        if self.head is None or node is None:
            return

        if self.head == node:
            self.head = node.next

        if self.tail == node:
            self.tail = node.prev

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.index:
            return -1
        self.back_to_front(key)

        return self.index[key].data

    def back_to_front(self, key):
        node = self.index[key]
        self.remove_node(node)
        self.append(node)


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.index:
            new_node = ListNode(key, value, None, None)
            self.index[key] = self.append(new_node)
            if len(self.index) > self.capacity:
                del self.index[self.tail.key]
                self.remove_node(self.tail)
        else:
            self.index[key].data = value
            self.back_to_front(key)

    def __str__(self):
        s = ""
        ptr = self.head
        while ptr is not None:
            s += "{} {} - ".format(ptr.key,ptr.data)
            ptr = ptr.next
        return s


if __name__ == '__main__':

    cache = LRUCache( 10 )


    op = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    par = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

    for i in range(len(op)):
        if op[i] == "put":
            print "put {} {}".format(par[i][0], par[i][1])
            cache.put(par[i][0], par[i][1])
        else:
            print "get {}".format(par[i][0])
            cache.get(par[i][0])
    '''
    cache.put(1, 1)
    cache.put(2, 2)
    print cache.get(1)       # returns 1
    cache.put(3, 3)    # evicts key 2
    print cache.get(2)       # returns -1 (not found)
    cache.put(4, 4)    # evicts key 1
    print cache.get(1)       # returns -1 (not found)
    print cache.get(3)       # returns 3
    print cache.get(4)       # returns 4
    '''