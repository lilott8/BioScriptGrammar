/* parser/listener/visitor header section */

// Generated from /Users/jason/Projects/java/BSPrototype/src/main/resources/BSParser.g4 by ANTLR 4.7

#pragma once


#include "antlr4-runtime.h"
#include "BSParser.h"


/**
 * This interface defines an abstract listener for a parse tree produced by BSParser.
 */
class  BSParserListener : public antlr4::tree::ParseTreeListener {
public:

  virtual void enterProgram(BSParser::ProgramContext *ctx) = 0;
  virtual void exitProgram(BSParser::ProgramContext *ctx) = 0;

  virtual void enterModuleDeclaration(BSParser::ModuleDeclarationContext *ctx) = 0;
  virtual void exitModuleDeclaration(BSParser::ModuleDeclarationContext *ctx) = 0;

  virtual void enterManifestDeclaration(BSParser::ManifestDeclarationContext *ctx) = 0;
  virtual void exitManifestDeclaration(BSParser::ManifestDeclarationContext *ctx) = 0;

  virtual void enterStationaryDeclaration(BSParser::StationaryDeclarationContext *ctx) = 0;
  virtual void exitStationaryDeclaration(BSParser::StationaryDeclarationContext *ctx) = 0;

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

  virtual void enterAssignmentOperations(BSParser::AssignmentOperationsContext *ctx) = 0;
  virtual void exitAssignmentOperations(BSParser::AssignmentOperationsContext *ctx) = 0;

  virtual void enterStatements(BSParser::StatementsContext *ctx) = 0;
  virtual void exitStatements(BSParser::StatementsContext *ctx) = 0;

  virtual void enterIfStatement(BSParser::IfStatementContext *ctx) = 0;
  virtual void exitIfStatement(BSParser::IfStatementContext *ctx) = 0;

  virtual void enterWhileStatement(BSParser::WhileStatementContext *ctx) = 0;
  virtual void exitWhileStatement(BSParser::WhileStatementContext *ctx) = 0;

  virtual void enterRepeat(BSParser::RepeatContext *ctx) = 0;
  virtual void exitRepeat(BSParser::RepeatContext *ctx) = 0;

  virtual void enterMix(BSParser::MixContext *ctx) = 0;
  virtual void exitMix(BSParser::MixContext *ctx) = 0;

  virtual void enterDetect(BSParser::DetectContext *ctx) = 0;
  virtual void exitDetect(BSParser::DetectContext *ctx) = 0;

  virtual void enterHeat(BSParser::HeatContext *ctx) = 0;
  virtual void exitHeat(BSParser::HeatContext *ctx) = 0;

  virtual void enterSplit(BSParser::SplitContext *ctx) = 0;
  virtual void exitSplit(BSParser::SplitContext *ctx) = 0;

  virtual void enterDispense(BSParser::DispenseContext *ctx) = 0;
  virtual void exitDispense(BSParser::DispenseContext *ctx) = 0;

  virtual void enterDispose(BSParser::DisposeContext *ctx) = 0;
  virtual void exitDispose(BSParser::DisposeContext *ctx) = 0;

  virtual void enterExpression(BSParser::ExpressionContext *ctx) = 0;
  virtual void exitExpression(BSParser::ExpressionContext *ctx) = 0;

  virtual void enterParExpression(BSParser::ParExpressionContext *ctx) = 0;
  virtual void exitParExpression(BSParser::ParExpressionContext *ctx) = 0;

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

  virtual void enterVariableDeclaratorId(BSParser::VariableDeclaratorIdContext *ctx) = 0;
  virtual void exitVariableDeclaratorId(BSParser::VariableDeclaratorIdContext *ctx) = 0;

  virtual void enterVariableDeclarator(BSParser::VariableDeclaratorContext *ctx) = 0;
  virtual void exitVariableDeclarator(BSParser::VariableDeclaratorContext *ctx) = 0;

  virtual void enterVariableInitializer(BSParser::VariableInitializerContext *ctx) = 0;
  virtual void exitVariableInitializer(BSParser::VariableInitializerContext *ctx) = 0;

  virtual void enterArrayInitializer(BSParser::ArrayInitializerContext *ctx) = 0;
  virtual void exitArrayInitializer(BSParser::ArrayInitializerContext *ctx) = 0;

  virtual void enterLocalVariableDeclaration(BSParser::LocalVariableDeclarationContext *ctx) = 0;
  virtual void exitLocalVariableDeclaration(BSParser::LocalVariableDeclarationContext *ctx) = 0;

  virtual void enterPrimary(BSParser::PrimaryContext *ctx) = 0;
  virtual void exitPrimary(BSParser::PrimaryContext *ctx) = 0;

  virtual void enterLiteral(BSParser::LiteralContext *ctx) = 0;
  virtual void exitLiteral(BSParser::LiteralContext *ctx) = 0;

  virtual void enterPrimitiveType(BSParser::PrimitiveTypeContext *ctx) = 0;
  virtual void exitPrimitiveType(BSParser::PrimitiveTypeContext *ctx) = 0;

  virtual void enterVolumeIdentifier(BSParser::VolumeIdentifierContext *ctx) = 0;
  virtual void exitVolumeIdentifier(BSParser::VolumeIdentifierContext *ctx) = 0;

  virtual void enterTimeIdentifier(BSParser::TimeIdentifierContext *ctx) = 0;
  virtual void exitTimeIdentifier(BSParser::TimeIdentifierContext *ctx) = 0;

  virtual void enterTemperatureIdentifier(BSParser::TemperatureIdentifierContext *ctx) = 0;
  virtual void exitTemperatureIdentifier(BSParser::TemperatureIdentifierContext *ctx) = 0;


private:  
};

