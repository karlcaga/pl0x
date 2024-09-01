from .expr import Visitor 
from .token_type import TokenType

def to_string(val):
    if val is None:
        return 'nil'
    if isinstance(val, bool):
        if val:
            return 'true'
        return 'false'
    if isinstance(val, float):
        text = str(val)
        if text.endswith(".0"):
            text = text[:-2]
        return text
    return str(val)

class Interpreter(Visitor):
    def evaluate(self, expr): 
        return expr.accept(self)
    
    def visit_literal(self, expr):
        return expr.value   
    
    def visit_grouping(self, expr):
        return self.evaluate(expr.expression)
    
    def visit_unary(self, expr):
        right = self.evaluate(expr.right)
        match expr.operator.type:
            case TokenType.MINUS:
                return -(float(right))
            case TokenType.BANG:
                return not self.is_truthy(right)

    def visit_binary(self, expr):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)
        match expr.operator.type:
            case TokenType.SLASH:
                return float(left) / float(right)
            case TokenType.STAR:
                return float(left) * float(right)
            case TokenType.MINUS:
                return float(left) - float(right)
            case TokenType.PLUS:
                return float(left) + float(right)
    
    def is_truthy(self, obj):
        if obj is None:
            return False
        if isinstance(obj, bool):
            return bool(obj)
        return True