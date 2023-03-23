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
    
def matcher(string) -> bool:
    s, d = Stack(), {"(" : ")",
                     "[" : "]",
                     "{" : "}"}

    for c in string:
        if c in d:
            s.push(c)
        else:
            try:
                if d[s.top()] == c:
                    s.pop()
            except:
                return False

    return s.is_empty()