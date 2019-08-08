lexer grammar BSLexer;

// Keywords

// Control flow
IF:             'if';
ELSE:           'else';
REPEAT:         'repeat';
WHILE:          'while';
FUNCTION:       'function';
RETURN:         'return';

// Declarations
MANIFEST:       'manifest';
MODULE:         'module';
STATIONARY:     'stationary';
FUNCTIONS:      'functions';
INSTRUCTIONS:   'instructions';

// Operations
DETECT:         'detect';
MIX:            'mix';
SPLIT:          'split';
HEAT:           'heat';
DRAIN:          'drain';
DISPENSE:       'dispense';
DISPOSE:        'dispose';
GRADIENT:       'gradient';

// Other Keywords
AT:             'at';
WITH:           'with';
FOR:            'for';
INTO:           'into';
TIMES:          'times';
ON:             'on';
OF:             'of';

// Typing
NAT:            'nat';
REAL:           'real';
MAT:            'mat';
BOOL:           'bool';




IDENTIFIER:         Letter LetterOrDigit*;

// Literals
STRING_LITERAL:     '"' (~["\\\r\n] | EscapeSequence)* '"';
BOOL_LITERAL:       'true'
            |       'false'
            ;
FLOAT_LITERAL:      (Digits '.' Digits? | '.' Digits);
INTEGER_LITERAL:    Digits ( Digits ) *;
TIME_NUMBER:        (FLOAT_LITERAL | INTEGER_LITERAL)TimeUnits;
VOLUME_NUMBER:      (FLOAT_LITERAL | INTEGER_LITERAL)VolumeUnits;
TEMP_NUMBER:        (FLOAT_LITERAL | INTEGER_LITERAL)TempUnits;
// Physics
MASS_NUMBER:               'mass';
EFFICIENCY_NUMBER:         'efficiency';
PRESSURE_NUMBER:           'pressure';
FORCE_NUMBER:              'force';
SPEED_NUMBER:              'speed';
FRICTION_NUMBER:           'friction';
USEBY:                     'useby';

//Physcs 2: Now with more physics:





// Separators
LPAREN:             '(';
RPAREN:             ')';
LBRACE:             '{';
RBRACE:             '}';
LBRACKET:           '[';
RBRACKET:           ']';
SEMICOLON:          ';';
COMMA:              ',';
DOT:                '.';

// Operators
ASSIGN:             '=';
GT:                 '>';
LT:                 '<';
BANG:               '!';
TILDE:              '~';
QUESTION:           '?';
COLON:              ':';
EQUALITY:           '==';
LTE:                '<=';
GTE:                '>=';
NOTEQUAL:           '!=';
AND:                '&&';
OR:                 '||';
INC:                '++';
DEC:                '--';
ADDITION:           '+';
SUBTRACT:           '-';
MULTIPLY:           '*';
DIVIDE:             '/';
BITAND:             '&';
BITOR:              '|';
CARET:              '^';
MOD:                '%';
UNDERSCORE:         '_';
AT_SYMBOL:          '@';

// Time and Volume Units
NANOSECOND:         'ns';
MICROSECOND:        'us';
MILLISECOND:        'ms';
CENTISECOND:        'cs';
DECISECOND:         'ds';
SECOND:             's';
MINUTE:             'm';
HOUR:               'h';
DAY:                'd';
WEEK:               'w';
MONTH:              'mo';
YEAR:               'y';
NANOLITRE:          'nL';
MICROLITRE:         'uL';
MILLILITRE:         'mL';
CENTILITRE:         'cL';
DECILITRE:          'dL';
LITRE:              'L';
DECALITRE:          'daL';
CELSIUS:            'c';
FAHRENHEIT:         'f';
KELVIN:             'k';



// Whitespace and comments
WS:                 [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT:            '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*    -> channel(HIDDEN);

fragment TimeUnits
    : NANOSECOND | MICROSECOND | MILLISECOND | CENTISECOND | DECISECOND | SECOND | MINUTE | HOUR | DAY | WEEK | MONTH | YEAR
    ;

fragment VolumeUnits
    : NANOLITRE | MICROLITRE | MILLILITRE | CENTILITRE | LITRE | DECALITRE
    ;

fragment TempUnits
    : FAHRENHEIT | CELSIUS | KELVIN
    ;

fragment Digits
    : [0-9] ([0-9_]* [0-9])?
    ;

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;

fragment Letter
    : [a-zA-Z$_] // these are the "java letters" below 0x7F
    | ~[\u0000-\u007F\uD800-\uDBFF] // covers all characters above 0x7F which are not a surrogate
    | [\uD800-\uDBFF] [\uDC00-\uDFFF] // covers UTF-16 surrogate pairs encodings for U+10000 to U+10FFFF
    ;

fragment EscapeSequence
    : '\\' [btnfr"'\\]
    | '\\' ([0-3]? [0-7])? [0-7]
    ;

fragment SPACES
 : [ \t]+
 ;

fragment NEWLINE
 : '\r'? '\n'
 | '\r'
 | '\f'
 ;
