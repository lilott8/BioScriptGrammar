/* parser/listener/visitor header section */

// Generated from /bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.7

/* parser precinclude section */

#include "BSParserListener.h"
#include "BSParserVisitor.h"

#include "BSParser.h"


using namespace antlrcpp;
using namespace antlr4;

BSParser::BSParser(TokenStream *input) : Parser(input) {
  _interpreter = new atn::ParserATNSimulator(this, _atn, _decisionToDFA, _sharedContextCache);
}

BSParser::~BSParser() {
  delete _interpreter;
}

std::string BSParser::getGrammarFileName() const {
  return "BSParser.g4";
}

const std::vector<std::string>& BSParser::getRuleNames() const {
  return _ruleNames;
}

dfa::Vocabulary& BSParser::getVocabulary() const {
  return _vocabulary;
}

/* parser definitions section */

//----------------- ProgmaramContext ------------------------------------------------------------------

BSParser::ProgmaramContext::ProgmaramContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::ProgmaramContext::INSTRUCTIONS() {
  return getToken(BSParser::INSTRUCTIONS, 0);
}

tree::TerminalNode* BSParser::ProgmaramContext::COLON() {
  return getToken(BSParser::COLON, 0);
}

tree::TerminalNode* BSParser::ProgmaramContext::EOF() {
  return getToken(BSParser::EOF, 0);
}

std::vector<BSParser::GlobalDeclarationsContext *> BSParser::ProgmaramContext::globalDeclarations() {
  return getRuleContexts<BSParser::GlobalDeclarationsContext>();
}

BSParser::GlobalDeclarationsContext* BSParser::ProgmaramContext::globalDeclarations(size_t i) {
  return getRuleContext<BSParser::GlobalDeclarationsContext>(i);
}

BSParser::FunctionsContext* BSParser::ProgmaramContext::functions() {
  return getRuleContext<BSParser::FunctionsContext>(0);
}

std::vector<BSParser::StatementsContext *> BSParser::ProgmaramContext::statements() {
  return getRuleContexts<BSParser::StatementsContext>();
}

BSParser::StatementsContext* BSParser::ProgmaramContext::statements(size_t i) {
  return getRuleContext<BSParser::StatementsContext>(i);
}


size_t BSParser::ProgmaramContext::getRuleIndex() const {
  return BSParser::RuleProgmaram;
}

void BSParser::ProgmaramContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterProgmaram(this);
}

void BSParser::ProgmaramContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitProgmaram(this);
}


antlrcpp::Any BSParser::ProgmaramContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitProgmaram(this);
  else
    return visitor->visitChildren(this);
}

BSParser::ProgmaramContext* BSParser::progmaram() {
  ProgmaramContext *_localctx = _tracker.createInstance<ProgmaramContext>(_ctx, getState());
  enterRule(_localctx, 0, BSParser::RuleProgmaram);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(87);
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(86);
      globalDeclarations();
      setState(89);
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << BSParser::MANIFEST)
      | (1ULL << BSParser::MODULE)
      | (1ULL << BSParser::STATIONARY))) != 0));
    setState(92);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::FUNCTIONS) {
      setState(91);
      functions();
    }
    setState(94);
    match(BSParser::INSTRUCTIONS);
    setState(95);
    match(BSParser::COLON);
    setState(99);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << BSParser::IF)
      | (1ULL << BSParser::REPEAT)
      | (1ULL << BSParser::WHILE)
      | (1ULL << BSParser::HEAT)
      | (1ULL << BSParser::DRAIN)
      | (1ULL << BSParser::DISPOSE)
      | (1ULL << BSParser::STORE)
      | (1ULL << BSParser::IDENTIFIER)
      | (1ULL << BSParser::LBRACKET))) != 0)) {
      setState(96);
      statements();
      setState(101);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(102);
    match(BSParser::EOF);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- GlobalDeclarationsContext ------------------------------------------------------------------

BSParser::GlobalDeclarationsContext::GlobalDeclarationsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::ModuleDeclarationContext* BSParser::GlobalDeclarationsContext::moduleDeclaration() {
  return getRuleContext<BSParser::ModuleDeclarationContext>(0);
}

BSParser::ManifestDeclarationContext* BSParser::GlobalDeclarationsContext::manifestDeclaration() {
  return getRuleContext<BSParser::ManifestDeclarationContext>(0);
}

BSParser::StationaryDeclarationContext* BSParser::GlobalDeclarationsContext::stationaryDeclaration() {
  return getRuleContext<BSParser::StationaryDeclarationContext>(0);
}


size_t BSParser::GlobalDeclarationsContext::getRuleIndex() const {
  return BSParser::RuleGlobalDeclarations;
}

void BSParser::GlobalDeclarationsContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterGlobalDeclarations(this);
}

void BSParser::GlobalDeclarationsContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitGlobalDeclarations(this);
}


antlrcpp::Any BSParser::GlobalDeclarationsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitGlobalDeclarations(this);
  else
    return visitor->visitChildren(this);
}

BSParser::GlobalDeclarationsContext* BSParser::globalDeclarations() {
  GlobalDeclarationsContext *_localctx = _tracker.createInstance<GlobalDeclarationsContext>(_ctx, getState());
  enterRule(_localctx, 2, BSParser::RuleGlobalDeclarations);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    setState(107);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BSParser::MODULE: {
        enterOuterAlt(_localctx, 1);
        setState(104);
        moduleDeclaration();
        break;
      }

      case BSParser::MANIFEST: {
        enterOuterAlt(_localctx, 2);
        setState(105);
        manifestDeclaration();
        break;
      }

      case BSParser::STATIONARY: {
        enterOuterAlt(_localctx, 3);
        setState(106);
        stationaryDeclaration();
        break;
      }

    default:
      throw NoViableAltException(this);
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ModuleDeclarationContext ------------------------------------------------------------------

BSParser::ModuleDeclarationContext::ModuleDeclarationContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::ModuleDeclarationContext::MODULE() {
  return getToken(BSParser::MODULE, 0);
}

tree::TerminalNode* BSParser::ModuleDeclarationContext::IDENTIFIER() {
  return getToken(BSParser::IDENTIFIER, 0);
}


size_t BSParser::ModuleDeclarationContext::getRuleIndex() const {
  return BSParser::RuleModuleDeclaration;
}

void BSParser::ModuleDeclarationContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterModuleDeclaration(this);
}

void BSParser::ModuleDeclarationContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitModuleDeclaration(this);
}


antlrcpp::Any BSParser::ModuleDeclarationContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitModuleDeclaration(this);
  else
    return visitor->visitChildren(this);
}

BSParser::ModuleDeclarationContext* BSParser::moduleDeclaration() {
  ModuleDeclarationContext *_localctx = _tracker.createInstance<ModuleDeclarationContext>(_ctx, getState());
  enterRule(_localctx, 4, BSParser::RuleModuleDeclaration);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(109);
    match(BSParser::MODULE);
    setState(110);
    match(BSParser::IDENTIFIER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ManifestDeclarationContext ------------------------------------------------------------------

BSParser::ManifestDeclarationContext::ManifestDeclarationContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::ManifestDeclarationContext::MANIFEST() {
  return getToken(BSParser::MANIFEST, 0);
}

tree::TerminalNode* BSParser::ManifestDeclarationContext::IDENTIFIER() {
  return getToken(BSParser::IDENTIFIER, 0);
}


size_t BSParser::ManifestDeclarationContext::getRuleIndex() const {
  return BSParser::RuleManifestDeclaration;
}

void BSParser::ManifestDeclarationContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterManifestDeclaration(this);
}

void BSParser::ManifestDeclarationContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitManifestDeclaration(this);
}


antlrcpp::Any BSParser::ManifestDeclarationContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitManifestDeclaration(this);
  else
    return visitor->visitChildren(this);
}

BSParser::ManifestDeclarationContext* BSParser::manifestDeclaration() {
  ManifestDeclarationContext *_localctx = _tracker.createInstance<ManifestDeclarationContext>(_ctx, getState());
  enterRule(_localctx, 6, BSParser::RuleManifestDeclaration);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(112);
    match(BSParser::MANIFEST);
    setState(113);
    match(BSParser::IDENTIFIER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StationaryDeclarationContext ------------------------------------------------------------------

BSParser::StationaryDeclarationContext::StationaryDeclarationContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::StationaryDeclarationContext::STATIONARY() {
  return getToken(BSParser::STATIONARY, 0);
}

tree::TerminalNode* BSParser::StationaryDeclarationContext::IDENTIFIER() {
  return getToken(BSParser::IDENTIFIER, 0);
}


size_t BSParser::StationaryDeclarationContext::getRuleIndex() const {
  return BSParser::RuleStationaryDeclaration;
}

void BSParser::StationaryDeclarationContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterStationaryDeclaration(this);
}

void BSParser::StationaryDeclarationContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitStationaryDeclaration(this);
}


antlrcpp::Any BSParser::StationaryDeclarationContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitStationaryDeclaration(this);
  else
    return visitor->visitChildren(this);
}

BSParser::StationaryDeclarationContext* BSParser::stationaryDeclaration() {
  StationaryDeclarationContext *_localctx = _tracker.createInstance<StationaryDeclarationContext>(_ctx, getState());
  enterRule(_localctx, 8, BSParser::RuleStationaryDeclaration);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(115);
    match(BSParser::STATIONARY);
    setState(116);
    match(BSParser::IDENTIFIER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FunctionsContext ------------------------------------------------------------------

BSParser::FunctionsContext::FunctionsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::FunctionsContext::FUNCTIONS() {
  return getToken(BSParser::FUNCTIONS, 0);
}

tree::TerminalNode* BSParser::FunctionsContext::COLON() {
  return getToken(BSParser::COLON, 0);
}

std::vector<BSParser::FunctionDeclarationContext *> BSParser::FunctionsContext::functionDeclaration() {
  return getRuleContexts<BSParser::FunctionDeclarationContext>();
}

BSParser::FunctionDeclarationContext* BSParser::FunctionsContext::functionDeclaration(size_t i) {
  return getRuleContext<BSParser::FunctionDeclarationContext>(i);
}


size_t BSParser::FunctionsContext::getRuleIndex() const {
  return BSParser::RuleFunctions;
}

void BSParser::FunctionsContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterFunctions(this);
}

void BSParser::FunctionsContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitFunctions(this);
}


antlrcpp::Any BSParser::FunctionsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitFunctions(this);
  else
    return visitor->visitChildren(this);
}

BSParser::FunctionsContext* BSParser::functions() {
  FunctionsContext *_localctx = _tracker.createInstance<FunctionsContext>(_ctx, getState());
  enterRule(_localctx, 10, BSParser::RuleFunctions);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(118);
    match(BSParser::FUNCTIONS);
    setState(119);
    match(BSParser::COLON);
    setState(121);
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(120);
      functionDeclaration();
      setState(123);
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == BSParser::FUNCTION);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FunctionDeclarationContext ------------------------------------------------------------------

BSParser::FunctionDeclarationContext::FunctionDeclarationContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::FunctionDeclarationContext::FUNCTION() {
  return getToken(BSParser::FUNCTION, 0);
}

tree::TerminalNode* BSParser::FunctionDeclarationContext::IDENTIFIER() {
  return getToken(BSParser::IDENTIFIER, 0);
}

BSParser::FormalParametersContext* BSParser::FunctionDeclarationContext::formalParameters() {
  return getRuleContext<BSParser::FormalParametersContext>(0);
}

tree::TerminalNode* BSParser::FunctionDeclarationContext::LBRACE() {
  return getToken(BSParser::LBRACE, 0);
}

BSParser::ReturnStatementContext* BSParser::FunctionDeclarationContext::returnStatement() {
  return getRuleContext<BSParser::ReturnStatementContext>(0);
}

tree::TerminalNode* BSParser::FunctionDeclarationContext::RBRACE() {
  return getToken(BSParser::RBRACE, 0);
}

BSParser::FunctionTypingContext* BSParser::FunctionDeclarationContext::functionTyping() {
  return getRuleContext<BSParser::FunctionTypingContext>(0);
}

std::vector<BSParser::StatementsContext *> BSParser::FunctionDeclarationContext::statements() {
  return getRuleContexts<BSParser::StatementsContext>();
}

BSParser::StatementsContext* BSParser::FunctionDeclarationContext::statements(size_t i) {
  return getRuleContext<BSParser::StatementsContext>(i);
}


size_t BSParser::FunctionDeclarationContext::getRuleIndex() const {
  return BSParser::RuleFunctionDeclaration;
}

void BSParser::FunctionDeclarationContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterFunctionDeclaration(this);
}

void BSParser::FunctionDeclarationContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitFunctionDeclaration(this);
}


antlrcpp::Any BSParser::FunctionDeclarationContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitFunctionDeclaration(this);
  else
    return visitor->visitChildren(this);
}

BSParser::FunctionDeclarationContext* BSParser::functionDeclaration() {
  FunctionDeclarationContext *_localctx = _tracker.createInstance<FunctionDeclarationContext>(_ctx, getState());
  enterRule(_localctx, 12, BSParser::RuleFunctionDeclaration);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(125);
    match(BSParser::FUNCTION);
    setState(126);
    match(BSParser::IDENTIFIER);
    setState(127);
    formalParameters();
    setState(129);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::COLON) {
      setState(128);
      functionTyping();
    }
    setState(131);
    match(BSParser::LBRACE);
    setState(135);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << BSParser::IF)
      | (1ULL << BSParser::REPEAT)
      | (1ULL << BSParser::WHILE)
      | (1ULL << BSParser::HEAT)
      | (1ULL << BSParser::DRAIN)
      | (1ULL << BSParser::DISPOSE)
      | (1ULL << BSParser::STORE)
      | (1ULL << BSParser::IDENTIFIER)
      | (1ULL << BSParser::LBRACKET))) != 0)) {
      setState(132);
      statements();
      setState(137);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(138);
    returnStatement();
    setState(139);
    match(BSParser::RBRACE);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FormalParametersContext ------------------------------------------------------------------

BSParser::FormalParametersContext::FormalParametersContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::FormalParametersContext::LPAREN() {
  return getToken(BSParser::LPAREN, 0);
}

tree::TerminalNode* BSParser::FormalParametersContext::RPAREN() {
  return getToken(BSParser::RPAREN, 0);
}

BSParser::FormalParameterListContext* BSParser::FormalParametersContext::formalParameterList() {
  return getRuleContext<BSParser::FormalParameterListContext>(0);
}


size_t BSParser::FormalParametersContext::getRuleIndex() const {
  return BSParser::RuleFormalParameters;
}

void BSParser::FormalParametersContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterFormalParameters(this);
}

void BSParser::FormalParametersContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitFormalParameters(this);
}


antlrcpp::Any BSParser::FormalParametersContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitFormalParameters(this);
  else
    return visitor->visitChildren(this);
}

BSParser::FormalParametersContext* BSParser::formalParameters() {
  FormalParametersContext *_localctx = _tracker.createInstance<FormalParametersContext>(_ctx, getState());
  enterRule(_localctx, 14, BSParser::RuleFormalParameters);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(141);
    match(BSParser::LPAREN);
    setState(143);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::IDENTIFIER

    || _la == BSParser::LBRACKET) {
      setState(142);
      formalParameterList();
    }
    setState(145);
    match(BSParser::RPAREN);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FormalParameterListContext ------------------------------------------------------------------

BSParser::FormalParameterListContext::FormalParameterListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BSParser::FormalParameterContext *> BSParser::FormalParameterListContext::formalParameter() {
  return getRuleContexts<BSParser::FormalParameterContext>();
}

BSParser::FormalParameterContext* BSParser::FormalParameterListContext::formalParameter(size_t i) {
  return getRuleContext<BSParser::FormalParameterContext>(i);
}

std::vector<tree::TerminalNode *> BSParser::FormalParameterListContext::COMMA() {
  return getTokens(BSParser::COMMA);
}

tree::TerminalNode* BSParser::FormalParameterListContext::COMMA(size_t i) {
  return getToken(BSParser::COMMA, i);
}


size_t BSParser::FormalParameterListContext::getRuleIndex() const {
  return BSParser::RuleFormalParameterList;
}

void BSParser::FormalParameterListContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterFormalParameterList(this);
}

void BSParser::FormalParameterListContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitFormalParameterList(this);
}


antlrcpp::Any BSParser::FormalParameterListContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitFormalParameterList(this);
  else
    return visitor->visitChildren(this);
}

BSParser::FormalParameterListContext* BSParser::formalParameterList() {
  FormalParameterListContext *_localctx = _tracker.createInstance<FormalParameterListContext>(_ctx, getState());
  enterRule(_localctx, 16, BSParser::RuleFormalParameterList);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(147);
    formalParameter();
    setState(152);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BSParser::COMMA) {
      setState(148);
      match(BSParser::COMMA);
      setState(149);
      formalParameter();
      setState(154);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FormalParameterContext ------------------------------------------------------------------

BSParser::FormalParameterContext::FormalParameterContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::FormalParameterContext::IDENTIFIER() {
  return getToken(BSParser::IDENTIFIER, 0);
}

BSParser::UnionTypeContext* BSParser::FormalParameterContext::unionType() {
  return getRuleContext<BSParser::UnionTypeContext>(0);
}


size_t BSParser::FormalParameterContext::getRuleIndex() const {
  return BSParser::RuleFormalParameter;
}

void BSParser::FormalParameterContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterFormalParameter(this);
}

void BSParser::FormalParameterContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitFormalParameter(this);
}


antlrcpp::Any BSParser::FormalParameterContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitFormalParameter(this);
  else
    return visitor->visitChildren(this);
}

BSParser::FormalParameterContext* BSParser::formalParameter() {
  FormalParameterContext *_localctx = _tracker.createInstance<FormalParameterContext>(_ctx, getState());
  enterRule(_localctx, 18, BSParser::RuleFormalParameter);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(156);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::LBRACKET) {
      setState(155);
      unionType();
    }
    setState(158);
    match(BSParser::IDENTIFIER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FunctionTypingContext ------------------------------------------------------------------

BSParser::FunctionTypingContext::FunctionTypingContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::FunctionTypingContext::COLON() {
  return getToken(BSParser::COLON, 0);
}

BSParser::UnionTypeContext* BSParser::FunctionTypingContext::unionType() {
  return getRuleContext<BSParser::UnionTypeContext>(0);
}


size_t BSParser::FunctionTypingContext::getRuleIndex() const {
  return BSParser::RuleFunctionTyping;
}

void BSParser::FunctionTypingContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterFunctionTyping(this);
}

void BSParser::FunctionTypingContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitFunctionTyping(this);
}


antlrcpp::Any BSParser::FunctionTypingContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitFunctionTyping(this);
  else
    return visitor->visitChildren(this);
}

BSParser::FunctionTypingContext* BSParser::functionTyping() {
  FunctionTypingContext *_localctx = _tracker.createInstance<FunctionTypingContext>(_ctx, getState());
  enterRule(_localctx, 20, BSParser::RuleFunctionTyping);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(160);
    match(BSParser::COLON);
    setState(161);
    unionType();

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ReturnStatementContext ------------------------------------------------------------------

BSParser::ReturnStatementContext::ReturnStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::ReturnStatementContext::RETURN() {
  return getToken(BSParser::RETURN, 0);
}

BSParser::PrimaryContext* BSParser::ReturnStatementContext::primary() {
  return getRuleContext<BSParser::PrimaryContext>(0);
}

BSParser::MethodCallContext* BSParser::ReturnStatementContext::methodCall() {
  return getRuleContext<BSParser::MethodCallContext>(0);
}


size_t BSParser::ReturnStatementContext::getRuleIndex() const {
  return BSParser::RuleReturnStatement;
}

void BSParser::ReturnStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterReturnStatement(this);
}

void BSParser::ReturnStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitReturnStatement(this);
}


antlrcpp::Any BSParser::ReturnStatementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitReturnStatement(this);
  else
    return visitor->visitChildren(this);
}

BSParser::ReturnStatementContext* BSParser::returnStatement() {
  ReturnStatementContext *_localctx = _tracker.createInstance<ReturnStatementContext>(_ctx, getState());
  enterRule(_localctx, 22, BSParser::RuleReturnStatement);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    setState(167);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 10, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(163);
      match(BSParser::RETURN);
      setState(164);
      primary();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(165);
      match(BSParser::RETURN);
      setState(166);
      methodCall();
      break;
    }

    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- BlockStatementContext ------------------------------------------------------------------

BSParser::BlockStatementContext::BlockStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::BlockStatementContext::LBRACE() {
  return getToken(BSParser::LBRACE, 0);
}

tree::TerminalNode* BSParser::BlockStatementContext::RBRACE() {
  return getToken(BSParser::RBRACE, 0);
}

std::vector<BSParser::StatementsContext *> BSParser::BlockStatementContext::statements() {
  return getRuleContexts<BSParser::StatementsContext>();
}

BSParser::StatementsContext* BSParser::BlockStatementContext::statements(size_t i) {
  return getRuleContext<BSParser::StatementsContext>(i);
}


size_t BSParser::BlockStatementContext::getRuleIndex() const {
  return BSParser::RuleBlockStatement;
}

void BSParser::BlockStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterBlockStatement(this);
}

void BSParser::BlockStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitBlockStatement(this);
}


antlrcpp::Any BSParser::BlockStatementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitBlockStatement(this);
  else
    return visitor->visitChildren(this);
}

BSParser::BlockStatementContext* BSParser::blockStatement() {
  BlockStatementContext *_localctx = _tracker.createInstance<BlockStatementContext>(_ctx, getState());
  enterRule(_localctx, 24, BSParser::RuleBlockStatement);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(169);
    match(BSParser::LBRACE);
    setState(173);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << BSParser::IF)
      | (1ULL << BSParser::REPEAT)
      | (1ULL << BSParser::WHILE)
      | (1ULL << BSParser::HEAT)
      | (1ULL << BSParser::DRAIN)
      | (1ULL << BSParser::DISPOSE)
      | (1ULL << BSParser::STORE)
      | (1ULL << BSParser::IDENTIFIER)
      | (1ULL << BSParser::LBRACKET))) != 0)) {
      setState(170);
      statements();
      setState(175);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(176);
    match(BSParser::RBRACE);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StatementsContext ------------------------------------------------------------------

BSParser::StatementsContext::StatementsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::IfStatementContext* BSParser::StatementsContext::ifStatement() {
  return getRuleContext<BSParser::IfStatementContext>(0);
}

BSParser::WhileStatementContext* BSParser::StatementsContext::whileStatement() {
  return getRuleContext<BSParser::WhileStatementContext>(0);
}

BSParser::VariableDefinitionContext* BSParser::StatementsContext::variableDefinition() {
  return getRuleContext<BSParser::VariableDefinitionContext>(0);
}

BSParser::RepeatContext* BSParser::StatementsContext::repeat() {
  return getRuleContext<BSParser::RepeatContext>(0);
}

BSParser::HeatContext* BSParser::StatementsContext::heat() {
  return getRuleContext<BSParser::HeatContext>(0);
}

BSParser::DisposeContext* BSParser::StatementsContext::dispose() {
  return getRuleContext<BSParser::DisposeContext>(0);
}

BSParser::MixContext* BSParser::StatementsContext::mix() {
  return getRuleContext<BSParser::MixContext>(0);
}

BSParser::DispenseContext* BSParser::StatementsContext::dispense() {
  return getRuleContext<BSParser::DispenseContext>(0);
}

BSParser::SplitContext* BSParser::StatementsContext::split() {
  return getRuleContext<BSParser::SplitContext>(0);
}

BSParser::MethodInvocationContext* BSParser::StatementsContext::methodInvocation() {
  return getRuleContext<BSParser::MethodInvocationContext>(0);
}

BSParser::GradientContext* BSParser::StatementsContext::gradient() {
  return getRuleContext<BSParser::GradientContext>(0);
}

BSParser::DetectContext* BSParser::StatementsContext::detect() {
  return getRuleContext<BSParser::DetectContext>(0);
}

BSParser::StoreContext* BSParser::StatementsContext::store() {
  return getRuleContext<BSParser::StoreContext>(0);
}

BSParser::MathContext* BSParser::StatementsContext::math() {
  return getRuleContext<BSParser::MathContext>(0);
}

BSParser::NumberAssignmentContext* BSParser::StatementsContext::numberAssignment() {
  return getRuleContext<BSParser::NumberAssignmentContext>(0);
}


size_t BSParser::StatementsContext::getRuleIndex() const {
  return BSParser::RuleStatements;
}

void BSParser::StatementsContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterStatements(this);
}

void BSParser::StatementsContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitStatements(this);
}


antlrcpp::Any BSParser::StatementsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitStatements(this);
  else
    return visitor->visitChildren(this);
}

BSParser::StatementsContext* BSParser::statements() {
  StatementsContext *_localctx = _tracker.createInstance<StatementsContext>(_ctx, getState());
  enterRule(_localctx, 26, BSParser::RuleStatements);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    setState(193);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 12, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(178);
      ifStatement();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(179);
      whileStatement();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(180);
      variableDefinition();
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(181);
      repeat();
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(182);
      heat();
      break;
    }

    case 6: {
      enterOuterAlt(_localctx, 6);
      setState(183);
      dispose();
      break;
    }

    case 7: {
      enterOuterAlt(_localctx, 7);
      setState(184);
      mix();
      break;
    }

    case 8: {
      enterOuterAlt(_localctx, 8);
      setState(185);
      dispense();
      break;
    }

    case 9: {
      enterOuterAlt(_localctx, 9);
      setState(186);
      split();
      break;
    }

    case 10: {
      enterOuterAlt(_localctx, 10);
      setState(187);
      methodInvocation();
      break;
    }

    case 11: {
      enterOuterAlt(_localctx, 11);
      setState(188);
      gradient();
      break;
    }

    case 12: {
      enterOuterAlt(_localctx, 12);
      setState(189);
      detect();
      break;
    }

    case 13: {
      enterOuterAlt(_localctx, 13);
      setState(190);
      store();
      break;
    }

    case 14: {
      enterOuterAlt(_localctx, 14);
      setState(191);
      math();
      break;
    }

    case 15: {
      enterOuterAlt(_localctx, 15);
      setState(192);
      numberAssignment();
      break;
    }

    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- IfStatementContext ------------------------------------------------------------------

BSParser::IfStatementContext::IfStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::IfStatementContext::IF() {
  return getToken(BSParser::IF, 0);
}

BSParser::ParExpressionContext* BSParser::IfStatementContext::parExpression() {
  return getRuleContext<BSParser::ParExpressionContext>(0);
}

std::vector<BSParser::BlockStatementContext *> BSParser::IfStatementContext::blockStatement() {
  return getRuleContexts<BSParser::BlockStatementContext>();
}

BSParser::BlockStatementContext* BSParser::IfStatementContext::blockStatement(size_t i) {
  return getRuleContext<BSParser::BlockStatementContext>(i);
}

tree::TerminalNode* BSParser::IfStatementContext::ELSE() {
  return getToken(BSParser::ELSE, 0);
}


size_t BSParser::IfStatementContext::getRuleIndex() const {
  return BSParser::RuleIfStatement;
}

void BSParser::IfStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterIfStatement(this);
}

void BSParser::IfStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitIfStatement(this);
}


antlrcpp::Any BSParser::IfStatementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitIfStatement(this);
  else
    return visitor->visitChildren(this);
}

BSParser::IfStatementContext* BSParser::ifStatement() {
  IfStatementContext *_localctx = _tracker.createInstance<IfStatementContext>(_ctx, getState());
  enterRule(_localctx, 28, BSParser::RuleIfStatement);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(195);
    match(BSParser::IF);
    setState(196);
    parExpression();
    setState(197);
    blockStatement();
    setState(200);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::ELSE) {
      setState(198);
      match(BSParser::ELSE);
      setState(199);
      blockStatement();
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- WhileStatementContext ------------------------------------------------------------------

BSParser::WhileStatementContext::WhileStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::WhileStatementContext::WHILE() {
  return getToken(BSParser::WHILE, 0);
}

BSParser::ParExpressionContext* BSParser::WhileStatementContext::parExpression() {
  return getRuleContext<BSParser::ParExpressionContext>(0);
}

BSParser::BlockStatementContext* BSParser::WhileStatementContext::blockStatement() {
  return getRuleContext<BSParser::BlockStatementContext>(0);
}


size_t BSParser::WhileStatementContext::getRuleIndex() const {
  return BSParser::RuleWhileStatement;
}

void BSParser::WhileStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterWhileStatement(this);
}

void BSParser::WhileStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitWhileStatement(this);
}


antlrcpp::Any BSParser::WhileStatementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitWhileStatement(this);
  else
    return visitor->visitChildren(this);
}

BSParser::WhileStatementContext* BSParser::whileStatement() {
  WhileStatementContext *_localctx = _tracker.createInstance<WhileStatementContext>(_ctx, getState());
  enterRule(_localctx, 30, BSParser::RuleWhileStatement);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(202);
    match(BSParser::WHILE);
    setState(203);
    parExpression();
    setState(204);
    blockStatement();

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- RepeatContext ------------------------------------------------------------------

BSParser::RepeatContext::RepeatContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::RepeatContext::REPEAT() {
  return getToken(BSParser::REPEAT, 0);
}

tree::TerminalNode* BSParser::RepeatContext::INTEGER_LITERAL() {
  return getToken(BSParser::INTEGER_LITERAL, 0);
}

tree::TerminalNode* BSParser::RepeatContext::TIMES() {
  return getToken(BSParser::TIMES, 0);
}

BSParser::BlockStatementContext* BSParser::RepeatContext::blockStatement() {
  return getRuleContext<BSParser::BlockStatementContext>(0);
}


size_t BSParser::RepeatContext::getRuleIndex() const {
  return BSParser::RuleRepeat;
}

void BSParser::RepeatContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterRepeat(this);
}

void BSParser::RepeatContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitRepeat(this);
}


antlrcpp::Any BSParser::RepeatContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitRepeat(this);
  else
    return visitor->visitChildren(this);
}

BSParser::RepeatContext* BSParser::repeat() {
  RepeatContext *_localctx = _tracker.createInstance<RepeatContext>(_ctx, getState());
  enterRule(_localctx, 32, BSParser::RuleRepeat);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(206);
    match(BSParser::REPEAT);
    setState(207);
    match(BSParser::INTEGER_LITERAL);
    setState(208);
    match(BSParser::TIMES);
    setState(209);
    blockStatement();

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- HeatContext ------------------------------------------------------------------

BSParser::HeatContext::HeatContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::HeatContext::HEAT() {
  return getToken(BSParser::HEAT, 0);
}

BSParser::VariableContext* BSParser::HeatContext::variable() {
  return getRuleContext<BSParser::VariableContext>(0);
}

tree::TerminalNode* BSParser::HeatContext::AT() {
  return getToken(BSParser::AT, 0);
}

BSParser::TemperatureIdentifierContext* BSParser::HeatContext::temperatureIdentifier() {
  return getRuleContext<BSParser::TemperatureIdentifierContext>(0);
}

tree::TerminalNode* BSParser::HeatContext::FOR() {
  return getToken(BSParser::FOR, 0);
}

BSParser::TimeIdentifierContext* BSParser::HeatContext::timeIdentifier() {
  return getRuleContext<BSParser::TimeIdentifierContext>(0);
}


size_t BSParser::HeatContext::getRuleIndex() const {
  return BSParser::RuleHeat;
}

void BSParser::HeatContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterHeat(this);
}

void BSParser::HeatContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitHeat(this);
}


antlrcpp::Any BSParser::HeatContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitHeat(this);
  else
    return visitor->visitChildren(this);
}

BSParser::HeatContext* BSParser::heat() {
  HeatContext *_localctx = _tracker.createInstance<HeatContext>(_ctx, getState());
  enterRule(_localctx, 34, BSParser::RuleHeat);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(211);
    match(BSParser::HEAT);
    setState(212);
    variable();
    setState(213);
    match(BSParser::AT);
    setState(214);
    temperatureIdentifier();
    setState(217);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::FOR) {
      setState(215);
      match(BSParser::FOR);
      setState(216);
      timeIdentifier();
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DisposeContext ------------------------------------------------------------------

BSParser::DisposeContext::DisposeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::DisposeContext::DRAIN() {
  return getToken(BSParser::DRAIN, 0);
}

BSParser::VariableContext* BSParser::DisposeContext::variable() {
  return getRuleContext<BSParser::VariableContext>(0);
}

tree::TerminalNode* BSParser::DisposeContext::DISPOSE() {
  return getToken(BSParser::DISPOSE, 0);
}


size_t BSParser::DisposeContext::getRuleIndex() const {
  return BSParser::RuleDispose;
}

void BSParser::DisposeContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterDispose(this);
}

void BSParser::DisposeContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitDispose(this);
}


antlrcpp::Any BSParser::DisposeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitDispose(this);
  else
    return visitor->visitChildren(this);
}

BSParser::DisposeContext* BSParser::dispose() {
  DisposeContext *_localctx = _tracker.createInstance<DisposeContext>(_ctx, getState());
  enterRule(_localctx, 36, BSParser::RuleDispose);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    setState(223);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BSParser::DRAIN: {
        enterOuterAlt(_localctx, 1);
        setState(219);
        match(BSParser::DRAIN);
        setState(220);
        variable();
        break;
      }

      case BSParser::DISPOSE: {
        enterOuterAlt(_localctx, 2);
        setState(221);
        match(BSParser::DISPOSE);
        setState(222);
        variable();
        break;
      }

    default:
      throw NoViableAltException(this);
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- MixContext ------------------------------------------------------------------

BSParser::MixContext::MixContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::VariableDefinitionContext* BSParser::MixContext::variableDefinition() {
  return getRuleContext<BSParser::VariableDefinitionContext>(0);
}

tree::TerminalNode* BSParser::MixContext::MIX() {
  return getToken(BSParser::MIX, 0);
}

std::vector<BSParser::VariableContext *> BSParser::MixContext::variable() {
  return getRuleContexts<BSParser::VariableContext>();
}

BSParser::VariableContext* BSParser::MixContext::variable(size_t i) {
  return getRuleContext<BSParser::VariableContext>(i);
}

tree::TerminalNode* BSParser::MixContext::WITH() {
  return getToken(BSParser::WITH, 0);
}

std::vector<BSParser::UnitTrackerContext *> BSParser::MixContext::unitTracker() {
  return getRuleContexts<BSParser::UnitTrackerContext>();
}

BSParser::UnitTrackerContext* BSParser::MixContext::unitTracker(size_t i) {
  return getRuleContext<BSParser::UnitTrackerContext>(i);
}

tree::TerminalNode* BSParser::MixContext::FOR() {
  return getToken(BSParser::FOR, 0);
}

BSParser::TimeIdentifierContext* BSParser::MixContext::timeIdentifier() {
  return getRuleContext<BSParser::TimeIdentifierContext>(0);
}


size_t BSParser::MixContext::getRuleIndex() const {
  return BSParser::RuleMix;
}

void BSParser::MixContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterMix(this);
}

void BSParser::MixContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitMix(this);
}


antlrcpp::Any BSParser::MixContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitMix(this);
  else
    return visitor->visitChildren(this);
}

BSParser::MixContext* BSParser::mix() {
  MixContext *_localctx = _tracker.createInstance<MixContext>(_ctx, getState());
  enterRule(_localctx, 38, BSParser::RuleMix);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(225);
    variableDefinition();
    setState(226);
    match(BSParser::MIX);
    setState(228);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::INTEGER_LITERAL) {
      setState(227);
      unitTracker();
    }
    setState(230);
    variable();
    setState(231);
    match(BSParser::WITH);
    setState(233);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::INTEGER_LITERAL) {
      setState(232);
      unitTracker();
    }
    setState(235);
    variable();
    setState(238);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::FOR) {
      setState(236);
      match(BSParser::FOR);
      setState(237);
      timeIdentifier();
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DetectContext ------------------------------------------------------------------

BSParser::DetectContext::DetectContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::VariableDefinitionContext* BSParser::DetectContext::variableDefinition() {
  return getRuleContext<BSParser::VariableDefinitionContext>(0);
}

tree::TerminalNode* BSParser::DetectContext::DETECT() {
  return getToken(BSParser::DETECT, 0);
}

tree::TerminalNode* BSParser::DetectContext::IDENTIFIER() {
  return getToken(BSParser::IDENTIFIER, 0);
}

tree::TerminalNode* BSParser::DetectContext::ON() {
  return getToken(BSParser::ON, 0);
}

BSParser::VariableContext* BSParser::DetectContext::variable() {
  return getRuleContext<BSParser::VariableContext>(0);
}

tree::TerminalNode* BSParser::DetectContext::FOR() {
  return getToken(BSParser::FOR, 0);
}

BSParser::TimeIdentifierContext* BSParser::DetectContext::timeIdentifier() {
  return getRuleContext<BSParser::TimeIdentifierContext>(0);
}


size_t BSParser::DetectContext::getRuleIndex() const {
  return BSParser::RuleDetect;
}

void BSParser::DetectContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterDetect(this);
}

void BSParser::DetectContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitDetect(this);
}


antlrcpp::Any BSParser::DetectContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitDetect(this);
  else
    return visitor->visitChildren(this);
}

BSParser::DetectContext* BSParser::detect() {
  DetectContext *_localctx = _tracker.createInstance<DetectContext>(_ctx, getState());
  enterRule(_localctx, 40, BSParser::RuleDetect);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(240);
    variableDefinition();
    setState(241);
    match(BSParser::DETECT);
    setState(242);
    match(BSParser::IDENTIFIER);
    setState(243);
    match(BSParser::ON);
    setState(244);
    variable();
    setState(247);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::FOR) {
      setState(245);
      match(BSParser::FOR);
      setState(246);
      timeIdentifier();
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SplitContext ------------------------------------------------------------------

BSParser::SplitContext::SplitContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::VariableDefinitionContext* BSParser::SplitContext::variableDefinition() {
  return getRuleContext<BSParser::VariableDefinitionContext>(0);
}

tree::TerminalNode* BSParser::SplitContext::SPLIT() {
  return getToken(BSParser::SPLIT, 0);
}

BSParser::VariableContext* BSParser::SplitContext::variable() {
  return getRuleContext<BSParser::VariableContext>(0);
}

tree::TerminalNode* BSParser::SplitContext::INTO() {
  return getToken(BSParser::INTO, 0);
}

tree::TerminalNode* BSParser::SplitContext::INTEGER_LITERAL() {
  return getToken(BSParser::INTEGER_LITERAL, 0);
}


size_t BSParser::SplitContext::getRuleIndex() const {
  return BSParser::RuleSplit;
}

void BSParser::SplitContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterSplit(this);
}

void BSParser::SplitContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitSplit(this);
}


antlrcpp::Any BSParser::SplitContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitSplit(this);
  else
    return visitor->visitChildren(this);
}

BSParser::SplitContext* BSParser::split() {
  SplitContext *_localctx = _tracker.createInstance<SplitContext>(_ctx, getState());
  enterRule(_localctx, 42, BSParser::RuleSplit);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(249);
    variableDefinition();
    setState(250);
    match(BSParser::SPLIT);
    setState(251);
    variable();
    setState(252);
    match(BSParser::INTO);
    setState(253);
    match(BSParser::INTEGER_LITERAL);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DispenseContext ------------------------------------------------------------------

BSParser::DispenseContext::DispenseContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::VariableDefinitionContext* BSParser::DispenseContext::variableDefinition() {
  return getRuleContext<BSParser::VariableDefinitionContext>(0);
}

tree::TerminalNode* BSParser::DispenseContext::DISPENSE() {
  return getToken(BSParser::DISPENSE, 0);
}

tree::TerminalNode* BSParser::DispenseContext::IDENTIFIER() {
  return getToken(BSParser::IDENTIFIER, 0);
}

BSParser::UnitTrackerContext* BSParser::DispenseContext::unitTracker() {
  return getRuleContext<BSParser::UnitTrackerContext>(0);
}


size_t BSParser::DispenseContext::getRuleIndex() const {
  return BSParser::RuleDispense;
}

void BSParser::DispenseContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterDispense(this);
}

void BSParser::DispenseContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitDispense(this);
}


antlrcpp::Any BSParser::DispenseContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitDispense(this);
  else
    return visitor->visitChildren(this);
}

BSParser::DispenseContext* BSParser::dispense() {
  DispenseContext *_localctx = _tracker.createInstance<DispenseContext>(_ctx, getState());
  enterRule(_localctx, 44, BSParser::RuleDispense);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(255);
    variableDefinition();
    setState(256);
    match(BSParser::DISPENSE);
    setState(258);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::INTEGER_LITERAL) {
      setState(257);
      unitTracker();
    }
    setState(260);
    match(BSParser::IDENTIFIER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- GradientContext ------------------------------------------------------------------

BSParser::GradientContext::GradientContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::VariableDefinitionContext* BSParser::GradientContext::variableDefinition() {
  return getRuleContext<BSParser::VariableDefinitionContext>(0);
}

tree::TerminalNode* BSParser::GradientContext::GRADIENT() {
  return getToken(BSParser::GRADIENT, 0);
}

std::vector<tree::TerminalNode *> BSParser::GradientContext::IDENTIFIER() {
  return getTokens(BSParser::IDENTIFIER);
}

tree::TerminalNode* BSParser::GradientContext::IDENTIFIER(size_t i) {
  return getToken(BSParser::IDENTIFIER, i);
}

tree::TerminalNode* BSParser::GradientContext::WITH() {
  return getToken(BSParser::WITH, 0);
}

tree::TerminalNode* BSParser::GradientContext::RANGE() {
  return getToken(BSParser::RANGE, 0);
}

std::vector<tree::TerminalNode *> BSParser::GradientContext::INTEGER_LITERAL() {
  return getTokens(BSParser::INTEGER_LITERAL);
}

tree::TerminalNode* BSParser::GradientContext::INTEGER_LITERAL(size_t i) {
  return getToken(BSParser::INTEGER_LITERAL, i);
}

tree::TerminalNode* BSParser::GradientContext::COMMA() {
  return getToken(BSParser::COMMA, 0);
}

tree::TerminalNode* BSParser::GradientContext::AT() {
  return getToken(BSParser::AT, 0);
}


size_t BSParser::GradientContext::getRuleIndex() const {
  return BSParser::RuleGradient;
}

void BSParser::GradientContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterGradient(this);
}

void BSParser::GradientContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitGradient(this);
}


antlrcpp::Any BSParser::GradientContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitGradient(this);
  else
    return visitor->visitChildren(this);
}

BSParser::GradientContext* BSParser::gradient() {
  GradientContext *_localctx = _tracker.createInstance<GradientContext>(_ctx, getState());
  enterRule(_localctx, 46, BSParser::RuleGradient);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(262);
    variableDefinition();
    setState(263);
    match(BSParser::GRADIENT);
    setState(264);
    match(BSParser::IDENTIFIER);
    setState(265);
    match(BSParser::WITH);
    setState(266);
    match(BSParser::IDENTIFIER);
    setState(267);
    match(BSParser::RANGE);
    setState(268);
    match(BSParser::INTEGER_LITERAL);
    setState(269);
    match(BSParser::COMMA);
    setState(270);
    match(BSParser::INTEGER_LITERAL);
    setState(271);
    match(BSParser::AT);
    setState(272);
    match(BSParser::INTEGER_LITERAL);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StoreContext ------------------------------------------------------------------

BSParser::StoreContext::StoreContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::StoreContext::STORE() {
  return getToken(BSParser::STORE, 0);
}

BSParser::VariableContext* BSParser::StoreContext::variable() {
  return getRuleContext<BSParser::VariableContext>(0);
}


size_t BSParser::StoreContext::getRuleIndex() const {
  return BSParser::RuleStore;
}

void BSParser::StoreContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterStore(this);
}

void BSParser::StoreContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitStore(this);
}


antlrcpp::Any BSParser::StoreContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitStore(this);
  else
    return visitor->visitChildren(this);
}

BSParser::StoreContext* BSParser::store() {
  StoreContext *_localctx = _tracker.createInstance<StoreContext>(_ctx, getState());
  enterRule(_localctx, 48, BSParser::RuleStore);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(274);
    match(BSParser::STORE);
    setState(275);
    variable();

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberAssignmentContext ------------------------------------------------------------------

BSParser::NumberAssignmentContext::NumberAssignmentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::VariableDefinitionContext* BSParser::NumberAssignmentContext::variableDefinition() {
  return getRuleContext<BSParser::VariableDefinitionContext>(0);
}

BSParser::LiteralContext* BSParser::NumberAssignmentContext::literal() {
  return getRuleContext<BSParser::LiteralContext>(0);
}


size_t BSParser::NumberAssignmentContext::getRuleIndex() const {
  return BSParser::RuleNumberAssignment;
}

void BSParser::NumberAssignmentContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterNumberAssignment(this);
}

void BSParser::NumberAssignmentContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitNumberAssignment(this);
}


antlrcpp::Any BSParser::NumberAssignmentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitNumberAssignment(this);
  else
    return visitor->visitChildren(this);
}

BSParser::NumberAssignmentContext* BSParser::numberAssignment() {
  NumberAssignmentContext *_localctx = _tracker.createInstance<NumberAssignmentContext>(_ctx, getState());
  enterRule(_localctx, 50, BSParser::RuleNumberAssignment);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(277);
    variableDefinition();
    setState(278);
    literal();

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- MathContext ------------------------------------------------------------------

BSParser::MathContext::MathContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::VariableDefinitionContext* BSParser::MathContext::variableDefinition() {
  return getRuleContext<BSParser::VariableDefinitionContext>(0);
}

std::vector<BSParser::PrimaryContext *> BSParser::MathContext::primary() {
  return getRuleContexts<BSParser::PrimaryContext>();
}

BSParser::PrimaryContext* BSParser::MathContext::primary(size_t i) {
  return getRuleContext<BSParser::PrimaryContext>(i);
}

tree::TerminalNode* BSParser::MathContext::MULTIPLY() {
  return getToken(BSParser::MULTIPLY, 0);
}

tree::TerminalNode* BSParser::MathContext::DIVIDE() {
  return getToken(BSParser::DIVIDE, 0);
}

tree::TerminalNode* BSParser::MathContext::ADDITION() {
  return getToken(BSParser::ADDITION, 0);
}

tree::TerminalNode* BSParser::MathContext::SUBTRACT() {
  return getToken(BSParser::SUBTRACT, 0);
}


size_t BSParser::MathContext::getRuleIndex() const {
  return BSParser::RuleMath;
}

void BSParser::MathContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterMath(this);
}

void BSParser::MathContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitMath(this);
}


antlrcpp::Any BSParser::MathContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitMath(this);
  else
    return visitor->visitChildren(this);
}

BSParser::MathContext* BSParser::math() {
  MathContext *_localctx = _tracker.createInstance<MathContext>(_ctx, getState());
  enterRule(_localctx, 52, BSParser::RuleMath);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    setState(290);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 21, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(280);
      variableDefinition();
      setState(281);
      primary();
      setState(282);
      dynamic_cast<MathContext *>(_localctx)->bop = _input->LT(1);
      _la = _input->LA(1);
      if (!(((((_la - 68) & ~ 0x3fULL) == 0) &&
        ((1ULL << (_la - 68)) & ((1ULL << (BSParser::MULTIPLY - 68))
        | (1ULL << (BSParser::DIVIDE - 68))
        | (1ULL << (BSParser::MOD - 68)))) != 0))) {
        dynamic_cast<MathContext *>(_localctx)->bop = _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(283);
      primary();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(285);
      variableDefinition();
      setState(286);
      primary();
      setState(287);
      dynamic_cast<MathContext *>(_localctx)->bop = _input->LT(1);
      _la = _input->LA(1);
      if (!(_la == BSParser::ADDITION

      || _la == BSParser::SUBTRACT)) {
        dynamic_cast<MathContext *>(_localctx)->bop = _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(288);
      primary();
      break;
    }

    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- BinopsContext ------------------------------------------------------------------

BSParser::BinopsContext::BinopsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BSParser::PrimaryContext *> BSParser::BinopsContext::primary() {
  return getRuleContexts<BSParser::PrimaryContext>();
}

BSParser::PrimaryContext* BSParser::BinopsContext::primary(size_t i) {
  return getRuleContext<BSParser::PrimaryContext>(i);
}

std::vector<tree::TerminalNode *> BSParser::BinopsContext::LT() {
  return getTokens(BSParser::LT);
}

tree::TerminalNode* BSParser::BinopsContext::LT(size_t i) {
  return getToken(BSParser::LT, i);
}

std::vector<tree::TerminalNode *> BSParser::BinopsContext::GT() {
  return getTokens(BSParser::GT);
}

tree::TerminalNode* BSParser::BinopsContext::GT(size_t i) {
  return getToken(BSParser::GT, i);
}

tree::TerminalNode* BSParser::BinopsContext::LTE() {
  return getToken(BSParser::LTE, 0);
}

tree::TerminalNode* BSParser::BinopsContext::GTE() {
  return getToken(BSParser::GTE, 0);
}

tree::TerminalNode* BSParser::BinopsContext::EQUALITY() {
  return getToken(BSParser::EQUALITY, 0);
}

tree::TerminalNode* BSParser::BinopsContext::NOTEQUAL() {
  return getToken(BSParser::NOTEQUAL, 0);
}


size_t BSParser::BinopsContext::getRuleIndex() const {
  return BSParser::RuleBinops;
}

void BSParser::BinopsContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterBinops(this);
}

void BSParser::BinopsContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitBinops(this);
}


antlrcpp::Any BSParser::BinopsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitBinops(this);
  else
    return visitor->visitChildren(this);
}

BSParser::BinopsContext* BSParser::binops() {
  BinopsContext *_localctx = _tracker.createInstance<BinopsContext>(_ctx, getState());
  enterRule(_localctx, 54, BSParser::RuleBinops);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    setState(312);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(292);
      primary();
      setState(300);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx)) {
      case 1: {
        setState(293);
        match(BSParser::LT);
        setState(294);
        match(BSParser::LT);
        break;
      }

      case 2: {
        setState(295);
        match(BSParser::GT);
        setState(296);
        match(BSParser::GT);
        setState(297);
        match(BSParser::GT);
        break;
      }

      case 3: {
        setState(298);
        match(BSParser::GT);
        setState(299);
        match(BSParser::GT);
        break;
      }

      }
      setState(302);
      primary();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(304);
      primary();
      setState(305);
      dynamic_cast<BinopsContext *>(_localctx)->bop = _input->LT(1);
      _la = _input->LA(1);
      if (!((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & ((1ULL << BSParser::GT)
        | (1ULL << BSParser::LT)
        | (1ULL << BSParser::LTE)
        | (1ULL << BSParser::GTE))) != 0))) {
        dynamic_cast<BinopsContext *>(_localctx)->bop = _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(306);
      primary();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(308);
      primary();
      setState(309);
      dynamic_cast<BinopsContext *>(_localctx)->bop = _input->LT(1);
      _la = _input->LA(1);
      if (!(_la == BSParser::EQUALITY

      || _la == BSParser::NOTEQUAL)) {
        dynamic_cast<BinopsContext *>(_localctx)->bop = _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(310);
      primary();
      break;
    }

    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ParExpressionContext ------------------------------------------------------------------

BSParser::ParExpressionContext::ParExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::ParExpressionContext::LPAREN() {
  return getToken(BSParser::LPAREN, 0);
}

std::vector<BSParser::BinopsContext *> BSParser::ParExpressionContext::binops() {
  return getRuleContexts<BSParser::BinopsContext>();
}

BSParser::BinopsContext* BSParser::ParExpressionContext::binops(size_t i) {
  return getRuleContext<BSParser::BinopsContext>(i);
}

tree::TerminalNode* BSParser::ParExpressionContext::RPAREN() {
  return getToken(BSParser::RPAREN, 0);
}

std::vector<tree::TerminalNode *> BSParser::ParExpressionContext::AND() {
  return getTokens(BSParser::AND);
}

tree::TerminalNode* BSParser::ParExpressionContext::AND(size_t i) {
  return getToken(BSParser::AND, i);
}

std::vector<tree::TerminalNode *> BSParser::ParExpressionContext::OR() {
  return getTokens(BSParser::OR);
}

tree::TerminalNode* BSParser::ParExpressionContext::OR(size_t i) {
  return getToken(BSParser::OR, i);
}


size_t BSParser::ParExpressionContext::getRuleIndex() const {
  return BSParser::RuleParExpression;
}

void BSParser::ParExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterParExpression(this);
}

void BSParser::ParExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitParExpression(this);
}


antlrcpp::Any BSParser::ParExpressionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitParExpression(this);
  else
    return visitor->visitChildren(this);
}

BSParser::ParExpressionContext* BSParser::parExpression() {
  ParExpressionContext *_localctx = _tracker.createInstance<ParExpressionContext>(_ctx, getState());
  enterRule(_localctx, 56, BSParser::RuleParExpression);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(314);
    match(BSParser::LPAREN);
    setState(315);
    binops();
    setState(320);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BSParser::AND

    || _la == BSParser::OR) {
      setState(316);
      _la = _input->LA(1);
      if (!(_la == BSParser::AND

      || _la == BSParser::OR)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(317);
      binops();
      setState(322);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(323);
    match(BSParser::RPAREN);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- MethodInvocationContext ------------------------------------------------------------------

BSParser::MethodInvocationContext::MethodInvocationContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::VariableDefinitionContext* BSParser::MethodInvocationContext::variableDefinition() {
  return getRuleContext<BSParser::VariableDefinitionContext>(0);
}

BSParser::MethodCallContext* BSParser::MethodInvocationContext::methodCall() {
  return getRuleContext<BSParser::MethodCallContext>(0);
}


size_t BSParser::MethodInvocationContext::getRuleIndex() const {
  return BSParser::RuleMethodInvocation;
}

void BSParser::MethodInvocationContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterMethodInvocation(this);
}

void BSParser::MethodInvocationContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitMethodInvocation(this);
}


antlrcpp::Any BSParser::MethodInvocationContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitMethodInvocation(this);
  else
    return visitor->visitChildren(this);
}

BSParser::MethodInvocationContext* BSParser::methodInvocation() {
  MethodInvocationContext *_localctx = _tracker.createInstance<MethodInvocationContext>(_ctx, getState());
  enterRule(_localctx, 58, BSParser::RuleMethodInvocation);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(325);
    variableDefinition();
    setState(326);
    methodCall();

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- MethodCallContext ------------------------------------------------------------------

BSParser::MethodCallContext::MethodCallContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::MethodCallContext::IDENTIFIER() {
  return getToken(BSParser::IDENTIFIER, 0);
}

tree::TerminalNode* BSParser::MethodCallContext::LPAREN() {
  return getToken(BSParser::LPAREN, 0);
}

tree::TerminalNode* BSParser::MethodCallContext::RPAREN() {
  return getToken(BSParser::RPAREN, 0);
}

BSParser::ExpressionListContext* BSParser::MethodCallContext::expressionList() {
  return getRuleContext<BSParser::ExpressionListContext>(0);
}


size_t BSParser::MethodCallContext::getRuleIndex() const {
  return BSParser::RuleMethodCall;
}

void BSParser::MethodCallContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterMethodCall(this);
}

void BSParser::MethodCallContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitMethodCall(this);
}


antlrcpp::Any BSParser::MethodCallContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitMethodCall(this);
  else
    return visitor->visitChildren(this);
}

BSParser::MethodCallContext* BSParser::methodCall() {
  MethodCallContext *_localctx = _tracker.createInstance<MethodCallContext>(_ctx, getState());
  enterRule(_localctx, 60, BSParser::RuleMethodCall);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(328);
    match(BSParser::IDENTIFIER);
    setState(329);
    match(BSParser::LPAREN);
    setState(331);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << BSParser::IDENTIFIER)
      | (1ULL << BSParser::STRING_LITERAL)
      | (1ULL << BSParser::BOOL_LITERAL)
      | (1ULL << BSParser::FLOAT_LITERAL)
      | (1ULL << BSParser::INTEGER_LITERAL))) != 0)) {
      setState(330);
      expressionList();
    }
    setState(333);
    match(BSParser::RPAREN);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ExpressionListContext ------------------------------------------------------------------

BSParser::ExpressionListContext::ExpressionListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BSParser::PrimaryContext *> BSParser::ExpressionListContext::primary() {
  return getRuleContexts<BSParser::PrimaryContext>();
}

BSParser::PrimaryContext* BSParser::ExpressionListContext::primary(size_t i) {
  return getRuleContext<BSParser::PrimaryContext>(i);
}

std::vector<tree::TerminalNode *> BSParser::ExpressionListContext::COMMA() {
  return getTokens(BSParser::COMMA);
}

tree::TerminalNode* BSParser::ExpressionListContext::COMMA(size_t i) {
  return getToken(BSParser::COMMA, i);
}


size_t BSParser::ExpressionListContext::getRuleIndex() const {
  return BSParser::RuleExpressionList;
}

void BSParser::ExpressionListContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterExpressionList(this);
}

void BSParser::ExpressionListContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitExpressionList(this);
}


antlrcpp::Any BSParser::ExpressionListContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitExpressionList(this);
  else
    return visitor->visitChildren(this);
}

BSParser::ExpressionListContext* BSParser::expressionList() {
  ExpressionListContext *_localctx = _tracker.createInstance<ExpressionListContext>(_ctx, getState());
  enterRule(_localctx, 62, BSParser::RuleExpressionList);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(335);
    primary();
    setState(340);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BSParser::COMMA) {
      setState(336);
      match(BSParser::COMMA);
      setState(337);
      primary();
      setState(342);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- TypeTypeContext ------------------------------------------------------------------

BSParser::TypeTypeContext::TypeTypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::PrimitiveTypeContext* BSParser::TypeTypeContext::primitiveType() {
  return getRuleContext<BSParser::PrimitiveTypeContext>(0);
}


size_t BSParser::TypeTypeContext::getRuleIndex() const {
  return BSParser::RuleTypeType;
}

void BSParser::TypeTypeContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterTypeType(this);
}

void BSParser::TypeTypeContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitTypeType(this);
}


antlrcpp::Any BSParser::TypeTypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitTypeType(this);
  else
    return visitor->visitChildren(this);
}

BSParser::TypeTypeContext* BSParser::typeType() {
  TypeTypeContext *_localctx = _tracker.createInstance<TypeTypeContext>(_ctx, getState());
  enterRule(_localctx, 64, BSParser::RuleTypeType);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(343);
    primitiveType();

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- UnionTypeContext ------------------------------------------------------------------

BSParser::UnionTypeContext::UnionTypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::UnionTypeContext::LBRACKET() {
  return getToken(BSParser::LBRACKET, 0);
}

BSParser::TypesListContext* BSParser::UnionTypeContext::typesList() {
  return getRuleContext<BSParser::TypesListContext>(0);
}

tree::TerminalNode* BSParser::UnionTypeContext::RBRACKET() {
  return getToken(BSParser::RBRACKET, 0);
}


size_t BSParser::UnionTypeContext::getRuleIndex() const {
  return BSParser::RuleUnionType;
}

void BSParser::UnionTypeContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterUnionType(this);
}

void BSParser::UnionTypeContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitUnionType(this);
}


antlrcpp::Any BSParser::UnionTypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitUnionType(this);
  else
    return visitor->visitChildren(this);
}

BSParser::UnionTypeContext* BSParser::unionType() {
  UnionTypeContext *_localctx = _tracker.createInstance<UnionTypeContext>(_ctx, getState());
  enterRule(_localctx, 66, BSParser::RuleUnionType);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(345);
    match(BSParser::LBRACKET);
    setState(346);
    typesList();
    setState(347);
    match(BSParser::RBRACKET);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- TypesListContext ------------------------------------------------------------------

BSParser::TypesListContext::TypesListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<BSParser::TypeTypeContext *> BSParser::TypesListContext::typeType() {
  return getRuleContexts<BSParser::TypeTypeContext>();
}

BSParser::TypeTypeContext* BSParser::TypesListContext::typeType(size_t i) {
  return getRuleContext<BSParser::TypeTypeContext>(i);
}

std::vector<tree::TerminalNode *> BSParser::TypesListContext::SEMICOLON() {
  return getTokens(BSParser::SEMICOLON);
}

tree::TerminalNode* BSParser::TypesListContext::SEMICOLON(size_t i) {
  return getToken(BSParser::SEMICOLON, i);
}


size_t BSParser::TypesListContext::getRuleIndex() const {
  return BSParser::RuleTypesList;
}

void BSParser::TypesListContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterTypesList(this);
}

void BSParser::TypesListContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitTypesList(this);
}


antlrcpp::Any BSParser::TypesListContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitTypesList(this);
  else
    return visitor->visitChildren(this);
}

BSParser::TypesListContext* BSParser::typesList() {
  TypesListContext *_localctx = _tracker.createInstance<TypesListContext>(_ctx, getState());
  enterRule(_localctx, 68, BSParser::RuleTypesList);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(349);
    typeType();
    setState(354);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BSParser::SEMICOLON) {
      setState(350);
      match(BSParser::SEMICOLON);
      setState(351);
      typeType();
      setState(356);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- VariableDefinitionContext ------------------------------------------------------------------

BSParser::VariableDefinitionContext::VariableDefinitionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::VariableContext* BSParser::VariableDefinitionContext::variable() {
  return getRuleContext<BSParser::VariableContext>(0);
}

tree::TerminalNode* BSParser::VariableDefinitionContext::ASSIGN() {
  return getToken(BSParser::ASSIGN, 0);
}

BSParser::UnionTypeContext* BSParser::VariableDefinitionContext::unionType() {
  return getRuleContext<BSParser::UnionTypeContext>(0);
}


size_t BSParser::VariableDefinitionContext::getRuleIndex() const {
  return BSParser::RuleVariableDefinition;
}

void BSParser::VariableDefinitionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterVariableDefinition(this);
}

void BSParser::VariableDefinitionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitVariableDefinition(this);
}


antlrcpp::Any BSParser::VariableDefinitionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitVariableDefinition(this);
  else
    return visitor->visitChildren(this);
}

BSParser::VariableDefinitionContext* BSParser::variableDefinition() {
  VariableDefinitionContext *_localctx = _tracker.createInstance<VariableDefinitionContext>(_ctx, getState());
  enterRule(_localctx, 70, BSParser::RuleVariableDefinition);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(358);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::LBRACKET) {
      setState(357);
      unionType();
    }
    setState(360);
    variable();
    setState(361);
    match(BSParser::ASSIGN);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- VariableContext ------------------------------------------------------------------

BSParser::VariableContext::VariableContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::VariableContext::IDENTIFIER() {
  return getToken(BSParser::IDENTIFIER, 0);
}

tree::TerminalNode* BSParser::VariableContext::LBRACKET() {
  return getToken(BSParser::LBRACKET, 0);
}

tree::TerminalNode* BSParser::VariableContext::INTEGER_LITERAL() {
  return getToken(BSParser::INTEGER_LITERAL, 0);
}

tree::TerminalNode* BSParser::VariableContext::RBRACKET() {
  return getToken(BSParser::RBRACKET, 0);
}


size_t BSParser::VariableContext::getRuleIndex() const {
  return BSParser::RuleVariable;
}

void BSParser::VariableContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterVariable(this);
}

void BSParser::VariableContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitVariable(this);
}


antlrcpp::Any BSParser::VariableContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitVariable(this);
  else
    return visitor->visitChildren(this);
}

BSParser::VariableContext* BSParser::variable() {
  VariableContext *_localctx = _tracker.createInstance<VariableContext>(_ctx, getState());
  enterRule(_localctx, 72, BSParser::RuleVariable);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(363);
    match(BSParser::IDENTIFIER);
    setState(367);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 29, _ctx)) {
    case 1: {
      setState(364);
      match(BSParser::LBRACKET);
      setState(365);
      match(BSParser::INTEGER_LITERAL);
      setState(366);
      match(BSParser::RBRACKET);
      break;
    }

    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- PrimaryContext ------------------------------------------------------------------

BSParser::PrimaryContext::PrimaryContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

BSParser::LiteralContext* BSParser::PrimaryContext::literal() {
  return getRuleContext<BSParser::LiteralContext>(0);
}

BSParser::VariableContext* BSParser::PrimaryContext::variable() {
  return getRuleContext<BSParser::VariableContext>(0);
}


size_t BSParser::PrimaryContext::getRuleIndex() const {
  return BSParser::RulePrimary;
}

void BSParser::PrimaryContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterPrimary(this);
}

void BSParser::PrimaryContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitPrimary(this);
}


antlrcpp::Any BSParser::PrimaryContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitPrimary(this);
  else
    return visitor->visitChildren(this);
}

BSParser::PrimaryContext* BSParser::primary() {
  PrimaryContext *_localctx = _tracker.createInstance<PrimaryContext>(_ctx, getState());
  enterRule(_localctx, 74, BSParser::RulePrimary);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    setState(371);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BSParser::STRING_LITERAL:
      case BSParser::BOOL_LITERAL:
      case BSParser::FLOAT_LITERAL:
      case BSParser::INTEGER_LITERAL: {
        enterOuterAlt(_localctx, 1);
        setState(369);
        literal();
        break;
      }

      case BSParser::IDENTIFIER: {
        enterOuterAlt(_localctx, 2);
        setState(370);
        variable();
        break;
      }

    default:
      throw NoViableAltException(this);
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LiteralContext ------------------------------------------------------------------

BSParser::LiteralContext::LiteralContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::LiteralContext::INTEGER_LITERAL() {
  return getToken(BSParser::INTEGER_LITERAL, 0);
}

tree::TerminalNode* BSParser::LiteralContext::FLOAT_LITERAL() {
  return getToken(BSParser::FLOAT_LITERAL, 0);
}

tree::TerminalNode* BSParser::LiteralContext::BOOL_LITERAL() {
  return getToken(BSParser::BOOL_LITERAL, 0);
}

tree::TerminalNode* BSParser::LiteralContext::STRING_LITERAL() {
  return getToken(BSParser::STRING_LITERAL, 0);
}


size_t BSParser::LiteralContext::getRuleIndex() const {
  return BSParser::RuleLiteral;
}

void BSParser::LiteralContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterLiteral(this);
}

void BSParser::LiteralContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitLiteral(this);
}


antlrcpp::Any BSParser::LiteralContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitLiteral(this);
  else
    return visitor->visitChildren(this);
}

BSParser::LiteralContext* BSParser::literal() {
  LiteralContext *_localctx = _tracker.createInstance<LiteralContext>(_ctx, getState());
  enterRule(_localctx, 76, BSParser::RuleLiteral);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(373);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << BSParser::STRING_LITERAL)
      | (1ULL << BSParser::BOOL_LITERAL)
      | (1ULL << BSParser::FLOAT_LITERAL)
      | (1ULL << BSParser::INTEGER_LITERAL))) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- PrimitiveTypeContext ------------------------------------------------------------------

BSParser::PrimitiveTypeContext::PrimitiveTypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::PrimitiveTypeContext::BOOL() {
  return getToken(BSParser::BOOL, 0);
}

tree::TerminalNode* BSParser::PrimitiveTypeContext::NAT() {
  return getToken(BSParser::NAT, 0);
}

tree::TerminalNode* BSParser::PrimitiveTypeContext::REAL() {
  return getToken(BSParser::REAL, 0);
}

tree::TerminalNode* BSParser::PrimitiveTypeContext::MAT() {
  return getToken(BSParser::MAT, 0);
}


size_t BSParser::PrimitiveTypeContext::getRuleIndex() const {
  return BSParser::RulePrimitiveType;
}

void BSParser::PrimitiveTypeContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterPrimitiveType(this);
}

void BSParser::PrimitiveTypeContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitPrimitiveType(this);
}


antlrcpp::Any BSParser::PrimitiveTypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitPrimitiveType(this);
  else
    return visitor->visitChildren(this);
}

BSParser::PrimitiveTypeContext* BSParser::primitiveType() {
  PrimitiveTypeContext *_localctx = _tracker.createInstance<PrimitiveTypeContext>(_ctx, getState());
  enterRule(_localctx, 78, BSParser::RulePrimitiveType);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(375);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << BSParser::NAT)
      | (1ULL << BSParser::REAL)
      | (1ULL << BSParser::MAT)
      | (1ULL << BSParser::BOOL))) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- TimeIdentifierContext ------------------------------------------------------------------

BSParser::TimeIdentifierContext::TimeIdentifierContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::TimeIdentifierContext::TIME_NUMBER() {
  return getToken(BSParser::TIME_NUMBER, 0);
}


size_t BSParser::TimeIdentifierContext::getRuleIndex() const {
  return BSParser::RuleTimeIdentifier;
}

void BSParser::TimeIdentifierContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterTimeIdentifier(this);
}

void BSParser::TimeIdentifierContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitTimeIdentifier(this);
}


antlrcpp::Any BSParser::TimeIdentifierContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitTimeIdentifier(this);
  else
    return visitor->visitChildren(this);
}

BSParser::TimeIdentifierContext* BSParser::timeIdentifier() {
  TimeIdentifierContext *_localctx = _tracker.createInstance<TimeIdentifierContext>(_ctx, getState());
  enterRule(_localctx, 80, BSParser::RuleTimeIdentifier);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(377);
    match(BSParser::TIME_NUMBER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- TemperatureIdentifierContext ------------------------------------------------------------------

BSParser::TemperatureIdentifierContext::TemperatureIdentifierContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::TemperatureIdentifierContext::TEMP_NUMBER() {
  return getToken(BSParser::TEMP_NUMBER, 0);
}


size_t BSParser::TemperatureIdentifierContext::getRuleIndex() const {
  return BSParser::RuleTemperatureIdentifier;
}

void BSParser::TemperatureIdentifierContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterTemperatureIdentifier(this);
}

void BSParser::TemperatureIdentifierContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitTemperatureIdentifier(this);
}


antlrcpp::Any BSParser::TemperatureIdentifierContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitTemperatureIdentifier(this);
  else
    return visitor->visitChildren(this);
}

BSParser::TemperatureIdentifierContext* BSParser::temperatureIdentifier() {
  TemperatureIdentifierContext *_localctx = _tracker.createInstance<TemperatureIdentifierContext>(_ctx, getState());
  enterRule(_localctx, 82, BSParser::RuleTemperatureIdentifier);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(379);
    match(BSParser::TEMP_NUMBER);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- UnitTrackerContext ------------------------------------------------------------------

BSParser::UnitTrackerContext::UnitTrackerContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::UnitTrackerContext::INTEGER_LITERAL() {
  return getToken(BSParser::INTEGER_LITERAL, 0);
}

tree::TerminalNode* BSParser::UnitTrackerContext::UNITS() {
  return getToken(BSParser::UNITS, 0);
}

tree::TerminalNode* BSParser::UnitTrackerContext::OF() {
  return getToken(BSParser::OF, 0);
}


size_t BSParser::UnitTrackerContext::getRuleIndex() const {
  return BSParser::RuleUnitTracker;
}

void BSParser::UnitTrackerContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterUnitTracker(this);
}

void BSParser::UnitTrackerContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitUnitTracker(this);
}


antlrcpp::Any BSParser::UnitTrackerContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitUnitTracker(this);
  else
    return visitor->visitChildren(this);
}

BSParser::UnitTrackerContext* BSParser::unitTracker() {
  UnitTrackerContext *_localctx = _tracker.createInstance<UnitTrackerContext>(_ctx, getState());
  enterRule(_localctx, 84, BSParser::RuleUnitTracker);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(381);
    match(BSParser::INTEGER_LITERAL);
    setState(382);
    match(BSParser::UNITS);
    setState(383);
    match(BSParser::OF);

  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

// Static vars and initialization.
std::vector<dfa::DFA> BSParser::_decisionToDFA;
atn::PredictionContextCache BSParser::_sharedContextCache;

// We own the ATN which in turn owns the ATN states.
atn::ATN BSParser::_atn;
std::vector<uint16_t> BSParser::_serializedATN;

std::vector<std::string> BSParser::_ruleNames = {
  "progmaram", "globalDeclarations", "moduleDeclaration", "manifestDeclaration",
  "stationaryDeclaration", "functions", "functionDeclaration", "formalParameters",
  "formalParameterList", "formalParameter", "functionTyping", "returnStatement",
  "blockStatement", "statements", "ifStatement", "whileStatement", "repeat",
  "heat", "dispose", "mix", "detect", "split", "dispense", "gradient", "store",
  "numberAssignment", "math", "binops", "parExpression", "methodInvocation",
  "methodCall", "expressionList", "typeType", "unionType", "typesList",
  "variableDefinition", "variable", "primary", "literal", "primitiveType",
  "timeIdentifier", "temperatureIdentifier", "unitTracker"
};

std::vector<std::string> BSParser::_literalNames = {
  "", "'if'", "'else'", "'repeat'", "'while'", "'function'", "'return'",
  "'manifest'", "'module'", "'stationary'", "'functions'", "'instructions'",
  "'detect'", "'mix'", "'split'", "'heat'", "'drain'", "'dispense'", "'dispose'",
  "'gradient'", "'store'", "'range'", "'at'", "'with'", "'for'", "'into'",
  "'times'", "'on'", "'of'", "'units'", "'nat'", "'real'", "'mat'", "'bool'",
  "", "", "", "", "", "", "", "", "'('", "')'", "'{'", "'}'", "'['", "']'",
  "';'", "','", "'.'", "'='", "'>'", "'<'", "'!'", "'~'", "'?'", "':'",
  "'=='", "'<='", "'>='", "'!='", "'&&'", "'||'", "'++'", "'--'", "'+'",
  "'-'", "'*'", "'/'", "'&'", "'|'", "'^'", "'%'", "'_'", "'ns'", "'us'",
  "'ms'", "'cs'", "'ds'", "'s'", "'m'", "'h'", "'d'", "'w'", "'mo'", "'y'",
  "'nL'", "'uL'", "'mL'", "'cL'", "'dL'", "'L'", "'daL'", "'c'", "'f'",
  "'k'"
};

std::vector<std::string> BSParser::_symbolicNames = {
  "", "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", "RETURN", "MANIFEST",
  "MODULE", "STATIONARY", "FUNCTIONS", "INSTRUCTIONS", "DETECT", "MIX",
  "SPLIT", "HEAT", "DRAIN", "DISPENSE", "DISPOSE", "GRADIENT", "STORE",
  "RANGE", "AT", "WITH", "FOR", "INTO", "TIMES", "ON", "OF", "UNITS", "NAT",
  "REAL", "MAT", "BOOL", "IDENTIFIER", "STRING_LITERAL", "BOOL_LITERAL",
  "FLOAT_LITERAL", "INTEGER_LITERAL", "TIME_NUMBER", "VOLUME_NUMBER", "TEMP_NUMBER",
  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON",
  "COMMA", "DOT", "ASSIGN", "GT", "LT", "BANG", "TILDE", "QUESTION", "COLON",
  "EQUALITY", "LTE", "GTE", "NOTEQUAL", "AND", "OR", "INC", "DEC", "ADDITION",
  "SUBTRACT", "MULTIPLY", "DIVIDE", "BITAND", "BITOR", "CARET", "MOD", "UNDERSCORE",
  "NANOSECOND", "MICROSECOND", "MILLISECOND", "CENTISECOND", "DECISECOND",
  "SECOND", "MINUTE", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", "NANOLITRE",
  "MICROLITRE", "MILLILITRE", "CENTILITRE", "DECILITRE", "LITRE", "DECALITRE",
  "CELSIUS", "FAHRENHEIT", "KELVIN", "WS", "COMMENT", "LINE_COMMENT"
};

dfa::Vocabulary BSParser::_vocabulary(_literalNames, _symbolicNames);

std::vector<std::string> BSParser::_tokenNames;

BSParser::Initializer::Initializer() {
	for (size_t i = 0; i < _symbolicNames.size(); ++i) {
		std::string name = _vocabulary.getLiteralName(i);
		if (name.empty()) {
			name = _vocabulary.getSymbolicName(i);
		}

		if (name.empty()) {
			_tokenNames.push_back("<INVALID>");
		} else {
      _tokenNames.push_back(name);
    }
	}

  _serializedATN = {
    0x3, 0x608b, 0xa72a, 0x8133, 0xb9ed, 0x417c, 0x3be7, 0x7786, 0x5964,
    0x3, 0x65, 0x184, 0x4, 0x2, 0x9, 0x2, 0x4, 0x3, 0x9, 0x3, 0x4, 0x4,
    0x9, 0x4, 0x4, 0x5, 0x9, 0x5, 0x4, 0x6, 0x9, 0x6, 0x4, 0x7, 0x9, 0x7,
    0x4, 0x8, 0x9, 0x8, 0x4, 0x9, 0x9, 0x9, 0x4, 0xa, 0x9, 0xa, 0x4, 0xb,
    0x9, 0xb, 0x4, 0xc, 0x9, 0xc, 0x4, 0xd, 0x9, 0xd, 0x4, 0xe, 0x9, 0xe,
    0x4, 0xf, 0x9, 0xf, 0x4, 0x10, 0x9, 0x10, 0x4, 0x11, 0x9, 0x11, 0x4,
    0x12, 0x9, 0x12, 0x4, 0x13, 0x9, 0x13, 0x4, 0x14, 0x9, 0x14, 0x4, 0x15,
    0x9, 0x15, 0x4, 0x16, 0x9, 0x16, 0x4, 0x17, 0x9, 0x17, 0x4, 0x18, 0x9,
    0x18, 0x4, 0x19, 0x9, 0x19, 0x4, 0x1a, 0x9, 0x1a, 0x4, 0x1b, 0x9, 0x1b,
    0x4, 0x1c, 0x9, 0x1c, 0x4, 0x1d, 0x9, 0x1d, 0x4, 0x1e, 0x9, 0x1e, 0x4,
    0x1f, 0x9, 0x1f, 0x4, 0x20, 0x9, 0x20, 0x4, 0x21, 0x9, 0x21, 0x4, 0x22,
    0x9, 0x22, 0x4, 0x23, 0x9, 0x23, 0x4, 0x24, 0x9, 0x24, 0x4, 0x25, 0x9,
    0x25, 0x4, 0x26, 0x9, 0x26, 0x4, 0x27, 0x9, 0x27, 0x4, 0x28, 0x9, 0x28,
    0x4, 0x29, 0x9, 0x29, 0x4, 0x2a, 0x9, 0x2a, 0x4, 0x2b, 0x9, 0x2b, 0x4,
    0x2c, 0x9, 0x2c, 0x3, 0x2, 0x6, 0x2, 0x5a, 0xa, 0x2, 0xd, 0x2, 0xe,
    0x2, 0x5b, 0x3, 0x2, 0x5, 0x2, 0x5f, 0xa, 0x2, 0x3, 0x2, 0x3, 0x2, 0x3,
    0x2, 0x7, 0x2, 0x64, 0xa, 0x2, 0xc, 0x2, 0xe, 0x2, 0x67, 0xb, 0x2, 0x3,
    0x2, 0x3, 0x2, 0x3, 0x3, 0x3, 0x3, 0x3, 0x3, 0x5, 0x3, 0x6e, 0xa, 0x3,
    0x3, 0x4, 0x3, 0x4, 0x3, 0x4, 0x3, 0x5, 0x3, 0x5, 0x3, 0x5, 0x3, 0x6,
    0x3, 0x6, 0x3, 0x6, 0x3, 0x7, 0x3, 0x7, 0x3, 0x7, 0x6, 0x7, 0x7c, 0xa,
    0x7, 0xd, 0x7, 0xe, 0x7, 0x7d, 0x3, 0x8, 0x3, 0x8, 0x3, 0x8, 0x3, 0x8,
    0x5, 0x8, 0x84, 0xa, 0x8, 0x3, 0x8, 0x3, 0x8, 0x7, 0x8, 0x88, 0xa, 0x8,
    0xc, 0x8, 0xe, 0x8, 0x8b, 0xb, 0x8, 0x3, 0x8, 0x3, 0x8, 0x3, 0x8, 0x3,
    0x9, 0x3, 0x9, 0x5, 0x9, 0x92, 0xa, 0x9, 0x3, 0x9, 0x3, 0x9, 0x3, 0xa,
    0x3, 0xa, 0x3, 0xa, 0x7, 0xa, 0x99, 0xa, 0xa, 0xc, 0xa, 0xe, 0xa, 0x9c,
    0xb, 0xa, 0x3, 0xb, 0x5, 0xb, 0x9f, 0xa, 0xb, 0x3, 0xb, 0x3, 0xb, 0x3,
    0xc, 0x3, 0xc, 0x3, 0xc, 0x3, 0xd, 0x3, 0xd, 0x3, 0xd, 0x3, 0xd, 0x5,
    0xd, 0xaa, 0xa, 0xd, 0x3, 0xe, 0x3, 0xe, 0x7, 0xe, 0xae, 0xa, 0xe, 0xc,
    0xe, 0xe, 0xe, 0xb1, 0xb, 0xe, 0x3, 0xe, 0x3, 0xe, 0x3, 0xf, 0x3, 0xf,
    0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf,
    0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x5, 0xf,
    0xc4, 0xa, 0xf, 0x3, 0x10, 0x3, 0x10, 0x3, 0x10, 0x3, 0x10, 0x3, 0x10,
    0x5, 0x10, 0xcb, 0xa, 0x10, 0x3, 0x11, 0x3, 0x11, 0x3, 0x11, 0x3, 0x11,
    0x3, 0x12, 0x3, 0x12, 0x3, 0x12, 0x3, 0x12, 0x3, 0x12, 0x3, 0x13, 0x3,
    0x13, 0x3, 0x13, 0x3, 0x13, 0x3, 0x13, 0x3, 0x13, 0x5, 0x13, 0xdc, 0xa,
    0x13, 0x3, 0x14, 0x3, 0x14, 0x3, 0x14, 0x3, 0x14, 0x5, 0x14, 0xe2, 0xa,
    0x14, 0x3, 0x15, 0x3, 0x15, 0x3, 0x15, 0x5, 0x15, 0xe7, 0xa, 0x15, 0x3,
    0x15, 0x3, 0x15, 0x3, 0x15, 0x5, 0x15, 0xec, 0xa, 0x15, 0x3, 0x15, 0x3,
    0x15, 0x3, 0x15, 0x5, 0x15, 0xf1, 0xa, 0x15, 0x3, 0x16, 0x3, 0x16, 0x3,
    0x16, 0x3, 0x16, 0x3, 0x16, 0x3, 0x16, 0x3, 0x16, 0x5, 0x16, 0xfa, 0xa,
    0x16, 0x3, 0x17, 0x3, 0x17, 0x3, 0x17, 0x3, 0x17, 0x3, 0x17, 0x3, 0x17,
    0x3, 0x18, 0x3, 0x18, 0x3, 0x18, 0x5, 0x18, 0x105, 0xa, 0x18, 0x3, 0x18,
    0x3, 0x18, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19, 0x3,
    0x19, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19,
    0x3, 0x1a, 0x3, 0x1a, 0x3, 0x1a, 0x3, 0x1b, 0x3, 0x1b, 0x3, 0x1b, 0x3,
    0x1c, 0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1c,
    0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1c, 0x5, 0x1c, 0x125, 0xa, 0x1c, 0x3, 0x1d,
    0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3,
    0x1d, 0x5, 0x1d, 0x12f, 0xa, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d,
    0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3,
    0x1d, 0x5, 0x1d, 0x13b, 0xa, 0x1d, 0x3, 0x1e, 0x3, 0x1e, 0x3, 0x1e,
    0x3, 0x1e, 0x7, 0x1e, 0x141, 0xa, 0x1e, 0xc, 0x1e, 0xe, 0x1e, 0x144,
    0xb, 0x1e, 0x3, 0x1e, 0x3, 0x1e, 0x3, 0x1f, 0x3, 0x1f, 0x3, 0x1f, 0x3,
    0x20, 0x3, 0x20, 0x3, 0x20, 0x5, 0x20, 0x14e, 0xa, 0x20, 0x3, 0x20,
    0x3, 0x20, 0x3, 0x21, 0x3, 0x21, 0x3, 0x21, 0x7, 0x21, 0x155, 0xa, 0x21,
    0xc, 0x21, 0xe, 0x21, 0x158, 0xb, 0x21, 0x3, 0x22, 0x3, 0x22, 0x3, 0x23,
    0x3, 0x23, 0x3, 0x23, 0x3, 0x23, 0x3, 0x24, 0x3, 0x24, 0x3, 0x24, 0x7,
    0x24, 0x163, 0xa, 0x24, 0xc, 0x24, 0xe, 0x24, 0x166, 0xb, 0x24, 0x3,
    0x25, 0x5, 0x25, 0x169, 0xa, 0x25, 0x3, 0x25, 0x3, 0x25, 0x3, 0x25,
    0x3, 0x26, 0x3, 0x26, 0x3, 0x26, 0x3, 0x26, 0x5, 0x26, 0x172, 0xa, 0x26,
    0x3, 0x27, 0x3, 0x27, 0x5, 0x27, 0x176, 0xa, 0x27, 0x3, 0x28, 0x3, 0x28,
    0x3, 0x29, 0x3, 0x29, 0x3, 0x2a, 0x3, 0x2a, 0x3, 0x2b, 0x3, 0x2b, 0x3,
    0x2c, 0x3, 0x2c, 0x3, 0x2c, 0x3, 0x2c, 0x3, 0x2c, 0x2, 0x2, 0x2d, 0x2,
    0x4, 0x6, 0x8, 0xa, 0xc, 0xe, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c,
    0x1e, 0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34,
    0x36, 0x38, 0x3a, 0x3c, 0x3e, 0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c,
    0x4e, 0x50, 0x52, 0x54, 0x56, 0x2, 0x9, 0x4, 0x2, 0x46, 0x47, 0x4b,
    0x4b, 0x3, 0x2, 0x44, 0x45, 0x4, 0x2, 0x36, 0x37, 0x3d, 0x3e, 0x4, 0x2,
    0x3c, 0x3c, 0x3f, 0x3f, 0x3, 0x2, 0x40, 0x41, 0x3, 0x2, 0x25, 0x28,
    0x3, 0x2, 0x20, 0x23, 0x2, 0x187, 0x2, 0x59, 0x3, 0x2, 0x2, 0x2, 0x4,
    0x6d, 0x3, 0x2, 0x2, 0x2, 0x6, 0x6f, 0x3, 0x2, 0x2, 0x2, 0x8, 0x72,
    0x3, 0x2, 0x2, 0x2, 0xa, 0x75, 0x3, 0x2, 0x2, 0x2, 0xc, 0x78, 0x3, 0x2,
    0x2, 0x2, 0xe, 0x7f, 0x3, 0x2, 0x2, 0x2, 0x10, 0x8f, 0x3, 0x2, 0x2,
    0x2, 0x12, 0x95, 0x3, 0x2, 0x2, 0x2, 0x14, 0x9e, 0x3, 0x2, 0x2, 0x2,
    0x16, 0xa2, 0x3, 0x2, 0x2, 0x2, 0x18, 0xa9, 0x3, 0x2, 0x2, 0x2, 0x1a,
    0xab, 0x3, 0x2, 0x2, 0x2, 0x1c, 0xc3, 0x3, 0x2, 0x2, 0x2, 0x1e, 0xc5,
    0x3, 0x2, 0x2, 0x2, 0x20, 0xcc, 0x3, 0x2, 0x2, 0x2, 0x22, 0xd0, 0x3,
    0x2, 0x2, 0x2, 0x24, 0xd5, 0x3, 0x2, 0x2, 0x2, 0x26, 0xe1, 0x3, 0x2,
    0x2, 0x2, 0x28, 0xe3, 0x3, 0x2, 0x2, 0x2, 0x2a, 0xf2, 0x3, 0x2, 0x2,
    0x2, 0x2c, 0xfb, 0x3, 0x2, 0x2, 0x2, 0x2e, 0x101, 0x3, 0x2, 0x2, 0x2,
    0x30, 0x108, 0x3, 0x2, 0x2, 0x2, 0x32, 0x114, 0x3, 0x2, 0x2, 0x2, 0x34,
    0x117, 0x3, 0x2, 0x2, 0x2, 0x36, 0x124, 0x3, 0x2, 0x2, 0x2, 0x38, 0x13a,
    0x3, 0x2, 0x2, 0x2, 0x3a, 0x13c, 0x3, 0x2, 0x2, 0x2, 0x3c, 0x147, 0x3,
    0x2, 0x2, 0x2, 0x3e, 0x14a, 0x3, 0x2, 0x2, 0x2, 0x40, 0x151, 0x3, 0x2,
    0x2, 0x2, 0x42, 0x159, 0x3, 0x2, 0x2, 0x2, 0x44, 0x15b, 0x3, 0x2, 0x2,
    0x2, 0x46, 0x15f, 0x3, 0x2, 0x2, 0x2, 0x48, 0x168, 0x3, 0x2, 0x2, 0x2,
    0x4a, 0x16d, 0x3, 0x2, 0x2, 0x2, 0x4c, 0x175, 0x3, 0x2, 0x2, 0x2, 0x4e,
    0x177, 0x3, 0x2, 0x2, 0x2, 0x50, 0x179, 0x3, 0x2, 0x2, 0x2, 0x52, 0x17b,
    0x3, 0x2, 0x2, 0x2, 0x54, 0x17d, 0x3, 0x2, 0x2, 0x2, 0x56, 0x17f, 0x3,
    0x2, 0x2, 0x2, 0x58, 0x5a, 0x5, 0x4, 0x3, 0x2, 0x59, 0x58, 0x3, 0x2,
    0x2, 0x2, 0x5a, 0x5b, 0x3, 0x2, 0x2, 0x2, 0x5b, 0x59, 0x3, 0x2, 0x2,
    0x2, 0x5b, 0x5c, 0x3, 0x2, 0x2, 0x2, 0x5c, 0x5e, 0x3, 0x2, 0x2, 0x2,
    0x5d, 0x5f, 0x5, 0xc, 0x7, 0x2, 0x5e, 0x5d, 0x3, 0x2, 0x2, 0x2, 0x5e,
    0x5f, 0x3, 0x2, 0x2, 0x2, 0x5f, 0x60, 0x3, 0x2, 0x2, 0x2, 0x60, 0x61,
    0x7, 0xd, 0x2, 0x2, 0x61, 0x65, 0x7, 0x3b, 0x2, 0x2, 0x62, 0x64, 0x5,
    0x1c, 0xf, 0x2, 0x63, 0x62, 0x3, 0x2, 0x2, 0x2, 0x64, 0x67, 0x3, 0x2,
    0x2, 0x2, 0x65, 0x63, 0x3, 0x2, 0x2, 0x2, 0x65, 0x66, 0x3, 0x2, 0x2,
    0x2, 0x66, 0x68, 0x3, 0x2, 0x2, 0x2, 0x67, 0x65, 0x3, 0x2, 0x2, 0x2,
    0x68, 0x69, 0x7, 0x2, 0x2, 0x3, 0x69, 0x3, 0x3, 0x2, 0x2, 0x2, 0x6a,
    0x6e, 0x5, 0x6, 0x4, 0x2, 0x6b, 0x6e, 0x5, 0x8, 0x5, 0x2, 0x6c, 0x6e,
    0x5, 0xa, 0x6, 0x2, 0x6d, 0x6a, 0x3, 0x2, 0x2, 0x2, 0x6d, 0x6b, 0x3,
    0x2, 0x2, 0x2, 0x6d, 0x6c, 0x3, 0x2, 0x2, 0x2, 0x6e, 0x5, 0x3, 0x2,
    0x2, 0x2, 0x6f, 0x70, 0x7, 0xa, 0x2, 0x2, 0x70, 0x71, 0x7, 0x24, 0x2,
    0x2, 0x71, 0x7, 0x3, 0x2, 0x2, 0x2, 0x72, 0x73, 0x7, 0x9, 0x2, 0x2,
    0x73, 0x74, 0x7, 0x24, 0x2, 0x2, 0x74, 0x9, 0x3, 0x2, 0x2, 0x2, 0x75,
    0x76, 0x7, 0xb, 0x2, 0x2, 0x76, 0x77, 0x7, 0x24, 0x2, 0x2, 0x77, 0xb,
    0x3, 0x2, 0x2, 0x2, 0x78, 0x79, 0x7, 0xc, 0x2, 0x2, 0x79, 0x7b, 0x7,
    0x3b, 0x2, 0x2, 0x7a, 0x7c, 0x5, 0xe, 0x8, 0x2, 0x7b, 0x7a, 0x3, 0x2,
    0x2, 0x2, 0x7c, 0x7d, 0x3, 0x2, 0x2, 0x2, 0x7d, 0x7b, 0x3, 0x2, 0x2,
    0x2, 0x7d, 0x7e, 0x3, 0x2, 0x2, 0x2, 0x7e, 0xd, 0x3, 0x2, 0x2, 0x2,
    0x7f, 0x80, 0x7, 0x7, 0x2, 0x2, 0x80, 0x81, 0x7, 0x24, 0x2, 0x2, 0x81,
    0x83, 0x5, 0x10, 0x9, 0x2, 0x82, 0x84, 0x5, 0x16, 0xc, 0x2, 0x83, 0x82,
    0x3, 0x2, 0x2, 0x2, 0x83, 0x84, 0x3, 0x2, 0x2, 0x2, 0x84, 0x85, 0x3,
    0x2, 0x2, 0x2, 0x85, 0x89, 0x7, 0x2e, 0x2, 0x2, 0x86, 0x88, 0x5, 0x1c,
    0xf, 0x2, 0x87, 0x86, 0x3, 0x2, 0x2, 0x2, 0x88, 0x8b, 0x3, 0x2, 0x2,
    0x2, 0x89, 0x87, 0x3, 0x2, 0x2, 0x2, 0x89, 0x8a, 0x3, 0x2, 0x2, 0x2,
    0x8a, 0x8c, 0x3, 0x2, 0x2, 0x2, 0x8b, 0x89, 0x3, 0x2, 0x2, 0x2, 0x8c,
    0x8d, 0x5, 0x18, 0xd, 0x2, 0x8d, 0x8e, 0x7, 0x2f, 0x2, 0x2, 0x8e, 0xf,
    0x3, 0x2, 0x2, 0x2, 0x8f, 0x91, 0x7, 0x2c, 0x2, 0x2, 0x90, 0x92, 0x5,
    0x12, 0xa, 0x2, 0x91, 0x90, 0x3, 0x2, 0x2, 0x2, 0x91, 0x92, 0x3, 0x2,
    0x2, 0x2, 0x92, 0x93, 0x3, 0x2, 0x2, 0x2, 0x93, 0x94, 0x7, 0x2d, 0x2,
    0x2, 0x94, 0x11, 0x3, 0x2, 0x2, 0x2, 0x95, 0x9a, 0x5, 0x14, 0xb, 0x2,
    0x96, 0x97, 0x7, 0x33, 0x2, 0x2, 0x97, 0x99, 0x5, 0x14, 0xb, 0x2, 0x98,
    0x96, 0x3, 0x2, 0x2, 0x2, 0x99, 0x9c, 0x3, 0x2, 0x2, 0x2, 0x9a, 0x98,
    0x3, 0x2, 0x2, 0x2, 0x9a, 0x9b, 0x3, 0x2, 0x2, 0x2, 0x9b, 0x13, 0x3,
    0x2, 0x2, 0x2, 0x9c, 0x9a, 0x3, 0x2, 0x2, 0x2, 0x9d, 0x9f, 0x5, 0x44,
    0x23, 0x2, 0x9e, 0x9d, 0x3, 0x2, 0x2, 0x2, 0x9e, 0x9f, 0x3, 0x2, 0x2,
    0x2, 0x9f, 0xa0, 0x3, 0x2, 0x2, 0x2, 0xa0, 0xa1, 0x7, 0x24, 0x2, 0x2,
    0xa1, 0x15, 0x3, 0x2, 0x2, 0x2, 0xa2, 0xa3, 0x7, 0x3b, 0x2, 0x2, 0xa3,
    0xa4, 0x5, 0x44, 0x23, 0x2, 0xa4, 0x17, 0x3, 0x2, 0x2, 0x2, 0xa5, 0xa6,
    0x7, 0x8, 0x2, 0x2, 0xa6, 0xaa, 0x5, 0x4c, 0x27, 0x2, 0xa7, 0xa8, 0x7,
    0x8, 0x2, 0x2, 0xa8, 0xaa, 0x5, 0x3e, 0x20, 0x2, 0xa9, 0xa5, 0x3, 0x2,
    0x2, 0x2, 0xa9, 0xa7, 0x3, 0x2, 0x2, 0x2, 0xaa, 0x19, 0x3, 0x2, 0x2,
    0x2, 0xab, 0xaf, 0x7, 0x2e, 0x2, 0x2, 0xac, 0xae, 0x5, 0x1c, 0xf, 0x2,
    0xad, 0xac, 0x3, 0x2, 0x2, 0x2, 0xae, 0xb1, 0x3, 0x2, 0x2, 0x2, 0xaf,
    0xad, 0x3, 0x2, 0x2, 0x2, 0xaf, 0xb0, 0x3, 0x2, 0x2, 0x2, 0xb0, 0xb2,
    0x3, 0x2, 0x2, 0x2, 0xb1, 0xaf, 0x3, 0x2, 0x2, 0x2, 0xb2, 0xb3, 0x7,
    0x2f, 0x2, 0x2, 0xb3, 0x1b, 0x3, 0x2, 0x2, 0x2, 0xb4, 0xc4, 0x5, 0x1e,
    0x10, 0x2, 0xb5, 0xc4, 0x5, 0x20, 0x11, 0x2, 0xb6, 0xc4, 0x5, 0x48,
    0x25, 0x2, 0xb7, 0xc4, 0x5, 0x22, 0x12, 0x2, 0xb8, 0xc4, 0x5, 0x24,
    0x13, 0x2, 0xb9, 0xc4, 0x5, 0x26, 0x14, 0x2, 0xba, 0xc4, 0x5, 0x28,
    0x15, 0x2, 0xbb, 0xc4, 0x5, 0x2e, 0x18, 0x2, 0xbc, 0xc4, 0x5, 0x2c,
    0x17, 0x2, 0xbd, 0xc4, 0x5, 0x3c, 0x1f, 0x2, 0xbe, 0xc4, 0x5, 0x30,
    0x19, 0x2, 0xbf, 0xc4, 0x5, 0x2a, 0x16, 0x2, 0xc0, 0xc4, 0x5, 0x32,
    0x1a, 0x2, 0xc1, 0xc4, 0x5, 0x36, 0x1c, 0x2, 0xc2, 0xc4, 0x5, 0x34,
    0x1b, 0x2, 0xc3, 0xb4, 0x3, 0x2, 0x2, 0x2, 0xc3, 0xb5, 0x3, 0x2, 0x2,
    0x2, 0xc3, 0xb6, 0x3, 0x2, 0x2, 0x2, 0xc3, 0xb7, 0x3, 0x2, 0x2, 0x2,
    0xc3, 0xb8, 0x3, 0x2, 0x2, 0x2, 0xc3, 0xb9, 0x3, 0x2, 0x2, 0x2, 0xc3,
    0xba, 0x3, 0x2, 0x2, 0x2, 0xc3, 0xbb, 0x3, 0x2, 0x2, 0x2, 0xc3, 0xbc,
    0x3, 0x2, 0x2, 0x2, 0xc3, 0xbd, 0x3, 0x2, 0x2, 0x2, 0xc3, 0xbe, 0x3,
    0x2, 0x2, 0x2, 0xc3, 0xbf, 0x3, 0x2, 0x2, 0x2, 0xc3, 0xc0, 0x3, 0x2,
    0x2, 0x2, 0xc3, 0xc1, 0x3, 0x2, 0x2, 0x2, 0xc3, 0xc2, 0x3, 0x2, 0x2,
    0x2, 0xc4, 0x1d, 0x3, 0x2, 0x2, 0x2, 0xc5, 0xc6, 0x7, 0x3, 0x2, 0x2,
    0xc6, 0xc7, 0x5, 0x3a, 0x1e, 0x2, 0xc7, 0xca, 0x5, 0x1a, 0xe, 0x2, 0xc8,
    0xc9, 0x7, 0x4, 0x2, 0x2, 0xc9, 0xcb, 0x5, 0x1a, 0xe, 0x2, 0xca, 0xc8,
    0x3, 0x2, 0x2, 0x2, 0xca, 0xcb, 0x3, 0x2, 0x2, 0x2, 0xcb, 0x1f, 0x3,
    0x2, 0x2, 0x2, 0xcc, 0xcd, 0x7, 0x6, 0x2, 0x2, 0xcd, 0xce, 0x5, 0x3a,
    0x1e, 0x2, 0xce, 0xcf, 0x5, 0x1a, 0xe, 0x2, 0xcf, 0x21, 0x3, 0x2, 0x2,
    0x2, 0xd0, 0xd1, 0x7, 0x5, 0x2, 0x2, 0xd1, 0xd2, 0x7, 0x28, 0x2, 0x2,
    0xd2, 0xd3, 0x7, 0x1c, 0x2, 0x2, 0xd3, 0xd4, 0x5, 0x1a, 0xe, 0x2, 0xd4,
    0x23, 0x3, 0x2, 0x2, 0x2, 0xd5, 0xd6, 0x7, 0x11, 0x2, 0x2, 0xd6, 0xd7,
    0x5, 0x4a, 0x26, 0x2, 0xd7, 0xd8, 0x7, 0x18, 0x2, 0x2, 0xd8, 0xdb, 0x5,
    0x54, 0x2b, 0x2, 0xd9, 0xda, 0x7, 0x1a, 0x2, 0x2, 0xda, 0xdc, 0x5, 0x52,
    0x2a, 0x2, 0xdb, 0xd9, 0x3, 0x2, 0x2, 0x2, 0xdb, 0xdc, 0x3, 0x2, 0x2,
    0x2, 0xdc, 0x25, 0x3, 0x2, 0x2, 0x2, 0xdd, 0xde, 0x7, 0x12, 0x2, 0x2,
    0xde, 0xe2, 0x5, 0x4a, 0x26, 0x2, 0xdf, 0xe0, 0x7, 0x14, 0x2, 0x2, 0xe0,
    0xe2, 0x5, 0x4a, 0x26, 0x2, 0xe1, 0xdd, 0x3, 0x2, 0x2, 0x2, 0xe1, 0xdf,
    0x3, 0x2, 0x2, 0x2, 0xe2, 0x27, 0x3, 0x2, 0x2, 0x2, 0xe3, 0xe4, 0x5,
    0x48, 0x25, 0x2, 0xe4, 0xe6, 0x7, 0xf, 0x2, 0x2, 0xe5, 0xe7, 0x5, 0x56,
    0x2c, 0x2, 0xe6, 0xe5, 0x3, 0x2, 0x2, 0x2, 0xe6, 0xe7, 0x3, 0x2, 0x2,
    0x2, 0xe7, 0xe8, 0x3, 0x2, 0x2, 0x2, 0xe8, 0xe9, 0x5, 0x4a, 0x26, 0x2,
    0xe9, 0xeb, 0x7, 0x19, 0x2, 0x2, 0xea, 0xec, 0x5, 0x56, 0x2c, 0x2, 0xeb,
    0xea, 0x3, 0x2, 0x2, 0x2, 0xeb, 0xec, 0x3, 0x2, 0x2, 0x2, 0xec, 0xed,
    0x3, 0x2, 0x2, 0x2, 0xed, 0xf0, 0x5, 0x4a, 0x26, 0x2, 0xee, 0xef, 0x7,
    0x1a, 0x2, 0x2, 0xef, 0xf1, 0x5, 0x52, 0x2a, 0x2, 0xf0, 0xee, 0x3, 0x2,
    0x2, 0x2, 0xf0, 0xf1, 0x3, 0x2, 0x2, 0x2, 0xf1, 0x29, 0x3, 0x2, 0x2,
    0x2, 0xf2, 0xf3, 0x5, 0x48, 0x25, 0x2, 0xf3, 0xf4, 0x7, 0xe, 0x2, 0x2,
    0xf4, 0xf5, 0x7, 0x24, 0x2, 0x2, 0xf5, 0xf6, 0x7, 0x1d, 0x2, 0x2, 0xf6,
    0xf9, 0x5, 0x4a, 0x26, 0x2, 0xf7, 0xf8, 0x7, 0x1a, 0x2, 0x2, 0xf8, 0xfa,
    0x5, 0x52, 0x2a, 0x2, 0xf9, 0xf7, 0x3, 0x2, 0x2, 0x2, 0xf9, 0xfa, 0x3,
    0x2, 0x2, 0x2, 0xfa, 0x2b, 0x3, 0x2, 0x2, 0x2, 0xfb, 0xfc, 0x5, 0x48,
    0x25, 0x2, 0xfc, 0xfd, 0x7, 0x10, 0x2, 0x2, 0xfd, 0xfe, 0x5, 0x4a, 0x26,
    0x2, 0xfe, 0xff, 0x7, 0x1b, 0x2, 0x2, 0xff, 0x100, 0x7, 0x28, 0x2, 0x2,
    0x100, 0x2d, 0x3, 0x2, 0x2, 0x2, 0x101, 0x102, 0x5, 0x48, 0x25, 0x2,
    0x102, 0x104, 0x7, 0x13, 0x2, 0x2, 0x103, 0x105, 0x5, 0x56, 0x2c, 0x2,
    0x104, 0x103, 0x3, 0x2, 0x2, 0x2, 0x104, 0x105, 0x3, 0x2, 0x2, 0x2,
    0x105, 0x106, 0x3, 0x2, 0x2, 0x2, 0x106, 0x107, 0x7, 0x24, 0x2, 0x2,
    0x107, 0x2f, 0x3, 0x2, 0x2, 0x2, 0x108, 0x109, 0x5, 0x48, 0x25, 0x2,
    0x109, 0x10a, 0x7, 0x15, 0x2, 0x2, 0x10a, 0x10b, 0x7, 0x24, 0x2, 0x2,
    0x10b, 0x10c, 0x7, 0x19, 0x2, 0x2, 0x10c, 0x10d, 0x7, 0x24, 0x2, 0x2,
    0x10d, 0x10e, 0x7, 0x17, 0x2, 0x2, 0x10e, 0x10f, 0x7, 0x28, 0x2, 0x2,
    0x10f, 0x110, 0x7, 0x33, 0x2, 0x2, 0x110, 0x111, 0x7, 0x28, 0x2, 0x2,
    0x111, 0x112, 0x7, 0x18, 0x2, 0x2, 0x112, 0x113, 0x7, 0x28, 0x2, 0x2,
    0x113, 0x31, 0x3, 0x2, 0x2, 0x2, 0x114, 0x115, 0x7, 0x16, 0x2, 0x2,
    0x115, 0x116, 0x5, 0x4a, 0x26, 0x2, 0x116, 0x33, 0x3, 0x2, 0x2, 0x2,
    0x117, 0x118, 0x5, 0x48, 0x25, 0x2, 0x118, 0x119, 0x5, 0x4e, 0x28, 0x2,
    0x119, 0x35, 0x3, 0x2, 0x2, 0x2, 0x11a, 0x11b, 0x5, 0x48, 0x25, 0x2,
    0x11b, 0x11c, 0x5, 0x4c, 0x27, 0x2, 0x11c, 0x11d, 0x9, 0x2, 0x2, 0x2,
    0x11d, 0x11e, 0x5, 0x4c, 0x27, 0x2, 0x11e, 0x125, 0x3, 0x2, 0x2, 0x2,
    0x11f, 0x120, 0x5, 0x48, 0x25, 0x2, 0x120, 0x121, 0x5, 0x4c, 0x27, 0x2,
    0x121, 0x122, 0x9, 0x3, 0x2, 0x2, 0x122, 0x123, 0x5, 0x4c, 0x27, 0x2,
    0x123, 0x125, 0x3, 0x2, 0x2, 0x2, 0x124, 0x11a, 0x3, 0x2, 0x2, 0x2,
    0x124, 0x11f, 0x3, 0x2, 0x2, 0x2, 0x125, 0x37, 0x3, 0x2, 0x2, 0x2, 0x126,
    0x12e, 0x5, 0x4c, 0x27, 0x2, 0x127, 0x128, 0x7, 0x37, 0x2, 0x2, 0x128,
    0x12f, 0x7, 0x37, 0x2, 0x2, 0x129, 0x12a, 0x7, 0x36, 0x2, 0x2, 0x12a,
    0x12b, 0x7, 0x36, 0x2, 0x2, 0x12b, 0x12f, 0x7, 0x36, 0x2, 0x2, 0x12c,
    0x12d, 0x7, 0x36, 0x2, 0x2, 0x12d, 0x12f, 0x7, 0x36, 0x2, 0x2, 0x12e,
    0x127, 0x3, 0x2, 0x2, 0x2, 0x12e, 0x129, 0x3, 0x2, 0x2, 0x2, 0x12e,
    0x12c, 0x3, 0x2, 0x2, 0x2, 0x12f, 0x130, 0x3, 0x2, 0x2, 0x2, 0x130,
    0x131, 0x5, 0x4c, 0x27, 0x2, 0x131, 0x13b, 0x3, 0x2, 0x2, 0x2, 0x132,
    0x133, 0x5, 0x4c, 0x27, 0x2, 0x133, 0x134, 0x9, 0x4, 0x2, 0x2, 0x134,
    0x135, 0x5, 0x4c, 0x27, 0x2, 0x135, 0x13b, 0x3, 0x2, 0x2, 0x2, 0x136,
    0x137, 0x5, 0x4c, 0x27, 0x2, 0x137, 0x138, 0x9, 0x5, 0x2, 0x2, 0x138,
    0x139, 0x5, 0x4c, 0x27, 0x2, 0x139, 0x13b, 0x3, 0x2, 0x2, 0x2, 0x13a,
    0x126, 0x3, 0x2, 0x2, 0x2, 0x13a, 0x132, 0x3, 0x2, 0x2, 0x2, 0x13a,
    0x136, 0x3, 0x2, 0x2, 0x2, 0x13b, 0x39, 0x3, 0x2, 0x2, 0x2, 0x13c, 0x13d,
    0x7, 0x2c, 0x2, 0x2, 0x13d, 0x142, 0x5, 0x38, 0x1d, 0x2, 0x13e, 0x13f,
    0x9, 0x6, 0x2, 0x2, 0x13f, 0x141, 0x5, 0x38, 0x1d, 0x2, 0x140, 0x13e,
    0x3, 0x2, 0x2, 0x2, 0x141, 0x144, 0x3, 0x2, 0x2, 0x2, 0x142, 0x140,
    0x3, 0x2, 0x2, 0x2, 0x142, 0x143, 0x3, 0x2, 0x2, 0x2, 0x143, 0x145,
    0x3, 0x2, 0x2, 0x2, 0x144, 0x142, 0x3, 0x2, 0x2, 0x2, 0x145, 0x146,
    0x7, 0x2d, 0x2, 0x2, 0x146, 0x3b, 0x3, 0x2, 0x2, 0x2, 0x147, 0x148,
    0x5, 0x48, 0x25, 0x2, 0x148, 0x149, 0x5, 0x3e, 0x20, 0x2, 0x149, 0x3d,
    0x3, 0x2, 0x2, 0x2, 0x14a, 0x14b, 0x7, 0x24, 0x2, 0x2, 0x14b, 0x14d,
    0x7, 0x2c, 0x2, 0x2, 0x14c, 0x14e, 0x5, 0x40, 0x21, 0x2, 0x14d, 0x14c,
    0x3, 0x2, 0x2, 0x2, 0x14d, 0x14e, 0x3, 0x2, 0x2, 0x2, 0x14e, 0x14f,
    0x3, 0x2, 0x2, 0x2, 0x14f, 0x150, 0x7, 0x2d, 0x2, 0x2, 0x150, 0x3f,
    0x3, 0x2, 0x2, 0x2, 0x151, 0x156, 0x5, 0x4c, 0x27, 0x2, 0x152, 0x153,
    0x7, 0x33, 0x2, 0x2, 0x153, 0x155, 0x5, 0x4c, 0x27, 0x2, 0x154, 0x152,
    0x3, 0x2, 0x2, 0x2, 0x155, 0x158, 0x3, 0x2, 0x2, 0x2, 0x156, 0x154,
    0x3, 0x2, 0x2, 0x2, 0x156, 0x157, 0x3, 0x2, 0x2, 0x2, 0x157, 0x41, 0x3,
    0x2, 0x2, 0x2, 0x158, 0x156, 0x3, 0x2, 0x2, 0x2, 0x159, 0x15a, 0x5,
    0x50, 0x29, 0x2, 0x15a, 0x43, 0x3, 0x2, 0x2, 0x2, 0x15b, 0x15c, 0x7,
    0x30, 0x2, 0x2, 0x15c, 0x15d, 0x5, 0x46, 0x24, 0x2, 0x15d, 0x15e, 0x7,
    0x31, 0x2, 0x2, 0x15e, 0x45, 0x3, 0x2, 0x2, 0x2, 0x15f, 0x164, 0x5,
    0x42, 0x22, 0x2, 0x160, 0x161, 0x7, 0x32, 0x2, 0x2, 0x161, 0x163, 0x5,
    0x42, 0x22, 0x2, 0x162, 0x160, 0x3, 0x2, 0x2, 0x2, 0x163, 0x166, 0x3,
    0x2, 0x2, 0x2, 0x164, 0x162, 0x3, 0x2, 0x2, 0x2, 0x164, 0x165, 0x3,
    0x2, 0x2, 0x2, 0x165, 0x47, 0x3, 0x2, 0x2, 0x2, 0x166, 0x164, 0x3, 0x2,
    0x2, 0x2, 0x167, 0x169, 0x5, 0x44, 0x23, 0x2, 0x168, 0x167, 0x3, 0x2,
    0x2, 0x2, 0x168, 0x169, 0x3, 0x2, 0x2, 0x2, 0x169, 0x16a, 0x3, 0x2,
    0x2, 0x2, 0x16a, 0x16b, 0x5, 0x4a, 0x26, 0x2, 0x16b, 0x16c, 0x7, 0x35,
    0x2, 0x2, 0x16c, 0x49, 0x3, 0x2, 0x2, 0x2, 0x16d, 0x171, 0x7, 0x24,
    0x2, 0x2, 0x16e, 0x16f, 0x7, 0x30, 0x2, 0x2, 0x16f, 0x170, 0x7, 0x28,
    0x2, 0x2, 0x170, 0x172, 0x7, 0x31, 0x2, 0x2, 0x171, 0x16e, 0x3, 0x2,
    0x2, 0x2, 0x171, 0x172, 0x3, 0x2, 0x2, 0x2, 0x172, 0x4b, 0x3, 0x2, 0x2,
    0x2, 0x173, 0x176, 0x5, 0x4e, 0x28, 0x2, 0x174, 0x176, 0x5, 0x4a, 0x26,
    0x2, 0x175, 0x173, 0x3, 0x2, 0x2, 0x2, 0x175, 0x174, 0x3, 0x2, 0x2,
    0x2, 0x176, 0x4d, 0x3, 0x2, 0x2, 0x2, 0x177, 0x178, 0x9, 0x7, 0x2, 0x2,
    0x178, 0x4f, 0x3, 0x2, 0x2, 0x2, 0x179, 0x17a, 0x9, 0x8, 0x2, 0x2, 0x17a,
    0x51, 0x3, 0x2, 0x2, 0x2, 0x17b, 0x17c, 0x7, 0x29, 0x2, 0x2, 0x17c,
    0x53, 0x3, 0x2, 0x2, 0x2, 0x17d, 0x17e, 0x7, 0x2b, 0x2, 0x2, 0x17e,
    0x55, 0x3, 0x2, 0x2, 0x2, 0x17f, 0x180, 0x7, 0x28, 0x2, 0x2, 0x180,
    0x181, 0x7, 0x1f, 0x2, 0x2, 0x181, 0x182, 0x7, 0x1e, 0x2, 0x2, 0x182,
    0x57, 0x3, 0x2, 0x2, 0x2, 0x21, 0x5b, 0x5e, 0x65, 0x6d, 0x7d, 0x83,
    0x89, 0x91, 0x9a, 0x9e, 0xa9, 0xaf, 0xc3, 0xca, 0xdb, 0xe1, 0xe6, 0xeb,
    0xf0, 0xf9, 0x104, 0x124, 0x12e, 0x13a, 0x142, 0x14d, 0x156, 0x164,
    0x168, 0x171, 0x175,
  };

  atn::ATNDeserializer deserializer;
  _atn = deserializer.deserialize(_serializedATN);

  size_t count = _atn.getNumberOfDecisions();
  _decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) {
    _decisionToDFA.emplace_back(_atn.getDecisionState(i), i);
  }
}

BSParser::Initializer BSParser::_init;
