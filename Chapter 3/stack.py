class Stack(object):
    def __init__(self, element=None):
        self.elements = []
        if element is not None:
            self.elements.append(element)

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        else:
            return None

    def top(self):
        if not self.is_empty():
            return self.elements[-1]
        else:
            return None

    def is_empty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def reset(self):
        self.elements = []
