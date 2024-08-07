class Queue:
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        return str(self.queue)
        
    def addq(self, v):
        self.queue.append(v)
        
    def isempty(self):
        return self.queue == []
    
    def deq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
