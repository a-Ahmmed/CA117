class Queue():

    def __init__(self) -> None:
        self.l = []

    def enqueue(self, obj) -> None:
        self.l.append(obj)

    def dequeue(self):
        return self.l.pop(0)

    def first(self):
        return self.l[0]
    
    def is_empty(self) -> bool:
        return len(self.l) == 0
    
    def __len__(self) -> int:
        return len(self.l)