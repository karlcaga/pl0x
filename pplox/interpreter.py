from .expr import Visitor 

def to_string(val):
    if val is None:
        return 'nil'
    if isinstance(val, bool):
        if val:
            return 'true'
        return 'false'
    return str(val)

class Interpreter(Visitor):
    def evaluate(self, expr):
        return expr.accept(self)
    
    def visit_literal(self, expr):
        return expr.value   
    