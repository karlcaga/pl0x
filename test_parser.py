from pplox.parser import Parser 
from pplox.scanner import Scanner
from pplox.expr import Literal

def parse(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    return parser.parse()

def test_boolean_nil():
    assert parse('true').value == Literal(True).value
    assert parse('false').value == Literal(False).value
    assert parse('nil').value == Literal(None).value

def test_number():
    assert parse("42.47").value == Literal(42.47).value

def test_string():
    assert parse('"hello"').value == Literal("hello").value

def test_paren():
    assert parse ('("foo")').expression.value == Literal("foo").value

def test_unary():
    result = parse("!true")
    assert result.operator.lexeme == "!"
    assert result.right.value == Literal(True).value

def test_binary():
    binary_test = parse("16 * 38")
    assert binary_test.operator.lexeme == "*"
    assert binary_test.left.value == Literal(16).value
    assert binary_test.right.value == Literal(38).value