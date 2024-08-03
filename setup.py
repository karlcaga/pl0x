from setuptools import setup

setup(
    name="pl0x",
    version="1.0",
    description="Interpreter for the Lox programming language",
    long_description="Interpreter for the Lox programming language from the Crafting Interpreters book",
    author="Karl Cagalawan",
    author_email="karl.cagalawan@gmail.com",
    url="https://www.github.com/karlcaga/pl0x",
    packages=["pl0x"],
    entry_points={
        "console_scripts": [
            "pl0x = pl0x.cli:main",
        ]
    },
)
