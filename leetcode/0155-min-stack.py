class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        item = Item(val)
        if len(self.stack) > 0:
            item.min = min(item.min, self.stack[-1].min)
        
        self.stack.append(item)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[-1].min


    def __str__(self) -> str:
        return ','.join(str(item) for item in self.stack)
    
    def __iter__(self):
        for p in self.stack:
            yield p
        

class Item:
    
    def __init__(self, val):
        self.val = val
        self.min = val
    
    def __str__(self) -> str:
        return f'{self.val}'


if __name__ == "__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(4)
    obj.push(5)
    obj.push(2)
    obj.push(6)    
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()

    print(obj)
    print(param_3)
    print(param_4)

    for item in obj:
        print(f'min for each item is: {item.min}')
