set(ANTLR_PARSING_SOURCES
        BSLexer.cpp
        BSParser.cpp
        BSParserBaseListener.cpp
        BSParserBaseVisitor.cpp
        BSParserListener.cpp
        BSParserVisitor.cpp
)


add_library(ANTLR_PARSING ${ANTLR_PARSING_SOURCES})
