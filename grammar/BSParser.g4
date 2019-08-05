parser grammar BSParser;

options { tokenVocab=BSLexer; }

@parser::header {/* parser/listener/visitor header section */}
// Appears before any #include in h + cpp files.
@parser::preinclude {/* parser precinclude section */}
// Directly preceeds the parser class declaration in the h file (e.g. for additional types etc.).
@parser::context {/* parser context section */}
// Appears in the public part of the parser in the h file.
@parser::declarations {/* private parser declarations section */}
// Appears in line with the other class member definitions in the cpp file.
@parser::definitions {/* parser definitions section */}

@parser::listenerpreinclude{}
@parser::listenerpostinclude{}
@parser::listenerdeclarations{}
@parser::listenermembers{}
@parser::listenerdefinitions{}
@parser::baselistenerpreinclude{}
@parser::baselistenerpostinclude{}
@parser::baselistenerdeclarations{}
@parser::baselistenermembers{}
@parser::baselistenerdefinitions{}
@parser::visitorpreinclude{}
@parser::visitorpostinclude{}
@parser::visitordeclarations{}
@parser::visitormembers{}
@parser::visitordefinitions{}
@parser::basevisitorpreinclude{}
@parser::basevisitorpostinclude{}
@parser::basevisitordeclarations{}
@parser::basevisitormembers{}
@parser::basevisitordefinitions{}

program
    : (globalDeclarations )+
    functions?
    INSTRUCTIONS COLON
    ( statements )*
    EOF
    ;

/******************************************
 * Header declaration information
******************************************/
globalDeclarations
    : moduleDeclaration
    | manifestDeclaration
    | stationaryDeclaration
    ;

moduleDeclaration
    : MODULE IDENTIFIER
    ;

manifestDeclaration
    : MANIFEST IDENTIFIER
    ;

stationaryDeclaration
    : STATIONARY IDENTIFIER
    ;

/******************************************
 * Function Declaration
******************************************/
functions
    : FUNCTIONS COLON
      functionDeclaration+
    ;

functionDeclaration
    : FUNCTION IDENTIFIER formalParameters ( functionTyping )? LBRACE
            ( statements )*
            returnStatement
     RBRACE
    ;

formalParameters
    : LPAREN (formalParameterList)? RPAREN
    ;

formalParameterList
    :  formalParameter (COMMA formalParameter)*
    ;

/******************************************
This has to be an identifier, because it
doesn't make sense to define: x[3] as a
parameter to a function.
******************************************/
formalParameter
    : (unionType)? IDENTIFIER
    ;

// TODO: make mat an id and repeatable
functionTyping
    : COLON unionType
    ;

// This is mandatory so that we can
// force the translation into an assignment.
returnStatement
    : RETURN primary
    | RETURN methodCall
    ;

/******************************************
 * Statements
******************************************/
blockStatement
    : LBRACE ( statements )* RBRACE
    ;

statements
    : ifStatement
    | whileStatement
    | variableDefinition
    | repeat
    | heat
    | dispose
    | mix
    | dispense
    | split
    | methodInvocation
    | gradient
    | detect
    | store
    | math
    | numberAssignment
    ;

ifStatement
    : IF parExpression blockStatement (ELSE blockStatement )?
    ;

whileStatement
    : WHILE parExpression blockStatement
    ;

repeat
    : REPEAT INTEGER_LITERAL TIMES blockStatement
    ;

heat
    : HEAT variable AT temperatureIdentifier (FOR timeIdentifier)?
    ;

dispose
    : DRAIN variable
    | DISPOSE variable
    ;

mix
    : variableDefinition MIX variable WITH variable (FOR timeIdentifier)?
    ;

/********************************************************
The first one is intentionally an IDENTIFIER.  It has
to be a module, thus it cannot be indexed as an array.
********************************************************/
detect
    : variableDefinition DETECT IDENTIFIER ON variable (FOR timeIdentifier)?
    ;

split
    : variableDefinition SPLIT variable INTO INTEGER_LITERAL
    ;

/********************************************************
You can only dispense a global variable.  Thus, it has no
indexing capabilities.  Hence the identifier.
********************************************************/
dispense
    : variableDefinition DISPENSE IDENTIFIER
    ;

gradient
    : variableDefinition GRADIENT variable WITH variable RANGE FLOAT_LITERAL COMMA FLOAT_LITERAL AT FLOAT_LITERAL
    ;

store
    : STORE variable
    ;
/******************************************
 * Expressions
******************************************/
numberAssignment
    : variableDefinition literal
    ;

math
    : variableDefinition primary bop=(MULTIPLY | DIVIDE | '%') primary
    | variableDefinition primary bop=(ADDITION | SUBTRACT) primary
    ;

binops
    : primary (LT LT | GT GT GT | GT GT) primary
    | primary bop=(LTE | GTE | GT | LT) primary
    | primary bop=(EQUALITY | NOTEQUAL) primary
    ;

parExpression
    : LPAREN binops((AND | OR) binops)* RPAREN
    ;
/******************************************
 * Method Call
******************************************/
methodInvocation
    : variableDefinition methodCall
    ;

methodCall
    : IDENTIFIER LPAREN ( expressionList )? RPAREN
    ;

expressionList
    : primary (COMMA primary)*
    ;


/******************************************
 * Variables and Accounting
******************************************/
// If you want to inlcude an array of types:
// https://github.com/jar/grammars-v4/blob/master/java/JavaParser.g4#L582
typeType
    : primitiveType
    ;

unionType
    : LBRACKET typesList RBRACKET
    ;

typesList
    : typeType (SEMICOLON typeType)*
    ;

variableDefinition
    : (unionType)? variable ASSIGN
    ;

variable
    : IDENTIFIER(LBRACKET INTEGER_LITERAL RBRACKET)?
    ;

primary
    : literal
    | variable
    ;

literal
    : INTEGER_LITERAL
    | FLOAT_LITERAL
    | BOOL_LITERAL
    | STRING_LITERAL
    ;

primitiveType
 : BOOL
 | NAT
 | REAL
 | MAT
 ;

timeIdentifier
    : TIME_NUMBER
    ;

temperatureIdentifier
    : TEMP_NUMBER
    ;