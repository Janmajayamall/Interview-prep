class Cache():
    
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None


class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.current_cap=0
        self.hash_map=dict()
        self.head = Cache(None, None)
        self.tail = Cache(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if self.hash_map.get(key):
            ref = self.hash_map.get(key)
            
            ref.prev.next = ref.next
            ref.next.prev = ref.prev
            
            ref.next = self.head.next
            ref.prev = self.head
            self.head.next.prev = ref
            self.head.next = ref
            
            return ref.val
            
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if self.hash_map.get(key):
            ref = self.hash_map.get(key)
            
            ref.val = value
            ref.prev.next = ref.next
            ref.next.prev = ref.prev
            
            ref.next = self.head.next
            ref.prev = self.head
            self.head.next.prev = ref
            self.head.next = ref
            self.hash_map[key]=ref

        
        else:
        
            if self.current_cap>=self.capacity:
                del self.hash_map[self.tail.prev.key]
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
                self.current_cap-=1

            self.current_cap+=1
            newCache = Cache(key, value)
            newCache.next = self.head.next 
            newCache.prev = self.head
            self.head.next.prev = newCache
            self.head.next = newCache
            self.hash_map[key]=newCache


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)