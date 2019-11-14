/* parser/listener/visitor header section */

// Generated from /bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.7

#pragma once


#include "antlr4-runtime.h"
#include "BSParserVisitor.h"


/**
 * This class provides an empty implementation of BSParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  BSParserBaseVisitor : public BSParserVisitor {
public:

  virtual antlrcpp::Any visitProgram(BSParser::ProgramContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitGlobalDeclarations(BSParser::GlobalDeclarationsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitModuleDeclaration(BSParser::ModuleDeclarationContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitManifestDeclaration(BSParser::ManifestDeclarationContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitStationaryDeclaration(BSParser::StationaryDeclarationContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitFunctions(BSParser::FunctionsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitFunctionDeclaration(BSParser::FunctionDeclarationContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitFormalParameters(BSParser::FormalParametersContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitFormalParameterList(BSParser::FormalParameterListContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitFormalParameter(BSParser::FormalParameterContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitFunctionTyping(BSParser::FunctionTypingContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitReturnStatement(BSParser::ReturnStatementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitBlockStatement(BSParser::BlockStatementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitStatements(BSParser::StatementsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitIfStatement(BSParser::IfStatementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitWhileStatement(BSParser::WhileStatementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitRepeat(BSParser::RepeatContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitHeat(BSParser::HeatContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitDispose(BSParser::DisposeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitMix(BSParser::MixContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitDetect(BSParser::DetectContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitSplit(BSParser::SplitContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitDispense(BSParser::DispenseContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitGradient(BSParser::GradientContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitStore(BSParser::StoreContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitNumberAssignment(BSParser::NumberAssignmentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitMath(BSParser::MathContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitBinops(BSParser::BinopsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitParExpression(BSParser::ParExpressionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitMethodInvocation(BSParser::MethodInvocationContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitMethodCall(BSParser::MethodCallContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitExpressionList(BSParser::ExpressionListContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitTypeType(BSParser::TypeTypeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitUnionType(BSParser::UnionTypeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitTypesList(BSParser::TypesListContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitVariableDefinition(BSParser::VariableDefinitionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitVariable(BSParser::VariableContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitPrimary(BSParser::PrimaryContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitLiteral(BSParser::LiteralContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitPrimitiveType(BSParser::PrimitiveTypeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitChemicalType(BSParser::ChemicalTypeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitTimeIdentifier(BSParser::TimeIdentifierContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitTemperatureIdentifier(BSParser::TemperatureIdentifierContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitUnitTracker(BSParser::UnitTrackerContext *ctx) override {
    return visitChildren(ctx);
  }


private:
};

