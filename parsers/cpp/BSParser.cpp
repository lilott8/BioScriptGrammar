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

//----------------- ProgramContext ------------------------------------------------------------------

BSParser::ProgramContext::ProgramContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::ProgramContext::INSTRUCTIONS() {
  return getToken(BSParser::INSTRUCTIONS, 0);
}

tree::TerminalNode* BSParser::ProgramContext::COLON() {
  return getToken(BSParser::COLON, 0);
}

tree::TerminalNode* BSParser::ProgramContext::EOF() {
  return getToken(BSParser::EOF, 0);
}

std::vector<BSParser::GlobalDeclarationsContext *> BSParser::ProgramContext::globalDeclarations() {
  return getRuleContexts<BSParser::GlobalDeclarationsContext>();
}

BSParser::GlobalDeclarationsContext* BSParser::ProgramContext::globalDeclarations(size_t i) {
  return getRuleContext<BSParser::GlobalDeclarationsContext>(i);
}

BSParser::FunctionsContext* BSParser::ProgramContext::functions() {
  return getRuleContext<BSParser::FunctionsContext>(0);
}

std::vector<BSParser::StatementsContext *> BSParser::ProgramContext::statements() {
  return getRuleContexts<BSParser::StatementsContext>();
}

BSParser::StatementsContext* BSParser::ProgramContext::statements(size_t i) {
  return getRuleContext<BSParser::StatementsContext>(i);
}


size_t BSParser::ProgramContext::getRuleIndex() const {
  return BSParser::RuleProgram;
}

void BSParser::ProgramContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterProgram(this);
}

void BSParser::ProgramContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitProgram(this);
}


antlrcpp::Any BSParser::ProgramContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitProgram(this);
  else
    return visitor->visitChildren(this);
}

BSParser::ProgramContext* BSParser::program() {
  ProgramContext *_localctx = _tracker.createInstance<ProgramContext>(_ctx, getState());
  enterRule(_localctx, 0, BSParser::RuleProgram);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(89);
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(88);
      globalDeclarations();
      setState(91);
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << BSParser::MANIFEST)
      | (1ULL << BSParser::MODULE)
      | (1ULL << BSParser::STATIONARY)
      | (1ULL << BSParser::LBRACKET))) != 0));
    setState(94);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::FUNCTIONS) {
      setState(93);
      functions();
    }
    setState(96);
    match(BSParser::INSTRUCTIONS);
    setState(97);
    match(BSParser::COLON);
    setState(101);
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
      setState(98);
      statements();
      setState(103);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(104);
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
    setState(109);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(106);
      moduleDeclaration();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(107);
      manifestDeclaration();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(108);
      stationaryDeclaration();
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
    setState(111);
    match(BSParser::MODULE);
    setState(112);
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

BSParser::UnionTypeContext* BSParser::ManifestDeclarationContext::unionType() {
  return getRuleContext<BSParser::UnionTypeContext>(0);
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
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(115);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::LBRACKET) {
      setState(114);
      unionType();
    }
    setState(117);
    match(BSParser::MANIFEST);
    setState(118);
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

BSParser::UnionTypeContext* BSParser::StationaryDeclarationContext::unionType() {
  return getRuleContext<BSParser::UnionTypeContext>(0);
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
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(121);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::LBRACKET) {
      setState(120);
      unionType();
    }
    setState(123);
    match(BSParser::STATIONARY);
    setState(124);
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
    setState(126);
    match(BSParser::FUNCTIONS);
    setState(127);
    match(BSParser::COLON);
    setState(129);
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(128);
      functionDeclaration();
      setState(131);
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
    setState(133);
    match(BSParser::FUNCTION);
    setState(134);
    match(BSParser::IDENTIFIER);
    setState(135);
    formalParameters();
    setState(137);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::COLON) {
      setState(136);
      functionTyping();
    }
    setState(139);
    match(BSParser::LBRACE);
    setState(143);
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
      setState(140);
      statements();
      setState(145);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(146);
    returnStatement();
    setState(147);
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
    setState(149);
    match(BSParser::LPAREN);
    setState(151);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::IDENTIFIER

    || _la == BSParser::LBRACKET) {
      setState(150);
      formalParameterList();
    }
    setState(153);
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
    setState(155);
    formalParameter();
    setState(160);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BSParser::COMMA) {
      setState(156);
      match(BSParser::COMMA);
      setState(157);
      formalParameter();
      setState(162);
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
    setState(164);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::LBRACKET) {
      setState(163);
      unionType();
    }
    setState(166);
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
    setState(168);
    match(BSParser::COLON);
    setState(169);
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
    setState(175);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 12, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(171);
      match(BSParser::RETURN);
      setState(172);
      primary();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(173);
      match(BSParser::RETURN);
      setState(174);
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
    setState(177);
    match(BSParser::LBRACE);
    setState(181);
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
      setState(178);
      statements();
      setState(183);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(184);
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
    setState(201);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(186);
      ifStatement();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(187);
      whileStatement();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(188);
      variableDefinition();
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(189);
      repeat();
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(190);
      heat();
      break;
    }

    case 6: {
      enterOuterAlt(_localctx, 6);
      setState(191);
      dispose();
      break;
    }

    case 7: {
      enterOuterAlt(_localctx, 7);
      setState(192);
      mix();
      break;
    }

    case 8: {
      enterOuterAlt(_localctx, 8);
      setState(193);
      dispense();
      break;
    }

    case 9: {
      enterOuterAlt(_localctx, 9);
      setState(194);
      split();
      break;
    }

    case 10: {
      enterOuterAlt(_localctx, 10);
      setState(195);
      methodInvocation();
      break;
    }

    case 11: {
      enterOuterAlt(_localctx, 11);
      setState(196);
      gradient();
      break;
    }

    case 12: {
      enterOuterAlt(_localctx, 12);
      setState(197);
      detect();
      break;
    }

    case 13: {
      enterOuterAlt(_localctx, 13);
      setState(198);
      store();
      break;
    }

    case 14: {
      enterOuterAlt(_localctx, 14);
      setState(199);
      math();
      break;
    }

    case 15: {
      enterOuterAlt(_localctx, 15);
      setState(200);
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
    setState(203);
    match(BSParser::IF);
    setState(204);
    parExpression();
    setState(205);
    blockStatement();
    setState(208);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::ELSE) {
      setState(206);
      match(BSParser::ELSE);
      setState(207);
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
    setState(210);
    match(BSParser::WHILE);
    setState(211);
    parExpression();
    setState(212);
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
    setState(214);
    match(BSParser::REPEAT);
    setState(215);
    match(BSParser::INTEGER_LITERAL);
    setState(216);
    match(BSParser::TIMES);
    setState(217);
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
    setState(219);
    match(BSParser::HEAT);
    setState(220);
    variable();
    setState(221);
    match(BSParser::AT);
    setState(222);
    temperatureIdentifier();
    setState(225);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::FOR) {
      setState(223);
      match(BSParser::FOR);
      setState(224);
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
    setState(231);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BSParser::DRAIN: {
        enterOuterAlt(_localctx, 1);
        setState(227);
        match(BSParser::DRAIN);
        setState(228);
        variable();
        break;
      }

      case BSParser::DISPOSE: {
        enterOuterAlt(_localctx, 2);
        setState(229);
        match(BSParser::DISPOSE);
        setState(230);
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
    setState(233);
    variableDefinition();
    setState(234);
    match(BSParser::MIX);
    setState(236);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::INTEGER_LITERAL) {
      setState(235);
      unitTracker();
    }
    setState(238);
    variable();
    setState(239);
    match(BSParser::WITH);
    setState(241);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::INTEGER_LITERAL) {
      setState(240);
      unitTracker();
    }
    setState(243);
    variable();
    setState(246);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::FOR) {
      setState(244);
      match(BSParser::FOR);
      setState(245);
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
    setState(248);
    variableDefinition();
    setState(249);
    match(BSParser::DETECT);
    setState(250);
    match(BSParser::IDENTIFIER);
    setState(251);
    match(BSParser::ON);
    setState(252);
    variable();
    setState(255);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::FOR) {
      setState(253);
      match(BSParser::FOR);
      setState(254);
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
    setState(257);
    variableDefinition();
    setState(258);
    match(BSParser::SPLIT);
    setState(259);
    variable();
    setState(260);
    match(BSParser::INTO);
    setState(261);
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
    setState(263);
    variableDefinition();
    setState(264);
    match(BSParser::DISPENSE);
    setState(266);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::INTEGER_LITERAL) {
      setState(265);
      unitTracker();
    }
    setState(268);
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

std::vector<BSParser::VariableContext *> BSParser::GradientContext::variable() {
  return getRuleContexts<BSParser::VariableContext>();
}

BSParser::VariableContext* BSParser::GradientContext::variable(size_t i) {
  return getRuleContext<BSParser::VariableContext>(i);
}

tree::TerminalNode* BSParser::GradientContext::WITH() {
  return getToken(BSParser::WITH, 0);
}

tree::TerminalNode* BSParser::GradientContext::RANGE() {
  return getToken(BSParser::RANGE, 0);
}

std::vector<tree::TerminalNode *> BSParser::GradientContext::FLOAT_LITERAL() {
  return getTokens(BSParser::FLOAT_LITERAL);
}

tree::TerminalNode* BSParser::GradientContext::FLOAT_LITERAL(size_t i) {
  return getToken(BSParser::FLOAT_LITERAL, i);
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
    setState(270);
    variableDefinition();
    setState(271);
    match(BSParser::GRADIENT);
    setState(272);
    variable();
    setState(273);
    match(BSParser::WITH);
    setState(274);
    variable();
    setState(275);
    match(BSParser::RANGE);
    setState(276);
    match(BSParser::FLOAT_LITERAL);
    setState(277);
    match(BSParser::COMMA);
    setState(278);
    match(BSParser::FLOAT_LITERAL);
    setState(279);
    match(BSParser::AT);
    setState(280);
    match(BSParser::FLOAT_LITERAL);

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
    setState(282);
    match(BSParser::STORE);
    setState(283);
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
    setState(285);
    variableDefinition();
    setState(286);
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
    setState(298);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(288);
      variableDefinition();
      setState(289);
      primary();
      setState(290);
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
      setState(291);
      primary();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(293);
      variableDefinition();
      setState(294);
      primary();
      setState(295);
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
      setState(296);
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
    setState(320);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 25, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(300);
      primary();
      setState(308);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 24, _ctx)) {
      case 1: {
        setState(301);
        match(BSParser::LT);
        setState(302);
        match(BSParser::LT);
        break;
      }

      case 2: {
        setState(303);
        match(BSParser::GT);
        setState(304);
        match(BSParser::GT);
        setState(305);
        match(BSParser::GT);
        break;
      }

      case 3: {
        setState(306);
        match(BSParser::GT);
        setState(307);
        match(BSParser::GT);
        break;
      }

      }
      setState(310);
      primary();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(312);
      primary();
      setState(313);
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
      setState(314);
      primary();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(316);
      primary();
      setState(317);
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
      setState(318);
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
    setState(322);
    match(BSParser::LPAREN);
    setState(323);
    binops();
    setState(328);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BSParser::AND

    || _la == BSParser::OR) {
      setState(324);
      _la = _input->LA(1);
      if (!(_la == BSParser::AND

      || _la == BSParser::OR)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(325);
      binops();
      setState(330);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(331);
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
    setState(333);
    variableDefinition();
    setState(334);
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
    setState(336);
    match(BSParser::IDENTIFIER);
    setState(337);
    match(BSParser::LPAREN);
    setState(339);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & ((1ULL << BSParser::IDENTIFIER)
      | (1ULL << BSParser::STRING_LITERAL)
      | (1ULL << BSParser::BOOL_LITERAL)
      | (1ULL << BSParser::FLOAT_LITERAL)
      | (1ULL << BSParser::INTEGER_LITERAL))) != 0)) {
      setState(338);
      expressionList();
    }
    setState(341);
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
    setState(343);
    primary();
    setState(348);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BSParser::COMMA) {
      setState(344);
      match(BSParser::COMMA);
      setState(345);
      primary();
      setState(350);
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

BSParser::ChemicalTypeContext* BSParser::TypeTypeContext::chemicalType() {
  return getRuleContext<BSParser::ChemicalTypeContext>(0);
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
    setState(353);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BSParser::NAT:
      case BSParser::REAL:
      case BSParser::MAT:
      case BSParser::BOOL: {
        enterOuterAlt(_localctx, 1);
        setState(351);
        primitiveType();
        break;
      }

      case BSParser::INTEGER_LITERAL:
      case BSParser::ACIDS_STRONG_NON_OXIDIZING:
      case BSParser::ACIDS_STRONG_OXIDIZING:
      case BSParser::ACIDS_CARBOXYLIC:
      case BSParser::ALCOHOLS_AND_POLYOLS:
      case BSParser::ALDEHYDES:
      case BSParser::AMIDES_AND_IMIDES:
      case BSParser::AMINES_PHOSPHINES_AND_PYRIDINES:
      case BSParser::AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS:
      case BSParser::CARBAMATES:
      case BSParser::BASES_STRONG:
      case BSParser::CYANIDES_INORGANIC:
      case BSParser::THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS:
      case BSParser::ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS:
      case BSParser::ETHERS:
      case BSParser::FLUORIDES_INORGANIC:
      case BSParser::HYDROCARBONS_AROMATIC:
      case BSParser::HALOGENATED_ORGANIC_COMPOUNDS:
      case BSParser::ISOCYANATES_AND_ISOTHIOCYANATES:
      case BSParser::KETONES:
      case BSParser::SULFIDES_ORGANIC:
      case BSParser::METALS_ALKALI_VERY_ACTIVE:
      case BSParser::METALS_ELEMENTAL_AND_POWDER_ACTIVE:
      case BSParser::METALS_LESS_REACTIVE:
      case BSParser::METALS_AND_METAL_COMPOUNDS_TOXIC:
      case BSParser::DIAZONIUM_SALTS:
      case BSParser::NITRILES:
      case BSParser::NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC:
      case BSParser::HYDROCARBONS_ALIPHATIC_UNSATURATED:
      case BSParser::HYDROCARBONS_ALIPHATIC_SATURATED:
      case BSParser::PEROXIDES_ORGANIC:
      case BSParser::PHENOLS_AND_CRESOLS:
      case BSParser::SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC:
      case BSParser::SULFIDES_INORGANIC:
      case BSParser::EPOXIDES:
      case BSParser::METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES:
      case BSParser::ANHYDRIDES:
      case BSParser::SALTS_ACIDIC:
      case BSParser::SALTS_BASIC:
      case BSParser::ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES:
      case BSParser::ORGANOMETALLICS:
      case BSParser::OXIDIZING_AGENTS_STRONG:
      case BSParser::REDUCING_AGENTS_STRONG:
      case BSParser::NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS:
      case BSParser::FLUORINATED_ORGANIC_COMPOUNDS:
      case BSParser::FLUORIDE_SALTS_SOLUBLE:
      case BSParser::OXIDIZING_AGENTS_WEAK:
      case BSParser::REDUCING_AGENTS_WEAK:
      case BSParser::NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES:
      case BSParser::CHLOROSILANES:
      case BSParser::SILOXANES:
      case BSParser::HALOGENATING_AGENTS:
      case BSParser::ACIDS_WEAK:
      case BSParser::BASES_WEAK:
      case BSParser::CARBONATE_SALTS:
      case BSParser::ALKYNES_WITH_ACETYLENIC_HYDROGEN:
      case BSParser::ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN:
      case BSParser::CONJUGATED_DIENES:
      case BSParser::ARYL_HALIDES:
      case BSParser::AMINES_AROMATIC:
      case BSParser::NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC:
      case BSParser::ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS:
      case BSParser::ACRYLATES_AND_ACRYLIC_ACIDS:
      case BSParser::PHENOLIC_SALTS:
      case BSParser::QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS:
      case BSParser::SULFITE_AND_THIOSULFATE_SALTS:
      case BSParser::OXIMES:
      case BSParser::POLYMERIZABLE_COMPOUNDS:
      case BSParser::NOT_CHEMICALLY_REACTIVE:
      case BSParser::INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION:
      case BSParser::WATER_AND_AQUEOUS_SOLUTIONS:
      case BSParser::NULL:
      case BSParser::UNKNOWN: {
        enterOuterAlt(_localctx, 2);
        setState(352);
        chemicalType();
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
    setState(355);
    match(BSParser::LBRACKET);
    setState(356);
    typesList();
    setState(357);
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
    setState(359);
    typeType();
    setState(364);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == BSParser::SEMICOLON) {
      setState(360);
      match(BSParser::SEMICOLON);
      setState(361);
      typeType();
      setState(366);
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
    setState(368);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == BSParser::LBRACKET) {
      setState(367);
      unionType();
    }
    setState(370);
    variable();
    setState(371);
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
    setState(373);
    match(BSParser::IDENTIFIER);
    setState(377);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 32, _ctx)) {
    case 1: {
      setState(374);
      match(BSParser::LBRACKET);
      setState(375);
      match(BSParser::INTEGER_LITERAL);
      setState(376);
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
    setState(381);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case BSParser::STRING_LITERAL:
      case BSParser::BOOL_LITERAL:
      case BSParser::FLOAT_LITERAL:
      case BSParser::INTEGER_LITERAL: {
        enterOuterAlt(_localctx, 1);
        setState(379);
        literal();
        break;
      }

      case BSParser::IDENTIFIER: {
        enterOuterAlt(_localctx, 2);
        setState(380);
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
    setState(383);
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
    setState(385);
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

//----------------- ChemicalTypeContext ------------------------------------------------------------------

BSParser::ChemicalTypeContext::ChemicalTypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* BSParser::ChemicalTypeContext::INTEGER_LITERAL() {
  return getToken(BSParser::INTEGER_LITERAL, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ACIDS_STRONG_NON_OXIDIZING() {
  return getToken(BSParser::ACIDS_STRONG_NON_OXIDIZING, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ACIDS_STRONG_OXIDIZING() {
  return getToken(BSParser::ACIDS_STRONG_OXIDIZING, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ACIDS_CARBOXYLIC() {
  return getToken(BSParser::ACIDS_CARBOXYLIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ALCOHOLS_AND_POLYOLS() {
  return getToken(BSParser::ALCOHOLS_AND_POLYOLS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ALDEHYDES() {
  return getToken(BSParser::ALDEHYDES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::AMIDES_AND_IMIDES() {
  return getToken(BSParser::AMIDES_AND_IMIDES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::AMINES_PHOSPHINES_AND_PYRIDINES() {
  return getToken(BSParser::AMINES_PHOSPHINES_AND_PYRIDINES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS() {
  return getToken(BSParser::AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::CARBAMATES() {
  return getToken(BSParser::CARBAMATES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::BASES_STRONG() {
  return getToken(BSParser::BASES_STRONG, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::CYANIDES_INORGANIC() {
  return getToken(BSParser::CYANIDES_INORGANIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS() {
  return getToken(BSParser::THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS() {
  return getToken(BSParser::ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ETHERS() {
  return getToken(BSParser::ETHERS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::FLUORIDES_INORGANIC() {
  return getToken(BSParser::FLUORIDES_INORGANIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::HYDROCARBONS_AROMATIC() {
  return getToken(BSParser::HYDROCARBONS_AROMATIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::HALOGENATED_ORGANIC_COMPOUNDS() {
  return getToken(BSParser::HALOGENATED_ORGANIC_COMPOUNDS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ISOCYANATES_AND_ISOTHIOCYANATES() {
  return getToken(BSParser::ISOCYANATES_AND_ISOTHIOCYANATES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::KETONES() {
  return getToken(BSParser::KETONES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::SULFIDES_ORGANIC() {
  return getToken(BSParser::SULFIDES_ORGANIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::METALS_ALKALI_VERY_ACTIVE() {
  return getToken(BSParser::METALS_ALKALI_VERY_ACTIVE, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::METALS_ELEMENTAL_AND_POWDER_ACTIVE() {
  return getToken(BSParser::METALS_ELEMENTAL_AND_POWDER_ACTIVE, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::METALS_LESS_REACTIVE() {
  return getToken(BSParser::METALS_LESS_REACTIVE, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::METALS_AND_METAL_COMPOUNDS_TOXIC() {
  return getToken(BSParser::METALS_AND_METAL_COMPOUNDS_TOXIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::DIAZONIUM_SALTS() {
  return getToken(BSParser::DIAZONIUM_SALTS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::NITRILES() {
  return getToken(BSParser::NITRILES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC() {
  return getToken(BSParser::NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::HYDROCARBONS_ALIPHATIC_UNSATURATED() {
  return getToken(BSParser::HYDROCARBONS_ALIPHATIC_UNSATURATED, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::HYDROCARBONS_ALIPHATIC_SATURATED() {
  return getToken(BSParser::HYDROCARBONS_ALIPHATIC_SATURATED, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::PEROXIDES_ORGANIC() {
  return getToken(BSParser::PEROXIDES_ORGANIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::PHENOLS_AND_CRESOLS() {
  return getToken(BSParser::PHENOLS_AND_CRESOLS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC() {
  return getToken(BSParser::SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::SULFIDES_INORGANIC() {
  return getToken(BSParser::SULFIDES_INORGANIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::EPOXIDES() {
  return getToken(BSParser::EPOXIDES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES() {
  return getToken(BSParser::METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ANHYDRIDES() {
  return getToken(BSParser::ANHYDRIDES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::SALTS_ACIDIC() {
  return getToken(BSParser::SALTS_ACIDIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::SALTS_BASIC() {
  return getToken(BSParser::SALTS_BASIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES() {
  return getToken(BSParser::ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ORGANOMETALLICS() {
  return getToken(BSParser::ORGANOMETALLICS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::OXIDIZING_AGENTS_STRONG() {
  return getToken(BSParser::OXIDIZING_AGENTS_STRONG, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::REDUCING_AGENTS_STRONG() {
  return getToken(BSParser::REDUCING_AGENTS_STRONG, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS() {
  return getToken(BSParser::NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::FLUORINATED_ORGANIC_COMPOUNDS() {
  return getToken(BSParser::FLUORINATED_ORGANIC_COMPOUNDS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::FLUORIDE_SALTS_SOLUBLE() {
  return getToken(BSParser::FLUORIDE_SALTS_SOLUBLE, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::OXIDIZING_AGENTS_WEAK() {
  return getToken(BSParser::OXIDIZING_AGENTS_WEAK, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::REDUCING_AGENTS_WEAK() {
  return getToken(BSParser::REDUCING_AGENTS_WEAK, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES() {
  return getToken(BSParser::NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::CHLOROSILANES() {
  return getToken(BSParser::CHLOROSILANES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::SILOXANES() {
  return getToken(BSParser::SILOXANES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::HALOGENATING_AGENTS() {
  return getToken(BSParser::HALOGENATING_AGENTS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ACIDS_WEAK() {
  return getToken(BSParser::ACIDS_WEAK, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::BASES_WEAK() {
  return getToken(BSParser::BASES_WEAK, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::CARBONATE_SALTS() {
  return getToken(BSParser::CARBONATE_SALTS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ALKYNES_WITH_ACETYLENIC_HYDROGEN() {
  return getToken(BSParser::ALKYNES_WITH_ACETYLENIC_HYDROGEN, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN() {
  return getToken(BSParser::ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::CONJUGATED_DIENES() {
  return getToken(BSParser::CONJUGATED_DIENES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ARYL_HALIDES() {
  return getToken(BSParser::ARYL_HALIDES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::AMINES_AROMATIC() {
  return getToken(BSParser::AMINES_AROMATIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC() {
  return getToken(BSParser::NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS() {
  return getToken(BSParser::ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::ACRYLATES_AND_ACRYLIC_ACIDS() {
  return getToken(BSParser::ACRYLATES_AND_ACRYLIC_ACIDS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::PHENOLIC_SALTS() {
  return getToken(BSParser::PHENOLIC_SALTS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS() {
  return getToken(BSParser::QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::SULFITE_AND_THIOSULFATE_SALTS() {
  return getToken(BSParser::SULFITE_AND_THIOSULFATE_SALTS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::OXIMES() {
  return getToken(BSParser::OXIMES, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::POLYMERIZABLE_COMPOUNDS() {
  return getToken(BSParser::POLYMERIZABLE_COMPOUNDS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::NOT_CHEMICALLY_REACTIVE() {
  return getToken(BSParser::NOT_CHEMICALLY_REACTIVE, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION() {
  return getToken(BSParser::INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::WATER_AND_AQUEOUS_SOLUTIONS() {
  return getToken(BSParser::WATER_AND_AQUEOUS_SOLUTIONS, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::NULL() {
  return getToken(BSParser::NULL, 0);
}

tree::TerminalNode* BSParser::ChemicalTypeContext::UNKNOWN() {
  return getToken(BSParser::UNKNOWN, 0);
}


size_t BSParser::ChemicalTypeContext::getRuleIndex() const {
  return BSParser::RuleChemicalType;
}

void BSParser::ChemicalTypeContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterChemicalType(this);
}

void BSParser::ChemicalTypeContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<BSParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitChemicalType(this);
}


antlrcpp::Any BSParser::ChemicalTypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<BSParserVisitor*>(visitor))
    return parserVisitor->visitChemicalType(this);
  else
    return visitor->visitChildren(this);
}

BSParser::ChemicalTypeContext* BSParser::chemicalType() {
  ChemicalTypeContext *_localctx = _tracker.createInstance<ChemicalTypeContext>(_ctx, getState());
  enterRule(_localctx, 80, BSParser::RuleChemicalType);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(387);
    _la = _input->LA(1);
    if (!(_la == BSParser::INTEGER_LITERAL || ((((_la - 97) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 97)) & ((1ULL << (BSParser::ACIDS_STRONG_NON_OXIDIZING - 97))
      | (1ULL << (BSParser::ACIDS_STRONG_OXIDIZING - 97))
      | (1ULL << (BSParser::ACIDS_CARBOXYLIC - 97))
      | (1ULL << (BSParser::ALCOHOLS_AND_POLYOLS - 97))
      | (1ULL << (BSParser::ALDEHYDES - 97))
      | (1ULL << (BSParser::AMIDES_AND_IMIDES - 97))
      | (1ULL << (BSParser::AMINES_PHOSPHINES_AND_PYRIDINES - 97))
      | (1ULL << (BSParser::AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS - 97))
      | (1ULL << (BSParser::CARBAMATES - 97))
      | (1ULL << (BSParser::BASES_STRONG - 97))
      | (1ULL << (BSParser::CYANIDES_INORGANIC - 97))
      | (1ULL << (BSParser::THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS - 97))
      | (1ULL << (BSParser::ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS - 97))
      | (1ULL << (BSParser::ETHERS - 97))
      | (1ULL << (BSParser::FLUORIDES_INORGANIC - 97))
      | (1ULL << (BSParser::HYDROCARBONS_AROMATIC - 97))
      | (1ULL << (BSParser::HALOGENATED_ORGANIC_COMPOUNDS - 97))
      | (1ULL << (BSParser::ISOCYANATES_AND_ISOTHIOCYANATES - 97))
      | (1ULL << (BSParser::KETONES - 97))
      | (1ULL << (BSParser::SULFIDES_ORGANIC - 97))
      | (1ULL << (BSParser::METALS_ALKALI_VERY_ACTIVE - 97))
      | (1ULL << (BSParser::METALS_ELEMENTAL_AND_POWDER_ACTIVE - 97))
      | (1ULL << (BSParser::METALS_LESS_REACTIVE - 97))
      | (1ULL << (BSParser::METALS_AND_METAL_COMPOUNDS_TOXIC - 97))
      | (1ULL << (BSParser::DIAZONIUM_SALTS - 97))
      | (1ULL << (BSParser::NITRILES - 97))
      | (1ULL << (BSParser::NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC - 97))
      | (1ULL << (BSParser::HYDROCARBONS_ALIPHATIC_UNSATURATED - 97))
      | (1ULL << (BSParser::HYDROCARBONS_ALIPHATIC_SATURATED - 97))
      | (1ULL << (BSParser::PEROXIDES_ORGANIC - 97))
      | (1ULL << (BSParser::PHENOLS_AND_CRESOLS - 97))
      | (1ULL << (BSParser::SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC - 97))
      | (1ULL << (BSParser::SULFIDES_INORGANIC - 97))
      | (1ULL << (BSParser::EPOXIDES - 97))
      | (1ULL << (BSParser::METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES - 97))
      | (1ULL << (BSParser::ANHYDRIDES - 97))
      | (1ULL << (BSParser::SALTS_ACIDIC - 97))
      | (1ULL << (BSParser::SALTS_BASIC - 97))
      | (1ULL << (BSParser::ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES - 97))
      | (1ULL << (BSParser::ORGANOMETALLICS - 97))
      | (1ULL << (BSParser::OXIDIZING_AGENTS_STRONG - 97))
      | (1ULL << (BSParser::REDUCING_AGENTS_STRONG - 97))
      | (1ULL << (BSParser::NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS - 97))
      | (1ULL << (BSParser::FLUORINATED_ORGANIC_COMPOUNDS - 97))
      | (1ULL << (BSParser::FLUORIDE_SALTS_SOLUBLE - 97))
      | (1ULL << (BSParser::OXIDIZING_AGENTS_WEAK - 97))
      | (1ULL << (BSParser::REDUCING_AGENTS_WEAK - 97))
      | (1ULL << (BSParser::NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES - 97))
      | (1ULL << (BSParser::CHLOROSILANES - 97))
      | (1ULL << (BSParser::SILOXANES - 97))
      | (1ULL << (BSParser::HALOGENATING_AGENTS - 97))
      | (1ULL << (BSParser::ACIDS_WEAK - 97))
      | (1ULL << (BSParser::BASES_WEAK - 97))
      | (1ULL << (BSParser::CARBONATE_SALTS - 97))
      | (1ULL << (BSParser::ALKYNES_WITH_ACETYLENIC_HYDROGEN - 97))
      | (1ULL << (BSParser::ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN - 97))
      | (1ULL << (BSParser::CONJUGATED_DIENES - 97))
      | (1ULL << (BSParser::ARYL_HALIDES - 97))
      | (1ULL << (BSParser::AMINES_AROMATIC - 97))
      | (1ULL << (BSParser::NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC - 97))
      | (1ULL << (BSParser::ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS - 97))
      | (1ULL << (BSParser::ACRYLATES_AND_ACRYLIC_ACIDS - 97))
      | (1ULL << (BSParser::PHENOLIC_SALTS - 97))
      | (1ULL << (BSParser::QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS - 97)))) != 0) || ((((_la - 161) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 161)) & ((1ULL << (BSParser::SULFITE_AND_THIOSULFATE_SALTS - 161))
      | (1ULL << (BSParser::OXIMES - 161))
      | (1ULL << (BSParser::POLYMERIZABLE_COMPOUNDS - 161))
      | (1ULL << (BSParser::NOT_CHEMICALLY_REACTIVE - 161))
      | (1ULL << (BSParser::INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION - 161))
      | (1ULL << (BSParser::WATER_AND_AQUEOUS_SOLUTIONS - 161))
      | (1ULL << (BSParser::NULL - 161))
      | (1ULL << (BSParser::UNKNOWN - 161)))) != 0))) {
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
  enterRule(_localctx, 82, BSParser::RuleTimeIdentifier);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(389);
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
  enterRule(_localctx, 84, BSParser::RuleTemperatureIdentifier);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(391);
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
  enterRule(_localctx, 86, BSParser::RuleUnitTracker);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(393);
    match(BSParser::INTEGER_LITERAL);
    setState(394);
    match(BSParser::UNITS);
    setState(395);
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
  "program", "globalDeclarations", "moduleDeclaration", "manifestDeclaration",
  "stationaryDeclaration", "functions", "functionDeclaration", "formalParameters",
  "formalParameterList", "formalParameter", "functionTyping", "returnStatement",
  "blockStatement", "statements", "ifStatement", "whileStatement", "repeat",
  "heat", "dispose", "mix", "detect", "split", "dispense", "gradient", "store",
  "numberAssignment", "math", "binops", "parExpression", "methodInvocation",
  "methodCall", "expressionList", "typeType", "unionType", "typesList",
  "variableDefinition", "variable", "primary", "literal", "primitiveType",
  "chemicalType", "timeIdentifier", "temperatureIdentifier", "unitTracker"
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
  "'k'", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", "'8'", "'9'",
  "'10'", "'11'", "'12'", "'13'", "'14'", "'15'", "'16'", "'17'", "'18'",
  "'19'", "'20'", "'21'", "'22'", "'23'", "'24'", "'25'", "'26'", "'27'",
  "'28'", "'29'", "'30'", "'31'", "'32'", "'33'", "'34'", "'35'", "'37'",
  "'38'", "'39'", "'40'", "'42'", "'44'", "'45'", "'46'", "'47'", "'48'",
  "'49'", "'50'", "'51'", "'55'", "'58'", "'59'", "'60'", "'61'", "'62'",
  "'63'", "'64'", "'65'", "'66'", "'68'", "'69'", "'70'", "'71'", "'72'",
  "'73'", "'74'", "'75'", "'76'", "'98'", "'99'", "'100'", "'134'", "'-1'"
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
  "CELSIUS", "FAHRENHEIT", "KELVIN", "ACIDS_STRONG_NON_OXIDIZING", "ACIDS_STRONG_OXIDIZING",
  "ACIDS_CARBOXYLIC", "ALCOHOLS_AND_POLYOLS", "ALDEHYDES", "AMIDES_AND_IMIDES",
  "AMINES_PHOSPHINES_AND_PYRIDINES", "AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS",
  "CARBAMATES", "BASES_STRONG", "CYANIDES_INORGANIC", "THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS",
  "ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS",
  "ETHERS", "FLUORIDES_INORGANIC", "HYDROCARBONS_AROMATIC", "HALOGENATED_ORGANIC_COMPOUNDS",
  "ISOCYANATES_AND_ISOTHIOCYANATES", "KETONES", "SULFIDES_ORGANIC", "METALS_ALKALI_VERY_ACTIVE",
  "METALS_ELEMENTAL_AND_POWDER_ACTIVE", "METALS_LESS_REACTIVE", "METALS_AND_METAL_COMPOUNDS_TOXIC",
  "DIAZONIUM_SALTS", "NITRILES", "NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC",
  "HYDROCARBONS_ALIPHATIC_UNSATURATED", "HYDROCARBONS_ALIPHATIC_SATURATED",
  "PEROXIDES_ORGANIC", "PHENOLS_AND_CRESOLS", "SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC",
  "SULFIDES_INORGANIC", "EPOXIDES", "METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES",
  "ANHYDRIDES", "SALTS_ACIDIC", "SALTS_BASIC", "ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES",
  "ORGANOMETALLICS", "OXIDIZING_AGENTS_STRONG", "REDUCING_AGENTS_STRONG",
  "NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS", "FLUORINATED_ORGANIC_COMPOUNDS",
  "FLUORIDE_SALTS_SOLUBLE", "OXIDIZING_AGENTS_WEAK", "REDUCING_AGENTS_WEAK",
  "NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES", "CHLOROSILANES", "SILOXANES",
  "HALOGENATING_AGENTS", "ACIDS_WEAK", "BASES_WEAK", "CARBONATE_SALTS",
  "ALKYNES_WITH_ACETYLENIC_HYDROGEN", "ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN",
  "CONJUGATED_DIENES", "ARYL_HALIDES", "AMINES_AROMATIC", "NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC",
  "ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS", "ACRYLATES_AND_ACRYLIC_ACIDS",
  "PHENOLIC_SALTS", "QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS", "SULFITE_AND_THIOSULFATE_SALTS",
  "OXIMES", "POLYMERIZABLE_COMPOUNDS", "NOT_CHEMICALLY_REACTIVE", "INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION",
  "WATER_AND_AQUEOUS_SOLUTIONS", "NULL", "UNKNOWN", "WS", "COMMENT", "LINE_COMMENT"
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
    0x3, 0xad, 0x190, 0x4, 0x2, 0x9, 0x2, 0x4, 0x3, 0x9, 0x3, 0x4, 0x4,
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
    0x2c, 0x9, 0x2c, 0x4, 0x2d, 0x9, 0x2d, 0x3, 0x2, 0x6, 0x2, 0x5c, 0xa,
    0x2, 0xd, 0x2, 0xe, 0x2, 0x5d, 0x3, 0x2, 0x5, 0x2, 0x61, 0xa, 0x2, 0x3,
    0x2, 0x3, 0x2, 0x3, 0x2, 0x7, 0x2, 0x66, 0xa, 0x2, 0xc, 0x2, 0xe, 0x2,
    0x69, 0xb, 0x2, 0x3, 0x2, 0x3, 0x2, 0x3, 0x3, 0x3, 0x3, 0x3, 0x3, 0x5,
    0x3, 0x70, 0xa, 0x3, 0x3, 0x4, 0x3, 0x4, 0x3, 0x4, 0x3, 0x5, 0x5, 0x5,
    0x76, 0xa, 0x5, 0x3, 0x5, 0x3, 0x5, 0x3, 0x5, 0x3, 0x6, 0x5, 0x6, 0x7c,
    0xa, 0x6, 0x3, 0x6, 0x3, 0x6, 0x3, 0x6, 0x3, 0x7, 0x3, 0x7, 0x3, 0x7,
    0x6, 0x7, 0x84, 0xa, 0x7, 0xd, 0x7, 0xe, 0x7, 0x85, 0x3, 0x8, 0x3, 0x8,
    0x3, 0x8, 0x3, 0x8, 0x5, 0x8, 0x8c, 0xa, 0x8, 0x3, 0x8, 0x3, 0x8, 0x7,
    0x8, 0x90, 0xa, 0x8, 0xc, 0x8, 0xe, 0x8, 0x93, 0xb, 0x8, 0x3, 0x8, 0x3,
    0x8, 0x3, 0x8, 0x3, 0x9, 0x3, 0x9, 0x5, 0x9, 0x9a, 0xa, 0x9, 0x3, 0x9,
    0x3, 0x9, 0x3, 0xa, 0x3, 0xa, 0x3, 0xa, 0x7, 0xa, 0xa1, 0xa, 0xa, 0xc,
    0xa, 0xe, 0xa, 0xa4, 0xb, 0xa, 0x3, 0xb, 0x5, 0xb, 0xa7, 0xa, 0xb, 0x3,
    0xb, 0x3, 0xb, 0x3, 0xc, 0x3, 0xc, 0x3, 0xc, 0x3, 0xd, 0x3, 0xd, 0x3,
    0xd, 0x3, 0xd, 0x5, 0xd, 0xb2, 0xa, 0xd, 0x3, 0xe, 0x3, 0xe, 0x7, 0xe,
    0xb6, 0xa, 0xe, 0xc, 0xe, 0xe, 0xe, 0xb9, 0xb, 0xe, 0x3, 0xe, 0x3, 0xe,
    0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf,
    0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf,
    0x3, 0xf, 0x5, 0xf, 0xcc, 0xa, 0xf, 0x3, 0x10, 0x3, 0x10, 0x3, 0x10,
    0x3, 0x10, 0x3, 0x10, 0x5, 0x10, 0xd3, 0xa, 0x10, 0x3, 0x11, 0x3, 0x11,
    0x3, 0x11, 0x3, 0x11, 0x3, 0x12, 0x3, 0x12, 0x3, 0x12, 0x3, 0x12, 0x3,
    0x12, 0x3, 0x13, 0x3, 0x13, 0x3, 0x13, 0x3, 0x13, 0x3, 0x13, 0x3, 0x13,
    0x5, 0x13, 0xe4, 0xa, 0x13, 0x3, 0x14, 0x3, 0x14, 0x3, 0x14, 0x3, 0x14,
    0x5, 0x14, 0xea, 0xa, 0x14, 0x3, 0x15, 0x3, 0x15, 0x3, 0x15, 0x5, 0x15,
    0xef, 0xa, 0x15, 0x3, 0x15, 0x3, 0x15, 0x3, 0x15, 0x5, 0x15, 0xf4, 0xa,
    0x15, 0x3, 0x15, 0x3, 0x15, 0x3, 0x15, 0x5, 0x15, 0xf9, 0xa, 0x15, 0x3,
    0x16, 0x3, 0x16, 0x3, 0x16, 0x3, 0x16, 0x3, 0x16, 0x3, 0x16, 0x3, 0x16,
    0x5, 0x16, 0x102, 0xa, 0x16, 0x3, 0x17, 0x3, 0x17, 0x3, 0x17, 0x3, 0x17,
    0x3, 0x17, 0x3, 0x17, 0x3, 0x18, 0x3, 0x18, 0x3, 0x18, 0x5, 0x18, 0x10d,
    0xa, 0x18, 0x3, 0x18, 0x3, 0x18, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19, 0x3,
    0x19, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19, 0x3, 0x19,
    0x3, 0x19, 0x3, 0x19, 0x3, 0x1a, 0x3, 0x1a, 0x3, 0x1a, 0x3, 0x1b, 0x3,
    0x1b, 0x3, 0x1b, 0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1c,
    0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1c, 0x5, 0x1c, 0x12d,
    0xa, 0x1c, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3,
    0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x5, 0x1d, 0x137, 0xa, 0x1d, 0x3, 0x1d,
    0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3,
    0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x5, 0x1d, 0x143, 0xa, 0x1d, 0x3, 0x1e,
    0x3, 0x1e, 0x3, 0x1e, 0x3, 0x1e, 0x7, 0x1e, 0x149, 0xa, 0x1e, 0xc, 0x1e,
    0xe, 0x1e, 0x14c, 0xb, 0x1e, 0x3, 0x1e, 0x3, 0x1e, 0x3, 0x1f, 0x3, 0x1f,
    0x3, 0x1f, 0x3, 0x20, 0x3, 0x20, 0x3, 0x20, 0x5, 0x20, 0x156, 0xa, 0x20,
    0x3, 0x20, 0x3, 0x20, 0x3, 0x21, 0x3, 0x21, 0x3, 0x21, 0x7, 0x21, 0x15d,
    0xa, 0x21, 0xc, 0x21, 0xe, 0x21, 0x160, 0xb, 0x21, 0x3, 0x22, 0x3, 0x22,
    0x5, 0x22, 0x164, 0xa, 0x22, 0x3, 0x23, 0x3, 0x23, 0x3, 0x23, 0x3, 0x23,
    0x3, 0x24, 0x3, 0x24, 0x3, 0x24, 0x7, 0x24, 0x16d, 0xa, 0x24, 0xc, 0x24,
    0xe, 0x24, 0x170, 0xb, 0x24, 0x3, 0x25, 0x5, 0x25, 0x173, 0xa, 0x25,
    0x3, 0x25, 0x3, 0x25, 0x3, 0x25, 0x3, 0x26, 0x3, 0x26, 0x3, 0x26, 0x3,
    0x26, 0x5, 0x26, 0x17c, 0xa, 0x26, 0x3, 0x27, 0x3, 0x27, 0x5, 0x27,
    0x180, 0xa, 0x27, 0x3, 0x28, 0x3, 0x28, 0x3, 0x29, 0x3, 0x29, 0x3, 0x2a,
    0x3, 0x2a, 0x3, 0x2b, 0x3, 0x2b, 0x3, 0x2c, 0x3, 0x2c, 0x3, 0x2d, 0x3,
    0x2d, 0x3, 0x2d, 0x3, 0x2d, 0x3, 0x2d, 0x2, 0x2, 0x2e, 0x2, 0x4, 0x6,
    0x8, 0xa, 0xc, 0xe, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e,
    0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36,
    0x38, 0x3a, 0x3c, 0x3e, 0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e,
    0x50, 0x52, 0x54, 0x56, 0x58, 0x2, 0xa, 0x4, 0x2, 0x46, 0x47, 0x4b,
    0x4b, 0x3, 0x2, 0x44, 0x45, 0x4, 0x2, 0x36, 0x37, 0x3d, 0x3e, 0x4, 0x2,
    0x3c, 0x3c, 0x3f, 0x3f, 0x3, 0x2, 0x40, 0x41, 0x3, 0x2, 0x25, 0x28,
    0x3, 0x2, 0x20, 0x23, 0x4, 0x2, 0x28, 0x28, 0x63, 0xaa, 0x2, 0x195,
    0x2, 0x5b, 0x3, 0x2, 0x2, 0x2, 0x4, 0x6f, 0x3, 0x2, 0x2, 0x2, 0x6, 0x71,
    0x3, 0x2, 0x2, 0x2, 0x8, 0x75, 0x3, 0x2, 0x2, 0x2, 0xa, 0x7b, 0x3, 0x2,
    0x2, 0x2, 0xc, 0x80, 0x3, 0x2, 0x2, 0x2, 0xe, 0x87, 0x3, 0x2, 0x2, 0x2,
    0x10, 0x97, 0x3, 0x2, 0x2, 0x2, 0x12, 0x9d, 0x3, 0x2, 0x2, 0x2, 0x14,
    0xa6, 0x3, 0x2, 0x2, 0x2, 0x16, 0xaa, 0x3, 0x2, 0x2, 0x2, 0x18, 0xb1,
    0x3, 0x2, 0x2, 0x2, 0x1a, 0xb3, 0x3, 0x2, 0x2, 0x2, 0x1c, 0xcb, 0x3,
    0x2, 0x2, 0x2, 0x1e, 0xcd, 0x3, 0x2, 0x2, 0x2, 0x20, 0xd4, 0x3, 0x2,
    0x2, 0x2, 0x22, 0xd8, 0x3, 0x2, 0x2, 0x2, 0x24, 0xdd, 0x3, 0x2, 0x2,
    0x2, 0x26, 0xe9, 0x3, 0x2, 0x2, 0x2, 0x28, 0xeb, 0x3, 0x2, 0x2, 0x2,
    0x2a, 0xfa, 0x3, 0x2, 0x2, 0x2, 0x2c, 0x103, 0x3, 0x2, 0x2, 0x2, 0x2e,
    0x109, 0x3, 0x2, 0x2, 0x2, 0x30, 0x110, 0x3, 0x2, 0x2, 0x2, 0x32, 0x11c,
    0x3, 0x2, 0x2, 0x2, 0x34, 0x11f, 0x3, 0x2, 0x2, 0x2, 0x36, 0x12c, 0x3,
    0x2, 0x2, 0x2, 0x38, 0x142, 0x3, 0x2, 0x2, 0x2, 0x3a, 0x144, 0x3, 0x2,
    0x2, 0x2, 0x3c, 0x14f, 0x3, 0x2, 0x2, 0x2, 0x3e, 0x152, 0x3, 0x2, 0x2,
    0x2, 0x40, 0x159, 0x3, 0x2, 0x2, 0x2, 0x42, 0x163, 0x3, 0x2, 0x2, 0x2,
    0x44, 0x165, 0x3, 0x2, 0x2, 0x2, 0x46, 0x169, 0x3, 0x2, 0x2, 0x2, 0x48,
    0x172, 0x3, 0x2, 0x2, 0x2, 0x4a, 0x177, 0x3, 0x2, 0x2, 0x2, 0x4c, 0x17f,
    0x3, 0x2, 0x2, 0x2, 0x4e, 0x181, 0x3, 0x2, 0x2, 0x2, 0x50, 0x183, 0x3,
    0x2, 0x2, 0x2, 0x52, 0x185, 0x3, 0x2, 0x2, 0x2, 0x54, 0x187, 0x3, 0x2,
    0x2, 0x2, 0x56, 0x189, 0x3, 0x2, 0x2, 0x2, 0x58, 0x18b, 0x3, 0x2, 0x2,
    0x2, 0x5a, 0x5c, 0x5, 0x4, 0x3, 0x2, 0x5b, 0x5a, 0x3, 0x2, 0x2, 0x2,
    0x5c, 0x5d, 0x3, 0x2, 0x2, 0x2, 0x5d, 0x5b, 0x3, 0x2, 0x2, 0x2, 0x5d,
    0x5e, 0x3, 0x2, 0x2, 0x2, 0x5e, 0x60, 0x3, 0x2, 0x2, 0x2, 0x5f, 0x61,
    0x5, 0xc, 0x7, 0x2, 0x60, 0x5f, 0x3, 0x2, 0x2, 0x2, 0x60, 0x61, 0x3,
    0x2, 0x2, 0x2, 0x61, 0x62, 0x3, 0x2, 0x2, 0x2, 0x62, 0x63, 0x7, 0xd,
    0x2, 0x2, 0x63, 0x67, 0x7, 0x3b, 0x2, 0x2, 0x64, 0x66, 0x5, 0x1c, 0xf,
    0x2, 0x65, 0x64, 0x3, 0x2, 0x2, 0x2, 0x66, 0x69, 0x3, 0x2, 0x2, 0x2,
    0x67, 0x65, 0x3, 0x2, 0x2, 0x2, 0x67, 0x68, 0x3, 0x2, 0x2, 0x2, 0x68,
    0x6a, 0x3, 0x2, 0x2, 0x2, 0x69, 0x67, 0x3, 0x2, 0x2, 0x2, 0x6a, 0x6b,
    0x7, 0x2, 0x2, 0x3, 0x6b, 0x3, 0x3, 0x2, 0x2, 0x2, 0x6c, 0x70, 0x5,
    0x6, 0x4, 0x2, 0x6d, 0x70, 0x5, 0x8, 0x5, 0x2, 0x6e, 0x70, 0x5, 0xa,
    0x6, 0x2, 0x6f, 0x6c, 0x3, 0x2, 0x2, 0x2, 0x6f, 0x6d, 0x3, 0x2, 0x2,
    0x2, 0x6f, 0x6e, 0x3, 0x2, 0x2, 0x2, 0x70, 0x5, 0x3, 0x2, 0x2, 0x2,
    0x71, 0x72, 0x7, 0xa, 0x2, 0x2, 0x72, 0x73, 0x7, 0x24, 0x2, 0x2, 0x73,
    0x7, 0x3, 0x2, 0x2, 0x2, 0x74, 0x76, 0x5, 0x44, 0x23, 0x2, 0x75, 0x74,
    0x3, 0x2, 0x2, 0x2, 0x75, 0x76, 0x3, 0x2, 0x2, 0x2, 0x76, 0x77, 0x3,
    0x2, 0x2, 0x2, 0x77, 0x78, 0x7, 0x9, 0x2, 0x2, 0x78, 0x79, 0x7, 0x24,
    0x2, 0x2, 0x79, 0x9, 0x3, 0x2, 0x2, 0x2, 0x7a, 0x7c, 0x5, 0x44, 0x23,
    0x2, 0x7b, 0x7a, 0x3, 0x2, 0x2, 0x2, 0x7b, 0x7c, 0x3, 0x2, 0x2, 0x2,
    0x7c, 0x7d, 0x3, 0x2, 0x2, 0x2, 0x7d, 0x7e, 0x7, 0xb, 0x2, 0x2, 0x7e,
    0x7f, 0x7, 0x24, 0x2, 0x2, 0x7f, 0xb, 0x3, 0x2, 0x2, 0x2, 0x80, 0x81,
    0x7, 0xc, 0x2, 0x2, 0x81, 0x83, 0x7, 0x3b, 0x2, 0x2, 0x82, 0x84, 0x5,
    0xe, 0x8, 0x2, 0x83, 0x82, 0x3, 0x2, 0x2, 0x2, 0x84, 0x85, 0x3, 0x2,
    0x2, 0x2, 0x85, 0x83, 0x3, 0x2, 0x2, 0x2, 0x85, 0x86, 0x3, 0x2, 0x2,
    0x2, 0x86, 0xd, 0x3, 0x2, 0x2, 0x2, 0x87, 0x88, 0x7, 0x7, 0x2, 0x2,
    0x88, 0x89, 0x7, 0x24, 0x2, 0x2, 0x89, 0x8b, 0x5, 0x10, 0x9, 0x2, 0x8a,
    0x8c, 0x5, 0x16, 0xc, 0x2, 0x8b, 0x8a, 0x3, 0x2, 0x2, 0x2, 0x8b, 0x8c,
    0x3, 0x2, 0x2, 0x2, 0x8c, 0x8d, 0x3, 0x2, 0x2, 0x2, 0x8d, 0x91, 0x7,
    0x2e, 0x2, 0x2, 0x8e, 0x90, 0x5, 0x1c, 0xf, 0x2, 0x8f, 0x8e, 0x3, 0x2,
    0x2, 0x2, 0x90, 0x93, 0x3, 0x2, 0x2, 0x2, 0x91, 0x8f, 0x3, 0x2, 0x2,
    0x2, 0x91, 0x92, 0x3, 0x2, 0x2, 0x2, 0x92, 0x94, 0x3, 0x2, 0x2, 0x2,
    0x93, 0x91, 0x3, 0x2, 0x2, 0x2, 0x94, 0x95, 0x5, 0x18, 0xd, 0x2, 0x95,
    0x96, 0x7, 0x2f, 0x2, 0x2, 0x96, 0xf, 0x3, 0x2, 0x2, 0x2, 0x97, 0x99,
    0x7, 0x2c, 0x2, 0x2, 0x98, 0x9a, 0x5, 0x12, 0xa, 0x2, 0x99, 0x98, 0x3,
    0x2, 0x2, 0x2, 0x99, 0x9a, 0x3, 0x2, 0x2, 0x2, 0x9a, 0x9b, 0x3, 0x2,
    0x2, 0x2, 0x9b, 0x9c, 0x7, 0x2d, 0x2, 0x2, 0x9c, 0x11, 0x3, 0x2, 0x2,
    0x2, 0x9d, 0xa2, 0x5, 0x14, 0xb, 0x2, 0x9e, 0x9f, 0x7, 0x33, 0x2, 0x2,
    0x9f, 0xa1, 0x5, 0x14, 0xb, 0x2, 0xa0, 0x9e, 0x3, 0x2, 0x2, 0x2, 0xa1,
    0xa4, 0x3, 0x2, 0x2, 0x2, 0xa2, 0xa0, 0x3, 0x2, 0x2, 0x2, 0xa2, 0xa3,
    0x3, 0x2, 0x2, 0x2, 0xa3, 0x13, 0x3, 0x2, 0x2, 0x2, 0xa4, 0xa2, 0x3,
    0x2, 0x2, 0x2, 0xa5, 0xa7, 0x5, 0x44, 0x23, 0x2, 0xa6, 0xa5, 0x3, 0x2,
    0x2, 0x2, 0xa6, 0xa7, 0x3, 0x2, 0x2, 0x2, 0xa7, 0xa8, 0x3, 0x2, 0x2,
    0x2, 0xa8, 0xa9, 0x7, 0x24, 0x2, 0x2, 0xa9, 0x15, 0x3, 0x2, 0x2, 0x2,
    0xaa, 0xab, 0x7, 0x3b, 0x2, 0x2, 0xab, 0xac, 0x5, 0x44, 0x23, 0x2, 0xac,
    0x17, 0x3, 0x2, 0x2, 0x2, 0xad, 0xae, 0x7, 0x8, 0x2, 0x2, 0xae, 0xb2,
    0x5, 0x4c, 0x27, 0x2, 0xaf, 0xb0, 0x7, 0x8, 0x2, 0x2, 0xb0, 0xb2, 0x5,
    0x3e, 0x20, 0x2, 0xb1, 0xad, 0x3, 0x2, 0x2, 0x2, 0xb1, 0xaf, 0x3, 0x2,
    0x2, 0x2, 0xb2, 0x19, 0x3, 0x2, 0x2, 0x2, 0xb3, 0xb7, 0x7, 0x2e, 0x2,
    0x2, 0xb4, 0xb6, 0x5, 0x1c, 0xf, 0x2, 0xb5, 0xb4, 0x3, 0x2, 0x2, 0x2,
    0xb6, 0xb9, 0x3, 0x2, 0x2, 0x2, 0xb7, 0xb5, 0x3, 0x2, 0x2, 0x2, 0xb7,
    0xb8, 0x3, 0x2, 0x2, 0x2, 0xb8, 0xba, 0x3, 0x2, 0x2, 0x2, 0xb9, 0xb7,
    0x3, 0x2, 0x2, 0x2, 0xba, 0xbb, 0x7, 0x2f, 0x2, 0x2, 0xbb, 0x1b, 0x3,
    0x2, 0x2, 0x2, 0xbc, 0xcc, 0x5, 0x1e, 0x10, 0x2, 0xbd, 0xcc, 0x5, 0x20,
    0x11, 0x2, 0xbe, 0xcc, 0x5, 0x48, 0x25, 0x2, 0xbf, 0xcc, 0x5, 0x22,
    0x12, 0x2, 0xc0, 0xcc, 0x5, 0x24, 0x13, 0x2, 0xc1, 0xcc, 0x5, 0x26,
    0x14, 0x2, 0xc2, 0xcc, 0x5, 0x28, 0x15, 0x2, 0xc3, 0xcc, 0x5, 0x2e,
    0x18, 0x2, 0xc4, 0xcc, 0x5, 0x2c, 0x17, 0x2, 0xc5, 0xcc, 0x5, 0x3c,
    0x1f, 0x2, 0xc6, 0xcc, 0x5, 0x30, 0x19, 0x2, 0xc7, 0xcc, 0x5, 0x2a,
    0x16, 0x2, 0xc8, 0xcc, 0x5, 0x32, 0x1a, 0x2, 0xc9, 0xcc, 0x5, 0x36,
    0x1c, 0x2, 0xca, 0xcc, 0x5, 0x34, 0x1b, 0x2, 0xcb, 0xbc, 0x3, 0x2, 0x2,
    0x2, 0xcb, 0xbd, 0x3, 0x2, 0x2, 0x2, 0xcb, 0xbe, 0x3, 0x2, 0x2, 0x2,
    0xcb, 0xbf, 0x3, 0x2, 0x2, 0x2, 0xcb, 0xc0, 0x3, 0x2, 0x2, 0x2, 0xcb,
    0xc1, 0x3, 0x2, 0x2, 0x2, 0xcb, 0xc2, 0x3, 0x2, 0x2, 0x2, 0xcb, 0xc3,
    0x3, 0x2, 0x2, 0x2, 0xcb, 0xc4, 0x3, 0x2, 0x2, 0x2, 0xcb, 0xc5, 0x3,
    0x2, 0x2, 0x2, 0xcb, 0xc6, 0x3, 0x2, 0x2, 0x2, 0xcb, 0xc7, 0x3, 0x2,
    0x2, 0x2, 0xcb, 0xc8, 0x3, 0x2, 0x2, 0x2, 0xcb, 0xc9, 0x3, 0x2, 0x2,
    0x2, 0xcb, 0xca, 0x3, 0x2, 0x2, 0x2, 0xcc, 0x1d, 0x3, 0x2, 0x2, 0x2,
    0xcd, 0xce, 0x7, 0x3, 0x2, 0x2, 0xce, 0xcf, 0x5, 0x3a, 0x1e, 0x2, 0xcf,
    0xd2, 0x5, 0x1a, 0xe, 0x2, 0xd0, 0xd1, 0x7, 0x4, 0x2, 0x2, 0xd1, 0xd3,
    0x5, 0x1a, 0xe, 0x2, 0xd2, 0xd0, 0x3, 0x2, 0x2, 0x2, 0xd2, 0xd3, 0x3,
    0x2, 0x2, 0x2, 0xd3, 0x1f, 0x3, 0x2, 0x2, 0x2, 0xd4, 0xd5, 0x7, 0x6,
    0x2, 0x2, 0xd5, 0xd6, 0x5, 0x3a, 0x1e, 0x2, 0xd6, 0xd7, 0x5, 0x1a, 0xe,
    0x2, 0xd7, 0x21, 0x3, 0x2, 0x2, 0x2, 0xd8, 0xd9, 0x7, 0x5, 0x2, 0x2,
    0xd9, 0xda, 0x7, 0x28, 0x2, 0x2, 0xda, 0xdb, 0x7, 0x1c, 0x2, 0x2, 0xdb,
    0xdc, 0x5, 0x1a, 0xe, 0x2, 0xdc, 0x23, 0x3, 0x2, 0x2, 0x2, 0xdd, 0xde,
    0x7, 0x11, 0x2, 0x2, 0xde, 0xdf, 0x5, 0x4a, 0x26, 0x2, 0xdf, 0xe0, 0x7,
    0x18, 0x2, 0x2, 0xe0, 0xe3, 0x5, 0x56, 0x2c, 0x2, 0xe1, 0xe2, 0x7, 0x1a,
    0x2, 0x2, 0xe2, 0xe4, 0x5, 0x54, 0x2b, 0x2, 0xe3, 0xe1, 0x3, 0x2, 0x2,
    0x2, 0xe3, 0xe4, 0x3, 0x2, 0x2, 0x2, 0xe4, 0x25, 0x3, 0x2, 0x2, 0x2,
    0xe5, 0xe6, 0x7, 0x12, 0x2, 0x2, 0xe6, 0xea, 0x5, 0x4a, 0x26, 0x2, 0xe7,
    0xe8, 0x7, 0x14, 0x2, 0x2, 0xe8, 0xea, 0x5, 0x4a, 0x26, 0x2, 0xe9, 0xe5,
    0x3, 0x2, 0x2, 0x2, 0xe9, 0xe7, 0x3, 0x2, 0x2, 0x2, 0xea, 0x27, 0x3,
    0x2, 0x2, 0x2, 0xeb, 0xec, 0x5, 0x48, 0x25, 0x2, 0xec, 0xee, 0x7, 0xf,
    0x2, 0x2, 0xed, 0xef, 0x5, 0x58, 0x2d, 0x2, 0xee, 0xed, 0x3, 0x2, 0x2,
    0x2, 0xee, 0xef, 0x3, 0x2, 0x2, 0x2, 0xef, 0xf0, 0x3, 0x2, 0x2, 0x2,
    0xf0, 0xf1, 0x5, 0x4a, 0x26, 0x2, 0xf1, 0xf3, 0x7, 0x19, 0x2, 0x2, 0xf2,
    0xf4, 0x5, 0x58, 0x2d, 0x2, 0xf3, 0xf2, 0x3, 0x2, 0x2, 0x2, 0xf3, 0xf4,
    0x3, 0x2, 0x2, 0x2, 0xf4, 0xf5, 0x3, 0x2, 0x2, 0x2, 0xf5, 0xf8, 0x5,
    0x4a, 0x26, 0x2, 0xf6, 0xf7, 0x7, 0x1a, 0x2, 0x2, 0xf7, 0xf9, 0x5, 0x54,
    0x2b, 0x2, 0xf8, 0xf6, 0x3, 0x2, 0x2, 0x2, 0xf8, 0xf9, 0x3, 0x2, 0x2,
    0x2, 0xf9, 0x29, 0x3, 0x2, 0x2, 0x2, 0xfa, 0xfb, 0x5, 0x48, 0x25, 0x2,
    0xfb, 0xfc, 0x7, 0xe, 0x2, 0x2, 0xfc, 0xfd, 0x7, 0x24, 0x2, 0x2, 0xfd,
    0xfe, 0x7, 0x1d, 0x2, 0x2, 0xfe, 0x101, 0x5, 0x4a, 0x26, 0x2, 0xff,
    0x100, 0x7, 0x1a, 0x2, 0x2, 0x100, 0x102, 0x5, 0x54, 0x2b, 0x2, 0x101,
    0xff, 0x3, 0x2, 0x2, 0x2, 0x101, 0x102, 0x3, 0x2, 0x2, 0x2, 0x102, 0x2b,
    0x3, 0x2, 0x2, 0x2, 0x103, 0x104, 0x5, 0x48, 0x25, 0x2, 0x104, 0x105,
    0x7, 0x10, 0x2, 0x2, 0x105, 0x106, 0x5, 0x4a, 0x26, 0x2, 0x106, 0x107,
    0x7, 0x1b, 0x2, 0x2, 0x107, 0x108, 0x7, 0x28, 0x2, 0x2, 0x108, 0x2d,
    0x3, 0x2, 0x2, 0x2, 0x109, 0x10a, 0x5, 0x48, 0x25, 0x2, 0x10a, 0x10c,
    0x7, 0x13, 0x2, 0x2, 0x10b, 0x10d, 0x5, 0x58, 0x2d, 0x2, 0x10c, 0x10b,
    0x3, 0x2, 0x2, 0x2, 0x10c, 0x10d, 0x3, 0x2, 0x2, 0x2, 0x10d, 0x10e,
    0x3, 0x2, 0x2, 0x2, 0x10e, 0x10f, 0x7, 0x24, 0x2, 0x2, 0x10f, 0x2f,
    0x3, 0x2, 0x2, 0x2, 0x110, 0x111, 0x5, 0x48, 0x25, 0x2, 0x111, 0x112,
    0x7, 0x15, 0x2, 0x2, 0x112, 0x113, 0x5, 0x4a, 0x26, 0x2, 0x113, 0x114,
    0x7, 0x19, 0x2, 0x2, 0x114, 0x115, 0x5, 0x4a, 0x26, 0x2, 0x115, 0x116,
    0x7, 0x17, 0x2, 0x2, 0x116, 0x117, 0x7, 0x27, 0x2, 0x2, 0x117, 0x118,
    0x7, 0x33, 0x2, 0x2, 0x118, 0x119, 0x7, 0x27, 0x2, 0x2, 0x119, 0x11a,
    0x7, 0x18, 0x2, 0x2, 0x11a, 0x11b, 0x7, 0x27, 0x2, 0x2, 0x11b, 0x31,
    0x3, 0x2, 0x2, 0x2, 0x11c, 0x11d, 0x7, 0x16, 0x2, 0x2, 0x11d, 0x11e,
    0x5, 0x4a, 0x26, 0x2, 0x11e, 0x33, 0x3, 0x2, 0x2, 0x2, 0x11f, 0x120,
    0x5, 0x48, 0x25, 0x2, 0x120, 0x121, 0x5, 0x4e, 0x28, 0x2, 0x121, 0x35,
    0x3, 0x2, 0x2, 0x2, 0x122, 0x123, 0x5, 0x48, 0x25, 0x2, 0x123, 0x124,
    0x5, 0x4c, 0x27, 0x2, 0x124, 0x125, 0x9, 0x2, 0x2, 0x2, 0x125, 0x126,
    0x5, 0x4c, 0x27, 0x2, 0x126, 0x12d, 0x3, 0x2, 0x2, 0x2, 0x127, 0x128,
    0x5, 0x48, 0x25, 0x2, 0x128, 0x129, 0x5, 0x4c, 0x27, 0x2, 0x129, 0x12a,
    0x9, 0x3, 0x2, 0x2, 0x12a, 0x12b, 0x5, 0x4c, 0x27, 0x2, 0x12b, 0x12d,
    0x3, 0x2, 0x2, 0x2, 0x12c, 0x122, 0x3, 0x2, 0x2, 0x2, 0x12c, 0x127,
    0x3, 0x2, 0x2, 0x2, 0x12d, 0x37, 0x3, 0x2, 0x2, 0x2, 0x12e, 0x136, 0x5,
    0x4c, 0x27, 0x2, 0x12f, 0x130, 0x7, 0x37, 0x2, 0x2, 0x130, 0x137, 0x7,
    0x37, 0x2, 0x2, 0x131, 0x132, 0x7, 0x36, 0x2, 0x2, 0x132, 0x133, 0x7,
    0x36, 0x2, 0x2, 0x133, 0x137, 0x7, 0x36, 0x2, 0x2, 0x134, 0x135, 0x7,
    0x36, 0x2, 0x2, 0x135, 0x137, 0x7, 0x36, 0x2, 0x2, 0x136, 0x12f, 0x3,
    0x2, 0x2, 0x2, 0x136, 0x131, 0x3, 0x2, 0x2, 0x2, 0x136, 0x134, 0x3,
    0x2, 0x2, 0x2, 0x137, 0x138, 0x3, 0x2, 0x2, 0x2, 0x138, 0x139, 0x5,
    0x4c, 0x27, 0x2, 0x139, 0x143, 0x3, 0x2, 0x2, 0x2, 0x13a, 0x13b, 0x5,
    0x4c, 0x27, 0x2, 0x13b, 0x13c, 0x9, 0x4, 0x2, 0x2, 0x13c, 0x13d, 0x5,
    0x4c, 0x27, 0x2, 0x13d, 0x143, 0x3, 0x2, 0x2, 0x2, 0x13e, 0x13f, 0x5,
    0x4c, 0x27, 0x2, 0x13f, 0x140, 0x9, 0x5, 0x2, 0x2, 0x140, 0x141, 0x5,
    0x4c, 0x27, 0x2, 0x141, 0x143, 0x3, 0x2, 0x2, 0x2, 0x142, 0x12e, 0x3,
    0x2, 0x2, 0x2, 0x142, 0x13a, 0x3, 0x2, 0x2, 0x2, 0x142, 0x13e, 0x3,
    0x2, 0x2, 0x2, 0x143, 0x39, 0x3, 0x2, 0x2, 0x2, 0x144, 0x145, 0x7, 0x2c,
    0x2, 0x2, 0x145, 0x14a, 0x5, 0x38, 0x1d, 0x2, 0x146, 0x147, 0x9, 0x6,
    0x2, 0x2, 0x147, 0x149, 0x5, 0x38, 0x1d, 0x2, 0x148, 0x146, 0x3, 0x2,
    0x2, 0x2, 0x149, 0x14c, 0x3, 0x2, 0x2, 0x2, 0x14a, 0x148, 0x3, 0x2,
    0x2, 0x2, 0x14a, 0x14b, 0x3, 0x2, 0x2, 0x2, 0x14b, 0x14d, 0x3, 0x2,
    0x2, 0x2, 0x14c, 0x14a, 0x3, 0x2, 0x2, 0x2, 0x14d, 0x14e, 0x7, 0x2d,
    0x2, 0x2, 0x14e, 0x3b, 0x3, 0x2, 0x2, 0x2, 0x14f, 0x150, 0x5, 0x48,
    0x25, 0x2, 0x150, 0x151, 0x5, 0x3e, 0x20, 0x2, 0x151, 0x3d, 0x3, 0x2,
    0x2, 0x2, 0x152, 0x153, 0x7, 0x24, 0x2, 0x2, 0x153, 0x155, 0x7, 0x2c,
    0x2, 0x2, 0x154, 0x156, 0x5, 0x40, 0x21, 0x2, 0x155, 0x154, 0x3, 0x2,
    0x2, 0x2, 0x155, 0x156, 0x3, 0x2, 0x2, 0x2, 0x156, 0x157, 0x3, 0x2,
    0x2, 0x2, 0x157, 0x158, 0x7, 0x2d, 0x2, 0x2, 0x158, 0x3f, 0x3, 0x2,
    0x2, 0x2, 0x159, 0x15e, 0x5, 0x4c, 0x27, 0x2, 0x15a, 0x15b, 0x7, 0x33,
    0x2, 0x2, 0x15b, 0x15d, 0x5, 0x4c, 0x27, 0x2, 0x15c, 0x15a, 0x3, 0x2,
    0x2, 0x2, 0x15d, 0x160, 0x3, 0x2, 0x2, 0x2, 0x15e, 0x15c, 0x3, 0x2,
    0x2, 0x2, 0x15e, 0x15f, 0x3, 0x2, 0x2, 0x2, 0x15f, 0x41, 0x3, 0x2, 0x2,
    0x2, 0x160, 0x15e, 0x3, 0x2, 0x2, 0x2, 0x161, 0x164, 0x5, 0x50, 0x29,
    0x2, 0x162, 0x164, 0x5, 0x52, 0x2a, 0x2, 0x163, 0x161, 0x3, 0x2, 0x2,
    0x2, 0x163, 0x162, 0x3, 0x2, 0x2, 0x2, 0x164, 0x43, 0x3, 0x2, 0x2, 0x2,
    0x165, 0x166, 0x7, 0x30, 0x2, 0x2, 0x166, 0x167, 0x5, 0x46, 0x24, 0x2,
    0x167, 0x168, 0x7, 0x31, 0x2, 0x2, 0x168, 0x45, 0x3, 0x2, 0x2, 0x2,
    0x169, 0x16e, 0x5, 0x42, 0x22, 0x2, 0x16a, 0x16b, 0x7, 0x32, 0x2, 0x2,
    0x16b, 0x16d, 0x5, 0x42, 0x22, 0x2, 0x16c, 0x16a, 0x3, 0x2, 0x2, 0x2,
    0x16d, 0x170, 0x3, 0x2, 0x2, 0x2, 0x16e, 0x16c, 0x3, 0x2, 0x2, 0x2,
    0x16e, 0x16f, 0x3, 0x2, 0x2, 0x2, 0x16f, 0x47, 0x3, 0x2, 0x2, 0x2, 0x170,
    0x16e, 0x3, 0x2, 0x2, 0x2, 0x171, 0x173, 0x5, 0x44, 0x23, 0x2, 0x172,
    0x171, 0x3, 0x2, 0x2, 0x2, 0x172, 0x173, 0x3, 0x2, 0x2, 0x2, 0x173,
    0x174, 0x3, 0x2, 0x2, 0x2, 0x174, 0x175, 0x5, 0x4a, 0x26, 0x2, 0x175,
    0x176, 0x7, 0x35, 0x2, 0x2, 0x176, 0x49, 0x3, 0x2, 0x2, 0x2, 0x177,
    0x17b, 0x7, 0x24, 0x2, 0x2, 0x178, 0x179, 0x7, 0x30, 0x2, 0x2, 0x179,
    0x17a, 0x7, 0x28, 0x2, 0x2, 0x17a, 0x17c, 0x7, 0x31, 0x2, 0x2, 0x17b,
    0x178, 0x3, 0x2, 0x2, 0x2, 0x17b, 0x17c, 0x3, 0x2, 0x2, 0x2, 0x17c,
    0x4b, 0x3, 0x2, 0x2, 0x2, 0x17d, 0x180, 0x5, 0x4e, 0x28, 0x2, 0x17e,
    0x180, 0x5, 0x4a, 0x26, 0x2, 0x17f, 0x17d, 0x3, 0x2, 0x2, 0x2, 0x17f,
    0x17e, 0x3, 0x2, 0x2, 0x2, 0x180, 0x4d, 0x3, 0x2, 0x2, 0x2, 0x181, 0x182,
    0x9, 0x7, 0x2, 0x2, 0x182, 0x4f, 0x3, 0x2, 0x2, 0x2, 0x183, 0x184, 0x9,
    0x8, 0x2, 0x2, 0x184, 0x51, 0x3, 0x2, 0x2, 0x2, 0x185, 0x186, 0x9, 0x9,
    0x2, 0x2, 0x186, 0x53, 0x3, 0x2, 0x2, 0x2, 0x187, 0x188, 0x7, 0x29,
    0x2, 0x2, 0x188, 0x55, 0x3, 0x2, 0x2, 0x2, 0x189, 0x18a, 0x7, 0x2b,
    0x2, 0x2, 0x18a, 0x57, 0x3, 0x2, 0x2, 0x2, 0x18b, 0x18c, 0x7, 0x28,
    0x2, 0x2, 0x18c, 0x18d, 0x7, 0x1f, 0x2, 0x2, 0x18d, 0x18e, 0x7, 0x1e,
    0x2, 0x2, 0x18e, 0x59, 0x3, 0x2, 0x2, 0x2, 0x24, 0x5d, 0x60, 0x67, 0x6f,
    0x75, 0x7b, 0x85, 0x8b, 0x91, 0x99, 0xa2, 0xa6, 0xb1, 0xb7, 0xcb, 0xd2,
    0xe3, 0xe9, 0xee, 0xf3, 0xf8, 0x101, 0x10c, 0x12c, 0x136, 0x142, 0x14a,
    0x155, 0x15e, 0x163, 0x16e, 0x172, 0x17b, 0x17f,
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
