/* parser/listener/visitor header section */

// Generated from /bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.7

#pragma once


#include "antlr4-runtime.h"
#include "BSParser.h"


/**
 * This interface defines an abstract listener for a parse tree produced by BSParser.
 */
class  BSParserListener : public antlr4::tree::ParseTreeListener {
public:

  virtual void enterProgmaram(BSParser::ProgmaramContext *ctx) = 0;
  virtual void exitProgmaram(BSParser::ProgmaramContext *ctx) = 0;

  virtual void enterGlobalDeclarations(BSParser::GlobalDeclarationsContext *ctx) = 0;
  virtual void exitGlobalDeclarations(BSParser::GlobalDeclarationsContext *ctx) = 0;

  virtual void enterModuleDeclaration(BSParser::ModuleDeclarationContext *ctx) = 0;
  virtual void exitModuleDeclaration(BSParser::ModuleDeclarationContext *ctx) = 0;

  virtual void enterManifestDeclaration(BSParser::ManifestDeclarationContext *ctx) = 0;
  virtual void exitManifestDeclaration(BSParser::ManifestDeclarationContext *ctx) = 0;

  virtual void enterStationaryDeclaration(BSParser::StationaryDeclarationContext *ctx) = 0;
  virtual void exitStationaryDeclaration(BSParser::StationaryDeclarationContext *ctx) = 0;

  virtual void enterFunctions(BSParser::FunctionsContext *ctx) = 0;
  virtual void exitFunctions(BSParser::FunctionsContext *ctx) = 0;

  virtual void enterFunctionDeclaration(BSParser::FunctionDeclarationContext *ctx) = 0;
  virtual void exitFunctionDeclaration(BSParser::FunctionDeclarationContext *ctx) = 0;

  virtual void enterFormalParameters(BSParser::FormalParametersContext *ctx) = 0;
  virtual void exitFormalParameters(BSParser::FormalParametersContext *ctx) = 0;

  virtual void enterFormalParameterList(BSParser::FormalParameterListContext *ctx) = 0;
  virtual void exitFormalParameterList(BSParser::FormalParameterListContext *ctx) = 0;

  virtual void enterFormalParameter(BSParser::FormalParameterContext *ctx) = 0;
  virtual void exitFormalParameter(BSParser::FormalParameterContext *ctx) = 0;

  virtual void enterFunctionTyping(BSParser::FunctionTypingContext *ctx) = 0;
  virtual void exitFunctionTyping(BSParser::FunctionTypingContext *ctx) = 0;

  virtual void enterReturnStatement(BSParser::ReturnStatementContext *ctx) = 0;
  virtual void exitReturnStatement(BSParser::ReturnStatementContext *ctx) = 0;

  virtual void enterBlockStatement(BSParser::BlockStatementContext *ctx) = 0;
  virtual void exitBlockStatement(BSParser::BlockStatementContext *ctx) = 0;

  virtual void enterStatements(BSParser::StatementsContext *ctx) = 0;
  virtual void exitStatements(BSParser::StatementsContext *ctx) = 0;

  virtual void enterIfStatement(BSParser::IfStatementContext *ctx) = 0;
  virtual void exitIfStatement(BSParser::IfStatementContext *ctx) = 0;

  virtual void enterWhileStatement(BSParser::WhileStatementContext *ctx) = 0;
  virtual void exitWhileStatement(BSParser::WhileStatementContext *ctx) = 0;

  virtual void enterRepeat(BSParser::RepeatContext *ctx) = 0;
  virtual void exitRepeat(BSParser::RepeatContext *ctx) = 0;

  virtual void enterHeat(BSParser::HeatContext *ctx) = 0;
  virtual void exitHeat(BSParser::HeatContext *ctx) = 0;

  virtual void enterDispose(BSParser::DisposeContext *ctx) = 0;
  virtual void exitDispose(BSParser::DisposeContext *ctx) = 0;

  virtual void enterMix(BSParser::MixContext *ctx) = 0;
  virtual void exitMix(BSParser::MixContext *ctx) = 0;

  virtual void enterDetect(BSParser::DetectContext *ctx) = 0;
  virtual void exitDetect(BSParser::DetectContext *ctx) = 0;

  virtual void enterSplit(BSParser::SplitContext *ctx) = 0;
  virtual void exitSplit(BSParser::SplitContext *ctx) = 0;

  virtual void enterDispense(BSParser::DispenseContext *ctx) = 0;
  virtual void exitDispense(BSParser::DispenseContext *ctx) = 0;

  virtual void enterGradient(BSParser::GradientContext *ctx) = 0;
  virtual void exitGradient(BSParser::GradientContext *ctx) = 0;

  virtual void enterStore(BSParser::StoreContext *ctx) = 0;
  virtual void exitStore(BSParser::StoreContext *ctx) = 0;

  virtual void enterNumberAssignment(BSParser::NumberAssignmentContext *ctx) = 0;
  virtual void exitNumberAssignment(BSParser::NumberAssignmentContext *ctx) = 0;

  virtual void enterMath(BSParser::MathContext *ctx) = 0;
  virtual void exitMath(BSParser::MathContext *ctx) = 0;

  virtual void enterBinops(BSParser::BinopsContext *ctx) = 0;
  virtual void exitBinops(BSParser::BinopsContext *ctx) = 0;

  virtual void enterParExpression(BSParser::ParExpressionContext *ctx) = 0;
  virtual void exitParExpression(BSParser::ParExpressionContext *ctx) = 0;

  virtual void enterMethodInvocation(BSParser::MethodInvocationContext *ctx) = 0;
  virtual void exitMethodInvocation(BSParser::MethodInvocationContext *ctx) = 0;

  virtual void enterMethodCall(BSParser::MethodCallContext *ctx) = 0;
  virtual void exitMethodCall(BSParser::MethodCallContext *ctx) = 0;

  virtual void enterExpressionList(BSParser::ExpressionListContext *ctx) = 0;
  virtual void exitExpressionList(BSParser::ExpressionListContext *ctx) = 0;

  virtual void enterTypeType(BSParser::TypeTypeContext *ctx) = 0;
  virtual void exitTypeType(BSParser::TypeTypeContext *ctx) = 0;

  virtual void enterUnionType(BSParser::UnionTypeContext *ctx) = 0;
  virtual void exitUnionType(BSParser::UnionTypeContext *ctx) = 0;

  virtual void enterTypesList(BSParser::TypesListContext *ctx) = 0;
  virtual void exitTypesList(BSParser::TypesListContext *ctx) = 0;

  virtual void enterVariableDefinition(BSParser::VariableDefinitionContext *ctx) = 0;
  virtual void exitVariableDefinition(BSParser::VariableDefinitionContext *ctx) = 0;

  virtual void enterVariable(BSParser::VariableContext *ctx) = 0;
  virtual void exitVariable(BSParser::VariableContext *ctx) = 0;

  virtual void enterPrimary(BSParser::PrimaryContext *ctx) = 0;
  virtual void exitPrimary(BSParser::PrimaryContext *ctx) = 0;

  virtual void enterLiteral(BSParser::LiteralContext *ctx) = 0;
  virtual void exitLiteral(BSParser::LiteralContext *ctx) = 0;

  virtual void enterPrimitiveType(BSParser::PrimitiveTypeContext *ctx) = 0;
  virtual void exitPrimitiveType(BSParser::PrimitiveTypeContext *ctx) = 0;

  virtual void enterTimeIdentifier(BSParser::TimeIdentifierContext *ctx) = 0;
  virtual void exitTimeIdentifier(BSParser::TimeIdentifierContext *ctx) = 0;

  virtual void enterTemperatureIdentifier(BSParser::TemperatureIdentifierContext *ctx) = 0;
  virtual void exitTemperatureIdentifier(BSParser::TemperatureIdentifierContext *ctx) = 0;

  virtual void enterUnitTracker(BSParser::UnitTrackerContext *ctx) = 0;
  virtual void exitUnitTracker(BSParser::UnitTrackerContext *ctx) = 0;


private:
};

