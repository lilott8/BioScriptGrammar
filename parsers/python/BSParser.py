# Generated from /bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys

# parser/listener/visitor header section
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3`")
        buf.write("\u0172\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\3\2\3\2\3\2\3\2\3\2\7\2U\n\2\f\2\16\2X\13")
        buf.write("\2\3\2\3\2\3\2\7\2]\n\2\f\2\16\2`\13\2\3\2\3\2\3\3\3\3")
        buf.write("\7\3f\n\3\f\3\16\3i\13\3\3\4\3\4\6\4m\n\4\r\4\16\4n\3")
        buf.write("\5\3\5\7\5s\n\5\f\5\16\5v\13\5\3\6\3\6\3\6\3\6\5\6|\n")
        buf.write("\6\3\6\3\6\6\6\u0080\n\6\r\6\16\6\u0081\3\6\3\6\3\6\3")
        buf.write("\7\3\7\5\7\u0089\n\7\3\7\3\7\3\b\3\b\3\b\7\b\u0090\n\b")
        buf.write("\f\b\16\b\u0093\13\b\3\t\5\t\u0096\n\t\3\t\3\t\3\t\5\t")
        buf.write("\u009b\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\7\f\u00a5")
        buf.write("\n\f\f\f\16\f\u00a8\13\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00b0")
        buf.write("\n\r\3\16\3\16\5\16\u00b4\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00bd\n\17\3\20\3\20\3\20\3\20\3\20\5")
        buf.write("\20\u00c4\n\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00d5\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\5\24\u00dd\n\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u00e5\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u00f3")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0106\n\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u011a\n\31\f")
        buf.write("\31\16\31\u011d\13\31\3\32\3\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\5\33\u0126\n\33\3\33\3\33\3\34\3\34\3\34\7\34\u012d")
        buf.write("\n\34\f\34\16\34\u0130\13\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\7\37\u013b\n\37\f\37\16\37\u013e")
        buf.write("\13\37\3 \5 \u0141\n \3 \3 \3 \3 \3!\5!\u0148\n!\3!\3")
        buf.write("!\3!\3!\3!\3!\5!\u0150\n!\3!\3!\3!\3!\5!\u0156\n!\3!\3")
        buf.write("!\5!\u015a\n!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0162\n\"\3")
        buf.write("#\3#\3$\3$\3%\3%\5%\u016a\n%\3%\3%\3&\3&\3\'\3\'\3\'\2")
        buf.write("\3\60(\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJL\2\t\4\2  $$\4\2BCGG\3\2@A\4\2")
        buf.write("\62\639:\4\288;;\3\2!$\3\2\34\37\2\u017b\2N\3\2\2\2\4")
        buf.write("g\3\2\2\2\6l\3\2\2\2\bt\3\2\2\2\nw\3\2\2\2\f\u0086\3\2")
        buf.write("\2\2\16\u008c\3\2\2\2\20\u0095\3\2\2\2\22\u009c\3\2\2")
        buf.write("\2\24\u009f\3\2\2\2\26\u00a2\3\2\2\2\30\u00af\3\2\2\2")
        buf.write("\32\u00b3\3\2\2\2\34\u00bc\3\2\2\2\36\u00be\3\2\2\2 \u00c5")
        buf.write("\3\2\2\2\"\u00c9\3\2\2\2$\u00ce\3\2\2\2&\u00d6\3\2\2\2")
        buf.write("(\u00de\3\2\2\2*\u00e6\3\2\2\2,\u00eb\3\2\2\2.\u00f2\3")
        buf.write("\2\2\2\60\u00f4\3\2\2\2\62\u011e\3\2\2\2\64\u0122\3\2")
        buf.write("\2\2\66\u0129\3\2\2\28\u0131\3\2\2\2:\u0133\3\2\2\2<\u0137")
        buf.write("\3\2\2\2>\u0140\3\2\2\2@\u0159\3\2\2\2B\u0161\3\2\2\2")
        buf.write("D\u0163\3\2\2\2F\u0165\3\2\2\2H\u0169\3\2\2\2J\u016d\3")
        buf.write("\2\2\2L\u016f\3\2\2\2NO\5\4\3\2OP\5\b\5\2PQ\5\6\4\2QR")
        buf.write("\7\f\2\2RV\7\67\2\2SU\5\n\6\2TS\3\2\2\2UX\3\2\2\2VT\3")
        buf.write("\2\2\2VW\3\2\2\2WY\3\2\2\2XV\3\2\2\2YZ\7\r\2\2Z^\7\67")
        buf.write("\2\2[]\5\34\17\2\\[\3\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2")
        buf.write("\2\2_a\3\2\2\2`^\3\2\2\2ab\7\2\2\3b\3\3\2\2\2cd\7\n\2")
        buf.write("\2df\7 \2\2ec\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\5")
        buf.write("\3\2\2\2ig\3\2\2\2jk\7\t\2\2km\7 \2\2lj\3\2\2\2mn\3\2")
        buf.write("\2\2nl\3\2\2\2no\3\2\2\2o\7\3\2\2\2pq\7\13\2\2qs\7 \2")
        buf.write("\2rp\3\2\2\2sv\3\2\2\2tr\3\2\2\2tu\3\2\2\2u\t\3\2\2\2")
        buf.write("vt\3\2\2\2wx\7\7\2\2xy\7 \2\2y{\5\f\7\2z|\5\22\n\2{z\3")
        buf.write("\2\2\2{|\3\2\2\2|}\3\2\2\2}\177\7*\2\2~\u0080\5\34\17")
        buf.write("\2\177~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\177\3\2\2\2")
        buf.write("\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\5")
        buf.write("\24\13\2\u0084\u0085\7+\2\2\u0085\13\3\2\2\2\u0086\u0088")
        buf.write("\7(\2\2\u0087\u0089\5\16\b\2\u0088\u0087\3\2\2\2\u0088")
        buf.write("\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\7)\2\2")
        buf.write("\u008b\r\3\2\2\2\u008c\u0091\5\20\t\2\u008d\u008e\7/\2")
        buf.write("\2\u008e\u0090\5\20\t\2\u008f\u008d\3\2\2\2\u0090\u0093")
        buf.write("\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\17\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0096\5:\36\2\u0095")
        buf.write("\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u009a\7 \2\2\u0098\u0099\7,\2\2\u0099\u009b\7-")
        buf.write("\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\21")
        buf.write("\3\2\2\2\u009c\u009d\7\67\2\2\u009d\u009e\5:\36\2\u009e")
        buf.write("\23\3\2\2\2\u009f\u00a0\7\b\2\2\u00a0\u00a1\7 \2\2\u00a1")
        buf.write("\25\3\2\2\2\u00a2\u00a6\7*\2\2\u00a3\u00a5\5\34\17\2\u00a4")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2")
        buf.write("\u00a6\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2\u00a8\u00a6\3")
        buf.write("\2\2\2\u00a9\u00aa\7+\2\2\u00aa\27\3\2\2\2\u00ab\u00b0")
        buf.write("\5$\23\2\u00ac\u00b0\5,\27\2\u00ad\u00b0\5*\26\2\u00ae")
        buf.write("\u00b0\5\64\33\2\u00af\u00ab\3\2\2\2\u00af\u00ac\3\2\2")
        buf.write("\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\31\3")
        buf.write("\2\2\2\u00b1\u00b4\5\60\31\2\u00b2\u00b4\5&\24\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\33\3\2\2\2\u00b5")
        buf.write("\u00bd\5\36\20\2\u00b6\u00bd\5 \21\2\u00b7\u00bd\5@!\2")
        buf.write("\u00b8\u00bd\5> \2\u00b9\u00bd\5\"\22\2\u00ba\u00bd\5")
        buf.write("(\25\2\u00bb\u00bd\5.\30\2\u00bc\u00b5\3\2\2\2\u00bc\u00b6")
        buf.write("\3\2\2\2\u00bc\u00b7\3\2\2\2\u00bc\u00b8\3\2\2\2\u00bc")
        buf.write("\u00b9\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bd\35\3\2\2\2\u00be\u00bf\7\3\2\2\u00bf\u00c0\5\62")
        buf.write("\32\2\u00c0\u00c3\5\26\f\2\u00c1\u00c2\7\4\2\2\u00c2\u00c4")
        buf.write("\5\26\f\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\37\3\2\2\2\u00c5\u00c6\7\6\2\2\u00c6\u00c7\5\62\32\2")
        buf.write("\u00c7\u00c8\5\26\f\2\u00c8!\3\2\2\2\u00c9\u00ca\7\5\2")
        buf.write("\2\u00ca\u00cb\t\2\2\2\u00cb\u00cc\7\31\2\2\u00cc\u00cd")
        buf.write("\5\26\f\2\u00cd#\3\2\2\2\u00ce\u00cf\7\17\2\2\u00cf\u00d0")
        buf.write("\5H%\2\u00d0\u00d1\7\26\2\2\u00d1\u00d4\5H%\2\u00d2\u00d3")
        buf.write("\7\27\2\2\u00d3\u00d5\5J&\2\u00d4\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5%\3\2\2\2\u00d6\u00d7\7\16\2\2\u00d7")
        buf.write("\u00d8\7 \2\2\u00d8\u00d9\7\32\2\2\u00d9\u00dc\7 \2\2")
        buf.write("\u00da\u00db\7\27\2\2\u00db\u00dd\5J&\2\u00dc\u00da\3")
        buf.write("\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\'\3\2\2\2\u00de\u00df")
        buf.write("\7\21\2\2\u00df\u00e0\7 \2\2\u00e0\u00e1\7\25\2\2\u00e1")
        buf.write("\u00e4\5L\'\2\u00e2\u00e3\7\27\2\2\u00e3\u00e5\5J&\2\u00e4")
        buf.write("\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5)\3\2\2\2\u00e6")
        buf.write("\u00e7\7\20\2\2\u00e7\u00e8\7 \2\2\u00e8\u00e9\7\30\2")
        buf.write("\2\u00e9\u00ea\7$\2\2\u00ea+\3\2\2\2\u00eb\u00ec\7\23")
        buf.write("\2\2\u00ec\u00ed\7 \2\2\u00ed-\3\2\2\2\u00ee\u00ef\7\22")
        buf.write("\2\2\u00ef\u00f3\7 \2\2\u00f0\u00f1\7\24\2\2\u00f1\u00f3")
        buf.write("\7 \2\2\u00f2\u00ee\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3")
        buf.write("/\3\2\2\2\u00f4\u00f5\b\31\1\2\u00f5\u00f6\5B\"\2\u00f6")
        buf.write("\u011b\3\2\2\2\u00f7\u00f8\f\t\2\2\u00f8\u00f9\t\3\2\2")
        buf.write("\u00f9\u011a\5\60\31\n\u00fa\u00fb\f\b\2\2\u00fb\u00fc")
        buf.write("\t\4\2\2\u00fc\u011a\5\60\31\t\u00fd\u0105\f\7\2\2\u00fe")
        buf.write("\u00ff\7\63\2\2\u00ff\u0106\7\63\2\2\u0100\u0101\7\62")
        buf.write("\2\2\u0101\u0102\7\62\2\2\u0102\u0106\7\62\2\2\u0103\u0104")
        buf.write("\7\62\2\2\u0104\u0106\7\62\2\2\u0105\u00fe\3\2\2\2\u0105")
        buf.write("\u0100\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0107\3\2\2\2")
        buf.write("\u0107\u011a\5\60\31\b\u0108\u0109\f\6\2\2\u0109\u010a")
        buf.write("\t\5\2\2\u010a\u011a\5\60\31\7\u010b\u010c\f\5\2\2\u010c")
        buf.write("\u010d\t\6\2\2\u010d\u011a\5\60\31\6\u010e\u010f\f\4\2")
        buf.write("\2\u010f\u0110\7<\2\2\u0110\u011a\5\60\31\5\u0111\u0112")
        buf.write("\f\3\2\2\u0112\u0113\7=\2\2\u0113\u011a\5\60\31\4\u0114")
        buf.write("\u0115\f\n\2\2\u0115\u0116\7,\2\2\u0116\u0117\5\60\31")
        buf.write("\2\u0117\u0118\7-\2\2\u0118\u011a\3\2\2\2\u0119\u00f7")
        buf.write("\3\2\2\2\u0119\u00fa\3\2\2\2\u0119\u00fd\3\2\2\2\u0119")
        buf.write("\u0108\3\2\2\2\u0119\u010b\3\2\2\2\u0119\u010e\3\2\2\2")
        buf.write("\u0119\u0111\3\2\2\2\u0119\u0114\3\2\2\2\u011a\u011d\3")
        buf.write("\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\61")
        buf.write("\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\7(\2\2\u011f")
        buf.write("\u0120\5\60\31\2\u0120\u0121\7)\2\2\u0121\63\3\2\2\2\u0122")
        buf.write("\u0123\7 \2\2\u0123\u0125\7(\2\2\u0124\u0126\5\66\34\2")
        buf.write("\u0125\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3")
        buf.write("\2\2\2\u0127\u0128\7)\2\2\u0128\65\3\2\2\2\u0129\u012e")
        buf.write("\5\60\31\2\u012a\u012b\7/\2\2\u012b\u012d\5\60\31\2\u012c")
        buf.write("\u012a\3\2\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2")
        buf.write("\u012e\u012f\3\2\2\2\u012f\67\3\2\2\2\u0130\u012e\3\2")
        buf.write("\2\2\u0131\u0132\5F$\2\u01329\3\2\2\2\u0133\u0134\7,\2")
        buf.write("\2\u0134\u0135\5<\37\2\u0135\u0136\7-\2\2\u0136;\3\2\2")
        buf.write("\2\u0137\u013c\58\35\2\u0138\u0139\7.\2\2\u0139\u013b")
        buf.write("\58\35\2\u013a\u0138\3\2\2\2\u013b\u013e\3\2\2\2\u013c")
        buf.write("\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d=\3\2\2\2\u013e")
        buf.write("\u013c\3\2\2\2\u013f\u0141\5:\36\2\u0140\u013f\3\2\2\2")
        buf.write("\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\7")
        buf.write(" \2\2\u0143\u0144\7\61\2\2\u0144\u0145\5\32\16\2\u0145")
        buf.write("?\3\2\2\2\u0146\u0148\5:\36\2\u0147\u0146\3\2\2\2\u0147")
        buf.write("\u0148\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\7 \2\2")
        buf.write("\u014a\u014b\7,\2\2\u014b\u014c\7-\2\2\u014c\u014d\7\61")
        buf.write("\2\2\u014d\u015a\5*\26\2\u014e\u0150\5:\36\2\u014f\u014e")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0155\7 \2\2\u0152\u0153\7,\2\2\u0153\u0154\7$\2\2\u0154")
        buf.write("\u0156\7-\2\2\u0155\u0152\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u0157\3\2\2\2\u0157\u0158\7\61\2\2\u0158\u015a")
        buf.write("\5\30\r\2\u0159\u0147\3\2\2\2\u0159\u014f\3\2\2\2\u015a")
        buf.write("A\3\2\2\2\u015b\u015c\7(\2\2\u015c\u015d\5\60\31\2\u015d")
        buf.write("\u015e\7)\2\2\u015e\u0162\3\2\2\2\u015f\u0162\5D#\2\u0160")
        buf.write("\u0162\7 \2\2\u0161\u015b\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0160\3\2\2\2\u0162C\3\2\2\2\u0163\u0164\t\7\2")
        buf.write("\2\u0164E\3\2\2\2\u0165\u0166\t\b\2\2\u0166G\3\2\2\2\u0167")
        buf.write("\u0168\7&\2\2\u0168\u016a\7\33\2\2\u0169\u0167\3\2\2\2")
        buf.write("\u0169\u016a\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\7")
        buf.write(" \2\2\u016cI\3\2\2\2\u016d\u016e\7%\2\2\u016eK\3\2\2\2")
        buf.write("\u016f\u0170\7\'\2\2\u0170M\3\2\2\2#V^gnt{\u0081\u0088")
        buf.write("\u0091\u0095\u009a\u00a6\u00af\u00b3\u00bc\u00c3\u00d4")
        buf.write("\u00dc\u00e4\u00f2\u0105\u0119\u011b\u0125\u012e\u013c")
        buf.write("\u0140\u0147\u014f\u0155\u0159\u0161\u0169")
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
    RULE_materialAssignmentOperations = 11
    RULE_numericAssignmentOperations = 12
    RULE_statements = 13
    RULE_ifStatement = 14
    RULE_whileStatement = 15
    RULE_repeat = 16
    RULE_mix = 17
    RULE_detect = 18
    RULE_heat = 19
    RULE_split = 20
    RULE_dispense = 21
    RULE_dispose = 22
    RULE_expression = 23
    RULE_parExpression = 24
    RULE_methodCall = 25
    RULE_expressionList = 26
    RULE_typeType = 27
    RULE_unionType = 28
    RULE_typesList = 29
    RULE_numericDeclaration = 30
    RULE_materialDeclaration = 31
    RULE_primary = 32
    RULE_literal = 33
    RULE_primitiveType = 34
    RULE_volumeIdentifier = 35
    RULE_timeIdentifier = 36
    RULE_temperatureIdentifier = 37

    ruleNames =  [ "program", "moduleDeclaration", "manifestDeclaration",
                   "stationaryDeclaration", "functionDeclaration", "formalParameters",
                   "formalParameterList", "formalParameter", "functionTyping",
                   "returnStatement", "blockStatement", "materialAssignmentOperations",
                   "numericAssignmentOperations", "statements", "ifStatement",
                   "whileStatement", "repeat", "mix", "detect", "heat",
                   "split", "dispense", "dispose", "expression", "parExpression",
                   "methodCall", "expressionList", "typeType", "unionType",
                   "typesList", "numericDeclaration", "materialDeclaration",
                   "primary", "literal", "primitiveType", "volumeIdentifier",
                   "timeIdentifier", "temperatureIdentifier" ]

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.moduleDeclaration()
            self.state = 77
            self.stationaryDeclaration()
            self.state = 78
            self.manifestDeclaration()
            self.state = 79
            self.match(BSParser.FUNCTIONS)
            self.state = 80
            self.match(BSParser.COLON)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.FUNCTION:
                self.state = 81
                self.functionDeclaration()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self.match(BSParser.INSTRUCTIONS)
            self.state = 88
            self.match(BSParser.COLON)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 89
                self.statements()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModuleDeclaration" ):
                return visitor.visitModuleDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def moduleDeclaration(self):

        localctx = BSParser.ModuleDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_moduleDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.MODULE:
                self.state = 97
                self.match(BSParser.MODULE)
                self.state = 98
                self.match(BSParser.IDENTIFIER)
                self.state = 103
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManifestDeclaration" ):
                return visitor.visitManifestDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def manifestDeclaration(self):

        localctx = BSParser.ManifestDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_manifestDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.match(BSParser.MANIFEST)
                self.state = 105
                self.match(BSParser.IDENTIFIER)
                self.state = 108
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStationaryDeclaration" ):
                return visitor.visitStationaryDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def stationaryDeclaration(self):

        localctx = BSParser.StationaryDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stationaryDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.STATIONARY:
                self.state = 110
                self.match(BSParser.STATIONARY)
                self.state = 111
                self.match(BSParser.IDENTIFIER)
                self.state = 116
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = BSParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(BSParser.FUNCTION)
            self.state = 118
            self.match(BSParser.IDENTIFIER)
            self.state = 119
            self.formalParameters()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.COLON:
                self.state = 120
                self.functionTyping()


            self.state = 123
            self.match(BSParser.LBRACE)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 124
                self.statements()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0)):
                    break

            self.state = 129
            self.returnStatement()
            self.state = 130
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameters" ):
                return visitor.visitFormalParameters(self)
            else:
                return visitor.visitChildren(self)




    def formalParameters(self):

        localctx = BSParser.FormalParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_formalParameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(BSParser.LPAREN)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.IDENTIFIER or _la==BSParser.LBRACKET:
                self.state = 133
                self.formalParameterList()


            self.state = 136
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameterList" ):
                return visitor.visitFormalParameterList(self)
            else:
                return visitor.visitChildren(self)




    def formalParameterList(self):

        localctx = BSParser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.formalParameter()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 139
                self.match(BSParser.COMMA)
                self.state = 140
                self.formalParameter()
                self.state = 145
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameter" ):
                return visitor.visitFormalParameter(self)
            else:
                return visitor.visitChildren(self)




    def formalParameter(self):

        localctx = BSParser.FormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_formalParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 146
                self.unionType()


            self.state = 149
            self.match(BSParser.IDENTIFIER)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 150
                self.match(BSParser.LBRACKET)
                self.state = 151
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionTyping" ):
                return visitor.visitFunctionTyping(self)
            else:
                return visitor.visitChildren(self)




    def functionTyping(self):

        localctx = BSParser.FunctionTypingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionTyping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(BSParser.COLON)
            self.state = 155
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = BSParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(BSParser.RETURN)
            self.state = 158
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = BSParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(BSParser.LBRACE)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 161
                self.statements()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(BSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MaterialAssignmentOperationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mix(self):
            return self.getTypedRuleContext(BSParser.MixContext,0)


        def dispense(self):
            return self.getTypedRuleContext(BSParser.DispenseContext,0)


        def split(self):
            return self.getTypedRuleContext(BSParser.SplitContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(BSParser.MethodCallContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_materialAssignmentOperations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaterialAssignmentOperations" ):
                listener.enterMaterialAssignmentOperations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaterialAssignmentOperations" ):
                listener.exitMaterialAssignmentOperations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaterialAssignmentOperations" ):
                return visitor.visitMaterialAssignmentOperations(self)
            else:
                return visitor.visitChildren(self)




    def materialAssignmentOperations(self):

        localctx = BSParser.MaterialAssignmentOperationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_materialAssignmentOperations)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.MIX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.mix()
                pass
            elif token in [BSParser.DISPENSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.dispense()
                pass
            elif token in [BSParser.SPLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.split()
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 172
                self.methodCall()
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

    class NumericAssignmentOperationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BSParser.ExpressionContext,0)


        def detect(self):
            return self.getTypedRuleContext(BSParser.DetectContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_numericAssignmentOperations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericAssignmentOperations" ):
                listener.enterNumericAssignmentOperations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericAssignmentOperations" ):
                listener.exitNumericAssignmentOperations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericAssignmentOperations" ):
                return visitor.visitNumericAssignmentOperations(self)
            else:
                return visitor.visitChildren(self)




    def numericAssignmentOperations(self):

        localctx = BSParser.NumericAssignmentOperationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_numericAssignmentOperations)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.IDENTIFIER, BSParser.STRING_LITERAL, BSParser.BOOL_LITERAL, BSParser.FLOAT_LITERAL, BSParser.INTEGER_LITERAL, BSParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.expression(0)
                pass
            elif token in [BSParser.DETECT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.detect()
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

    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(BSParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(BSParser.WhileStatementContext,0)


        def materialDeclaration(self):
            return self.getTypedRuleContext(BSParser.MaterialDeclarationContext,0)


        def numericDeclaration(self):
            return self.getTypedRuleContext(BSParser.NumericDeclarationContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = BSParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statements)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.materialDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                self.numericDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 183
                self.repeat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 184
                self.heat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 185
                self.dispose()
                pass


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = BSParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(BSParser.IF)
            self.state = 189
            self.parExpression()
            self.state = 190
            self.blockStatement()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ELSE:
                self.state = 191
                self.match(BSParser.ELSE)
                self.state = 192
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = BSParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(BSParser.WHILE)
            self.state = 196
            self.parExpression()
            self.state = 197
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat" ):
                return visitor.visitRepeat(self)
            else:
                return visitor.visitChildren(self)




    def repeat(self):

        localctx = BSParser.RepeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_repeat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(BSParser.REPEAT)
            self.state = 200
            _la = self._input.LA(1)
            if not(_la==BSParser.IDENTIFIER or _la==BSParser.INTEGER_LITERAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 201
            self.match(BSParser.TIMES)
            self.state = 202
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMix" ):
                return visitor.visitMix(self)
            else:
                return visitor.visitChildren(self)




    def mix(self):

        localctx = BSParser.MixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_mix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(BSParser.MIX)
            self.state = 205
            self.volumeIdentifier()
            self.state = 206
            self.match(BSParser.WITH)
            self.state = 207
            self.volumeIdentifier()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 208
                self.match(BSParser.FOR)
                self.state = 209
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetect" ):
                return visitor.visitDetect(self)
            else:
                return visitor.visitChildren(self)




    def detect(self):

        localctx = BSParser.DetectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_detect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(BSParser.DETECT)
            self.state = 213
            self.match(BSParser.IDENTIFIER)
            self.state = 214
            self.match(BSParser.ON)
            self.state = 215
            self.match(BSParser.IDENTIFIER)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 216
                self.match(BSParser.FOR)
                self.state = 217
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeat" ):
                return visitor.visitHeat(self)
            else:
                return visitor.visitChildren(self)




    def heat(self):

        localctx = BSParser.HeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_heat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(BSParser.HEAT)
            self.state = 221
            self.match(BSParser.IDENTIFIER)
            self.state = 222
            self.match(BSParser.AT)
            self.state = 223
            self.temperatureIdentifier()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 224
                self.match(BSParser.FOR)
                self.state = 225
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSplit" ):
                return visitor.visitSplit(self)
            else:
                return visitor.visitChildren(self)




    def split(self):

        localctx = BSParser.SplitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_split)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(BSParser.SPLIT)
            self.state = 229
            self.match(BSParser.IDENTIFIER)
            self.state = 230
            self.match(BSParser.INTO)
            self.state = 231
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDispense" ):
                return visitor.visitDispense(self)
            else:
                return visitor.visitChildren(self)




    def dispense(self):

        localctx = BSParser.DispenseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_dispense)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(BSParser.DISPENSE)
            self.state = 234
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDispose" ):
                return visitor.visitDispose(self)
            else:
                return visitor.visitChildren(self)




    def dispose(self):

        localctx = BSParser.DisposeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_dispose)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.DRAIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(BSParser.DRAIN)
                self.state = 237
                self.match(BSParser.IDENTIFIER)
                pass
            elif token in [BSParser.DISPOSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.match(BSParser.DISPOSE)
                self.state = 239
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BSParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.primary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 279
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 245
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 246
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BSParser.MULTIPLY - 64)) | (1 << (BSParser.DIVIDE - 64)) | (1 << (BSParser.MOD - 64)))) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 247
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 248
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 249
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BSParser.ADDITION or _la==BSParser.SUBTRACT):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 250
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 251
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 259
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                        if la_ == 1:
                            self.state = 252
                            self.match(BSParser.LT)
                            self.state = 253
                            self.match(BSParser.LT)
                            pass

                        elif la_ == 2:
                            self.state = 254
                            self.match(BSParser.GT)
                            self.state = 255
                            self.match(BSParser.GT)
                            self.state = 256
                            self.match(BSParser.GT)
                            pass

                        elif la_ == 3:
                            self.state = 257
                            self.match(BSParser.GT)
                            self.state = 258
                            self.match(BSParser.GT)
                            pass


                        self.state = 261
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 262
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 263
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.GT) | (1 << BSParser.LT) | (1 << BSParser.LTE) | (1 << BSParser.GTE))) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 264
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 265
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 266
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BSParser.EQUALITY or _la==BSParser.NOTEQUAL):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 267
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 268
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 269
                        localctx.bop = self.match(BSParser.AND)
                        self.state = 270
                        self.expression(3)
                        pass

                    elif la_ == 7:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 271
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 272
                        localctx.bop = self.match(BSParser.OR)
                        self.state = 273
                        self.expression(2)
                        pass

                    elif la_ == 8:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 274
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 275
                        self.match(BSParser.LBRACKET)
                        self.state = 276
                        self.expression(0)
                        self.state = 277
                        self.match(BSParser.RBRACKET)
                        pass


                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParExpression" ):
                return visitor.visitParExpression(self)
            else:
                return visitor.visitChildren(self)




    def parExpression(self):

        localctx = BSParser.ParExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_parExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(BSParser.LPAREN)
            self.state = 285
            self.expression(0)
            self.state = 286
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = BSParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(BSParser.IDENTIFIER)
            self.state = 289
            self.match(BSParser.LPAREN)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IDENTIFIER) | (1 << BSParser.STRING_LITERAL) | (1 << BSParser.BOOL_LITERAL) | (1 << BSParser.FLOAT_LITERAL) | (1 << BSParser.INTEGER_LITERAL) | (1 << BSParser.LPAREN))) != 0):
                self.state = 290
                self.expressionList()


            self.state = 293
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = BSParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.expression(0)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 296
                self.match(BSParser.COMMA)
                self.state = 297
                self.expression(0)
                self.state = 302
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeType" ):
                return visitor.visitTypeType(self)
            else:
                return visitor.visitChildren(self)




    def typeType(self):

        localctx = BSParser.TypeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_typeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnionType" ):
                return visitor.visitUnionType(self)
            else:
                return visitor.visitChildren(self)




    def unionType(self):

        localctx = BSParser.UnionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_unionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(BSParser.LBRACKET)
            self.state = 306
            self.typesList()
            self.state = 307
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypesList" ):
                return visitor.visitTypesList(self)
            else:
                return visitor.visitChildren(self)




    def typesList(self):

        localctx = BSParser.TypesListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_typesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.typeType()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.SEMICOLON:
                self.state = 310
                self.match(BSParser.SEMICOLON)
                self.state = 311
                self.typeType()
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(BSParser.ASSIGN, 0)

        def numericAssignmentOperations(self):
            return self.getTypedRuleContext(BSParser.NumericAssignmentOperationsContext,0)


        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_numericDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericDeclaration" ):
                listener.enterNumericDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericDeclaration" ):
                listener.exitNumericDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericDeclaration" ):
                return visitor.visitNumericDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def numericDeclaration(self):

        localctx = BSParser.NumericDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_numericDeclaration)
        self._la = 0 # Token type
        try:
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
            self.numericAssignmentOperations()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MaterialDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def ASSIGN(self):
            return self.getToken(BSParser.ASSIGN, 0)

        def split(self):
            return self.getTypedRuleContext(BSParser.SplitContext,0)


        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def materialAssignmentOperations(self):
            return self.getTypedRuleContext(BSParser.MaterialAssignmentOperationsContext,0)


        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def getRuleIndex(self):
            return BSParser.RULE_materialDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaterialDeclaration" ):
                listener.enterMaterialDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaterialDeclaration" ):
                listener.exitMaterialDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaterialDeclaration" ):
                return visitor.visitMaterialDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def materialDeclaration(self):

        localctx = BSParser.MaterialDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_materialDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.LBRACKET:
                    self.state = 324
                    self.unionType()


                self.state = 327
                self.match(BSParser.IDENTIFIER)
                self.state = 328
                self.match(BSParser.LBRACKET)
                self.state = 329
                self.match(BSParser.RBRACKET)
                self.state = 330
                self.match(BSParser.ASSIGN)
                self.state = 331
                self.split()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.LBRACKET:
                    self.state = 332
                    self.unionType()


                self.state = 335
                self.match(BSParser.IDENTIFIER)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.LBRACKET:
                    self.state = 336
                    self.match(BSParser.LBRACKET)
                    self.state = 337
                    self.match(BSParser.INTEGER_LITERAL)
                    self.state = 338
                    self.match(BSParser.RBRACKET)


                self.state = 341
                self.match(BSParser.ASSIGN)
                self.state = 342
                self.materialAssignmentOperations()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = BSParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_primary)
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(BSParser.LPAREN)
                self.state = 346
                self.expression(0)
                self.state = 347
                self.match(BSParser.RPAREN)
                pass
            elif token in [BSParser.STRING_LITERAL, BSParser.BOOL_LITERAL, BSParser.FLOAT_LITERAL, BSParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.literal()
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BSParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = BSParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVolumeIdentifier" ):
                return visitor.visitVolumeIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def volumeIdentifier(self):

        localctx = BSParser.VolumeIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_volumeIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.VOLUME_NUMBER:
                self.state = 357
                self.match(BSParser.VOLUME_NUMBER)
                self.state = 358
                self.match(BSParser.OF)


            self.state = 361
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimeIdentifier" ):
                return visitor.visitTimeIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def timeIdentifier(self):

        localctx = BSParser.TimeIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_timeIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemperatureIdentifier" ):
                return visitor.visitTemperatureIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def temperatureIdentifier(self):

        localctx = BSParser.TemperatureIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_temperatureIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
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
        self._predicates[23] = self.expression_sempred
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





