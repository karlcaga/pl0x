from .interpreter_error import InterpreterError

class Environment:
    def __init__(self):
        self.values = {}

    def define(self, name, value):
        self.values[name] = value

    def get(self, name):
        if name.lexeme in self.values:
            return self.values[name.lexeme] 
        
        raise InterpreterError(name, "Undefined variable '" + name.lexeme + "'.")