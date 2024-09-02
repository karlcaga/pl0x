
class Visitor:
    def visit_print(self, stmt):
        ...

    def visit_expression(self, stmt):
        ...
    
    def visit_var(self, stmt):
        ...

class Stmt:
    def accept(self, visitor):
        ...

class Var(Stmt):
    def __init__(self, name, initializer):
        self.name = name
        self.initializer = initializer

    def accept(self, visitor):
        return visitor.visit_var(self)
    
class Expression(Stmt):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visit_expression(self)

class Print(Stmt):
    def __init__(self, expression):
        self.expression = expression
    
    def accept(self, visitor):
        return visitor.visit_print(self)
