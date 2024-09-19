# Welcome to pplox

pplox is a pure Python implementation of the Lox programming language from Robert Nystrom's [Crafting Interpreters](https://craftinginterpreters.com/).
This project was developed using additional material and automated test cases provided by CodeCrafters.
Alongside the interpreter, this also includes continuous integration and continuous deployment using GitHub Actions for automated testing and release.

We have two primary pipelines defined in `cicd.yml` and `pr.yml`.

- `cicd.yml` runs on merges to the master branch and tag pushes.
    - This is responsible for building and deploying our package to PyPI.

- `pr.yml` runs on pull requests.
    - This runs all of our pre-merge checks. If any of these fails then merging is blocked.

Since we want to check our code on both PRs to main and after merging, we use GitHub Actions' reusable workflows to share duplicate checks between both pipelines

## Usage

To use this project, we provide a `pip` package which you can install using `pip install pplox`. 

To use the tokenizer run `pplox --tokenize <filename>`.
This reads the file and prints the tokens.

To use the parser use `pplox --parse <filename>`.
This prints out an abstract syntax tree of the file.

## API Usage

pplox provides a set of classes to interpret Lox code which may be used by other applications.
This section covers the classes and their public APIs.
We first cover the main classes used in the interpreter pipeline: `Scanner`, `Parser`, `Interpreter`.
These classes use a set of helper classes to represent intermediate data: `Token`, `Stmt`.
We describe these classes next.

A minimal example of a Lox interpreter is
```py
from pplox.scanner import Scanner
from pplox.parser import Parser
from pplox.interpreter import Interpreter

scanner = Scanner('print "Hello world";')
tokens = scanner.scan_tokens()
parser = Parser(tokens)
statements = parser.parse()
interpreter = Interpreter()
interpreter.interpret(statements)
```

### `pplox.scanner`

To use the scanner import the `scanner` module using `import pplox.scanner`, this provides the Scanner class.

#### `Scanner(self, source: str)`

Constructs a scanner over the Lox source code in the string `source`.

#### `Scanner.scan_tokens(self) -> list[Token]`

Scans the source and returns a list of tokens representing the source.

### `pplox.parser`
 
Use it with `import pplox.parser`.

#### `Parser(self, tokens: list[Token])`

Constructs a parser which parses `tokens`.

#### `Parser.parse(self) -> list[Stmt]`

Parses the tokens and returns a list of statements representing a parse tree.

### `pplox.interpreter`

Import this with `import pplox.interpreter`.

#### `Interpreter(self)`

Constructs an interpreter with its own set of variables.
Variables are not shared across different instances of `Interpreter`.

#### `Interpeter.interpret(self, statements: list[Stmt])`

Interprets the Lox program represented by `statements`.
The output of `print` statements are directed to stdout.

### `pplox.token`

This module contains a token class which represents all source code in Lox as chunks of characters for the parser.

#### `Token(self, type: TokenType, lexeme: str, literal: any, line: int)`

Constructs a token of type `type` with source code representation `lexeme` and literal value `literal` on line `line`.
For more information on token types, see `token_type.py`

### `pplox.stmt`

The `stmt` module handles statements which is a tree representation of the source code.

#### `Stmt(self)`

This is the abstract base class which represents all statements.

## Project Layout

    .github/workflows/            
        cicd.yml                  # The CI/CD configuration pipeline
        pr.yml                    # The pre-merge checks that run on pull requests that must pass before merging
        ...                       # The reusable workflows 
    pplox/
        cli.py                    # The command-line interface
        ...                       # The interpreter implementation
    test_scanner.py               # Test for the scanner
    docs/                         # Project documentation

## Build Pipeline

We have build pipelines set up to publish every push to [TestPyPI](https://test.pypi.org/project/pplox/) and every tag to [PyPI](https://pypi.org/project/pplox/).

## Developing

If you want to contribute, the source code is hosted on [https://github.com/karlcaga/pplox](https://github.com/karlcaga/pplox).
Clone the repo with `git@github.com:karlcaga/pplox.git`.
Report bugs to [https://github.com/karlcaga/pplox/issues](https://github.com/karlcaga/pplox/issues).
