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
STORE:          'store';
RANGE:          'range';

// Other Keywords
AT:             'at';
WITH:           'with';
FOR:            'for';
INTO:           'into';
TIMES:          'times';
ON:             'on';
OF:             'of';
UNITS:          'units';
USEIN:          'usein';

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
ATSIGN:             '@';

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

ACIDS_STRONG_NON_OXIDIZING: '1';
ACIDS_STRONG_OXIDIZING: '2';
ACIDS_CARBOXYLIC: '3';
ALCOHOLS_AND_POLYOLS: '4';
ALDEHYDES: '5';
AMIDES_AND_IMIDES: '6';
AMINES_PHOSPHINES_AND_PYRIDINES: '7';
AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS: '8';
CARBAMATES: '9';
BASES_STRONG: '10';
CYANIDES_INORGANIC: '11';
THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS: '12';
ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS: '13';
ETHERS: '14';
FLUORIDES_INORGANIC: '15';
HYDROCARBONS_AROMATIC: '16';
HALOGENATED_ORGANIC_COMPOUNDS: '17';
ISOCYANATES_AND_ISOTHIOCYANATES: '18';
KETONES: '19';
SULFIDES_ORGANIC: '20';
METALS_ALKALI_VERY_ACTIVE: '21';
METALS_ELEMENTAL_AND_POWDER_ACTIVE: '22';
METALS_LESS_REACTIVE: '23';
METALS_AND_METAL_COMPOUNDS_TOXIC: '24';
DIAZONIUM_SALTS: '25';
NITRILES: '26';
NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC: '27';
HYDROCARBONS_ALIPHATIC_UNSATURATED: '28';
HYDROCARBONS_ALIPHATIC_SATURATED: '29';
PEROXIDES_ORGANIC: '30';
PHENOLS_AND_CRESOLS: '31';
SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC: '32';
SULFIDES_INORGANIC: '33';
EPOXIDES: '34';
METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES: '35';
ANHYDRIDES: '37';
SALTS_ACIDIC: '38';
SALTS_BASIC: '39';
ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES: '40';
ORGANOMETALLICS: '42';
OXIDIZING_AGENTS_STRONG: '44';
REDUCING_AGENTS_STRONG: '45';
NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS: '46';
FLUORINATED_ORGANIC_COMPOUNDS: '47';
FLUORIDE_SALTS_SOLUBLE: '48';
OXIDIZING_AGENTS_WEAK: '49';
REDUCING_AGENTS_WEAK: '50';
NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES: '51';
CHLOROSILANES: '55';
SILOXANES: '58';
HALOGENATING_AGENTS: '59';
ACIDS_WEAK: '60';
BASES_WEAK: '61';
CARBONATE_SALTS: '62';
ALKYNES_WITH_ACETYLENIC_HYDROGEN: '63';
ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN: '64';
CONJUGATED_DIENES: '65';
ARYL_HALIDES: '66';
AMINES_AROMATIC: '68';
NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC: '69';
ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS: '70';
ACRYLATES_AND_ACRYLIC_ACIDS: '71';
PHENOLIC_SALTS: '72';
QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS: '73';
SULFITE_AND_THIOSULFATE_SALTS: '74';
OXIMES: '75';
POLYMERIZABLE_COMPOUNDS: '76';
NOT_CHEMICALLY_REACTIVE: '98';
INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION: '99';
WATER_AND_AQUEOUS_SOLUTIONS: '100';
NULL: '134';
UNKNOWN: '-1';


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
