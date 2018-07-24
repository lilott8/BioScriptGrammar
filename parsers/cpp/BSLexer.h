
// Generated from /Users/jason/Projects/java/BSPrototype/src/main/resources/BSLexer.g4 by ANTLR 4.7

#pragma once


#include "antlr4-runtime.h"




class  BSLexer : public antlr4::Lexer {
public:
  enum {
    IF = 1, ELSE = 2, REPEAT = 3, WHILE = 4, FUNCTION = 5, RETURN = 6, MANIFEST = 7, 
    MODULE = 8, STATIONARY = 9, FUNCTIONS = 10, INSTRUCTIONS = 11, DETECT = 12, 
    MIX = 13, SPLIT = 14, HEAT = 15, DRAIN = 16, DISPENSE = 17, DISPOSE = 18, 
    AT = 19, WITH = 20, FOR = 21, INTO = 22, TIMES = 23, ON = 24, OF = 25, 
    NAT = 26, REAL = 27, MAT = 28, BOOL = 29, IDENTIFIER = 30, STRING_LITERAL = 31, 
    BOOL_LITERAL = 32, FLOAT_LITERAL = 33, INTEGER_LITERAL = 34, TIME_NUMBER = 35, 
    VOLUME_NUMBER = 36, TEMP_NUMBER = 37, LPAREN = 38, RPAREN = 39, LBRACE = 40, 
    RBRACE = 41, LBRACKET = 42, RBRACKET = 43, SEMICOLON = 44, COMMA = 45, 
    DOT = 46, ASSIGN = 47, GT = 48, LT = 49, BANG = 50, TILDE = 51, QUESTION = 52, 
    COLON = 53, EQUALITY = 54, LTE = 55, GTE = 56, NOTEQUAL = 57, AND = 58, 
    OR = 59, INC = 60, DEC = 61, ADDITION = 62, SUBTRACT = 63, MULTIPLY = 64, 
    DIVIDE = 65, BITAND = 66, BITOR = 67, CARET = 68, MOD = 69, UNDERSCORE = 70, 
    NANOSECOND = 71, MICROSECOND = 72, MILLISECOND = 73, CENTISECOND = 74, 
    DECISECOND = 75, SECOND = 76, HOUR = 77, DAY = 78, WEEK = 79, MONTH = 80, 
    YEAR = 81, NANOLITRE = 82, MICROLITRE = 83, MILLILITRE = 84, CENTILITRE = 85, 
    DECILITRE = 86, LITRE = 87, DECALITRE = 88, CELSIUS = 89, FAHRENHEIT = 90, 
    KELVIN = 91, WS = 92, COMMENT = 93, LINE_COMMENT = 94
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

