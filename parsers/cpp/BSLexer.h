
// Generated from /Users/jason/Projects/java/bioscriptgrammar/grammar/BSLexer.g4 by ANTLR 4.7

#pragma once


#include "antlr4-runtime.h"




class  BSLexer : public antlr4::Lexer {
public:
  enum {
    IF = 1, ELSE = 2, REPEAT = 3, WHILE = 4, FUNCTION = 5, RETURN = 6, MANIFEST = 7, 
    MODULE = 8, STATIONARY = 9, FUNCTIONS = 10, INSTRUCTIONS = 11, DETECT = 12, 
    MIX = 13, SPLIT = 14, HEAT = 15, DRAIN = 16, DISPENSE = 17, DISPOSE = 18, 
    GRADIENT = 19, STORE = 20, RANGE = 21, AT = 22, WITH = 23, FOR = 24, 
    INTO = 25, TIMES = 26, ON = 27, OF = 28, UNITS = 29, NAT = 30, REAL = 31, 
    MAT = 32, BOOL = 33, IDENTIFIER = 34, STRING_LITERAL = 35, BOOL_LITERAL = 36, 
    FLOAT_LITERAL = 37, INTEGER_LITERAL = 38, TIME_NUMBER = 39, VOLUME_NUMBER = 40, 
    TEMP_NUMBER = 41, LPAREN = 42, RPAREN = 43, LBRACE = 44, RBRACE = 45, 
    LBRACKET = 46, RBRACKET = 47, SEMICOLON = 48, COMMA = 49, DOT = 50, 
    ASSIGN = 51, GT = 52, LT = 53, BANG = 54, TILDE = 55, QUESTION = 56, 
    COLON = 57, EQUALITY = 58, LTE = 59, GTE = 60, NOTEQUAL = 61, AND = 62, 
    OR = 63, INC = 64, DEC = 65, ADDITION = 66, SUBTRACT = 67, MULTIPLY = 68, 
    DIVIDE = 69, BITAND = 70, BITOR = 71, CARET = 72, MOD = 73, UNDERSCORE = 74, 
    NANOSECOND = 75, MICROSECOND = 76, MILLISECOND = 77, CENTISECOND = 78, 
    DECISECOND = 79, SECOND = 80, MINUTE = 81, HOUR = 82, DAY = 83, WEEK = 84, 
    MONTH = 85, YEAR = 86, NANOLITRE = 87, MICROLITRE = 88, MILLILITRE = 89, 
    CENTILITRE = 90, DECILITRE = 91, LITRE = 92, DECALITRE = 93, CELSIUS = 94, 
    FAHRENHEIT = 95, KELVIN = 96, WS = 97, COMMENT = 98, LINE_COMMENT = 99
  };

  BSLexer(antlr4::CharStream *input);
  ~BSLexer();

  virtual std::string getGrammarFileName() const override;
  virtual const std::vector<std::string>& getRuleNames() const override;

  virtual const std::vector<std::string>& getChannelNames() const override;
  virtual const std::vector<std::string>& getModeNames() const override;
  virtual const std::vector<std::string>& getTokenNames() const override; // deprecated, use vocabulary instead
  virtual antlr4::dfa::Vocabulary& getVocabulary() const override;

  virtual const std::vector<uint16_t> getSerializedATN() const override;
  virtual const antlr4::atn::ATN& getATN() const override;

private:
  static std::vector<antlr4::dfa::DFA> _decisionToDFA;
  static antlr4::atn::PredictionContextCache _sharedContextCache;
  static std::vector<std::string> _ruleNames;
  static std::vector<std::string> _tokenNames;
  static std::vector<std::string> _channelNames;
  static std::vector<std::string> _modeNames;

  static std::vector<std::string> _literalNames;
  static std::vector<std::string> _symbolicNames;
  static antlr4::dfa::Vocabulary _vocabulary;
  static antlr4::atn::ATN _atn;
  static std::vector<uint16_t> _serializedATN;


  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.

  struct Initializer {
    Initializer();
  };
  static Initializer _init;
};

