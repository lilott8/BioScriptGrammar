# Generated from /bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BSParser import BSParser
else:
    from BSParser import BSParser
# /* parser/listener/visitor header section */

# This class defines a complete generic visitor for a parse tree produced by BSParser.

class BSParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BSParser#program.
    def visitProgram(self, ctx:BSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#globalDeclarations.
    def visitGlobalDeclarations(self, ctx:BSParser.GlobalDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#moduleDeclaration.
    def visitModuleDeclaration(self, ctx:BSParser.ModuleDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#manifestDeclaration.
    def visitManifestDeclaration(self, ctx:BSParser.ManifestDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#stationaryDeclaration.
    def visitStationaryDeclaration(self, ctx:BSParser.StationaryDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#functions.
    def visitFunctions(self, ctx:BSParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:BSParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#formalParameters.
    def visitFormalParameters(self, ctx:BSParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#formalParameterList.
    def visitFormalParameterList(self, ctx:BSParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#formalParameter.
    def visitFormalParameter(self, ctx:BSParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#functionTyping.
    def visitFunctionTyping(self, ctx:BSParser.FunctionTypingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#returnStatement.
    def visitReturnStatement(self, ctx:BSParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#blockStatement.
    def visitBlockStatement(self, ctx:BSParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#statements.
    def visitStatements(self, ctx:BSParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#ifStatement.
    def visitIfStatement(self, ctx:BSParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#whileStatement.
    def visitWhileStatement(self, ctx:BSParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#repeat.
    def visitRepeat(self, ctx:BSParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#heat.
    def visitHeat(self, ctx:BSParser.HeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#dispose.
    def visitDispose(self, ctx:BSParser.DisposeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#mix.
    def visitMix(self, ctx:BSParser.MixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#detect.
    def visitDetect(self, ctx:BSParser.DetectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#split.
    def visitSplit(self, ctx:BSParser.SplitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#dispense.
    def visitDispense(self, ctx:BSParser.DispenseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#gradient.
    def visitGradient(self, ctx:BSParser.GradientContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#store.
    def visitStore(self, ctx:BSParser.StoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#numberAssignment.
    def visitNumberAssignment(self, ctx:BSParser.NumberAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#math.
    def visitMath(self, ctx:BSParser.MathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#binops.
    def visitBinops(self, ctx:BSParser.BinopsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#parExpression.
    def visitParExpression(self, ctx:BSParser.ParExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#methodInvocation.
    def visitMethodInvocation(self, ctx:BSParser.MethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#methodCall.
    def visitMethodCall(self, ctx:BSParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#expressionList.
    def visitExpressionList(self, ctx:BSParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#typeType.
    def visitTypeType(self, ctx:BSParser.TypeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#unionType.
    def visitUnionType(self, ctx:BSParser.UnionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#typesList.
    def visitTypesList(self, ctx:BSParser.TypesListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#variableDefinition.
    def visitVariableDefinition(self, ctx:BSParser.VariableDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#variable.
    def visitVariable(self, ctx:BSParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#primary.
    def visitPrimary(self, ctx:BSParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#literal.
    def visitLiteral(self, ctx:BSParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#primitiveType.
    def visitPrimitiveType(self, ctx:BSParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#timeIdentifier.
    def visitTimeIdentifier(self, ctx:BSParser.TimeIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSParser#temperatureIdentifier.
    def visitTemperatureIdentifier(self, ctx:BSParser.TemperatureIdentifierContext):
        return self.visitChildren(ctx)



del BSParser