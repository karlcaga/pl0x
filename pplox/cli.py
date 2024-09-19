#!/usr/bin/env python
import sys
import argparse
from .scanner import Scanner
from .parser import Parser, ParseError
from .ast_printer import AstPrinter
from .interpreter import Interpreter
from .interpreter_error import InterpreterError

def main():
    parser = argparse.ArgumentParser(
        prog='pplox',
        description='A Lox interpreter',
    )
    parser.add_argument('filename')           
    parser.add_argument('-t', '--tokenize', action='store_true')
    parser.add_argument('-p', '--parse', action='store_true')
    args = parser.parse_args()

    with open(args.filename) as file:
        file_contents = file.read()
    
    if args.tokenize or args.parse:
        scanner = Scanner(file_contents)
        tokens = scanner.scan_tokens()
        for token in tokens:
            print(token.to_string())
        if args.parse:
            parser = Parser(tokens)
            AstPrinter().print(parser.parse())
    else:
        scanner = Scanner(file_contents)
        tokens = scanner.scan_tokens()
        try:
            parser = Parser(tokens)
            statements = parser.parse()
            if statements:
                try:
                    Interpreter().interpret(statements)
                except InterpreterError as e:
                    print(e, file = sys.stderr)
                    exit(70)
        except ParseError:
            exit(65)

if __name__ == "__main__":
    main()
