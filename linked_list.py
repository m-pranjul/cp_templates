class Node:
    def __init__(self,val) -> None:
        self.data=val
        self.next=None

class deque:
    def __init__(self) -> None:
        pass

class array:
    def __init__(self,arr) -> None:
        self.arr=arr
    def append(self,val):
        self.arr.append(val)
    def array_concat(self,arr1,arr2):
        return self.arr1 + self.arr2
