from pplox.parser import Parser 
from pplox.scanner import Scanner
from pplox.interpreter import Interpreter

def evaluate(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    return Interpreter().evaluate(parser.parse())

def test_true_false_nil():
    assert evaluate('true') == True
    assert evaluate('false') == False
    assert evaluate('nil') is None
