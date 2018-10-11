# Generated from /bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys

# parser/listener/visitor header section */
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3`")
        buf.write("\u018d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\3\2\3\2\3\2\3\2\3\2\7\2W\n\2\f\2\16")
        buf.write("\2Z\13\2\3\2\3\2\3\2\7\2_\n\2\f\2\16\2b\13\2\3\2\3\2\3")
        buf.write("\3\3\3\7\3h\n\3\f\3\16\3k\13\3\3\4\3\4\6\4o\n\4\r\4\16")
        buf.write("\4p\3\5\3\5\7\5u\n\5\f\5\16\5x\13\5\3\6\3\6\3\6\3\6\5")
        buf.write("\6~\n\6\3\6\3\6\7\6\u0082\n\6\f\6\16\6\u0085\13\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\5\7\u008c\n\7\3\7\3\7\3\b\3\b\3\b\7\b")
        buf.write("\u0093\n\b\f\b\16\b\u0096\13\b\3\t\5\t\u0099\n\t\3\t\3")
        buf.write("\t\3\t\5\t\u009e\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00a9\n\13\3\f\3\f\7\f\u00ad\n\f\f\f\16")
        buf.write("\f\u00b0\13\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00b8\n\r\3")
        buf.write("\16\3\16\3\16\5\16\u00bd\n\16\3\17\3\17\3\17\5\17\u00c2")
        buf.write("\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00cb\n")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\5\21\u00d2\n\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u00e3\n\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u00eb\n\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u00f3\n\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u0101\n\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u0114\n\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\7\32\u0128\n\32\f\32\16\32\u012b\13\32\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\5\34\u0134\n\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\7\35\u013b\n\35\f\35\16\35\u013e\13")
        buf.write("\35\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \7 \u0149\n")
        buf.write(" \f \16 \u014c\13 \3!\5!\u014f\n!\3!\3!\3!\3!\3\"\5\"")
        buf.write("\u0156\n\"\3\"\3\"\3\"\7\"\u015b\n\"\f\"\16\"\u015e\13")
        buf.write("\"\3\"\3\"\3\"\5\"\u0163\n\"\3\"\3\"\3\"\6\"\u0168\n\"")
        buf.write("\r\"\16\"\u0169\3\"\3\"\3\"\3\"\5\"\u0170\n\"\3\"\3\"")
        buf.write("\3\"\5\"\u0175\n\"\3#\3#\3#\3#\3#\3#\5#\u017d\n#\3$\3")
        buf.write("$\3%\3%\3&\3&\5&\u0185\n&\3&\3&\3\'\3\'\3(\3(\3(\2\3\62")
        buf.write(")\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLN\2\t\4\2  $$\4\2BCGG\3\2@A\4\2\62\63")
        buf.write("9:\4\288;;\3\2!$\3\2\34\37\2\u019d\2P\3\2\2\2\4i\3\2\2")
        buf.write("\2\6n\3\2\2\2\bv\3\2\2\2\ny\3\2\2\2\f\u0089\3\2\2\2\16")
        buf.write("\u008f\3\2\2\2\20\u0098\3\2\2\2\22\u009f\3\2\2\2\24\u00a8")
        buf.write("\3\2\2\2\26\u00aa\3\2\2\2\30\u00b7\3\2\2\2\32\u00bc\3")
        buf.write("\2\2\2\34\u00c1\3\2\2\2\36\u00ca\3\2\2\2 \u00cc\3\2\2")
        buf.write("\2\"\u00d3\3\2\2\2$\u00d7\3\2\2\2&\u00dc\3\2\2\2(\u00e4")
        buf.write("\3\2\2\2*\u00ec\3\2\2\2,\u00f4\3\2\2\2.\u00f9\3\2\2\2")
        buf.write("\60\u0100\3\2\2\2\62\u0102\3\2\2\2\64\u012c\3\2\2\2\66")
        buf.write("\u0130\3\2\2\28\u0137\3\2\2\2:\u013f\3\2\2\2<\u0141\3")
        buf.write("\2\2\2>\u0145\3\2\2\2@\u014e\3\2\2\2B\u0174\3\2\2\2D\u017c")
        buf.write("\3\2\2\2F\u017e\3\2\2\2H\u0180\3\2\2\2J\u0184\3\2\2\2")
        buf.write("L\u0188\3\2\2\2N\u018a\3\2\2\2PQ\5\4\3\2QR\5\b\5\2RS\5")
        buf.write("\6\4\2ST\7\f\2\2TX\7\67\2\2UW\5\n\6\2VU\3\2\2\2WZ\3\2")
        buf.write("\2\2XV\3\2\2\2XY\3\2\2\2Y[\3\2\2\2ZX\3\2\2\2[\\\7\r\2")
        buf.write("\2\\`\7\67\2\2]_\5\36\20\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2")
        buf.write("\2`a\3\2\2\2ac\3\2\2\2b`\3\2\2\2cd\7\2\2\3d\3\3\2\2\2")
        buf.write("ef\7\n\2\2fh\7 \2\2ge\3\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3")
        buf.write("\2\2\2j\5\3\2\2\2ki\3\2\2\2lm\7\t\2\2mo\7 \2\2nl\3\2\2")
        buf.write("\2op\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\7\3\2\2\2rs\7\13\2\2")
        buf.write("su\7 \2\2tr\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\t\3")
        buf.write("\2\2\2xv\3\2\2\2yz\7\7\2\2z{\7 \2\2{}\5\f\7\2|~\5\22\n")
        buf.write("\2}|\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0083\7*\2\2\u0080")
        buf.write("\u0082\5\36\20\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2")
        buf.write("\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0086")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087\5\24\13\2\u0087")
        buf.write("\u0088\7+\2\2\u0088\13\3\2\2\2\u0089\u008b\7(\2\2\u008a")
        buf.write("\u008c\5\16\b\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2")
        buf.write("\2\u008c\u008d\3\2\2\2\u008d\u008e\7)\2\2\u008e\r\3\2")
        buf.write("\2\2\u008f\u0094\5\20\t\2\u0090\u0091\7/\2\2\u0091\u0093")
        buf.write("\5\20\t\2\u0092\u0090\3\2\2\2\u0093\u0096\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\17\3\2\2\2\u0096")
        buf.write("\u0094\3\2\2\2\u0097\u0099\5<\37\2\u0098\u0097\3\2\2\2")
        buf.write("\u0098\u0099\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009d\7")
        buf.write(" \2\2\u009b\u009c\7,\2\2\u009c\u009e\7-\2\2\u009d\u009b")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\21\3\2\2\2\u009f\u00a0")
        buf.write("\7\67\2\2\u00a0\u00a1\5<\37\2\u00a1\23\3\2\2\2\u00a2\u00a3")
        buf.write("\7\b\2\2\u00a3\u00a9\7 \2\2\u00a4\u00a5\7\b\2\2\u00a5")
        buf.write("\u00a9\5F$\2\u00a6\u00a7\7\b\2\2\u00a7\u00a9\5\66\34\2")
        buf.write("\u00a8\u00a2\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a8\u00a6\3")
        buf.write("\2\2\2\u00a9\25\3\2\2\2\u00aa\u00ae\7*\2\2\u00ab\u00ad")
        buf.write("\5\36\20\2\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b1\u00b2\7+\2\2\u00b2\27\3\2\2")
        buf.write("\2\u00b3\u00b8\5&\24\2\u00b4\u00b8\5.\30\2\u00b5\u00b8")
        buf.write("\5,\27\2\u00b6\u00b8\5\66\34\2\u00b7\u00b3\3\2\2\2\u00b7")
        buf.write("\u00b4\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2")
        buf.write("\u00b8\31\3\2\2\2\u00b9\u00bd\5.\30\2\u00ba\u00bd\5,\27")
        buf.write("\2\u00bb\u00bd\5\66\34\2\u00bc\u00b9\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\33\3\2\2\2\u00be\u00c2")
        buf.write("\5\62\32\2\u00bf\u00c2\5(\25\2\u00c0\u00c2\5\66\34\2\u00c1")
        buf.write("\u00be\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2")
        buf.write("\u00c2\35\3\2\2\2\u00c3\u00cb\5 \21\2\u00c4\u00cb\5\"")
        buf.write("\22\2\u00c5\u00cb\5B\"\2\u00c6\u00cb\5@!\2\u00c7\u00cb")
        buf.write("\5$\23\2\u00c8\u00cb\5*\26\2\u00c9\u00cb\5\60\31\2\u00ca")
        buf.write("\u00c3\3\2\2\2\u00ca\u00c4\3\2\2\2\u00ca\u00c5\3\2\2\2")
        buf.write("\u00ca\u00c6\3\2\2\2\u00ca\u00c7\3\2\2\2\u00ca\u00c8\3")
        buf.write("\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\37\3\2\2\2\u00cc\u00cd")
        buf.write("\7\3\2\2\u00cd\u00ce\5\64\33\2\u00ce\u00d1\5\26\f\2\u00cf")
        buf.write("\u00d0\7\4\2\2\u00d0\u00d2\5\26\f\2\u00d1\u00cf\3\2\2")
        buf.write("\2\u00d1\u00d2\3\2\2\2\u00d2!\3\2\2\2\u00d3\u00d4\7\6")
        buf.write("\2\2\u00d4\u00d5\5\64\33\2\u00d5\u00d6\5\26\f\2\u00d6")
        buf.write("#\3\2\2\2\u00d7\u00d8\7\5\2\2\u00d8\u00d9\t\2\2\2\u00d9")
        buf.write("\u00da\7\31\2\2\u00da\u00db\5\26\f\2\u00db%\3\2\2\2\u00dc")
        buf.write("\u00dd\7\17\2\2\u00dd\u00de\5J&\2\u00de\u00df\7\26\2\2")
        buf.write("\u00df\u00e2\5J&\2\u00e0\u00e1\7\27\2\2\u00e1\u00e3\5")
        buf.write("L\'\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\'")
        buf.write("\3\2\2\2\u00e4\u00e5\7\16\2\2\u00e5\u00e6\7 \2\2\u00e6")
        buf.write("\u00e7\7\32\2\2\u00e7\u00ea\7 \2\2\u00e8\u00e9\7\27\2")
        buf.write("\2\u00e9\u00eb\5L\'\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb")
        buf.write("\3\2\2\2\u00eb)\3\2\2\2\u00ec\u00ed\7\21\2\2\u00ed\u00ee")
        buf.write("\7 \2\2\u00ee\u00ef\7\25\2\2\u00ef\u00f2\5N(\2\u00f0\u00f1")
        buf.write("\7\27\2\2\u00f1\u00f3\5L\'\2\u00f2\u00f0\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3+\3\2\2\2\u00f4\u00f5\7\20\2\2\u00f5")
        buf.write("\u00f6\7 \2\2\u00f6\u00f7\7\30\2\2\u00f7\u00f8\7$\2\2")
        buf.write("\u00f8-\3\2\2\2\u00f9\u00fa\7\23\2\2\u00fa\u00fb\7 \2")
        buf.write("\2\u00fb/\3\2\2\2\u00fc\u00fd\7\22\2\2\u00fd\u0101\7 ")
        buf.write("\2\2\u00fe\u00ff\7\24\2\2\u00ff\u0101\7 \2\2\u0100\u00fc")
        buf.write("\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\61\3\2\2\2\u0102\u0103")
        buf.write("\b\32\1\2\u0103\u0104\5D#\2\u0104\u0129\3\2\2\2\u0105")
        buf.write("\u0106\f\t\2\2\u0106\u0107\t\3\2\2\u0107\u0128\5\62\32")
        buf.write("\n\u0108\u0109\f\b\2\2\u0109\u010a\t\4\2\2\u010a\u0128")
        buf.write("\5\62\32\t\u010b\u0113\f\7\2\2\u010c\u010d\7\63\2\2\u010d")
        buf.write("\u0114\7\63\2\2\u010e\u010f\7\62\2\2\u010f\u0110\7\62")
        buf.write("\2\2\u0110\u0114\7\62\2\2\u0111\u0112\7\62\2\2\u0112\u0114")
        buf.write("\7\62\2\2\u0113\u010c\3\2\2\2\u0113\u010e\3\2\2\2\u0113")
        buf.write("\u0111\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0128\5\62\32")
        buf.write("\b\u0116\u0117\f\6\2\2\u0117\u0118\t\5\2\2\u0118\u0128")
        buf.write("\5\62\32\7\u0119\u011a\f\5\2\2\u011a\u011b\t\6\2\2\u011b")
        buf.write("\u0128\5\62\32\6\u011c\u011d\f\4\2\2\u011d\u011e\7<\2")
        buf.write("\2\u011e\u0128\5\62\32\5\u011f\u0120\f\3\2\2\u0120\u0121")
        buf.write("\7=\2\2\u0121\u0128\5\62\32\4\u0122\u0123\f\n\2\2\u0123")
        buf.write("\u0124\7,\2\2\u0124\u0125\5\62\32\2\u0125\u0126\7-\2\2")
        buf.write("\u0126\u0128\3\2\2\2\u0127\u0105\3\2\2\2\u0127\u0108\3")
        buf.write("\2\2\2\u0127\u010b\3\2\2\2\u0127\u0116\3\2\2\2\u0127\u0119")
        buf.write("\3\2\2\2\u0127\u011c\3\2\2\2\u0127\u011f\3\2\2\2\u0127")
        buf.write("\u0122\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012a\63\3\2\2\2\u012b\u0129\3\2")
        buf.write("\2\2\u012c\u012d\7(\2\2\u012d\u012e\5\62\32\2\u012e\u012f")
        buf.write("\7)\2\2\u012f\65\3\2\2\2\u0130\u0131\7 \2\2\u0131\u0133")
        buf.write("\7(\2\2\u0132\u0134\58\35\2\u0133\u0132\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\7)\2\2")
        buf.write("\u0136\67\3\2\2\2\u0137\u013c\5\62\32\2\u0138\u0139\7")
        buf.write("/\2\2\u0139\u013b\5\62\32\2\u013a\u0138\3\2\2\2\u013b")
        buf.write("\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d9\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0140\5H%\2")
        buf.write("\u0140;\3\2\2\2\u0141\u0142\7,\2\2\u0142\u0143\5> \2\u0143")
        buf.write("\u0144\7-\2\2\u0144=\3\2\2\2\u0145\u014a\5:\36\2\u0146")
        buf.write("\u0147\7.\2\2\u0147\u0149\5:\36\2\u0148\u0146\3\2\2\2")
        buf.write("\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3")
        buf.write("\2\2\2\u014b?\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u014f")
        buf.write("\5<\37\2\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u0151\7 \2\2\u0151\u0152\7\61\2\2")
        buf.write("\u0152\u0153\5\34\17\2\u0153A\3\2\2\2\u0154\u0156\5<\37")
        buf.write("\2\u0155\u0154\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\u015c\7 \2\2\u0158\u0159\7/\2\2\u0159\u015b")
        buf.write("\7 \2\2\u015a\u0158\3\2\2\2\u015b\u015e\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015f\u0160\7\61\2\2\u0160\u0175")
        buf.write("\5,\27\2\u0161\u0163\5<\37\2\u0162\u0161\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\7 \2\2")
        buf.write("\u0165\u0167\7,\2\2\u0166\u0168\7$\2\2\u0167\u0166\3\2")
        buf.write("\2\2\u0168\u0169\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\7-\2\2\u016c")
        buf.write("\u016d\7\61\2\2\u016d\u0175\5,\27\2\u016e\u0170\5<\37")
        buf.write("\2\u016f\u016e\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171")
        buf.write("\3\2\2\2\u0171\u0172\7 \2\2\u0172\u0173\7\61\2\2\u0173")
        buf.write("\u0175\5\30\r\2\u0174\u0155\3\2\2\2\u0174\u0162\3\2\2")
        buf.write("\2\u0174\u016f\3\2\2\2\u0175C\3\2\2\2\u0176\u0177\7(\2")
        buf.write("\2\u0177\u0178\5\62\32\2\u0178\u0179\7)\2\2\u0179\u017d")
        buf.write("\3\2\2\2\u017a\u017d\5F$\2\u017b\u017d\7 \2\2\u017c\u0176")
        buf.write("\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017d")
        buf.write("E\3\2\2\2\u017e\u017f\t\7\2\2\u017fG\3\2\2\2\u0180\u0181")
        buf.write("\t\b\2\2\u0181I\3\2\2\2\u0182\u0183\7&\2\2\u0183\u0185")
        buf.write("\7\33\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186\u0187\7 \2\2\u0187K\3\2\2\2\u0188")
        buf.write("\u0189\7%\2\2\u0189M\3\2\2\2\u018a\u018b\7\'\2\2\u018b")
        buf.write("O\3\2\2\2\'X`ipv}\u0083\u008b\u0094\u0098\u009d\u00a8")
        buf.write("\u00ae\u00b7\u00bc\u00c1\u00ca\u00d1\u00e2\u00ea\u00f2")
        buf.write("\u0100\u0113\u0127\u0129\u0133\u013c\u014a\u014e\u0155")
        buf.write("\u015c\u0162\u0169\u016f\u0174\u017c\u0184")
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
    RULE_materialArrayAssignmentOperations = 12
    RULE_numericAssignmentOperations = 13
    RULE_statements = 14
    RULE_ifStatement = 15
    RULE_whileStatement = 16
    RULE_repeat = 17
    RULE_mix = 18
    RULE_detect = 19
    RULE_heat = 20
    RULE_split = 21
    RULE_dispense = 22
    RULE_dispose = 23
    RULE_expression = 24
    RULE_parExpression = 25
    RULE_methodCall = 26
    RULE_expressionList = 27
    RULE_typeType = 28
    RULE_unionType = 29
    RULE_typesList = 30
    RULE_numericDeclaration = 31
    RULE_materialDeclaration = 32
    RULE_primary = 33
    RULE_literal = 34
    RULE_primitiveType = 35
    RULE_volumeIdentifier = 36
    RULE_timeIdentifier = 37
    RULE_temperatureIdentifier = 38

    ruleNames =  [ "program", "moduleDeclaration", "manifestDeclaration",
                   "stationaryDeclaration", "functionDeclaration", "formalParameters",
                   "formalParameterList", "formalParameter", "functionTyping",
                   "returnStatement", "blockStatement", "materialAssignmentOperations",
                   "materialArrayAssignmentOperations", "numericAssignmentOperations",
                   "statements", "ifStatement", "whileStatement", "repeat",
                   "mix", "detect", "heat", "split", "dispense", "dispose",
                   "expression", "parExpression", "methodCall", "expressionList",
                   "typeType", "unionType", "typesList", "numericDeclaration",
                   "materialDeclaration", "primary", "literal", "primitiveType",
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
            self.state = 78
            self.moduleDeclaration()
            self.state = 79
            self.stationaryDeclaration()
            self.state = 80
            self.manifestDeclaration()
            self.state = 81
            self.match(BSParser.FUNCTIONS)
            self.state = 82
            self.match(BSParser.COLON)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.FUNCTION:
                self.state = 83
                self.functionDeclaration()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(BSParser.INSTRUCTIONS)
            self.state = 90
            self.match(BSParser.COLON)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 91
                self.statements()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
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
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.MODULE:
                self.state = 99
                self.match(BSParser.MODULE)
                self.state = 100
                self.match(BSParser.IDENTIFIER)
                self.state = 105
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
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.match(BSParser.MANIFEST)
                self.state = 107
                self.match(BSParser.IDENTIFIER)
                self.state = 110
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
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.STATIONARY:
                self.state = 112
                self.match(BSParser.STATIONARY)
                self.state = 113
                self.match(BSParser.IDENTIFIER)
                self.state = 118
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
            self.state = 119
            self.match(BSParser.FUNCTION)
            self.state = 120
            self.match(BSParser.IDENTIFIER)
            self.state = 121
            self.formalParameters()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.COLON:
                self.state = 122
                self.functionTyping()


            self.state = 125
            self.match(BSParser.LBRACE)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 126
                self.statements()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.returnStatement()
            self.state = 133
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
            self.state = 135
            self.match(BSParser.LPAREN)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.IDENTIFIER or _la==BSParser.LBRACKET:
                self.state = 136
                self.formalParameterList()


            self.state = 139
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
            self.state = 141
            self.formalParameter()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 142
                self.match(BSParser.COMMA)
                self.state = 143
                self.formalParameter()
                self.state = 148
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
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 149
                self.unionType()


            self.state = 152
            self.match(BSParser.IDENTIFIER)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 153
                self.match(BSParser.LBRACKET)
                self.state = 154
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
            self.state = 157
            self.match(BSParser.COLON)
            self.state = 158
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

        def literal(self):
            return self.getTypedRuleContext(BSParser.LiteralContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(BSParser.MethodCallContext,0)


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
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(BSParser.RETURN)
                self.state = 161
                self.match(BSParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(BSParser.RETURN)
                self.state = 163
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(BSParser.RETURN)
                self.state = 165
                self.methodCall()
                pass


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
            self.state = 168
            self.match(BSParser.LBRACE)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 169
                self.statements()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 175
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
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.MIX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.mix()
                pass
            elif token in [BSParser.DISPENSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.dispense()
                pass
            elif token in [BSParser.SPLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.split()
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
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

    class MaterialArrayAssignmentOperationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dispense(self):
            return self.getTypedRuleContext(BSParser.DispenseContext,0)


        def split(self):
            return self.getTypedRuleContext(BSParser.SplitContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(BSParser.MethodCallContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_materialArrayAssignmentOperations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaterialArrayAssignmentOperations" ):
                listener.enterMaterialArrayAssignmentOperations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaterialArrayAssignmentOperations" ):
                listener.exitMaterialArrayAssignmentOperations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaterialArrayAssignmentOperations" ):
                return visitor.visitMaterialArrayAssignmentOperations(self)
            else:
                return visitor.visitChildren(self)




    def materialArrayAssignmentOperations(self):

        localctx = BSParser.MaterialArrayAssignmentOperationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_materialArrayAssignmentOperations)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.DISPENSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.dispense()
                pass
            elif token in [BSParser.SPLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.split()
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
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


        def methodCall(self):
            return self.getTypedRuleContext(BSParser.MethodCallContext,0)


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
        self.enterRule(localctx, 26, self.RULE_numericAssignmentOperations)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.detect()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
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
        self.enterRule(localctx, 28, self.RULE_statements)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.materialDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.numericDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 197
                self.repeat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 198
                self.heat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 199
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
        self.enterRule(localctx, 30, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(BSParser.IF)
            self.state = 203
            self.parExpression()
            self.state = 204
            self.blockStatement()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ELSE:
                self.state = 205
                self.match(BSParser.ELSE)
                self.state = 206
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
        self.enterRule(localctx, 32, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(BSParser.WHILE)
            self.state = 210
            self.parExpression()
            self.state = 211
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
        self.enterRule(localctx, 34, self.RULE_repeat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(BSParser.REPEAT)
            self.state = 214
            _la = self._input.LA(1)
            if not(_la==BSParser.IDENTIFIER or _la==BSParser.INTEGER_LITERAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 215
            self.match(BSParser.TIMES)
            self.state = 216
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
        self.enterRule(localctx, 36, self.RULE_mix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(BSParser.MIX)
            self.state = 219
            self.volumeIdentifier()
            self.state = 220
            self.match(BSParser.WITH)
            self.state = 221
            self.volumeIdentifier()
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 222
                self.match(BSParser.FOR)
                self.state = 223
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
        self.enterRule(localctx, 38, self.RULE_detect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(BSParser.DETECT)
            self.state = 227
            self.match(BSParser.IDENTIFIER)
            self.state = 228
            self.match(BSParser.ON)
            self.state = 229
            self.match(BSParser.IDENTIFIER)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 230
                self.match(BSParser.FOR)
                self.state = 231
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
        self.enterRule(localctx, 40, self.RULE_heat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(BSParser.HEAT)
            self.state = 235
            self.match(BSParser.IDENTIFIER)
            self.state = 236
            self.match(BSParser.AT)
            self.state = 237
            self.temperatureIdentifier()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 238
                self.match(BSParser.FOR)
                self.state = 239
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
        self.enterRule(localctx, 42, self.RULE_split)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(BSParser.SPLIT)
            self.state = 243
            self.match(BSParser.IDENTIFIER)
            self.state = 244
            self.match(BSParser.INTO)
            self.state = 245
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
        self.enterRule(localctx, 44, self.RULE_dispense)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(BSParser.DISPENSE)
            self.state = 248
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
        self.enterRule(localctx, 46, self.RULE_dispose)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.DRAIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(BSParser.DRAIN)
                self.state = 251
                self.match(BSParser.IDENTIFIER)
                pass
            elif token in [BSParser.DISPOSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.match(BSParser.DISPOSE)
                self.state = 253
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.primary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 293
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 259
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 260
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BSParser.MULTIPLY - 64)) | (1 << (BSParser.DIVIDE - 64)) | (1 << (BSParser.MOD - 64)))) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 261
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 262
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 263
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BSParser.ADDITION or _la==BSParser.SUBTRACT):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 264
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 265
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 273
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                        if la_ == 1:
                            self.state = 266
                            self.match(BSParser.LT)
                            self.state = 267
                            self.match(BSParser.LT)
                            pass

                        elif la_ == 2:
                            self.state = 268
                            self.match(BSParser.GT)
                            self.state = 269
                            self.match(BSParser.GT)
                            self.state = 270
                            self.match(BSParser.GT)
                            pass

                        elif la_ == 3:
                            self.state = 271
                            self.match(BSParser.GT)
                            self.state = 272
                            self.match(BSParser.GT)
                            pass


                        self.state = 275
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 276
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 277
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.GT) | (1 << BSParser.LT) | (1 << BSParser.LTE) | (1 << BSParser.GTE))) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 278
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 279
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 280
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BSParser.EQUALITY or _la==BSParser.NOTEQUAL):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 281
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 282
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 283
                        localctx.bop = self.match(BSParser.AND)
                        self.state = 284
                        self.expression(3)
                        pass

                    elif la_ == 7:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 285
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 286
                        localctx.bop = self.match(BSParser.OR)
                        self.state = 287
                        self.expression(2)
                        pass

                    elif la_ == 8:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 288
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 289
                        self.match(BSParser.LBRACKET)
                        self.state = 290
                        self.expression(0)
                        self.state = 291
                        self.match(BSParser.RBRACKET)
                        pass


                self.state = 297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        self.enterRule(localctx, 50, self.RULE_parExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(BSParser.LPAREN)
            self.state = 299
            self.expression(0)
            self.state = 300
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
        self.enterRule(localctx, 52, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(BSParser.IDENTIFIER)
            self.state = 303
            self.match(BSParser.LPAREN)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IDENTIFIER) | (1 << BSParser.STRING_LITERAL) | (1 << BSParser.BOOL_LITERAL) | (1 << BSParser.FLOAT_LITERAL) | (1 << BSParser.INTEGER_LITERAL) | (1 << BSParser.LPAREN))) != 0):
                self.state = 304
                self.expressionList()


            self.state = 307
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
        self.enterRule(localctx, 54, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.expression(0)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 310
                self.match(BSParser.COMMA)
                self.state = 311
                self.expression(0)
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
        self.enterRule(localctx, 56, self.RULE_typeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
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
        self.enterRule(localctx, 58, self.RULE_unionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(BSParser.LBRACKET)
            self.state = 320
            self.typesList()
            self.state = 321
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
        self.enterRule(localctx, 60, self.RULE_typesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.typeType()
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.SEMICOLON:
                self.state = 324
                self.match(BSParser.SEMICOLON)
                self.state = 325
                self.typeType()
                self.state = 330
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
        self.enterRule(localctx, 62, self.RULE_numericDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 331
                self.unionType()


            self.state = 334
            self.match(BSParser.IDENTIFIER)
            self.state = 335
            self.match(BSParser.ASSIGN)
            self.state = 336
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.IDENTIFIER)
            else:
                return self.getToken(BSParser.IDENTIFIER, i)

        def ASSIGN(self):
            return self.getToken(BSParser.ASSIGN, 0)

        def split(self):
            return self.getTypedRuleContext(BSParser.SplitContext,0)


        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.COMMA)
            else:
                return self.getToken(BSParser.COMMA, i)

        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.INTEGER_LITERAL)
            else:
                return self.getToken(BSParser.INTEGER_LITERAL, i)

        def materialAssignmentOperations(self):
            return self.getTypedRuleContext(BSParser.MaterialAssignmentOperationsContext,0)


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
        self.enterRule(localctx, 64, self.RULE_materialDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.LBRACKET:
                    self.state = 338
                    self.unionType()


                self.state = 341
                self.match(BSParser.IDENTIFIER)
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BSParser.COMMA:
                    self.state = 342
                    self.match(BSParser.COMMA)
                    self.state = 343
                    self.match(BSParser.IDENTIFIER)
                    self.state = 348
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 349
                self.match(BSParser.ASSIGN)
                self.state = 350
                self.split()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.LBRACKET:
                    self.state = 351
                    self.unionType()


                self.state = 354
                self.match(BSParser.IDENTIFIER)
                self.state = 355
                self.match(BSParser.LBRACKET)
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 356
                    self.match(BSParser.INTEGER_LITERAL)
                    self.state = 359
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BSParser.INTEGER_LITERAL):
                        break

                self.state = 361
                self.match(BSParser.RBRACKET)
                self.state = 362
                self.match(BSParser.ASSIGN)
                self.state = 363
                self.split()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.LBRACKET:
                    self.state = 364
                    self.unionType()


                self.state = 367
                self.match(BSParser.IDENTIFIER)
                self.state = 368
                self.match(BSParser.ASSIGN)
                self.state = 369
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
        self.enterRule(localctx, 66, self.RULE_primary)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(BSParser.LPAREN)
                self.state = 373
                self.expression(0)
                self.state = 374
                self.match(BSParser.RPAREN)
                pass
            elif token in [BSParser.STRING_LITERAL, BSParser.BOOL_LITERAL, BSParser.FLOAT_LITERAL, BSParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.literal()
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
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
        self.enterRule(localctx, 68, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
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
        self.enterRule(localctx, 70, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
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
        self.enterRule(localctx, 72, self.RULE_volumeIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.VOLUME_NUMBER:
                self.state = 384
                self.match(BSParser.VOLUME_NUMBER)
                self.state = 385
                self.match(BSParser.OF)


            self.state = 388
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
        self.enterRule(localctx, 74, self.RULE_timeIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
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
        self.enterRule(localctx, 76, self.RULE_temperatureIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
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
        self._predicates[24] = self.expression_sempred
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





