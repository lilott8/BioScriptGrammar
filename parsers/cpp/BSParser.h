/* parser/listener/visitor header section */

// Generated from /bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.7

#pragma once

/* parser precinclude section */

#include "antlr4-runtime.h"



/* parser context section */

class  BSParser : public antlr4::Parser {
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
    FAHRENHEIT = 95, KELVIN = 96, ACIDS_STRONG_NON_OXIDIZING = 97, ACIDS_STRONG_OXIDIZING = 98,
    ACIDS_CARBOXYLIC = 99, ALCOHOLS_AND_POLYOLS = 100, ALDEHYDES = 101,
    AMIDES_AND_IMIDES = 102, AMINES_PHOSPHINES_AND_PYRIDINES = 103, AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS = 104,
    CARBAMATES = 105, BASES_STRONG = 106, CYANIDES_INORGANIC = 107, THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS = 108,
    ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS = 109,
    ETHERS = 110, FLUORIDES_INORGANIC = 111, HYDROCARBONS_AROMATIC = 112,
    HALOGENATED_ORGANIC_COMPOUNDS = 113, ISOCYANATES_AND_ISOTHIOCYANATES = 114,
    KETONES = 115, SULFIDES_ORGANIC = 116, METALS_ALKALI_VERY_ACTIVE = 117,
    METALS_ELEMENTAL_AND_POWDER_ACTIVE = 118, METALS_LESS_REACTIVE = 119,
    METALS_AND_METAL_COMPOUNDS_TOXIC = 120, DIAZONIUM_SALTS = 121, NITRILES = 122,
    NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC = 123, HYDROCARBONS_ALIPHATIC_UNSATURATED = 124,
    HYDROCARBONS_ALIPHATIC_SATURATED = 125, PEROXIDES_ORGANIC = 126, PHENOLS_AND_CRESOLS = 127,
    SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC = 128, SULFIDES_INORGANIC = 129,
    EPOXIDES = 130, METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES = 131,
    ANHYDRIDES = 132, SALTS_ACIDIC = 133, SALTS_BASIC = 134, ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES = 135,
    ORGANOMETALLICS = 136, OXIDIZING_AGENTS_STRONG = 137, REDUCING_AGENTS_STRONG = 138,
    NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS = 139, FLUORINATED_ORGANIC_COMPOUNDS = 140,
    FLUORIDE_SALTS_SOLUBLE = 141, OXIDIZING_AGENTS_WEAK = 142, REDUCING_AGENTS_WEAK = 143,
    NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES = 144, CHLOROSILANES = 145,
    SILOXANES = 146, HALOGENATING_AGENTS = 147, ACIDS_WEAK = 148, BASES_WEAK = 149,
    CARBONATE_SALTS = 150, ALKYNES_WITH_ACETYLENIC_HYDROGEN = 151, ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN = 152,
    CONJUGATED_DIENES = 153, ARYL_HALIDES = 154, AMINES_AROMATIC = 155,
    NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC = 156, ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS = 157,
    ACRYLATES_AND_ACRYLIC_ACIDS = 158, PHENOLIC_SALTS = 159, QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS = 160,
    SULFITE_AND_THIOSULFATE_SALTS = 161, OXIMES = 162, POLYMERIZABLE_COMPOUNDS = 163,
    NOT_CHEMICALLY_REACTIVE = 164, INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION = 165,
    WATER_AND_AQUEOUS_SOLUTIONS = 166, NULL = 167, UNKNOWN = 168, WS = 169,
    COMMENT = 170, LINE_COMMENT = 171
  };

  enum {
    RuleProgram = 0, RuleGlobalDeclarations = 1, RuleModuleDeclaration = 2,
    RuleManifestDeclaration = 3, RuleStationaryDeclaration = 4, RuleFunctions = 5,
    RuleFunctionDeclaration = 6, RuleFormalParameters = 7, RuleFormalParameterList = 8,
    RuleFormalParameter = 9, RuleFunctionTyping = 10, RuleReturnStatement = 11,
    RuleBlockStatement = 12, RuleStatements = 13, RuleIfStatement = 14,
    RuleWhileStatement = 15, RuleRepeat = 16, RuleHeat = 17, RuleDispose = 18,
    RuleMix = 19, RuleDetect = 20, RuleSplit = 21, RuleDispense = 22, RuleGradient = 23,
    RuleStore = 24, RuleNumberAssignment = 25, RuleMath = 26, RuleBinops = 27,
    RuleParExpression = 28, RuleMethodInvocation = 29, RuleMethodCall = 30,
    RuleExpressionList = 31, RuleTypeType = 32, RuleUnionType = 33, RuleTypesList = 34,
    RuleVariableDefinition = 35, RuleVariable = 36, RulePrimary = 37, RuleLiteral = 38,
    RulePrimitiveType = 39, RuleChemicalType = 40, RuleTimeIdentifier = 41,
    RuleTemperatureIdentifier = 42, RuleUnitTracker = 43
  };

  BSParser(antlr4::TokenStream *input);
  ~BSParser();

  virtual std::string getGrammarFileName() const override;
  virtual const antlr4::atn::ATN& getATN() const override { return _atn; };
  virtual const std::vector<std::string>& getTokenNames() const override { return _tokenNames; }; // deprecated: use vocabulary instead.
  virtual const std::vector<std::string>& getRuleNames() const override;
  virtual antlr4::dfa::Vocabulary& getVocabulary() const override;


  class ProgramContext;
  class GlobalDeclarationsContext;
  class ModuleDeclarationContext;
  class ManifestDeclarationContext;
  class StationaryDeclarationContext;
  class FunctionsContext;
  class FunctionDeclarationContext;
  class FormalParametersContext;
  class FormalParameterListContext;
  class FormalParameterContext;
  class FunctionTypingContext;
  class ReturnStatementContext;
  class BlockStatementContext;
  class StatementsContext;
  class IfStatementContext;
  class WhileStatementContext;
  class RepeatContext;
  class HeatContext;
  class DisposeContext;
  class MixContext;
  class DetectContext;
  class SplitContext;
  class DispenseContext;
  class GradientContext;
  class StoreContext;
  class NumberAssignmentContext;
  class MathContext;
  class BinopsContext;
  class ParExpressionContext;
  class MethodInvocationContext;
  class MethodCallContext;
  class ExpressionListContext;
  class TypeTypeContext;
  class UnionTypeContext;
  class TypesListContext;
  class VariableDefinitionContext;
  class VariableContext;
  class PrimaryContext;
  class LiteralContext;
  class PrimitiveTypeContext;
  class ChemicalTypeContext;
  class TimeIdentifierContext;
  class TemperatureIdentifierContext;
  class UnitTrackerContext;

  class  ProgramContext : public antlr4::ParserRuleContext {
  public:
    ProgramContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *INSTRUCTIONS();
    antlr4::tree::TerminalNode *COLON();
    antlr4::tree::TerminalNode *EOF();
    std::vector<GlobalDeclarationsContext *> globalDeclarations();
    GlobalDeclarationsContext* globalDeclarations(size_t i);
    FunctionsContext *functions();
    std::vector<StatementsContext *> statements();
    StatementsContext* statements(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ProgramContext* program();

  class  GlobalDeclarationsContext : public antlr4::ParserRuleContext {
  public:
    GlobalDeclarationsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    ModuleDeclarationContext *moduleDeclaration();
    ManifestDeclarationContext *manifestDeclaration();
    StationaryDeclarationContext *stationaryDeclaration();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  GlobalDeclarationsContext* globalDeclarations();

  class  ModuleDeclarationContext : public antlr4::ParserRuleContext {
  public:
    ModuleDeclarationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *MODULE();
    antlr4::tree::TerminalNode *IDENTIFIER();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ModuleDeclarationContext* moduleDeclaration();

  class  ManifestDeclarationContext : public antlr4::ParserRuleContext {
  public:
    ManifestDeclarationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *MANIFEST();
    antlr4::tree::TerminalNode *IDENTIFIER();
    UnionTypeContext *unionType();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ManifestDeclarationContext* manifestDeclaration();

  class  StationaryDeclarationContext : public antlr4::ParserRuleContext {
  public:
    StationaryDeclarationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *STATIONARY();
    antlr4::tree::TerminalNode *IDENTIFIER();
    UnionTypeContext *unionType();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  StationaryDeclarationContext* stationaryDeclaration();

  class  FunctionsContext : public antlr4::ParserRuleContext {
  public:
    FunctionsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FUNCTIONS();
    antlr4::tree::TerminalNode *COLON();
    std::vector<FunctionDeclarationContext *> functionDeclaration();
    FunctionDeclarationContext* functionDeclaration(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  FunctionsContext* functions();

  class  FunctionDeclarationContext : public antlr4::ParserRuleContext {
  public:
    FunctionDeclarationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *FUNCTION();
    antlr4::tree::TerminalNode *IDENTIFIER();
    FormalParametersContext *formalParameters();
    antlr4::tree::TerminalNode *LBRACE();
    ReturnStatementContext *returnStatement();
    antlr4::tree::TerminalNode *RBRACE();
    FunctionTypingContext *functionTyping();
    std::vector<StatementsContext *> statements();
    StatementsContext* statements(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  FunctionDeclarationContext* functionDeclaration();

  class  FormalParametersContext : public antlr4::ParserRuleContext {
  public:
    FormalParametersContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LPAREN();
    antlr4::tree::TerminalNode *RPAREN();
    FormalParameterListContext *formalParameterList();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  FormalParametersContext* formalParameters();

  class  FormalParameterListContext : public antlr4::ParserRuleContext {
  public:
    FormalParameterListContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<FormalParameterContext *> formalParameter();
    FormalParameterContext* formalParameter(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  FormalParameterListContext* formalParameterList();

  class  FormalParameterContext : public antlr4::ParserRuleContext {
  public:
    FormalParameterContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *IDENTIFIER();
    UnionTypeContext *unionType();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  FormalParameterContext* formalParameter();

  class  FunctionTypingContext : public antlr4::ParserRuleContext {
  public:
    FunctionTypingContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COLON();
    UnionTypeContext *unionType();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  FunctionTypingContext* functionTyping();

  class  ReturnStatementContext : public antlr4::ParserRuleContext {
  public:
    ReturnStatementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *RETURN();
    PrimaryContext *primary();
    MethodCallContext *methodCall();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ReturnStatementContext* returnStatement();

  class  BlockStatementContext : public antlr4::ParserRuleContext {
  public:
    BlockStatementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LBRACE();
    antlr4::tree::TerminalNode *RBRACE();
    std::vector<StatementsContext *> statements();
    StatementsContext* statements(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  BlockStatementContext* blockStatement();

  class  StatementsContext : public antlr4::ParserRuleContext {
  public:
    StatementsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    IfStatementContext *ifStatement();
    WhileStatementContext *whileStatement();
    VariableDefinitionContext *variableDefinition();
    RepeatContext *repeat();
    HeatContext *heat();
    DisposeContext *dispose();
    MixContext *mix();
    DispenseContext *dispense();
    SplitContext *split();
    MethodInvocationContext *methodInvocation();
    GradientContext *gradient();
    DetectContext *detect();
    StoreContext *store();
    MathContext *math();
    NumberAssignmentContext *numberAssignment();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  StatementsContext* statements();

  class  IfStatementContext : public antlr4::ParserRuleContext {
  public:
    IfStatementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *IF();
    ParExpressionContext *parExpression();
    std::vector<BlockStatementContext *> blockStatement();
    BlockStatementContext* blockStatement(size_t i);
    antlr4::tree::TerminalNode *ELSE();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  IfStatementContext* ifStatement();

  class  WhileStatementContext : public antlr4::ParserRuleContext {
  public:
    WhileStatementContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *WHILE();
    ParExpressionContext *parExpression();
    BlockStatementContext *blockStatement();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  WhileStatementContext* whileStatement();

  class  RepeatContext : public antlr4::ParserRuleContext {
  public:
    RepeatContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *REPEAT();
    antlr4::tree::TerminalNode *INTEGER_LITERAL();
    antlr4::tree::TerminalNode *TIMES();
    BlockStatementContext *blockStatement();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  RepeatContext* repeat();

  class  HeatContext : public antlr4::ParserRuleContext {
  public:
    HeatContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *HEAT();
    VariableContext *variable();
    antlr4::tree::TerminalNode *AT();
    TemperatureIdentifierContext *temperatureIdentifier();
    antlr4::tree::TerminalNode *FOR();
    TimeIdentifierContext *timeIdentifier();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  HeatContext* heat();

  class  DisposeContext : public antlr4::ParserRuleContext {
  public:
    DisposeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *DRAIN();
    VariableContext *variable();
    antlr4::tree::TerminalNode *DISPOSE();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  DisposeContext* dispose();

  class  MixContext : public antlr4::ParserRuleContext {
  public:
    MixContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VariableDefinitionContext *variableDefinition();
    antlr4::tree::TerminalNode *MIX();
    std::vector<VariableContext *> variable();
    VariableContext* variable(size_t i);
    antlr4::tree::TerminalNode *WITH();
    std::vector<UnitTrackerContext *> unitTracker();
    UnitTrackerContext* unitTracker(size_t i);
    antlr4::tree::TerminalNode *FOR();
    TimeIdentifierContext *timeIdentifier();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  MixContext* mix();

  class  DetectContext : public antlr4::ParserRuleContext {
  public:
    DetectContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VariableDefinitionContext *variableDefinition();
    antlr4::tree::TerminalNode *DETECT();
    antlr4::tree::TerminalNode *IDENTIFIER();
    antlr4::tree::TerminalNode *ON();
    VariableContext *variable();
    antlr4::tree::TerminalNode *FOR();
    TimeIdentifierContext *timeIdentifier();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  DetectContext* detect();

  class  SplitContext : public antlr4::ParserRuleContext {
  public:
    SplitContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VariableDefinitionContext *variableDefinition();
    antlr4::tree::TerminalNode *SPLIT();
    VariableContext *variable();
    antlr4::tree::TerminalNode *INTO();
    antlr4::tree::TerminalNode *INTEGER_LITERAL();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  SplitContext* split();

  class  DispenseContext : public antlr4::ParserRuleContext {
  public:
    DispenseContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VariableDefinitionContext *variableDefinition();
    antlr4::tree::TerminalNode *DISPENSE();
    antlr4::tree::TerminalNode *IDENTIFIER();
    UnitTrackerContext *unitTracker();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  DispenseContext* dispense();

  class  GradientContext : public antlr4::ParserRuleContext {
  public:
    GradientContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VariableDefinitionContext *variableDefinition();
    antlr4::tree::TerminalNode *GRADIENT();
    std::vector<VariableContext *> variable();
    VariableContext* variable(size_t i);
    antlr4::tree::TerminalNode *WITH();
    antlr4::tree::TerminalNode *RANGE();
    std::vector<antlr4::tree::TerminalNode *> FLOAT_LITERAL();
    antlr4::tree::TerminalNode* FLOAT_LITERAL(size_t i);
    antlr4::tree::TerminalNode *COMMA();
    antlr4::tree::TerminalNode *AT();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  GradientContext* gradient();

  class  StoreContext : public antlr4::ParserRuleContext {
  public:
    StoreContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *STORE();
    VariableContext *variable();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  StoreContext* store();

  class  NumberAssignmentContext : public antlr4::ParserRuleContext {
  public:
    NumberAssignmentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VariableDefinitionContext *variableDefinition();
    LiteralContext *literal();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  NumberAssignmentContext* numberAssignment();

  class  MathContext : public antlr4::ParserRuleContext {
  public:
    antlr4::Token *bop = nullptr;;
    MathContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VariableDefinitionContext *variableDefinition();
    std::vector<PrimaryContext *> primary();
    PrimaryContext* primary(size_t i);
    antlr4::tree::TerminalNode *MULTIPLY();
    antlr4::tree::TerminalNode *DIVIDE();
    antlr4::tree::TerminalNode *ADDITION();
    antlr4::tree::TerminalNode *SUBTRACT();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  MathContext* math();

  class  BinopsContext : public antlr4::ParserRuleContext {
  public:
    antlr4::Token *bop = nullptr;;
    BinopsContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<PrimaryContext *> primary();
    PrimaryContext* primary(size_t i);
    std::vector<antlr4::tree::TerminalNode *> LT();
    antlr4::tree::TerminalNode* LT(size_t i);
    std::vector<antlr4::tree::TerminalNode *> GT();
    antlr4::tree::TerminalNode* GT(size_t i);
    antlr4::tree::TerminalNode *LTE();
    antlr4::tree::TerminalNode *GTE();
    antlr4::tree::TerminalNode *EQUALITY();
    antlr4::tree::TerminalNode *NOTEQUAL();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  BinopsContext* binops();

  class  ParExpressionContext : public antlr4::ParserRuleContext {
  public:
    ParExpressionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LPAREN();
    std::vector<BinopsContext *> binops();
    BinopsContext* binops(size_t i);
    antlr4::tree::TerminalNode *RPAREN();
    std::vector<antlr4::tree::TerminalNode *> AND();
    antlr4::tree::TerminalNode* AND(size_t i);
    std::vector<antlr4::tree::TerminalNode *> OR();
    antlr4::tree::TerminalNode* OR(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ParExpressionContext* parExpression();

  class  MethodInvocationContext : public antlr4::ParserRuleContext {
  public:
    MethodInvocationContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VariableDefinitionContext *variableDefinition();
    MethodCallContext *methodCall();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  MethodInvocationContext* methodInvocation();

  class  MethodCallContext : public antlr4::ParserRuleContext {
  public:
    MethodCallContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *IDENTIFIER();
    antlr4::tree::TerminalNode *LPAREN();
    antlr4::tree::TerminalNode *RPAREN();
    ExpressionListContext *expressionList();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  MethodCallContext* methodCall();

  class  ExpressionListContext : public antlr4::ParserRuleContext {
  public:
    ExpressionListContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<PrimaryContext *> primary();
    PrimaryContext* primary(size_t i);
    std::vector<antlr4::tree::TerminalNode *> COMMA();
    antlr4::tree::TerminalNode* COMMA(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ExpressionListContext* expressionList();

  class  TypeTypeContext : public antlr4::ParserRuleContext {
  public:
    TypeTypeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    PrimitiveTypeContext *primitiveType();
    ChemicalTypeContext *chemicalType();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  TypeTypeContext* typeType();

  class  UnionTypeContext : public antlr4::ParserRuleContext {
  public:
    UnionTypeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *LBRACKET();
    TypesListContext *typesList();
    antlr4::tree::TerminalNode *RBRACKET();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  UnionTypeContext* unionType();

  class  TypesListContext : public antlr4::ParserRuleContext {
  public:
    TypesListContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<TypeTypeContext *> typeType();
    TypeTypeContext* typeType(size_t i);
    std::vector<antlr4::tree::TerminalNode *> SEMICOLON();
    antlr4::tree::TerminalNode* SEMICOLON(size_t i);

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  TypesListContext* typesList();

  class  VariableDefinitionContext : public antlr4::ParserRuleContext {
  public:
    VariableDefinitionContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    VariableContext *variable();
    antlr4::tree::TerminalNode *ASSIGN();
    UnionTypeContext *unionType();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  VariableDefinitionContext* variableDefinition();

  class  VariableContext : public antlr4::ParserRuleContext {
  public:
    VariableContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *IDENTIFIER();
    antlr4::tree::TerminalNode *LBRACKET();
    antlr4::tree::TerminalNode *INTEGER_LITERAL();
    antlr4::tree::TerminalNode *RBRACKET();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  VariableContext* variable();

  class  PrimaryContext : public antlr4::ParserRuleContext {
  public:
    PrimaryContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    LiteralContext *literal();
    VariableContext *variable();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  PrimaryContext* primary();

  class  LiteralContext : public antlr4::ParserRuleContext {
  public:
    LiteralContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *INTEGER_LITERAL();
    antlr4::tree::TerminalNode *FLOAT_LITERAL();
    antlr4::tree::TerminalNode *BOOL_LITERAL();
    antlr4::tree::TerminalNode *STRING_LITERAL();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  LiteralContext* literal();

  class  PrimitiveTypeContext : public antlr4::ParserRuleContext {
  public:
    PrimitiveTypeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *BOOL();
    antlr4::tree::TerminalNode *NAT();
    antlr4::tree::TerminalNode *REAL();
    antlr4::tree::TerminalNode *MAT();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  PrimitiveTypeContext* primitiveType();

  class  ChemicalTypeContext : public antlr4::ParserRuleContext {
  public:
    ChemicalTypeContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *INTEGER_LITERAL();
    antlr4::tree::TerminalNode *ACIDS_STRONG_NON_OXIDIZING();
    antlr4::tree::TerminalNode *ACIDS_STRONG_OXIDIZING();
    antlr4::tree::TerminalNode *ACIDS_CARBOXYLIC();
    antlr4::tree::TerminalNode *ALCOHOLS_AND_POLYOLS();
    antlr4::tree::TerminalNode *ALDEHYDES();
    antlr4::tree::TerminalNode *AMIDES_AND_IMIDES();
    antlr4::tree::TerminalNode *AMINES_PHOSPHINES_AND_PYRIDINES();
    antlr4::tree::TerminalNode *AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS();
    antlr4::tree::TerminalNode *CARBAMATES();
    antlr4::tree::TerminalNode *BASES_STRONG();
    antlr4::tree::TerminalNode *CYANIDES_INORGANIC();
    antlr4::tree::TerminalNode *THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS();
    antlr4::tree::TerminalNode *ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS();
    antlr4::tree::TerminalNode *ETHERS();
    antlr4::tree::TerminalNode *FLUORIDES_INORGANIC();
    antlr4::tree::TerminalNode *HYDROCARBONS_AROMATIC();
    antlr4::tree::TerminalNode *HALOGENATED_ORGANIC_COMPOUNDS();
    antlr4::tree::TerminalNode *ISOCYANATES_AND_ISOTHIOCYANATES();
    antlr4::tree::TerminalNode *KETONES();
    antlr4::tree::TerminalNode *SULFIDES_ORGANIC();
    antlr4::tree::TerminalNode *METALS_ALKALI_VERY_ACTIVE();
    antlr4::tree::TerminalNode *METALS_ELEMENTAL_AND_POWDER_ACTIVE();
    antlr4::tree::TerminalNode *METALS_LESS_REACTIVE();
    antlr4::tree::TerminalNode *METALS_AND_METAL_COMPOUNDS_TOXIC();
    antlr4::tree::TerminalNode *DIAZONIUM_SALTS();
    antlr4::tree::TerminalNode *NITRILES();
    antlr4::tree::TerminalNode *NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC();
    antlr4::tree::TerminalNode *HYDROCARBONS_ALIPHATIC_UNSATURATED();
    antlr4::tree::TerminalNode *HYDROCARBONS_ALIPHATIC_SATURATED();
    antlr4::tree::TerminalNode *PEROXIDES_ORGANIC();
    antlr4::tree::TerminalNode *PHENOLS_AND_CRESOLS();
    antlr4::tree::TerminalNode *SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC();
    antlr4::tree::TerminalNode *SULFIDES_INORGANIC();
    antlr4::tree::TerminalNode *EPOXIDES();
    antlr4::tree::TerminalNode *METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES();
    antlr4::tree::TerminalNode *ANHYDRIDES();
    antlr4::tree::TerminalNode *SALTS_ACIDIC();
    antlr4::tree::TerminalNode *SALTS_BASIC();
    antlr4::tree::TerminalNode *ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES();
    antlr4::tree::TerminalNode *ORGANOMETALLICS();
    antlr4::tree::TerminalNode *OXIDIZING_AGENTS_STRONG();
    antlr4::tree::TerminalNode *REDUCING_AGENTS_STRONG();
    antlr4::tree::TerminalNode *NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS();
    antlr4::tree::TerminalNode *FLUORINATED_ORGANIC_COMPOUNDS();
    antlr4::tree::TerminalNode *FLUORIDE_SALTS_SOLUBLE();
    antlr4::tree::TerminalNode *OXIDIZING_AGENTS_WEAK();
    antlr4::tree::TerminalNode *REDUCING_AGENTS_WEAK();
    antlr4::tree::TerminalNode *NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES();
    antlr4::tree::TerminalNode *CHLOROSILANES();
    antlr4::tree::TerminalNode *SILOXANES();
    antlr4::tree::TerminalNode *HALOGENATING_AGENTS();
    antlr4::tree::TerminalNode *ACIDS_WEAK();
    antlr4::tree::TerminalNode *BASES_WEAK();
    antlr4::tree::TerminalNode *CARBONATE_SALTS();
    antlr4::tree::TerminalNode *ALKYNES_WITH_ACETYLENIC_HYDROGEN();
    antlr4::tree::TerminalNode *ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN();
    antlr4::tree::TerminalNode *CONJUGATED_DIENES();
    antlr4::tree::TerminalNode *ARYL_HALIDES();
    antlr4::tree::TerminalNode *AMINES_AROMATIC();
    antlr4::tree::TerminalNode *NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC();
    antlr4::tree::TerminalNode *ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS();
    antlr4::tree::TerminalNode *ACRYLATES_AND_ACRYLIC_ACIDS();
    antlr4::tree::TerminalNode *PHENOLIC_SALTS();
    antlr4::tree::TerminalNode *QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS();
    antlr4::tree::TerminalNode *SULFITE_AND_THIOSULFATE_SALTS();
    antlr4::tree::TerminalNode *OXIMES();
    antlr4::tree::TerminalNode *POLYMERIZABLE_COMPOUNDS();
    antlr4::tree::TerminalNode *NOT_CHEMICALLY_REACTIVE();
    antlr4::tree::TerminalNode *INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION();
    antlr4::tree::TerminalNode *WATER_AND_AQUEOUS_SOLUTIONS();
    antlr4::tree::TerminalNode *NULL();
    antlr4::tree::TerminalNode *UNKNOWN();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  ChemicalTypeContext* chemicalType();

  class  TimeIdentifierContext : public antlr4::ParserRuleContext {
  public:
    TimeIdentifierContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *TIME_NUMBER();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  TimeIdentifierContext* timeIdentifier();

  class  TemperatureIdentifierContext : public antlr4::ParserRuleContext {
  public:
    TemperatureIdentifierContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *TEMP_NUMBER();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  TemperatureIdentifierContext* temperatureIdentifier();

  class  UnitTrackerContext : public antlr4::ParserRuleContext {
  public:
    UnitTrackerContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *INTEGER_LITERAL();
    antlr4::tree::TerminalNode *UNITS();
    antlr4::tree::TerminalNode *OF();

    virtual void enterRule(antlr4::tree::ParseTreeListener *listener) override;
    virtual void exitRule(antlr4::tree::ParseTreeListener *listener) override;

    virtual antlrcpp::Any accept(antlr4::tree::ParseTreeVisitor *visitor) override;

  };

  UnitTrackerContext* unitTracker();


private:
  static std::vector<antlr4::dfa::DFA> _decisionToDFA;
  static antlr4::atn::PredictionContextCache _sharedContextCache;
  static std::vector<std::string> _ruleNames;
  static std::vector<std::string> _tokenNames;

  static std::vector<std::string> _literalNames;
  static std::vector<std::string> _symbolicNames;
  static antlr4::dfa::Vocabulary _vocabulary;
  static antlr4::atn::ATN _atn;
  static std::vector<uint16_t> _serializedATN;

  /* private parser declarations section */

  struct Initializer {
    Initializer();
  };
  static Initializer _init;
};

