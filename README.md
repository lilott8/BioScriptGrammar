# BioScriptGrammar
This is the grammar defining BioScript

### Requirements:

Python3 (`apt-get install python3`), and antlr

Follow instructions to install antlr and set up your path here: https://github.com/antlr/antlr4/blob/master/doc/getting-started.md


### Configuration

Configure this such that:

1) `output directory`: path/to/parser/[language]
2) `language`: `Cpp` | `Python3`

Note: cpp has been deprecated

### Usage

`antlr4 -o [/path/to/output] -package [package\_name] -Dlanguage=[Cpp | Python3] -listener -visitor -lib [/path/to/grammar] [/path/to/Parser.g4] [/path/to/Lexer.g4]`
