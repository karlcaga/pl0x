from lox.scanner import Scanner

def test_parens():
    scanner = Scanner("(()")
    tokens = scanner.scan_tokens()
    assert len(tokens) == 4
    assert tokens[0].to_string() == "LEFT_PAREN ( null"
    assert tokens[1].to_string() == "LEFT_PAREN ( null"
    assert tokens[2].to_string() == "RIGHT_PAREN ) null"
    assert tokens[3].to_string() == "EOF  null"
    
def test_empty_file():
    scanner = Scanner("")
    tokens = scanner.scan_tokens()
    assert len(tokens) == 1
    assert tokens[0].to_string() == "EOF  null"
