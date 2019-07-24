/* parser/listener/visitor header section */

// Generated from /bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.7

#pragma once


#include "antlr4-runtime.h"
#include "BSParserListener.h"


/**
 * This class provides an empty implementation of BSParserListener,
 * which can be extended to create a listener which only needs to handle a subset
 * of the available methods.
 */
class  BSParserBaseListener : public BSParserListener {
public:

  virtual void enterProgram(BSParser::ProgramContext * /*ctx*/) override { }
  virtual void exitProgram(BSParser::ProgramContext * /*ctx*/) override { }

  virtual void enterModuleDeclaration(BSParser::ModuleDeclarationContext * /*ctx*/) override { }
  virtual void exitModuleDeclaration(BSParser::ModuleDeclarationContext * /*ctx*/) override { }

  virtual void enterManifestDeclaration(BSParser::ManifestDeclarationContext * /*ctx*/) override { }
  virtual void exitManifestDeclaration(BSParser::ManifestDeclarationContext * /*ctx*/) override { }

  virtual void enterStationaryDeclaration(BSParser::StationaryDeclarationContext * /*ctx*/) override { }
  virtual void exitStationaryDeclaration(BSParser::StationaryDeclarationContext * /*ctx*/) override { }

  virtual void enterFunctions(BSParser::FunctionsContext * /*ctx*/) override { }
  virtual void exitFunctions(BSParser::FunctionsContext * /*ctx*/) override { }

  virtual void enterFunctionDeclaration(BSParser::FunctionDeclarationContext * /*ctx*/) override { }
  virtual void exitFunctionDeclaration(BSParser::FunctionDeclarationContext * /*ctx*/) override { }

  virtual void enterFormalParameters(BSParser::FormalParametersContext * /*ctx*/) override { }
  virtual void exitFormalParameters(BSParser::FormalParametersContext * /*ctx*/) override { }

  virtual void enterFormalParameterList(BSParser::FormalParameterListContext * /*ctx*/) override { }
  virtual void exitFormalParameterList(BSParser::FormalParameterListContext * /*ctx*/) override { }

  virtual void enterFormalParameter(BSParser::FormalParameterContext * /*ctx*/) override { }
  virtual void exitFormalParameter(BSParser::FormalParameterContext * /*ctx*/) override { }

  virtual void enterFunctionTyping(BSParser::FunctionTypingContext * /*ctx*/) override { }
  virtual void exitFunctionTyping(BSParser::FunctionTypingContext * /*ctx*/) override { }

  virtual void enterReturnStatement(BSParser::ReturnStatementContext * /*ctx*/) override { }
  virtual void exitReturnStatement(BSParser::ReturnStatementContext * /*ctx*/) override { }

  virtual void enterBlockStatement(BSParser::BlockStatementContext * /*ctx*/) override { }
  virtual void exitBlockStatement(BSParser::BlockStatementContext * /*ctx*/) override { }

  virtual void enterStatements(BSParser::StatementsContext * /*ctx*/) override { }
  virtual void exitStatements(BSParser::StatementsContext * /*ctx*/) override { }

  virtual void enterIfStatement(BSParser::IfStatementContext * /*ctx*/) override { }
  virtual void exitIfStatement(BSParser::IfStatementContext * /*ctx*/) override { }

  virtual void enterWhileStatement(BSParser::WhileStatementContext * /*ctx*/) override { }
  virtual void exitWhileStatement(BSParser::WhileStatementContext * /*ctx*/) override { }

  virtual void enterRepeat(BSParser::RepeatContext * /*ctx*/) override { }
  virtual void exitRepeat(BSParser::RepeatContext * /*ctx*/) override { }

  virtual void enterHeat(BSParser::HeatContext * /*ctx*/) override { }
  virtual void exitHeat(BSParser::HeatContext * /*ctx*/) override { }

  virtual void enterDispose(BSParser::DisposeContext * /*ctx*/) override { }
  virtual void exitDispose(BSParser::DisposeContext * /*ctx*/) override { }

  virtual void enterMix(BSParser::MixContext * /*ctx*/) override { }
  virtual void exitMix(BSParser::MixContext * /*ctx*/) override { }

  virtual void enterDetect(BSParser::DetectContext * /*ctx*/) override { }
  virtual void exitDetect(BSParser::DetectContext * /*ctx*/) override { }

  virtual void enterSplit(BSParser::SplitContext * /*ctx*/) override { }
  virtual void exitSplit(BSParser::SplitContext * /*ctx*/) override { }

  virtual void enterDispense(BSParser::DispenseContext * /*ctx*/) override { }
  virtual void exitDispense(BSParser::DispenseContext * /*ctx*/) override { }

  virtual void enterGradient(BSParser::GradientContext * /*ctx*/) override { }
  virtual void exitGradient(BSParser::GradientContext * /*ctx*/) override { }

  virtual void enterStore(BSParser::StoreContext * /*ctx*/) override { }
  virtual void exitStore(BSParser::StoreContext * /*ctx*/) override { }

  virtual void enterMath(BSParser::MathContext * /*ctx*/) override { }
  virtual void exitMath(BSParser::MathContext * /*ctx*/) override { }

  virtual void enterBinops(BSParser::BinopsContext * /*ctx*/) override { }
  virtual void exitBinops(BSParser::BinopsContext * /*ctx*/) override { }

  virtual void enterParExpression(BSParser::ParExpressionContext * /*ctx*/) override { }
  virtual void exitParExpression(BSParser::ParExpressionContext * /*ctx*/) override { }

  virtual void enterMethodCall(BSParser::MethodCallContext * /*ctx*/) override { }
  virtual void exitMethodCall(BSParser::MethodCallContext * /*ctx*/) override { }

  virtual void enterExpressionList(BSParser::ExpressionListContext * /*ctx*/) override { }
  virtual void exitExpressionList(BSParser::ExpressionListContext * /*ctx*/) override { }

  virtual void enterTypeType(BSParser::TypeTypeContext * /*ctx*/) override { }
  virtual void exitTypeType(BSParser::TypeTypeContext * /*ctx*/) override { }

  virtual void enterUnionType(BSParser::UnionTypeContext * /*ctx*/) override { }
  virtual void exitUnionType(BSParser::UnionTypeContext * /*ctx*/) override { }

  virtual void enterTypesList(BSParser::TypesListContext * /*ctx*/) override { }
  virtual void exitTypesList(BSParser::TypesListContext * /*ctx*/) override { }

  virtual void enterVariableDefinition(BSParser::VariableDefinitionContext * /*ctx*/) override { }
  virtual void exitVariableDefinition(BSParser::VariableDefinitionContext * /*ctx*/) override { }

  virtual void enterVariable(BSParser::VariableContext * /*ctx*/) override { }
  virtual void exitVariable(BSParser::VariableContext * /*ctx*/) override { }

  virtual void enterPrimary(BSParser::PrimaryContext * /*ctx*/) override { }
  virtual void exitPrimary(BSParser::PrimaryContext * /*ctx*/) override { }

  virtual void enterLiteral(BSParser::LiteralContext * /*ctx*/) override { }
  virtual void exitLiteral(BSParser::LiteralContext * /*ctx*/) override { }

  virtual void enterPrimitiveType(BSParser::PrimitiveTypeContext * /*ctx*/) override { }
  virtual void exitPrimitiveType(BSParser::PrimitiveTypeContext * /*ctx*/) override { }

  virtual void enterTimeIdentifier(BSParser::TimeIdentifierContext * /*ctx*/) override { }
  virtual void exitTimeIdentifier(BSParser::TimeIdentifierContext * /*ctx*/) override { }

  virtual void enterTemperatureIdentifier(BSParser::TemperatureIdentifierContext * /*ctx*/) override { }
  virtual void exitTemperatureIdentifier(BSParser::TemperatureIdentifierContext * /*ctx*/) override { }


  virtual void enterEveryRule(antlr4::ParserRuleContext * /*ctx*/) override { }
  virtual void exitEveryRule(antlr4::ParserRuleContext * /*ctx*/) override { }
  virtual void visitTerminal(antlr4::tree::TerminalNode * /*node*/) override { }
  virtual void visitErrorNode(antlr4::tree::ErrorNode * /*node*/) override { }

private:
};

