# Generated from bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

# parser/listener/visitor header section
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3`")
        buf.write("\u016d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\3\2\3\2\3\2\3\2\3\2\3\2\7\2S\n\2\f\2\16\2V\13\2\3\2")
        buf.write("\3\2\3\2\7\2[\n\2\f\2\16\2^\13\2\3\2\3\2\3\3\3\3\7\3d")
        buf.write("\n\3\f\3\16\3g\13\3\3\4\3\4\6\4k\n\4\r\4\16\4l\3\5\3\5")
        buf.write("\7\5q\n\5\f\5\16\5t\13\5\3\6\3\6\3\6\3\6\5\6z\n\6\3\6")
        buf.write("\3\6\6\6~\n\6\r\6\16\6\177\3\6\3\6\3\6\3\7\3\7\5\7\u0087")
        buf.write("\n\7\3\7\3\7\3\b\3\b\3\b\7\b\u008e\n\b\f\b\16\b\u0091")
        buf.write("\13\b\3\t\5\t\u0094\n\t\3\t\3\t\3\t\5\t\u0099\n\t\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\f\3\f\7\f\u00a3\n\f\f\f\16\f")
        buf.write("\u00a6\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b0")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00b8\n\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\5\17\u00bf\n\17\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\5\22\u00d0\n\22\3\23\3\23\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u00d8\n\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00e0")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u00ee\n\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u0101\n\30\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\7\30\u0115\n\30\f\30\16\30\u0118\13\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\5\32\u0121\n\32\3\32\3\32\3")
        buf.write("\33\3\33\3\33\7\33\u0128\n\33\f\33\16\33\u012b\13\33\3")
        buf.write("\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\7\36\u0136")
        buf.write("\n\36\f\36\16\36\u0139\13\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \5 \u0141\n \3 \3 \3 \3 \5 \u0147\n \3 \3 \3 \3 \3")
        buf.write(" \3 \5 \u014f\n \3 \3 \3 \3 \5 \u0155\n \3!\3!\3!\3!\3")
        buf.write("!\3!\5!\u015d\n!\3\"\3\"\3#\3#\3$\3$\5$\u0165\n$\3$\3")
        buf.write("$\3%\3%\3&\3&\3&\2\3.\'\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJ\2\t\4\2  $$\4")
        buf.write("\2BCGG\3\2@A\4\2\62\639:\4\288;;\3\2!$\3\2\34\37\2\u0177")
        buf.write("\2L\3\2\2\2\4e\3\2\2\2\6j\3\2\2\2\br\3\2\2\2\nu\3\2\2")
        buf.write("\2\f\u0084\3\2\2\2\16\u008a\3\2\2\2\20\u0093\3\2\2\2\22")
        buf.write("\u009a\3\2\2\2\24\u009d\3\2\2\2\26\u00a0\3\2\2\2\30\u00af")
        buf.write("\3\2\2\2\32\u00b7\3\2\2\2\34\u00b9\3\2\2\2\36\u00c0\3")
        buf.write("\2\2\2 \u00c4\3\2\2\2\"\u00c9\3\2\2\2$\u00d1\3\2\2\2&")
        buf.write("\u00d9\3\2\2\2(\u00e1\3\2\2\2*\u00e6\3\2\2\2,\u00ed\3")
        buf.write("\2\2\2.\u00ef\3\2\2\2\60\u0119\3\2\2\2\62\u011d\3\2\2")
        buf.write("\2\64\u0124\3\2\2\2\66\u012c\3\2\2\28\u012e\3\2\2\2:\u0132")
        buf.write("\3\2\2\2<\u013a\3\2\2\2>\u0154\3\2\2\2@\u015c\3\2\2\2")
        buf.write("B\u015e\3\2\2\2D\u0160\3\2\2\2F\u0164\3\2\2\2H\u0168\3")
        buf.write("\2\2\2J\u016a\3\2\2\2LM\5\4\3\2MN\5\b\5\2NO\5\6\4\2OP")
        buf.write("\7\f\2\2PT\7\67\2\2QS\5\n\6\2RQ\3\2\2\2SV\3\2\2\2TR\3")
        buf.write("\2\2\2TU\3\2\2\2UW\3\2\2\2VT\3\2\2\2WX\7\r\2\2X\\\7\67")
        buf.write("\2\2Y[\5\32\16\2ZY\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2")
        buf.write("\2\2]_\3\2\2\2^\\\3\2\2\2_`\7\2\2\3`\3\3\2\2\2ab\7\n\2")
        buf.write("\2bd\7 \2\2ca\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\5")
        buf.write("\3\2\2\2ge\3\2\2\2hi\7\t\2\2ik\7 \2\2jh\3\2\2\2kl\3\2")
        buf.write("\2\2lj\3\2\2\2lm\3\2\2\2m\7\3\2\2\2no\7\13\2\2oq\7 \2")
        buf.write("\2pn\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2s\t\3\2\2\2")
        buf.write("tr\3\2\2\2uv\7\7\2\2vw\7 \2\2wy\5\f\7\2xz\5\22\n\2yx\3")
        buf.write("\2\2\2yz\3\2\2\2z{\3\2\2\2{}\7*\2\2|~\5\32\16\2}|\3\2")
        buf.write("\2\2~\177\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\u0082\5\24\13\2\u0082\u0083\7+\2")
        buf.write("\2\u0083\13\3\2\2\2\u0084\u0086\7(\2\2\u0085\u0087\5\16")
        buf.write("\b\2\u0086\u0085\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0088\u0089\7)\2\2\u0089\r\3\2\2\2\u008a\u008f")
        buf.write("\5\20\t\2\u008b\u008c\7/\2\2\u008c\u008e\5\20\t\2\u008d")
        buf.write("\u008b\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\17\3\2\2\2\u0091\u008f\3\2")
        buf.write("\2\2\u0092\u0094\58\35\2\u0093\u0092\3\2\2\2\u0093\u0094")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0098\7 \2\2\u0096")
        buf.write("\u0097\7,\2\2\u0097\u0099\7-\2\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\21\3\2\2\2\u009a\u009b\7\67\2\2\u009b")
        buf.write("\u009c\58\35\2\u009c\23\3\2\2\2\u009d\u009e\7\b\2\2\u009e")
        buf.write("\u009f\7 \2\2\u009f\25\3\2\2\2\u00a0\u00a4\7*\2\2\u00a1")
        buf.write("\u00a3\5\32\16\2\u00a2\u00a1\3\2\2\2\u00a3\u00a6\3\2\2")
        buf.write("\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a7")
        buf.write("\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a8\7+\2\2\u00a8")
        buf.write("\27\3\2\2\2\u00a9\u00b0\5\"\22\2\u00aa\u00b0\5$\23\2\u00ab")
        buf.write("\u00b0\5*\26\2\u00ac\u00b0\5(\25\2\u00ad\u00b0\5.\30\2")
        buf.write("\u00ae\u00b0\5\62\32\2\u00af\u00a9\3\2\2\2\u00af\u00aa")
        buf.write("\3\2\2\2\u00af\u00ab\3\2\2\2\u00af\u00ac\3\2\2\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\31\3\2\2\2\u00b1")
        buf.write("\u00b8\5\34\17\2\u00b2\u00b8\5\36\20\2\u00b3\u00b8\5>")
        buf.write(" \2\u00b4\u00b8\5 \21\2\u00b5\u00b8\5&\24\2\u00b6\u00b8")
        buf.write("\5,\27\2\u00b7\u00b1\3\2\2\2\u00b7\u00b2\3\2\2\2\u00b7")
        buf.write("\u00b3\3\2\2\2\u00b7\u00b4\3\2\2\2\u00b7\u00b5\3\2\2\2")
        buf.write("\u00b7\u00b6\3\2\2\2\u00b8\33\3\2\2\2\u00b9\u00ba\7\3")
        buf.write("\2\2\u00ba\u00bb\5\60\31\2\u00bb\u00be\5\26\f\2\u00bc")
        buf.write("\u00bd\7\4\2\2\u00bd\u00bf\5\26\f\2\u00be\u00bc\3\2\2")
        buf.write("\2\u00be\u00bf\3\2\2\2\u00bf\35\3\2\2\2\u00c0\u00c1\7")
        buf.write("\6\2\2\u00c1\u00c2\5\60\31\2\u00c2\u00c3\5\26\f\2\u00c3")
        buf.write("\37\3\2\2\2\u00c4\u00c5\7\5\2\2\u00c5\u00c6\t\2\2\2\u00c6")
        buf.write("\u00c7\7\31\2\2\u00c7\u00c8\5\26\f\2\u00c8!\3\2\2\2\u00c9")
        buf.write("\u00ca\7\17\2\2\u00ca\u00cb\5F$\2\u00cb\u00cc\7\26\2\2")
        buf.write("\u00cc\u00cf\5F$\2\u00cd\u00ce\7\27\2\2\u00ce\u00d0\5")
        buf.write("H%\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0#\3")
        buf.write("\2\2\2\u00d1\u00d2\7\16\2\2\u00d2\u00d3\7 \2\2\u00d3\u00d4")
        buf.write("\7\32\2\2\u00d4\u00d7\7 \2\2\u00d5\u00d6\7\27\2\2\u00d6")
        buf.write("\u00d8\5H%\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("%\3\2\2\2\u00d9\u00da\7\21\2\2\u00da\u00db\7 \2\2\u00db")
        buf.write("\u00dc\7\25\2\2\u00dc\u00df\5J&\2\u00dd\u00de\7\27\2\2")
        buf.write("\u00de\u00e0\5H%\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2")
        buf.write("\2\2\u00e0\'\3\2\2\2\u00e1\u00e2\7\20\2\2\u00e2\u00e3")
        buf.write("\7 \2\2\u00e3\u00e4\7\30\2\2\u00e4\u00e5\7$\2\2\u00e5")
        buf.write(")\3\2\2\2\u00e6\u00e7\7\23\2\2\u00e7\u00e8\7 \2\2\u00e8")
        buf.write("+\3\2\2\2\u00e9\u00ea\7\22\2\2\u00ea\u00ee\7 \2\2\u00eb")
        buf.write("\u00ec\7\24\2\2\u00ec\u00ee\7 \2\2\u00ed\u00e9\3\2\2\2")
        buf.write("\u00ed\u00eb\3\2\2\2\u00ee-\3\2\2\2\u00ef\u00f0\b\30\1")
        buf.write("\2\u00f0\u00f1\5@!\2\u00f1\u0116\3\2\2\2\u00f2\u00f3\f")
        buf.write("\t\2\2\u00f3\u00f4\t\3\2\2\u00f4\u0115\5.\30\n\u00f5\u00f6")
        buf.write("\f\b\2\2\u00f6\u00f7\t\4\2\2\u00f7\u0115\5.\30\t\u00f8")
        buf.write("\u0100\f\7\2\2\u00f9\u00fa\7\63\2\2\u00fa\u0101\7\63\2")
        buf.write("\2\u00fb\u00fc\7\62\2\2\u00fc\u00fd\7\62\2\2\u00fd\u0101")
        buf.write("\7\62\2\2\u00fe\u00ff\7\62\2\2\u00ff\u0101\7\62\2\2\u0100")
        buf.write("\u00f9\3\2\2\2\u0100\u00fb\3\2\2\2\u0100\u00fe\3\2\2\2")
        buf.write("\u0101\u0102\3\2\2\2\u0102\u0115\5.\30\b\u0103\u0104\f")
        buf.write("\6\2\2\u0104\u0105\t\5\2\2\u0105\u0115\5.\30\7\u0106\u0107")
        buf.write("\f\5\2\2\u0107\u0108\t\6\2\2\u0108\u0115\5.\30\6\u0109")
        buf.write("\u010a\f\4\2\2\u010a\u010b\7<\2\2\u010b\u0115\5.\30\5")
        buf.write("\u010c\u010d\f\3\2\2\u010d\u010e\7=\2\2\u010e\u0115\5")
        buf.write(".\30\4\u010f\u0110\f\n\2\2\u0110\u0111\7,\2\2\u0111\u0112")
        buf.write("\5.\30\2\u0112\u0113\7-\2\2\u0113\u0115\3\2\2\2\u0114")
        buf.write("\u00f2\3\2\2\2\u0114\u00f5\3\2\2\2\u0114\u00f8\3\2\2\2")
        buf.write("\u0114\u0103\3\2\2\2\u0114\u0106\3\2\2\2\u0114\u0109\3")
        buf.write("\2\2\2\u0114\u010c\3\2\2\2\u0114\u010f\3\2\2\2\u0115\u0118")
        buf.write("\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("/\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\7(\2\2\u011a")
        buf.write("\u011b\5.\30\2\u011b\u011c\7)\2\2\u011c\61\3\2\2\2\u011d")
        buf.write("\u011e\7 \2\2\u011e\u0120\7(\2\2\u011f\u0121\5\64\33\2")
        buf.write("\u0120\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\3")
        buf.write("\2\2\2\u0122\u0123\7)\2\2\u0123\63\3\2\2\2\u0124\u0129")
        buf.write("\5.\30\2\u0125\u0126\7/\2\2\u0126\u0128\5.\30\2\u0127")
        buf.write("\u0125\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012a\65\3\2\2\2\u012b\u0129\3\2")
        buf.write("\2\2\u012c\u012d\5D#\2\u012d\67\3\2\2\2\u012e\u012f\7")
        buf.write(",\2\2\u012f\u0130\5:\36\2\u0130\u0131\7-\2\2\u01319\3")
        buf.write("\2\2\2\u0132\u0137\5\66\34\2\u0133\u0134\7.\2\2\u0134")
        buf.write("\u0136\5\66\34\2\u0135\u0133\3\2\2\2\u0136\u0139\3\2\2")
        buf.write("\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138;\3\2")
        buf.write("\2\2\u0139\u0137\3\2\2\2\u013a\u013b\7 \2\2\u013b\u013c")
        buf.write("\7,\2\2\u013c\u013d\7$\2\2\u013d\u013e\7-\2\2\u013e=\3")
        buf.write("\2\2\2\u013f\u0141\58\35\2\u0140\u013f\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\7 \2\2\u0143")
        buf.write("\u0144\7\61\2\2\u0144\u0155\5\30\r\2\u0145\u0147\58\35")
        buf.write("\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0149\7 \2\2\u0149\u014a\7,\2\2\u014a\u014b")
        buf.write("\7-\2\2\u014b\u014c\7\61\2\2\u014c\u0155\5(\25\2\u014d")
        buf.write("\u014f\58\35\2\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150\u0151\5<\37\2\u0151\u0152\7")
        buf.write("\61\2\2\u0152\u0153\5\30\r\2\u0153\u0155\3\2\2\2\u0154")
        buf.write("\u0140\3\2\2\2\u0154\u0146\3\2\2\2\u0154\u014e\3\2\2\2")
        buf.write("\u0155?\3\2\2\2\u0156\u0157\7(\2\2\u0157\u0158\5.\30\2")
        buf.write("\u0158\u0159\7)\2\2\u0159\u015d\3\2\2\2\u015a\u015d\5")
        buf.write("B\"\2\u015b\u015d\7 \2\2\u015c\u0156\3\2\2\2\u015c\u015a")
        buf.write("\3\2\2\2\u015c\u015b\3\2\2\2\u015dA\3\2\2\2\u015e\u015f")
        buf.write("\t\7\2\2\u015fC\3\2\2\2\u0160\u0161\t\b\2\2\u0161E\3\2")
        buf.write("\2\2\u0162\u0163\7&\2\2\u0163\u0165\7\33\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0166")
        buf.write("\u0167\7 \2\2\u0167G\3\2\2\2\u0168\u0169\7%\2\2\u0169")
        buf.write("I\3\2\2\2\u016a\u016b\7\'\2\2\u016bK\3\2\2\2!T\\elry\177")
        buf.write("\u0086\u008f\u0093\u0098\u00a4\u00af\u00b7\u00be\u00cf")
        buf.write("\u00d7\u00df\u00ed\u0100\u0114\u0116\u0120\u0129\u0137")
        buf.write("\u0140\u0146\u014e\u0154\u015c\u0164")
        return buf.getvalue()


class BSParser ( Parser ):

    grammarFileName = "BSParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'repeat'", "'while'",
                     "'function'", "'return'", "'manifest'", "'module'",
                     "'stationary'", "'functions'", "'instructions'", "'detect'",
                     "'mix'", "'split'", "'heat'", "'drain'", "'dispense'",
                     "'dispose'", "'at'", "'with'", "'for'", "'into'", "'times'",
                     "'on'", "'of'", "'nat'", "'real'", "'mat'", "'bool'",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','",
                     "'.'", "'='", "'>'", "'<'", "'!'", "'~'", "'?'", "':'",
                     "'=='", "'<='", "'>='", "'!='", "'&&'", "'||'", "'++'",
                     "'--'", "'+'", "'-'", "'*'", "'/'", "'&'", "'|'", "'^'",
                     "'%'", "'_'", "'ns'", "'us'", "'ms'", "'cs'", "'ds'",
                     "'s'", "'h'", "'d'", "'w'", "'mo'", "'y'", "'nL'",
                     "'uL'", "'mL'", "'cL'", "'dL'", "'L'", "'daL'", "'c'",
                     "'f'", "'k'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION",
                      "RETURN", "MANIFEST", "MODULE", "STATIONARY", "FUNCTIONS",
                      "INSTRUCTIONS", "DETECT", "MIX", "SPLIT", "HEAT",
                      "DRAIN", "DISPENSE", "DISPOSE", "AT", "WITH", "FOR",
                      "INTO", "TIMES", "ON", "OF", "NAT", "REAL", "MAT",
                      "BOOL", "IDENTIFIER", "STRING_LITERAL", "BOOL_LITERAL",
                      "FLOAT_LITERAL", "INTEGER_LITERAL", "TIME_NUMBER",
                      "VOLUME_NUMBER", "TEMP_NUMBER", "LPAREN", "RPAREN",
                      "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON",
                      "COMMA", "DOT", "ASSIGN", "GT", "LT", "BANG", "TILDE",
                      "QUESTION", "COLON", "EQUALITY", "LTE", "GTE", "NOTEQUAL",
                      "AND", "OR", "INC", "DEC", "ADDITION", "SUBTRACT",
                      "MULTIPLY", "DIVIDE", "BITAND", "BITOR", "CARET",
                      "MOD", "UNDERSCORE", "NANOSECOND", "MICROSECOND",
                      "MILLISECOND", "CENTISECOND", "DECISECOND", "SECOND",
                      "HOUR", "DAY", "WEEK", "MONTH", "YEAR", "NANOLITRE",
                      "MICROLITRE", "MILLILITRE", "CENTILITRE", "DECILITRE",
                      "LITRE", "DECALITRE", "CELSIUS", "FAHRENHEIT", "KELVIN",
                      "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_moduleDeclaration = 1
    RULE_manifestDeclaration = 2
    RULE_stationaryDeclaration = 3
    RULE_functionDeclaration = 4
    RULE_formalParameters = 5
    RULE_formalParameterList = 6
    RULE_formalParameter = 7
    RULE_functionTyping = 8
    RULE_returnStatement = 9
    RULE_blockStatement = 10
    RULE_assignmentOperations = 11
    RULE_statements = 12
    RULE_ifStatement = 13
    RULE_whileStatement = 14
    RULE_repeat = 15
    RULE_mix = 16
    RULE_detect = 17
    RULE_heat = 18
    RULE_split = 19
    RULE_dispense = 20
    RULE_dispose = 21
    RULE_expression = 22
    RULE_parExpression = 23
    RULE_methodCall = 24
    RULE_expressionList = 25
    RULE_typeType = 26
    RULE_unionType = 27
    RULE_typesList = 28
    RULE_arrayInitializer = 29
    RULE_localVariableDeclaration = 30
    RULE_primary = 31
    RULE_literal = 32
    RULE_primitiveType = 33
    RULE_volumeIdentifier = 34
    RULE_timeIdentifier = 35
    RULE_temperatureIdentifier = 36

    ruleNames =  [ "program", "moduleDeclaration", "manifestDeclaration",
                   "stationaryDeclaration", "functionDeclaration", "formalParameters",
                   "formalParameterList", "formalParameter", "functionTyping",
                   "returnStatement", "blockStatement", "assignmentOperations",
                   "statements", "ifStatement", "whileStatement", "repeat",
                   "mix", "detect", "heat", "split", "dispense", "dispose",
                   "expression", "parExpression", "methodCall", "expressionList",
                   "typeType", "unionType", "typesList", "arrayInitializer",
                   "localVariableDeclaration", "primary", "literal", "primitiveType",
                   "volumeIdentifier", "timeIdentifier", "temperatureIdentifier" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    REPEAT=3
    WHILE=4
    FUNCTION=5
    RETURN=6
    MANIFEST=7
    MODULE=8
    STATIONARY=9
    FUNCTIONS=10
    INSTRUCTIONS=11
    DETECT=12
    MIX=13
    SPLIT=14
    HEAT=15
    DRAIN=16
    DISPENSE=17
    DISPOSE=18
    AT=19
    WITH=20
    FOR=21
    INTO=22
    TIMES=23
    ON=24
    OF=25
    NAT=26
    REAL=27
    MAT=28
    BOOL=29
    IDENTIFIER=30
    STRING_LITERAL=31
    BOOL_LITERAL=32
    FLOAT_LITERAL=33
    INTEGER_LITERAL=34
    TIME_NUMBER=35
    VOLUME_NUMBER=36
    TEMP_NUMBER=37
    LPAREN=38
    RPAREN=39
    LBRACE=40
    RBRACE=41
    LBRACKET=42
    RBRACKET=43
    SEMICOLON=44
    COMMA=45
    DOT=46
    ASSIGN=47
    GT=48
    LT=49
    BANG=50
    TILDE=51
    QUESTION=52
    COLON=53
    EQUALITY=54
    LTE=55
    GTE=56
    NOTEQUAL=57
    AND=58
    OR=59
    INC=60
    DEC=61
    ADDITION=62
    SUBTRACT=63
    MULTIPLY=64
    DIVIDE=65
    BITAND=66
    BITOR=67
    CARET=68
    MOD=69
    UNDERSCORE=70
    NANOSECOND=71
    MICROSECOND=72
    MILLISECOND=73
    CENTISECOND=74
    DECISECOND=75
    SECOND=76
    HOUR=77
    DAY=78
    WEEK=79
    MONTH=80
    YEAR=81
    NANOLITRE=82
    MICROLITRE=83
    MILLILITRE=84
    CENTILITRE=85
    DECILITRE=86
    LITRE=87
    DECALITRE=88
    CELSIUS=89
    FAHRENHEIT=90
    KELVIN=91
    WS=92
    COMMENT=93
    LINE_COMMENT=94

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moduleDeclaration(self):
            return self.getTypedRuleContext(BSParser.ModuleDeclarationContext,0)


        def stationaryDeclaration(self):
            return self.getTypedRuleContext(BSParser.StationaryDeclarationContext,0)


        def manifestDeclaration(self):
            return self.getTypedRuleContext(BSParser.ManifestDeclarationContext,0)


        def FUNCTIONS(self):
            return self.getToken(BSParser.FUNCTIONS, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.COLON)
            else:
                return self.getToken(BSParser.COLON, i)

        def INSTRUCTIONS(self):
            return self.getToken(BSParser.INSTRUCTIONS, 0)

        def EOF(self):
            return self.getToken(BSParser.EOF, 0)

        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(BSParser.FunctionDeclarationContext,i)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.StatementsContext)
            else:
                return self.getTypedRuleContext(BSParser.StatementsContext,i)


        def getRuleIndex(self):
            return BSParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = BSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.moduleDeclaration()
            self.state = 75
            self.stationaryDeclaration()
            self.state = 76
            self.manifestDeclaration()
            self.state = 77
            self.match(BSParser.FUNCTIONS)
            self.state = 78
            self.match(BSParser.COLON)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.FUNCTION:
                self.state = 79
                self.functionDeclaration()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(BSParser.INSTRUCTIONS)
            self.state = 86
            self.match(BSParser.COLON)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 87
                self.statements()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self.match(BSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuleDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODULE(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.MODULE)
            else:
                return self.getToken(BSParser.MODULE, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.IDENTIFIER)
            else:
                return self.getToken(BSParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return BSParser.RULE_moduleDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModuleDeclaration" ):
                listener.enterModuleDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModuleDeclaration" ):
                listener.exitModuleDeclaration(self)




    def moduleDeclaration(self):

        localctx = BSParser.ModuleDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_moduleDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.MODULE:
                self.state = 95
                self.match(BSParser.MODULE)
                self.state = 96
                self.match(BSParser.IDENTIFIER)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ManifestDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MANIFEST(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.MANIFEST)
            else:
                return self.getToken(BSParser.MANIFEST, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.IDENTIFIER)
            else:
                return self.getToken(BSParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return BSParser.RULE_manifestDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManifestDeclaration" ):
                listener.enterManifestDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManifestDeclaration" ):
                listener.exitManifestDeclaration(self)




    def manifestDeclaration(self):

        localctx = BSParser.ManifestDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_manifestDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.match(BSParser.MANIFEST)
                self.state = 103
                self.match(BSParser.IDENTIFIER)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BSParser.MANIFEST):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StationaryDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIONARY(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.STATIONARY)
            else:
                return self.getToken(BSParser.STATIONARY, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.IDENTIFIER)
            else:
                return self.getToken(BSParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return BSParser.RULE_stationaryDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStationaryDeclaration" ):
                listener.enterStationaryDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStationaryDeclaration" ):
                listener.exitStationaryDeclaration(self)




    def stationaryDeclaration(self):

        localctx = BSParser.StationaryDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stationaryDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.STATIONARY:
                self.state = 108
                self.match(BSParser.STATIONARY)
                self.state = 109
                self.match(BSParser.IDENTIFIER)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BSParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def formalParameters(self):
            return self.getTypedRuleContext(BSParser.FormalParametersContext,0)


        def LBRACE(self):
            return self.getToken(BSParser.LBRACE, 0)

        def returnStatement(self):
            return self.getTypedRuleContext(BSParser.ReturnStatementContext,0)


        def RBRACE(self):
            return self.getToken(BSParser.RBRACE, 0)

        def functionTyping(self):
            return self.getTypedRuleContext(BSParser.FunctionTypingContext,0)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.StatementsContext)
            else:
                return self.getTypedRuleContext(BSParser.StatementsContext,i)


        def getRuleIndex(self):
            return BSParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = BSParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(BSParser.FUNCTION)
            self.state = 116
            self.match(BSParser.IDENTIFIER)
            self.state = 117
            self.formalParameters()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.COLON:
                self.state = 118
                self.functionTyping()


            self.state = 121
            self.match(BSParser.LBRACE)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 122
                self.statements()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0)):
                    break

            self.state = 127
            self.returnStatement()
            self.state = 128
            self.match(BSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormalParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BSParser.RPAREN, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(BSParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_formalParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameters" ):
                listener.enterFormalParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameters" ):
                listener.exitFormalParameters(self)




    def formalParameters(self):

        localctx = BSParser.FormalParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_formalParameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(BSParser.LPAREN)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.IDENTIFIER or _la==BSParser.LBRACKET:
                self.state = 131
                self.formalParameterList()


            self.state = 134
            self.match(BSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormalParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formalParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.FormalParameterContext)
            else:
                return self.getTypedRuleContext(BSParser.FormalParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.COMMA)
            else:
                return self.getToken(BSParser.COMMA, i)

        def getRuleIndex(self):
            return BSParser.RULE_formalParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterList" ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterList" ):
                listener.exitFormalParameterList(self)




    def formalParameterList(self):

        localctx = BSParser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.formalParameter()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 137
                self.match(BSParser.COMMA)
                self.state = 138
                self.formalParameter()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormalParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def getRuleIndex(self):
            return BSParser.RULE_formalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameter" ):
                listener.enterFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameter" ):
                listener.exitFormalParameter(self)




    def formalParameter(self):

        localctx = BSParser.FormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_formalParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 144
                self.unionType()


            self.state = 147
            self.match(BSParser.IDENTIFIER)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 148
                self.match(BSParser.LBRACKET)
                self.state = 149
                self.match(BSParser.RBRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionTypingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(BSParser.COLON, 0)

        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_functionTyping

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionTyping" ):
                listener.enterFunctionTyping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionTyping" ):
                listener.exitFunctionTyping(self)




    def functionTyping(self):

        localctx = BSParser.FunctionTypingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionTyping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(BSParser.COLON)
            self.state = 153
            self.unionType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BSParser.RETURN, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = BSParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(BSParser.RETURN)
            self.state = 156
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(BSParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(BSParser.RBRACE, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.StatementsContext)
            else:
                return self.getTypedRuleContext(BSParser.StatementsContext,i)


        def getRuleIndex(self):
            return BSParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)




    def blockStatement(self):

        localctx = BSParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(BSParser.LBRACE)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 159
                self.statements()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self.match(BSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentOperationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mix(self):
            return self.getTypedRuleContext(BSParser.MixContext,0)


        def detect(self):
            return self.getTypedRuleContext(BSParser.DetectContext,0)


        def dispense(self):
            return self.getTypedRuleContext(BSParser.DispenseContext,0)


        def split(self):
            return self.getTypedRuleContext(BSParser.SplitContext,0)


        def expression(self):
            return self.getTypedRuleContext(BSParser.ExpressionContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(BSParser.MethodCallContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_assignmentOperations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperations" ):
                listener.enterAssignmentOperations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperations" ):
                listener.exitAssignmentOperations(self)




    def assignmentOperations(self):

        localctx = BSParser.AssignmentOperationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignmentOperations)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.mix()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.detect()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.dispense()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 170
                self.split()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 171
                self.expression(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 172
                self.methodCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(BSParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(BSParser.WhileStatementContext,0)


        def localVariableDeclaration(self):
            return self.getTypedRuleContext(BSParser.LocalVariableDeclarationContext,0)


        def repeat(self):
            return self.getTypedRuleContext(BSParser.RepeatContext,0)


        def heat(self):
            return self.getTypedRuleContext(BSParser.HeatContext,0)


        def dispose(self):
            return self.getTypedRuleContext(BSParser.DisposeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = BSParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statements)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.ifStatement()
                pass
            elif token in [BSParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.whileStatement()
                pass
            elif token in [BSParser.IDENTIFIER, BSParser.LBRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.localVariableDeclaration()
                pass
            elif token in [BSParser.REPEAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.repeat()
                pass
            elif token in [BSParser.HEAT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 179
                self.heat()
                pass
            elif token in [BSParser.DRAIN, BSParser.DISPOSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 180
                self.dispose()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BSParser.IF, 0)

        def parExpression(self):
            return self.getTypedRuleContext(BSParser.ParExpressionContext,0)


        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(BSParser.BlockStatementContext,i)


        def ELSE(self):
            return self.getToken(BSParser.ELSE, 0)

        def getRuleIndex(self):
            return BSParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = BSParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(BSParser.IF)
            self.state = 184
            self.parExpression()
            self.state = 185
            self.blockStatement()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ELSE:
                self.state = 186
                self.match(BSParser.ELSE)
                self.state = 187
                self.blockStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhileStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BSParser.WHILE, 0)

        def parExpression(self):
            return self.getTypedRuleContext(BSParser.ParExpressionContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(BSParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = BSParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(BSParser.WHILE)
            self.state = 191
            self.parExpression()
            self.state = 192
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RepeatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT(self):
            return self.getToken(BSParser.REPEAT, 0)

        def TIMES(self):
            return self.getToken(BSParser.TIMES, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(BSParser.BlockStatementContext,0)


        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def getRuleIndex(self):
            return BSParser.RULE_repeat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat" ):
                listener.enterRepeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat" ):
                listener.exitRepeat(self)




    def repeat(self):

        localctx = BSParser.RepeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_repeat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(BSParser.REPEAT)
            self.state = 195
            _la = self._input.LA(1)
            if not(_la==BSParser.IDENTIFIER or _la==BSParser.INTEGER_LITERAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 196
            self.match(BSParser.TIMES)
            self.state = 197
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIX(self):
            return self.getToken(BSParser.MIX, 0)

        def volumeIdentifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.VolumeIdentifierContext)
            else:
                return self.getTypedRuleContext(BSParser.VolumeIdentifierContext,i)


        def WITH(self):
            return self.getToken(BSParser.WITH, 0)

        def FOR(self):
            return self.getToken(BSParser.FOR, 0)

        def timeIdentifier(self):
            return self.getTypedRuleContext(BSParser.TimeIdentifierContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_mix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMix" ):
                listener.enterMix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMix" ):
                listener.exitMix(self)




    def mix(self):

        localctx = BSParser.MixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_mix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(BSParser.MIX)
            self.state = 200
            self.volumeIdentifier()
            self.state = 201
            self.match(BSParser.WITH)
            self.state = 202
            self.volumeIdentifier()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 203
                self.match(BSParser.FOR)
                self.state = 204
                self.timeIdentifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DetectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DETECT(self):
            return self.getToken(BSParser.DETECT, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.IDENTIFIER)
            else:
                return self.getToken(BSParser.IDENTIFIER, i)

        def ON(self):
            return self.getToken(BSParser.ON, 0)

        def FOR(self):
            return self.getToken(BSParser.FOR, 0)

        def timeIdentifier(self):
            return self.getTypedRuleContext(BSParser.TimeIdentifierContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_detect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetect" ):
                listener.enterDetect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetect" ):
                listener.exitDetect(self)




    def detect(self):

        localctx = BSParser.DetectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_detect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(BSParser.DETECT)
            self.state = 208
            self.match(BSParser.IDENTIFIER)
            self.state = 209
            self.match(BSParser.ON)
            self.state = 210
            self.match(BSParser.IDENTIFIER)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 211
                self.match(BSParser.FOR)
                self.state = 212
                self.timeIdentifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HeatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEAT(self):
            return self.getToken(BSParser.HEAT, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def AT(self):
            return self.getToken(BSParser.AT, 0)

        def temperatureIdentifier(self):
            return self.getTypedRuleContext(BSParser.TemperatureIdentifierContext,0)


        def FOR(self):
            return self.getToken(BSParser.FOR, 0)

        def timeIdentifier(self):
            return self.getTypedRuleContext(BSParser.TimeIdentifierContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_heat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeat" ):
                listener.enterHeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeat" ):
                listener.exitHeat(self)




    def heat(self):

        localctx = BSParser.HeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_heat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(BSParser.HEAT)
            self.state = 216
            self.match(BSParser.IDENTIFIER)
            self.state = 217
            self.match(BSParser.AT)
            self.state = 218
            self.temperatureIdentifier()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 219
                self.match(BSParser.FOR)
                self.state = 220
                self.timeIdentifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SplitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPLIT(self):
            return self.getToken(BSParser.SPLIT, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def INTO(self):
            return self.getToken(BSParser.INTO, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def getRuleIndex(self):
            return BSParser.RULE_split

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSplit" ):
                listener.enterSplit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSplit" ):
                listener.exitSplit(self)




    def split(self):

        localctx = BSParser.SplitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_split)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(BSParser.SPLIT)
            self.state = 224
            self.match(BSParser.IDENTIFIER)
            self.state = 225
            self.match(BSParser.INTO)
            self.state = 226
            self.match(BSParser.INTEGER_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DispenseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISPENSE(self):
            return self.getToken(BSParser.DISPENSE, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_dispense

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDispense" ):
                listener.enterDispense(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDispense" ):
                listener.exitDispense(self)




    def dispense(self):

        localctx = BSParser.DispenseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_dispense)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(BSParser.DISPENSE)
            self.state = 229
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DisposeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DRAIN(self):
            return self.getToken(BSParser.DRAIN, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def DISPOSE(self):
            return self.getToken(BSParser.DISPOSE, 0)

        def getRuleIndex(self):
            return BSParser.RULE_dispose

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDispose" ):
                listener.enterDispose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDispose" ):
                listener.exitDispose(self)




    def dispose(self):

        localctx = BSParser.DisposeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_dispose)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.DRAIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(BSParser.DRAIN)
                self.state = 232
                self.match(BSParser.IDENTIFIER)
                pass
            elif token in [BSParser.DISPOSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(BSParser.DISPOSE)
                self.state = 234
                self.match(BSParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bop = None # Token

        def primary(self):
            return self.getTypedRuleContext(BSParser.PrimaryContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BSParser.ExpressionContext,i)


        def MULTIPLY(self):
            return self.getToken(BSParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(BSParser.DIVIDE, 0)

        def ADDITION(self):
            return self.getToken(BSParser.ADDITION, 0)

        def SUBTRACT(self):
            return self.getToken(BSParser.SUBTRACT, 0)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.LT)
            else:
                return self.getToken(BSParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.GT)
            else:
                return self.getToken(BSParser.GT, i)

        def LTE(self):
            return self.getToken(BSParser.LTE, 0)

        def GTE(self):
            return self.getToken(BSParser.GTE, 0)

        def EQUALITY(self):
            return self.getToken(BSParser.EQUALITY, 0)

        def NOTEQUAL(self):
            return self.getToken(BSParser.NOTEQUAL, 0)

        def AND(self):
            return self.getToken(BSParser.AND, 0)

        def OR(self):
            return self.getToken(BSParser.OR, 0)

        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def getRuleIndex(self):
            return BSParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BSParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.primary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 274
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 240
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 241
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BSParser.MULTIPLY - 64)) | (1 << (BSParser.DIVIDE - 64)) | (1 << (BSParser.MOD - 64)))) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 242
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 243
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 244
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BSParser.ADDITION or _la==BSParser.SUBTRACT):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 245
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 246
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 254
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                        if la_ == 1:
                            self.state = 247
                            self.match(BSParser.LT)
                            self.state = 248
                            self.match(BSParser.LT)
                            pass

                        elif la_ == 2:
                            self.state = 249
                            self.match(BSParser.GT)
                            self.state = 250
                            self.match(BSParser.GT)
                            self.state = 251
                            self.match(BSParser.GT)
                            pass

                        elif la_ == 3:
                            self.state = 252
                            self.match(BSParser.GT)
                            self.state = 253
                            self.match(BSParser.GT)
                            pass


                        self.state = 256
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 257
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 258
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.GT) | (1 << BSParser.LT) | (1 << BSParser.LTE) | (1 << BSParser.GTE))) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 259
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 260
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 261
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BSParser.EQUALITY or _la==BSParser.NOTEQUAL):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 262
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 263
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 264
                        localctx.bop = self.match(BSParser.AND)
                        self.state = 265
                        self.expression(3)
                        pass

                    elif la_ == 7:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 266
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 267
                        localctx.bop = self.match(BSParser.OR)
                        self.state = 268
                        self.expression(2)
                        pass

                    elif la_ == 8:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 269
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 270
                        self.match(BSParser.LBRACKET)
                        self.state = 271
                        self.expression(0)
                        self.state = 272
                        self.match(BSParser.RBRACKET)
                        pass


                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ParExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BSParser.RPAREN, 0)

        def getRuleIndex(self):
            return BSParser.RULE_parExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParExpression" ):
                listener.enterParExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParExpression" ):
                listener.exitParExpression(self)




    def parExpression(self):

        localctx = BSParser.ParExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_parExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(BSParser.LPAREN)
            self.state = 280
            self.expression(0)
            self.state = 281
            self.match(BSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MethodCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(BSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BSParser.RPAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(BSParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_methodCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)




    def methodCall(self):

        localctx = BSParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(BSParser.IDENTIFIER)
            self.state = 284
            self.match(BSParser.LPAREN)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IDENTIFIER) | (1 << BSParser.STRING_LITERAL) | (1 << BSParser.BOOL_LITERAL) | (1 << BSParser.FLOAT_LITERAL) | (1 << BSParser.INTEGER_LITERAL) | (1 << BSParser.LPAREN))) != 0):
                self.state = 285
                self.expressionList()


            self.state = 288
            self.match(BSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BSParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.COMMA)
            else:
                return self.getToken(BSParser.COMMA, i)

        def getRuleIndex(self):
            return BSParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = BSParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.expression(0)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 291
                self.match(BSParser.COMMA)
                self.state = 292
                self.expression(0)
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(BSParser.PrimitiveTypeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_typeType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeType" ):
                listener.enterTypeType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeType" ):
                listener.exitTypeType(self)




    def typeType(self):

        localctx = BSParser.TypeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_typeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.primitiveType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnionTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def typesList(self):
            return self.getTypedRuleContext(BSParser.TypesListContext,0)


        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def getRuleIndex(self):
            return BSParser.RULE_unionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnionType" ):
                listener.enterUnionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnionType" ):
                listener.exitUnionType(self)




    def unionType(self):

        localctx = BSParser.UnionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(BSParser.LBRACKET)
            self.state = 301
            self.typesList()
            self.state = 302
            self.match(BSParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypesListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.TypeTypeContext)
            else:
                return self.getTypedRuleContext(BSParser.TypeTypeContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.SEMICOLON)
            else:
                return self.getToken(BSParser.SEMICOLON, i)

        def getRuleIndex(self):
            return BSParser.RULE_typesList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypesList" ):
                listener.enterTypesList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypesList" ):
                listener.exitTypesList(self)




    def typesList(self):

        localctx = BSParser.TypesListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_typesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.typeType()
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.SEMICOLON:
                self.state = 305
                self.match(BSParser.SEMICOLON)
                self.state = 306
                self.typeType()
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayInitializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def getRuleIndex(self):
            return BSParser.RULE_arrayInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayInitializer" ):
                listener.enterArrayInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayInitializer" ):
                listener.exitArrayInitializer(self)




    def arrayInitializer(self):

        localctx = BSParser.ArrayInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_arrayInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(BSParser.IDENTIFIER)
            self.state = 313
            self.match(BSParser.LBRACKET)
            self.state = 314
            self.match(BSParser.INTEGER_LITERAL)
            self.state = 315
            self.match(BSParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LocalVariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(BSParser.ASSIGN, 0)

        def assignmentOperations(self):
            return self.getTypedRuleContext(BSParser.AssignmentOperationsContext,0)


        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def split(self):
            return self.getTypedRuleContext(BSParser.SplitContext,0)


        def arrayInitializer(self):
            return self.getTypedRuleContext(BSParser.ArrayInitializerContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_localVariableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalVariableDeclaration" ):
                listener.enterLocalVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalVariableDeclaration" ):
                listener.exitLocalVariableDeclaration(self)




    def localVariableDeclaration(self):

        localctx = BSParser.LocalVariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_localVariableDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.LBRACKET:
                    self.state = 317
                    self.unionType()


                self.state = 320
                self.match(BSParser.IDENTIFIER)
                self.state = 321
                self.match(BSParser.ASSIGN)
                self.state = 322
                self.assignmentOperations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.LBRACKET:
                    self.state = 323
                    self.unionType()


                self.state = 326
                self.match(BSParser.IDENTIFIER)
                self.state = 327
                self.match(BSParser.LBRACKET)
                self.state = 328
                self.match(BSParser.RBRACKET)
                self.state = 329
                self.match(BSParser.ASSIGN)
                self.state = 330
                self.split()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.LBRACKET:
                    self.state = 331
                    self.unionType()


                self.state = 334
                self.arrayInitializer()
                self.state = 335
                self.match(BSParser.ASSIGN)
                self.state = 336
                self.assignmentOperations()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BSParser.RPAREN, 0)

        def literal(self):
            return self.getTypedRuleContext(BSParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = BSParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_primary)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(BSParser.LPAREN)
                self.state = 341
                self.expression(0)
                self.state = 342
                self.match(BSParser.RPAREN)
                pass
            elif token in [BSParser.STRING_LITERAL, BSParser.BOOL_LITERAL, BSParser.FLOAT_LITERAL, BSParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.literal()
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.match(BSParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(BSParser.FLOAT_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(BSParser.BOOL_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(BSParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return BSParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = BSParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.STRING_LITERAL) | (1 << BSParser.BOOL_LITERAL) | (1 << BSParser.FLOAT_LITERAL) | (1 << BSParser.INTEGER_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimitiveTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(BSParser.BOOL, 0)

        def NAT(self):
            return self.getToken(BSParser.NAT, 0)

        def REAL(self):
            return self.getToken(BSParser.REAL, 0)

        def MAT(self):
            return self.getToken(BSParser.MAT, 0)

        def getRuleIndex(self):
            return BSParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)




    def primitiveType(self):

        localctx = BSParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.NAT) | (1 << BSParser.REAL) | (1 << BSParser.MAT) | (1 << BSParser.BOOL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VolumeIdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def VOLUME_NUMBER(self):
            return self.getToken(BSParser.VOLUME_NUMBER, 0)

        def OF(self):
            return self.getToken(BSParser.OF, 0)

        def getRuleIndex(self):
            return BSParser.RULE_volumeIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVolumeIdentifier" ):
                listener.enterVolumeIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVolumeIdentifier" ):
                listener.exitVolumeIdentifier(self)




    def volumeIdentifier(self):

        localctx = BSParser.VolumeIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_volumeIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.VOLUME_NUMBER:
                self.state = 352
                self.match(BSParser.VOLUME_NUMBER)
                self.state = 353
                self.match(BSParser.OF)


            self.state = 356
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimeIdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIME_NUMBER(self):
            return self.getToken(BSParser.TIME_NUMBER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_timeIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeIdentifier" ):
                listener.enterTimeIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeIdentifier" ):
                listener.exitTimeIdentifier(self)




    def timeIdentifier(self):

        localctx = BSParser.TimeIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_timeIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(BSParser.TIME_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TemperatureIdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEMP_NUMBER(self):
            return self.getToken(BSParser.TEMP_NUMBER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_temperatureIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemperatureIdentifier" ):
                listener.enterTemperatureIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemperatureIdentifier" ):
                listener.exitTemperatureIdentifier(self)




    def temperatureIdentifier(self):

        localctx = BSParser.TemperatureIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_temperatureIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(BSParser.TEMP_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)


            if predIndex == 1:
                return self.precpred(self._ctx, 6)


            if predIndex == 2:
                return self.precpred(self._ctx, 5)


            if predIndex == 3:
                return self.precpred(self._ctx, 4)


            if predIndex == 4:
                return self.precpred(self._ctx, 3)


            if predIndex == 5:
                return self.precpred(self._ctx, 2)


            if predIndex == 6:
                return self.precpred(self._ctx, 1)


            if predIndex == 7:
                return self.precpred(self._ctx, 8)





