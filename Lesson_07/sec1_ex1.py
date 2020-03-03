# ex 1

class Query(object):
    def __init__(self, classification=None, justification=None, selector=None):
        self.classification = classification
        self.justification = justification
        self.selector = selector
    def __str__(self):
        return f"Class: {self.classification} Just: {self.justification} Select: {self.selector}"

