from .expr import Visitor 
from .token_type import TokenType
from .interpreter_error import InterpreterError

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
                self.check_number_operand(expr.operator, right)
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
                if isinstance(left, float) and isinstance(right, float):
                    return float(left) + float(right)
                if isinstance(left, str) and isinstance(right, str):
                    return str(left) + str(right)
            case TokenType.GREATER:
                return float(left) > float(right)
            case TokenType.GREATER_EQUAL:
                return float(left) >= float(right)
            case TokenType.LESS:
                return float(left) < float(right)
            case TokenType.LESS_EQUAL:
                return float(left) <= float(right)
            case TokenType.BANG_EQUAL:
                return not self.is_equal(left, right)
            case TokenType.EQUAL_EQUAL:
                return self.is_equal(left, right)

    def check_number_operand(self, operator, operand):
        if isinstance(operand, float):
            return
        raise InterpreterError(operator, "Operand must be a number.")

    def is_equal(self, a, b):
        if a is None and b is None:
            return True
        if a is None:
            return False
        return a == b
    
    def is_truthy(self, obj):
        if obj is None:
            return False
        if isinstance(obj, bool):
            return bool(obj)
        return True