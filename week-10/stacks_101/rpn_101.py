from math import sqrt

class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

def calculator(rpn) -> float:
    binops = {'+': float.__add__,
                '-': float.__sub__,
                '*': float.__mul__,
                '/': float.__truediv__}

    uniops = {'n': float.__neg__,
                'r': sqrt}
    
    nums = Stack() 

    rpn = rpn.split()
    for obj in rpn:
        try:
            nums.push(float(obj))
        except:
            if obj in binops:
                f1, f2 = nums.pop(), nums.pop()
                nums.push(binops[obj](f2, f1))
            else:
                nums.push(uniops[obj](nums.pop()))

    return nums.top()