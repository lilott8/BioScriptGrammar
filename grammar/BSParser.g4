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
    : moduleDeclaration
        stationaryDeclaration
        manifestDeclaration
        FUNCTIONS COLON
        (functionDeclaration)*
        INSTRUCTIONS COLON
        ( statements )*
        EOF
    ;

/******************************************
 * Header declaration information
******************************************/
moduleDeclaration
    : ( MODULE IDENTIFIER )*
    ;

manifestDeclaration
    : ( MANIFEST IDENTIFIER )+
    ;

stationaryDeclaration
    : ( STATIONARY IDENTIFIER )*
    ;

/******************************************
 * Function Declaration
******************************************/
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

formalParameter
    : (unionType)? IDENTIFIER (LBRACKET RBRACKET)?
    ;

// TODO: make mat an id and repeatable
functionTyping
    : COLON unionType
    ;

// This is mandatory so that we can
// force the translation into an assignment.
returnStatement
    : RETURN IDENTIFIER
    | RETURN literal
    | RETURN methodCall
    ;

/******************************************
 * Statements
******************************************/
blockStatement
    : LBRACE ( statements )* RBRACE
    ;

materialAssignmentOperations
    : mix
    | dispense
    | split
    | methodCall
    ;

materialArrayAssignmentOperations
    : dispense
    | split
    | methodCall
    ;

numericAssignmentOperations
    : expression
    | detect
    | methodCall
    ;

statements
    : ifStatement
    | whileStatement
    | materialDeclaration
    | numericDeclaration
    | repeat
    | heat
    | dispose
    ;

ifStatement
    : IF parExpression blockStatement (ELSE blockStatement )?
    ;

whileStatement
    : WHILE parExpression blockStatement
    ;

repeat
    : REPEAT (IDENTIFIER | INTEGER_LITERAL) TIMES blockStatement
    ;

mix
    : MIX volumeIdentifier WITH volumeIdentifier (FOR timeIdentifier)?
    ;

detect
    : DETECT IDENTIFIER ON IDENTIFIER (FOR timeIdentifier)?
    ;

heat
    : HEAT IDENTIFIER AT temperatureIdentifier (FOR timeIdentifier)?
    ;

split
    : SPLIT IDENTIFIER INTO INTEGER_LITERAL
    ;

dispense
    : DISPENSE IDENTIFIER
    ;

dispose
    : DRAIN IDENTIFIER
    | DISPOSE IDENTIFIER
    ;

/******************************************
 * Expressions
******************************************/
expression
    : primary
    | expression LBRACKET expression RBRACKET
    | expression bop=(MULTIPLY | DIVIDE |'%') expression
    | expression bop=(ADDITION | SUBTRACT) expression
    | expression (LT LT | GT GT GT | GT GT) expression
    | expression bop=(LTE | GTE | GT | LT) expression
    | expression bop=(EQUALITY | NOTEQUAL) expression
    | expression bop=AND expression
    | expression bop=OR expression
    ;

parExpression
    : LPAREN expression RPAREN
    ;
/******************************************
 * Method Call
******************************************/
methodCall
    : IDENTIFIER LPAREN ( expressionList )? RPAREN
    ;

expressionList
    : expression (COMMA expression)*
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

numericDeclaration
    : (unionType)? IDENTIFIER ASSIGN numericAssignmentOperations
    ;

materialDeclaration
    // Inferred from size of identifiers.
    : (unionType)? IDENTIFIER (COMMA IDENTIFIER)* ASSIGN split
    // Inferred size from split.
    | (unionType)? IDENTIFIER LBRACKET RBRACKET ASSIGN split
    // Defaults to INTEGER_LITERAL.
    | (unionType)? IDENTIFIER LBRACKET INTEGER_LITERAL RBRACKET ASSIGN materialArrayAssignmentOperations
    // Defaults to 1.
    | (unionType)? IDENTIFIER ASSIGN materialAssignmentOperations
    ;

primary
    : LPAREN expression RPAREN
    | literal
    | IDENTIFIER
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

volumeIdentifier
    : ( VOLUME_NUMBER OF )? IDENTIFIER
    ;

timeIdentifier
    : TIME_NUMBER
    ;

temperatureIdentifier
    : TEMP_NUMBER
    ;