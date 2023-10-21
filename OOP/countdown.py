class Counter:
    
    def __init__(self):
        self.value = 0
        
    def incr(self):
        self.value += 1

    def decr(self):
        self.value -= 1

    def incrby(self,n):
        self.value += n

    def decrby(self,n):
        self.value -= n
        
    def show(self):
        print(self.value)
        
obj = Counter()
obj.show()

obj.incr()
obj.show()

obj.decr()
obj.show()

obj.incrby(5)
obj.show()

obj.decrby(5)
obj.show()

