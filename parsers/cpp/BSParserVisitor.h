/* parser/listener/visitor header section */

// Generated from /Users/jason/Projects/java/bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.7

#pragma once


#include "antlr4-runtime.h"
#include "BSParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by BSParser.
 */
class  BSParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by BSParser.
   */
    virtual antlrcpp::Any visitProgram(BSParser::ProgramContext *context) = 0;

    virtual antlrcpp::Any visitModuleDeclaration(BSParser::ModuleDeclarationContext *context) = 0;

    virtual antlrcpp::Any visitManifestDeclaration(BSParser::ManifestDeclarationContext *context) = 0;

    virtual antlrcpp::Any visitStationaryDeclaration(BSParser::StationaryDeclarationContext *context) = 0;

    virtual antlrcpp::Any visitFunctionDeclaration(BSParser::FunctionDeclarationContext *context) = 0;

    virtual antlrcpp::Any visitFormalParameters(BSParser::FormalParametersContext *context) = 0;

    virtual antlrcpp::Any visitFormalParameterList(BSParser::FormalParameterListContext *context) = 0;

    virtual antlrcpp::Any visitFormalParameter(BSParser::FormalParameterContext *context) = 0;

    virtual antlrcpp::Any visitFunctionTyping(BSParser::FunctionTypingContext *context) = 0;

    virtual antlrcpp::Any visitReturnStatement(BSParser::ReturnStatementContext *context) = 0;

    virtual antlrcpp::Any visitBlockStatement(BSParser::BlockStatementContext *context) = 0;

    virtual antlrcpp::Any visitMaterialAssignmentOperations(BSParser::MaterialAssignmentOperationsContext *context) = 0;

    virtual antlrcpp::Any visitNumericAssignmentOperations(BSParser::NumericAssignmentOperationsContext *context) = 0;

    virtual antlrcpp::Any visitStatements(BSParser::StatementsContext *context) = 0;

    virtual antlrcpp::Any visitIfStatement(BSParser::IfStatementContext *context) = 0;

    virtual antlrcpp::Any visitWhileStatement(BSParser::WhileStatementContext *context) = 0;

    virtual antlrcpp::Any visitRepeat(BSParser::RepeatContext *context) = 0;

    virtual antlrcpp::Any visitMix(BSParser::MixContext *context) = 0;

    virtual antlrcpp::Any visitDetect(BSParser::DetectContext *context) = 0;

    virtual antlrcpp::Any visitHeat(BSParser::HeatContext *context) = 0;

    virtual antlrcpp::Any visitSplit(BSParser::SplitContext *context) = 0;

    virtual antlrcpp::Any visitDispense(BSParser::DispenseContext *context) = 0;

    virtual antlrcpp::Any visitDispose(BSParser::DisposeContext *context) = 0;

    virtual antlrcpp::Any visitExpression(BSParser::ExpressionContext *context) = 0;

    virtual antlrcpp::Any visitParExpression(BSParser::ParExpressionContext *context) = 0;

    virtual antlrcpp::Any visitMethodCall(BSParser::MethodCallContext *context) = 0;

    virtual antlrcpp::Any visitExpressionList(BSParser::ExpressionListContext *context) = 0;

    virtual antlrcpp::Any visitTypeType(BSParser::TypeTypeContext *context) = 0;

    virtual antlrcpp::Any visitUnionType(BSParser::UnionTypeContext *context) = 0;

    virtual antlrcpp::Any visitTypesList(BSParser::TypesListContext *context) = 0;

    virtual antlrcpp::Any visitNumericDeclaration(BSParser::NumericDeclarationContext *context) = 0;

    virtual antlrcpp::Any visitMaterialDeclaration(BSParser::MaterialDeclarationContext *context) = 0;

    virtual antlrcpp::Any visitPrimary(BSParser::PrimaryContext *context) = 0;

    virtual antlrcpp::Any visitLiteral(BSParser::LiteralContext *context) = 0;

    virtual antlrcpp::Any visitPrimitiveType(BSParser::PrimitiveTypeContext *context) = 0;

    virtual antlrcpp::Any visitVolumeIdentifier(BSParser::VolumeIdentifierContext *context) = 0;

    virtual antlrcpp::Any visitTimeIdentifier(BSParser::TimeIdentifierContext *context) = 0;

    virtual antlrcpp::Any visitTemperatureIdentifier(BSParser::TemperatureIdentifierContext *context) = 0;


private:  
};

