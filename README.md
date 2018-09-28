# BioScriptGrammar
This is the grammar defining BioScript

### Configuration

Configure this such that:
    1) `output directory`: path/to/parser/[language]
    2) `language`: `Cpp` | `Python3`

usage: `antlr4 -o [/path/to/output] -package [package\_name] -Dlanguage=[Cpp | Python3] -listener -visitor -lib [/path/to/grammar] [/path/to/Parser.g4] [/path/to/Lexer.g4]`
