
// Generated from /bioscriptgrammar/grammar/BSLexer.g4 by ANTLR 4.7

#pragma once


#include "antlr4-runtime.h"




class  BSLexer : public antlr4::Lexer {
public:
  enum {
    IF = 1, ELSE = 2, REPEAT = 3, WHILE = 4, FUNCTION = 5, RETURN = 6, MANIFEST = 7,
    MODULE = 8, STATIONARY = 9, FUNCTIONS = 10, INSTRUCTIONS = 11, DETECT = 12,
    MIX = 13, SPLIT = 14, HEAT = 15, DRAIN = 16, DISPENSE = 17, DISPOSE = 18,
    GRADIENT = 19, STORE = 20, RANGE = 21, AT = 22, WITH = 23, FOR = 24,
    INTO = 25, TIMES = 26, ON = 27, OF = 28, NAT = 29, REAL = 30, MAT = 31,
    BOOL = 32, IDENTIFIER = 33, STRING_LITERAL = 34, BOOL_LITERAL = 35,
    FLOAT_LITERAL = 36, INTEGER_LITERAL = 37, TIME_NUMBER = 38, VOLUME_NUMBER = 39,
    TEMP_NUMBER = 40, LPAREN = 41, RPAREN = 42, LBRACE = 43, RBRACE = 44,
    LBRACKET = 45, RBRACKET = 46, SEMICOLON = 47, COMMA = 48, DOT = 49,
    ASSIGN = 50, GT = 51, LT = 52, BANG = 53, TILDE = 54, QUESTION = 55,
    COLON = 56, EQUALITY = 57, LTE = 58, GTE = 59, NOTEQUAL = 60, AND = 61,
    OR = 62, INC = 63, DEC = 64, ADDITION = 65, SUBTRACT = 66, MULTIPLY = 67,
    DIVIDE = 68, BITAND = 69, BITOR = 70, CARET = 71, MOD = 72, UNDERSCORE = 73,
    NANOSECOND = 74, MICROSECOND = 75, MILLISECOND = 76, CENTISECOND = 77,
    DECISECOND = 78, SECOND = 79, MINUTE = 80, HOUR = 81, DAY = 82, WEEK = 83,
    MONTH = 84, YEAR = 85, NANOLITRE = 86, MICROLITRE = 87, MILLILITRE = 88,
    CENTILITRE = 89, DECILITRE = 90, LITRE = 91, DECALITRE = 92, CELSIUS = 93,
    FAHRENHEIT = 94, KELVIN = 95, WS = 96, COMMENT = 97, LINE_COMMENT = 98
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

