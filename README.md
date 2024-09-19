Interpreter for the Lox programming language.

This project was developed as our solution to the CodeCrafters Build-Your-Own-Interpreter challenge with a focus on the developer experience.
With this in mind, `pplox` was developed as a pure Python port of [`jlox`](https://github.com/munificent/craftinginterpreters/tree/master/java/com/craftinginterpreters) written in Java from Robert Nystrom's [Crafting Interpreters](https://craftinginterpreters.com/). 
See the [documentation](https://pplox.readthedocs.io/en/latest/) for more details on the GitHub Actions workflows we used to develop this interpreter.

# Getting Started

`pip install pplox`

Create your lox file. For example, `hello_world.lox` 

```
print "Hello world"
```

Tokenize the file with `pplox --tokenize hello_world.lox`.

Parse the file with `pplox --parse hello_world.lox`.

# Library Usage
pplox can also be used as a library in your own Python projects.
For example, if you want to implement your own Lox interpreter but want to skip writing the scanner, you can use pplox' scanner like so:
```python
from pplox.scanner import Scanner

scanner = Scanner('print "Hello world"')
tokens = scanner.scan_tokens()
```
This gives you a list of tokens to be parsed and interpreted.

For a minimal interpreter
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

See https://github.com/karlcaga/pplox_web/ for an example application of pplox being used as a library.