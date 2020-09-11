# Generated from /bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

# /* parser/listener/visitor header section */

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00af")
        buf.write("\u019c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\6\2^\n\2\r\2\16\2_\3\2\5\2c\n\2\3\2\3\2\3\2\7\2h\n")
        buf.write("\2\f\2\16\2k\13\2\3\2\3\2\3\3\3\3\3\3\5\3r\n\3\3\4\3\4")
        buf.write("\3\4\3\5\5\5x\n\5\3\5\3\5\3\5\3\6\5\6~\n\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\6\7\u0086\n\7\r\7\16\7\u0087\3\b\3\b\3\b")
        buf.write("\3\b\5\b\u008e\n\b\3\b\3\b\7\b\u0092\n\b\f\b\16\b\u0095")
        buf.write("\13\b\3\b\3\b\3\b\3\t\3\t\5\t\u009c\n\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\7\n\u00a3\n\n\f\n\16\n\u00a6\13\n\3\13\5\13\u00a9")
        buf.write("\n\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00b4")
        buf.write("\n\r\3\16\3\16\7\16\u00b8\n\16\f\16\16\16\u00bb\13\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00ce\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00d5\n\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\5\23\u00e1\n\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u00e9\n\23\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u00ef\n\24\3\25\5\25\u00f2\n\25\3\25\3\25\3")
        buf.write("\25\5\25\u00f7\n\25\3\25\3\25\3\25\5\25\u00fc\n\25\3\25")
        buf.write("\3\25\3\25\5\25\u0101\n\25\3\26\3\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\5\27\u010e\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\5\31\u0119\n\31\3")
        buf.write("\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0139\n")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0143")
        buf.write("\n\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u014f\n\36\3\37\3\37\3\37\3\37\7\37\u0155\n\37\f")
        buf.write("\37\16\37\u0158\13\37\3\37\3\37\3 \3 \3 \3!\3!\3!\5!\u0162")
        buf.write("\n!\3!\3!\3\"\3\"\3\"\7\"\u0169\n\"\f\"\16\"\u016c\13")
        buf.write("\"\3#\3#\5#\u0170\n#\3$\3$\3$\3$\3%\3%\3%\7%\u0179\n%")
        buf.write("\f%\16%\u017c\13%\3&\5&\u017f\n&\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3\'\5\'\u0188\n\'\3(\3(\5(\u018c\n(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3.\3.\3.\2\2/\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\2\n\4\2GHLL\3\2EF\4\2\678>?\4\2==@@\3\2AB\3\2&)\3")
        buf.write("\2!$\4\2))e\u00ac\2\u01a2\2]\3\2\2\2\4q\3\2\2\2\6s\3\2")
        buf.write("\2\2\bw\3\2\2\2\n}\3\2\2\2\f\u0082\3\2\2\2\16\u0089\3")
        buf.write("\2\2\2\20\u0099\3\2\2\2\22\u009f\3\2\2\2\24\u00a8\3\2")
        buf.write("\2\2\26\u00ac\3\2\2\2\30\u00b3\3\2\2\2\32\u00b5\3\2\2")
        buf.write("\2\34\u00cd\3\2\2\2\36\u00cf\3\2\2\2 \u00d6\3\2\2\2\"")
        buf.write("\u00da\3\2\2\2$\u00e0\3\2\2\2&\u00ee\3\2\2\2(\u00f1\3")
        buf.write("\2\2\2*\u0102\3\2\2\2,\u0106\3\2\2\2.\u010f\3\2\2\2\60")
        buf.write("\u0115\3\2\2\2\62\u011c\3\2\2\2\64\u0128\3\2\2\2\66\u012b")
        buf.write("\3\2\2\28\u0138\3\2\2\2:\u014e\3\2\2\2<\u0150\3\2\2\2")
        buf.write(">\u015b\3\2\2\2@\u015e\3\2\2\2B\u0165\3\2\2\2D\u016f\3")
        buf.write("\2\2\2F\u0171\3\2\2\2H\u0175\3\2\2\2J\u017e\3\2\2\2L\u0183")
        buf.write("\3\2\2\2N\u018b\3\2\2\2P\u018d\3\2\2\2R\u018f\3\2\2\2")
        buf.write("T\u0191\3\2\2\2V\u0193\3\2\2\2X\u0195\3\2\2\2Z\u0197\3")
        buf.write("\2\2\2\\^\5\4\3\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2")
        buf.write("\2\2`b\3\2\2\2ac\5\f\7\2ba\3\2\2\2bc\3\2\2\2cd\3\2\2\2")
        buf.write("de\7\r\2\2ei\7<\2\2fh\5\34\17\2gf\3\2\2\2hk\3\2\2\2ig")
        buf.write("\3\2\2\2ij\3\2\2\2jl\3\2\2\2ki\3\2\2\2lm\7\2\2\3m\3\3")
        buf.write("\2\2\2nr\5\6\4\2or\5\b\5\2pr\5\n\6\2qn\3\2\2\2qo\3\2\2")
        buf.write("\2qp\3\2\2\2r\5\3\2\2\2st\7\n\2\2tu\7%\2\2u\7\3\2\2\2")
        buf.write("vx\5F$\2wv\3\2\2\2wx\3\2\2\2xy\3\2\2\2yz\7\t\2\2z{\7%")
        buf.write("\2\2{\t\3\2\2\2|~\5F$\2}|\3\2\2\2}~\3\2\2\2~\177\3\2\2")
        buf.write("\2\177\u0080\7\13\2\2\u0080\u0081\7%\2\2\u0081\13\3\2")
        buf.write("\2\2\u0082\u0083\7\f\2\2\u0083\u0085\7<\2\2\u0084\u0086")
        buf.write("\5\16\b\2\u0085\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\r\3\2\2\2\u0089")
        buf.write("\u008a\7\7\2\2\u008a\u008b\7%\2\2\u008b\u008d\5\20\t\2")
        buf.write("\u008c\u008e\5\26\f\2\u008d\u008c\3\2\2\2\u008d\u008e")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0093\7/\2\2\u0090")
        buf.write("\u0092\5\34\17\2\u0091\u0090\3\2\2\2\u0092\u0095\3\2\2")
        buf.write("\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096")
        buf.write("\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097\5\30\r\2\u0097")
        buf.write("\u0098\7\60\2\2\u0098\17\3\2\2\2\u0099\u009b\7-\2\2\u009a")
        buf.write("\u009c\5\22\n\2\u009b\u009a\3\2\2\2\u009b\u009c\3\2\2")
        buf.write("\2\u009c\u009d\3\2\2\2\u009d\u009e\7.\2\2\u009e\21\3\2")
        buf.write("\2\2\u009f\u00a4\5\24\13\2\u00a0\u00a1\7\64\2\2\u00a1")
        buf.write("\u00a3\5\24\13\2\u00a2\u00a0\3\2\2\2\u00a3\u00a6\3\2\2")
        buf.write("\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\23\3")
        buf.write("\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a9\5F$\2\u00a8\u00a7")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa")
        buf.write("\u00ab\7%\2\2\u00ab\25\3\2\2\2\u00ac\u00ad\7<\2\2\u00ad")
        buf.write("\u00ae\5F$\2\u00ae\27\3\2\2\2\u00af\u00b0\7\b\2\2\u00b0")
        buf.write("\u00b4\5N(\2\u00b1\u00b2\7\b\2\2\u00b2\u00b4\5@!\2\u00b3")
        buf.write("\u00af\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\31\3\2\2\2\u00b5")
        buf.write("\u00b9\7/\2\2\u00b6\u00b8\5\34\17\2\u00b7\u00b6\3\2\2")
        buf.write("\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc")
        buf.write("\u00bd\7\60\2\2\u00bd\33\3\2\2\2\u00be\u00ce\5\36\20\2")
        buf.write("\u00bf\u00ce\5 \21\2\u00c0\u00ce\5J&\2\u00c1\u00ce\5\"")
        buf.write("\22\2\u00c2\u00ce\5$\23\2\u00c3\u00ce\5&\24\2\u00c4\u00ce")
        buf.write("\5(\25\2\u00c5\u00ce\5\60\31\2\u00c6\u00ce\5.\30\2\u00c7")
        buf.write("\u00ce\5> \2\u00c8\u00ce\5\62\32\2\u00c9\u00ce\5,\27\2")
        buf.write("\u00ca\u00ce\5\64\33\2\u00cb\u00ce\58\35\2\u00cc\u00ce")
        buf.write("\5\66\34\2\u00cd\u00be\3\2\2\2\u00cd\u00bf\3\2\2\2\u00cd")
        buf.write("\u00c0\3\2\2\2\u00cd\u00c1\3\2\2\2\u00cd\u00c2\3\2\2\2")
        buf.write("\u00cd\u00c3\3\2\2\2\u00cd\u00c4\3\2\2\2\u00cd\u00c5\3")
        buf.write("\2\2\2\u00cd\u00c6\3\2\2\2\u00cd\u00c7\3\2\2\2\u00cd\u00c8")
        buf.write("\3\2\2\2\u00cd\u00c9\3\2\2\2\u00cd\u00ca\3\2\2\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\35\3\2\2\2\u00cf")
        buf.write("\u00d0\7\3\2\2\u00d0\u00d1\5<\37\2\u00d1\u00d4\5\32\16")
        buf.write("\2\u00d2\u00d3\7\4\2\2\u00d3\u00d5\5\32\16\2\u00d4\u00d2")
        buf.write("\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\37\3\2\2\2\u00d6\u00d7")
        buf.write("\7\6\2\2\u00d7\u00d8\5<\37\2\u00d8\u00d9\5\32\16\2\u00d9")
        buf.write("!\3\2\2\2\u00da\u00db\7\5\2\2\u00db\u00dc\7)\2\2\u00dc")
        buf.write("\u00dd\7\34\2\2\u00dd\u00de\5\32\16\2\u00de#\3\2\2\2\u00df")
        buf.write("\u00e1\5*\26\2\u00e0\u00df\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e2\3\2\2\2\u00e2\u00e3\7\21\2\2\u00e3\u00e4")
        buf.write("\5L\'\2\u00e4\u00e5\7\30\2\2\u00e5\u00e8\5X-\2\u00e6\u00e7")
        buf.write("\7\32\2\2\u00e7\u00e9\5V,\2\u00e8\u00e6\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9%\3\2\2\2\u00ea\u00eb\7\22\2\2\u00eb")
        buf.write("\u00ef\5L\'\2\u00ec\u00ed\7\24\2\2\u00ed\u00ef\5L\'\2")
        buf.write("\u00ee\u00ea\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\'\3\2\2")
        buf.write("\2\u00f0\u00f2\5*\26\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2")
        buf.write("\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\5J&\2\u00f4\u00f6")
        buf.write("\7\17\2\2\u00f5\u00f7\5Z.\2\u00f6\u00f5\3\2\2\2\u00f6")
        buf.write("\u00f7\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\5L\'\2")
        buf.write("\u00f9\u00fb\7\31\2\2\u00fa\u00fc\5Z.\2\u00fb\u00fa\3")
        buf.write("\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u0100")
        buf.write("\5L\'\2\u00fe\u00ff\7\32\2\2\u00ff\u0101\5V,\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101)\3\2\2\2\u0102\u0103")
        buf.write("\7N\2\2\u0103\u0104\7 \2\2\u0104\u0105\5V,\2\u0105+\3")
        buf.write("\2\2\2\u0106\u0107\5J&\2\u0107\u0108\7\16\2\2\u0108\u0109")
        buf.write("\7%\2\2\u0109\u010a\7\35\2\2\u010a\u010d\5L\'\2\u010b")
        buf.write("\u010c\7\32\2\2\u010c\u010e\5V,\2\u010d\u010b\3\2\2\2")
        buf.write("\u010d\u010e\3\2\2\2\u010e-\3\2\2\2\u010f\u0110\5J&\2")
        buf.write("\u0110\u0111\7\20\2\2\u0111\u0112\5L\'\2\u0112\u0113\7")
        buf.write("\33\2\2\u0113\u0114\7)\2\2\u0114/\3\2\2\2\u0115\u0116")
        buf.write("\5J&\2\u0116\u0118\7\23\2\2\u0117\u0119\5Z.\2\u0118\u0117")
        buf.write("\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write("\u011b\7%\2\2\u011b\61\3\2\2\2\u011c\u011d\5J&\2\u011d")
        buf.write("\u011e\7\25\2\2\u011e\u011f\5L\'\2\u011f\u0120\7\31\2")
        buf.write("\2\u0120\u0121\5L\'\2\u0121\u0122\7\27\2\2\u0122\u0123")
        buf.write("\7(\2\2\u0123\u0124\7\64\2\2\u0124\u0125\7(\2\2\u0125")
        buf.write("\u0126\7\30\2\2\u0126\u0127\7(\2\2\u0127\63\3\2\2\2\u0128")
        buf.write("\u0129\7\26\2\2\u0129\u012a\5L\'\2\u012a\65\3\2\2\2\u012b")
        buf.write("\u012c\5J&\2\u012c\u012d\5P)\2\u012d\67\3\2\2\2\u012e")
        buf.write("\u012f\5J&\2\u012f\u0130\5N(\2\u0130\u0131\t\2\2\2\u0131")
        buf.write("\u0132\5N(\2\u0132\u0139\3\2\2\2\u0133\u0134\5J&\2\u0134")
        buf.write("\u0135\5N(\2\u0135\u0136\t\3\2\2\u0136\u0137\5N(\2\u0137")
        buf.write("\u0139\3\2\2\2\u0138\u012e\3\2\2\2\u0138\u0133\3\2\2\2")
        buf.write("\u01399\3\2\2\2\u013a\u0142\5N(\2\u013b\u013c\78\2\2\u013c")
        buf.write("\u0143\78\2\2\u013d\u013e\7\67\2\2\u013e\u013f\7\67\2")
        buf.write("\2\u013f\u0143\7\67\2\2\u0140\u0141\7\67\2\2\u0141\u0143")
        buf.write("\7\67\2\2\u0142\u013b\3\2\2\2\u0142\u013d\3\2\2\2\u0142")
        buf.write("\u0140\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0145\5N(\2\u0145")
        buf.write("\u014f\3\2\2\2\u0146\u0147\5N(\2\u0147\u0148\t\4\2\2\u0148")
        buf.write("\u0149\5N(\2\u0149\u014f\3\2\2\2\u014a\u014b\5N(\2\u014b")
        buf.write("\u014c\t\5\2\2\u014c\u014d\5N(\2\u014d\u014f\3\2\2\2\u014e")
        buf.write("\u013a\3\2\2\2\u014e\u0146\3\2\2\2\u014e\u014a\3\2\2\2")
        buf.write("\u014f;\3\2\2\2\u0150\u0151\7-\2\2\u0151\u0156\5:\36\2")
        buf.write("\u0152\u0153\t\6\2\2\u0153\u0155\5:\36\2\u0154\u0152\3")
        buf.write("\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u0156\3\2\2\2\u0159")
        buf.write("\u015a\7.\2\2\u015a=\3\2\2\2\u015b\u015c\5J&\2\u015c\u015d")
        buf.write("\5@!\2\u015d?\3\2\2\2\u015e\u015f\7%\2\2\u015f\u0161\7")
        buf.write("-\2\2\u0160\u0162\5B\"\2\u0161\u0160\3\2\2\2\u0161\u0162")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\7.\2\2\u0164")
        buf.write("A\3\2\2\2\u0165\u016a\5N(\2\u0166\u0167\7\64\2\2\u0167")
        buf.write("\u0169\5N(\2\u0168\u0166\3\2\2\2\u0169\u016c\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016bC\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016d\u0170\5R*\2\u016e\u0170\5T+\2\u016f")
        buf.write("\u016d\3\2\2\2\u016f\u016e\3\2\2\2\u0170E\3\2\2\2\u0171")
        buf.write("\u0172\7\61\2\2\u0172\u0173\5H%\2\u0173\u0174\7\62\2\2")
        buf.write("\u0174G\3\2\2\2\u0175\u017a\5D#\2\u0176\u0177\7\63\2\2")
        buf.write("\u0177\u0179\5D#\2\u0178\u0176\3\2\2\2\u0179\u017c\3\2")
        buf.write("\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017bI\3")
        buf.write("\2\2\2\u017c\u017a\3\2\2\2\u017d\u017f\5F$\2\u017e\u017d")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\5L\'\2\u0181\u0182\7\66\2\2\u0182K\3\2\2\2\u0183")
        buf.write("\u0187\7%\2\2\u0184\u0185\7\61\2\2\u0185\u0186\7)\2\2")
        buf.write("\u0186\u0188\7\62\2\2\u0187\u0184\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188M\3\2\2\2\u0189\u018c\5P)\2\u018a\u018c")
        buf.write("\5L\'\2\u018b\u0189\3\2\2\2\u018b\u018a\3\2\2\2\u018c")
        buf.write("O\3\2\2\2\u018d\u018e\t\7\2\2\u018eQ\3\2\2\2\u018f\u0190")
        buf.write("\t\b\2\2\u0190S\3\2\2\2\u0191\u0192\t\t\2\2\u0192U\3\2")
        buf.write("\2\2\u0193\u0194\7*\2\2\u0194W\3\2\2\2\u0195\u0196\7,")
        buf.write("\2\2\u0196Y\3\2\2\2\u0197\u0198\7)\2\2\u0198\u0199\7\37")
        buf.write("\2\2\u0199\u019a\7\36\2\2\u019a[\3\2\2\2&_biqw}\u0087")
        buf.write("\u008d\u0093\u009b\u00a4\u00a8\u00b3\u00b9\u00cd\u00d4")
        buf.write("\u00e0\u00e8\u00ee\u00f1\u00f6\u00fb\u0100\u010d\u0118")
        buf.write("\u0138\u0142\u014e\u0156\u0161\u016a\u016f\u017a\u017e")
        buf.write("\u0187\u018b")
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
                     "'dispose'", "'gradient'", "'store'", "'range'", "'at'", 
                     "'with'", "'for'", "'into'", "'times'", "'on'", "'of'", 
                     "'units'", "'usein'", "'nat'", "'real'", "'mat'", "'bool'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
                     "'.'", "'='", "'>'", "'<'", "'!'", "'~'", "'?'", "':'", 
                     "'=='", "'<='", "'>='", "'!='", "'&&'", "'||'", "'++'", 
                     "'--'", "'+'", "'-'", "'*'", "'/'", "'&'", "'|'", "'^'", 
                     "'%'", "'_'", "'@'", "'ns'", "'us'", "'ms'", "'cs'", 
                     "'ds'", "'s'", "'m'", "'h'", "'d'", "'w'", "'mo'", 
                     "'y'", "'nL'", "'uL'", "'mL'", "'cL'", "'dL'", "'L'", 
                     "'daL'", "'c'", "'f'", "'k'", "'1'", "'2'", "'3'", 
                     "'4'", "'5'", "'6'", "'7'", "'8'", "'9'", "'10'", "'11'", 
                     "'12'", "'13'", "'14'", "'15'", "'16'", "'17'", "'18'", 
                     "'19'", "'20'", "'21'", "'22'", "'23'", "'24'", "'25'", 
                     "'26'", "'27'", "'28'", "'29'", "'30'", "'31'", "'32'", 
                     "'33'", "'34'", "'35'", "'37'", "'38'", "'39'", "'40'", 
                     "'42'", "'44'", "'45'", "'46'", "'47'", "'48'", "'49'", 
                     "'50'", "'51'", "'55'", "'58'", "'59'", "'60'", "'61'", 
                     "'62'", "'63'", "'64'", "'65'", "'66'", "'68'", "'69'", 
                     "'70'", "'71'", "'72'", "'73'", "'74'", "'75'", "'76'", 
                     "'98'", "'99'", "'100'", "'134'", "'-1'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", 
                      "RETURN", "MANIFEST", "MODULE", "STATIONARY", "FUNCTIONS", 
                      "INSTRUCTIONS", "DETECT", "MIX", "SPLIT", "HEAT", 
                      "DRAIN", "DISPENSE", "DISPOSE", "GRADIENT", "STORE", 
                      "RANGE", "AT", "WITH", "FOR", "INTO", "TIMES", "ON", 
                      "OF", "UNITS", "USEIN", "NAT", "REAL", "MAT", "BOOL", 
                      "IDENTIFIER", "STRING_LITERAL", "BOOL_LITERAL", "FLOAT_LITERAL", 
                      "INTEGER_LITERAL", "TIME_NUMBER", "VOLUME_NUMBER", 
                      "TEMP_NUMBER", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "SEMICOLON", "COMMA", "DOT", 
                      "ASSIGN", "GT", "LT", "BANG", "TILDE", "QUESTION", 
                      "COLON", "EQUALITY", "LTE", "GTE", "NOTEQUAL", "AND", 
                      "OR", "INC", "DEC", "ADDITION", "SUBTRACT", "MULTIPLY", 
                      "DIVIDE", "BITAND", "BITOR", "CARET", "MOD", "UNDERSCORE", 
                      "ATSIGN", "NANOSECOND", "MICROSECOND", "MILLISECOND", 
                      "CENTISECOND", "DECISECOND", "SECOND", "MINUTE", "HOUR", 
                      "DAY", "WEEK", "MONTH", "YEAR", "NANOLITRE", "MICROLITRE", 
                      "MILLILITRE", "CENTILITRE", "DECILITRE", "LITRE", 
                      "DECALITRE", "CELSIUS", "FAHRENHEIT", "KELVIN", "ACIDS_STRONG_NON_OXIDIZING", 
                      "ACIDS_STRONG_OXIDIZING", "ACIDS_CARBOXYLIC", "ALCOHOLS_AND_POLYOLS", 
                      "ALDEHYDES", "AMIDES_AND_IMIDES", "AMINES_PHOSPHINES_AND_PYRIDINES", 
                      "AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS", "CARBAMATES", 
                      "BASES_STRONG", "CYANIDES_INORGANIC", "THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS", 
                      "ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS", 
                      "ETHERS", "FLUORIDES_INORGANIC", "HYDROCARBONS_AROMATIC", 
                      "HALOGENATED_ORGANIC_COMPOUNDS", "ISOCYANATES_AND_ISOTHIOCYANATES", 
                      "KETONES", "SULFIDES_ORGANIC", "METALS_ALKALI_VERY_ACTIVE", 
                      "METALS_ELEMENTAL_AND_POWDER_ACTIVE", "METALS_LESS_REACTIVE", 
                      "METALS_AND_METAL_COMPOUNDS_TOXIC", "DIAZONIUM_SALTS", 
                      "NITRILES", "NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC", 
                      "HYDROCARBONS_ALIPHATIC_UNSATURATED", "HYDROCARBONS_ALIPHATIC_SATURATED", 
                      "PEROXIDES_ORGANIC", "PHENOLS_AND_CRESOLS", "SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC", 
                      "SULFIDES_INORGANIC", "EPOXIDES", "METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES", 
                      "ANHYDRIDES", "SALTS_ACIDIC", "SALTS_BASIC", "ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES", 
                      "ORGANOMETALLICS", "OXIDIZING_AGENTS_STRONG", "REDUCING_AGENTS_STRONG", 
                      "NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS", "FLUORINATED_ORGANIC_COMPOUNDS", 
                      "FLUORIDE_SALTS_SOLUBLE", "OXIDIZING_AGENTS_WEAK", 
                      "REDUCING_AGENTS_WEAK", "NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES", 
                      "CHLOROSILANES", "SILOXANES", "HALOGENATING_AGENTS", 
                      "ACIDS_WEAK", "BASES_WEAK", "CARBONATE_SALTS", "ALKYNES_WITH_ACETYLENIC_HYDROGEN", 
                      "ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN", "CONJUGATED_DIENES", 
                      "ARYL_HALIDES", "AMINES_AROMATIC", "NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC", 
                      "ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS", "ACRYLATES_AND_ACRYLIC_ACIDS", 
                      "PHENOLIC_SALTS", "QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS", 
                      "SULFITE_AND_THIOSULFATE_SALTS", "OXIMES", "POLYMERIZABLE_COMPOUNDS", 
                      "NOT_CHEMICALLY_REACTIVE", "INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION", 
                      "WATER_AND_AQUEOUS_SOLUTIONS", "NULL", "UNKNOWN", 
                      "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_globalDeclarations = 1
    RULE_moduleDeclaration = 2
    RULE_manifestDeclaration = 3
    RULE_stationaryDeclaration = 4
    RULE_functions = 5
    RULE_functionDeclaration = 6
    RULE_formalParameters = 7
    RULE_formalParameterList = 8
    RULE_formalParameter = 9
    RULE_functionTyping = 10
    RULE_returnStatement = 11
    RULE_blockStatement = 12
    RULE_statements = 13
    RULE_ifStatement = 14
    RULE_whileStatement = 15
    RULE_repeat = 16
    RULE_heat = 17
    RULE_dispose = 18
    RULE_mix = 19
    RULE_usein = 20
    RULE_detect = 21
    RULE_split = 22
    RULE_dispense = 23
    RULE_gradient = 24
    RULE_store = 25
    RULE_numberAssignment = 26
    RULE_math = 27
    RULE_binops = 28
    RULE_parExpression = 29
    RULE_methodInvocation = 30
    RULE_methodCall = 31
    RULE_expressionList = 32
    RULE_typeType = 33
    RULE_unionType = 34
    RULE_typesList = 35
    RULE_variableDefinition = 36
    RULE_variable = 37
    RULE_primary = 38
    RULE_literal = 39
    RULE_primitiveType = 40
    RULE_chemicalType = 41
    RULE_timeIdentifier = 42
    RULE_temperatureIdentifier = 43
    RULE_unitTracker = 44

    ruleNames =  [ "program", "globalDeclarations", "moduleDeclaration", 
                   "manifestDeclaration", "stationaryDeclaration", "functions", 
                   "functionDeclaration", "formalParameters", "formalParameterList", 
                   "formalParameter", "functionTyping", "returnStatement", 
                   "blockStatement", "statements", "ifStatement", "whileStatement", 
                   "repeat", "heat", "dispose", "mix", "usein", "detect", 
                   "split", "dispense", "gradient", "store", "numberAssignment", 
                   "math", "binops", "parExpression", "methodInvocation", 
                   "methodCall", "expressionList", "typeType", "unionType", 
                   "typesList", "variableDefinition", "variable", "primary", 
                   "literal", "primitiveType", "chemicalType", "timeIdentifier", 
                   "temperatureIdentifier", "unitTracker" ]

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
    GRADIENT=19
    STORE=20
    RANGE=21
    AT=22
    WITH=23
    FOR=24
    INTO=25
    TIMES=26
    ON=27
    OF=28
    UNITS=29
    USEIN=30
    NAT=31
    REAL=32
    MAT=33
    BOOL=34
    IDENTIFIER=35
    STRING_LITERAL=36
    BOOL_LITERAL=37
    FLOAT_LITERAL=38
    INTEGER_LITERAL=39
    TIME_NUMBER=40
    VOLUME_NUMBER=41
    TEMP_NUMBER=42
    LPAREN=43
    RPAREN=44
    LBRACE=45
    RBRACE=46
    LBRACKET=47
    RBRACKET=48
    SEMICOLON=49
    COMMA=50
    DOT=51
    ASSIGN=52
    GT=53
    LT=54
    BANG=55
    TILDE=56
    QUESTION=57
    COLON=58
    EQUALITY=59
    LTE=60
    GTE=61
    NOTEQUAL=62
    AND=63
    OR=64
    INC=65
    DEC=66
    ADDITION=67
    SUBTRACT=68
    MULTIPLY=69
    DIVIDE=70
    BITAND=71
    BITOR=72
    CARET=73
    MOD=74
    UNDERSCORE=75
    ATSIGN=76
    NANOSECOND=77
    MICROSECOND=78
    MILLISECOND=79
    CENTISECOND=80
    DECISECOND=81
    SECOND=82
    MINUTE=83
    HOUR=84
    DAY=85
    WEEK=86
    MONTH=87
    YEAR=88
    NANOLITRE=89
    MICROLITRE=90
    MILLILITRE=91
    CENTILITRE=92
    DECILITRE=93
    LITRE=94
    DECALITRE=95
    CELSIUS=96
    FAHRENHEIT=97
    KELVIN=98
    ACIDS_STRONG_NON_OXIDIZING=99
    ACIDS_STRONG_OXIDIZING=100
    ACIDS_CARBOXYLIC=101
    ALCOHOLS_AND_POLYOLS=102
    ALDEHYDES=103
    AMIDES_AND_IMIDES=104
    AMINES_PHOSPHINES_AND_PYRIDINES=105
    AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS=106
    CARBAMATES=107
    BASES_STRONG=108
    CYANIDES_INORGANIC=109
    THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS=110
    ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS=111
    ETHERS=112
    FLUORIDES_INORGANIC=113
    HYDROCARBONS_AROMATIC=114
    HALOGENATED_ORGANIC_COMPOUNDS=115
    ISOCYANATES_AND_ISOTHIOCYANATES=116
    KETONES=117
    SULFIDES_ORGANIC=118
    METALS_ALKALI_VERY_ACTIVE=119
    METALS_ELEMENTAL_AND_POWDER_ACTIVE=120
    METALS_LESS_REACTIVE=121
    METALS_AND_METAL_COMPOUNDS_TOXIC=122
    DIAZONIUM_SALTS=123
    NITRILES=124
    NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC=125
    HYDROCARBONS_ALIPHATIC_UNSATURATED=126
    HYDROCARBONS_ALIPHATIC_SATURATED=127
    PEROXIDES_ORGANIC=128
    PHENOLS_AND_CRESOLS=129
    SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC=130
    SULFIDES_INORGANIC=131
    EPOXIDES=132
    METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES=133
    ANHYDRIDES=134
    SALTS_ACIDIC=135
    SALTS_BASIC=136
    ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES=137
    ORGANOMETALLICS=138
    OXIDIZING_AGENTS_STRONG=139
    REDUCING_AGENTS_STRONG=140
    NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS=141
    FLUORINATED_ORGANIC_COMPOUNDS=142
    FLUORIDE_SALTS_SOLUBLE=143
    OXIDIZING_AGENTS_WEAK=144
    REDUCING_AGENTS_WEAK=145
    NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES=146
    CHLOROSILANES=147
    SILOXANES=148
    HALOGENATING_AGENTS=149
    ACIDS_WEAK=150
    BASES_WEAK=151
    CARBONATE_SALTS=152
    ALKYNES_WITH_ACETYLENIC_HYDROGEN=153
    ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN=154
    CONJUGATED_DIENES=155
    ARYL_HALIDES=156
    AMINES_AROMATIC=157
    NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC=158
    ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS=159
    ACRYLATES_AND_ACRYLIC_ACIDS=160
    PHENOLIC_SALTS=161
    QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS=162
    SULFITE_AND_THIOSULFATE_SALTS=163
    OXIMES=164
    POLYMERIZABLE_COMPOUNDS=165
    NOT_CHEMICALLY_REACTIVE=166
    INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION=167
    WATER_AND_AQUEOUS_SOLUTIONS=168
    NULL=169
    UNKNOWN=170
    WS=171
    COMMENT=172
    LINE_COMMENT=173

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTRUCTIONS(self):
            return self.getToken(BSParser.INSTRUCTIONS, 0)

        def COLON(self):
            return self.getToken(BSParser.COLON, 0)

        def EOF(self):
            return self.getToken(BSParser.EOF, 0)

        def globalDeclarations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.GlobalDeclarationsContext)
            else:
                return self.getTypedRuleContext(BSParser.GlobalDeclarationsContext,i)


        def functions(self):
            return self.getTypedRuleContext(BSParser.FunctionsContext,0)


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
            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 90
                self.globalDeclarations()
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.MANIFEST) | (1 << BSParser.MODULE) | (1 << BSParser.STATIONARY) | (1 << BSParser.LBRACKET))) != 0)):
                    break

            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FUNCTIONS:
                self.state = 95
                self.functions()


            self.state = 98
            self.match(BSParser.INSTRUCTIONS)
            self.state = 99
            self.match(BSParser.COLON)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN:
                self.state = 100
                self.statements()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(BSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalDeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moduleDeclaration(self):
            return self.getTypedRuleContext(BSParser.ModuleDeclarationContext,0)


        def manifestDeclaration(self):
            return self.getTypedRuleContext(BSParser.ManifestDeclarationContext,0)


        def stationaryDeclaration(self):
            return self.getTypedRuleContext(BSParser.StationaryDeclarationContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_globalDeclarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalDeclarations" ):
                listener.enterGlobalDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalDeclarations" ):
                listener.exitGlobalDeclarations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalDeclarations" ):
                return visitor.visitGlobalDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def globalDeclarations(self):

        localctx = BSParser.GlobalDeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_globalDeclarations)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.moduleDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.manifestDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.stationaryDeclaration()
                pass


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

        def MODULE(self):
            return self.getToken(BSParser.MODULE, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 4, self.RULE_moduleDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(BSParser.MODULE)
            self.state = 114
            self.match(BSParser.IDENTIFIER)
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

        def MANIFEST(self):
            return self.getToken(BSParser.MANIFEST, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


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
        self.enterRule(localctx, 6, self.RULE_manifestDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 116
                self.unionType()


            self.state = 119
            self.match(BSParser.MANIFEST)
            self.state = 120
            self.match(BSParser.IDENTIFIER)
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

        def STATIONARY(self):
            return self.getToken(BSParser.STATIONARY, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


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
        self.enterRule(localctx, 8, self.RULE_stationaryDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 122
                self.unionType()


            self.state = 125
            self.match(BSParser.STATIONARY)
            self.state = 126
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTIONS(self):
            return self.getToken(BSParser.FUNCTIONS, 0)

        def COLON(self):
            return self.getToken(BSParser.COLON, 0)

        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(BSParser.FunctionDeclarationContext,i)


        def getRuleIndex(self):
            return BSParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions" ):
                return visitor.visitFunctions(self)
            else:
                return visitor.visitChildren(self)




    def functions(self):

        localctx = BSParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(BSParser.FUNCTIONS)
            self.state = 129
            self.match(BSParser.COLON)
            self.state = 131 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 130
                self.functionDeclaration()
                self.state = 133 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BSParser.FUNCTION):
                    break

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
        self.enterRule(localctx, 12, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(BSParser.FUNCTION)
            self.state = 136
            self.match(BSParser.IDENTIFIER)
            self.state = 137
            self.formalParameters()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.COLON:
                self.state = 138
                self.functionTyping()


            self.state = 141
            self.match(BSParser.LBRACE)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN:
                self.state = 142
                self.statements()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self.returnStatement()
            self.state = 149
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
        self.enterRule(localctx, 14, self.RULE_formalParameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(BSParser.LPAREN)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.IDENTIFIER or _la==BSParser.LBRACKET:
                self.state = 152
                self.formalParameterList()


            self.state = 155
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
        self.enterRule(localctx, 16, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.formalParameter()
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 158
                self.match(BSParser.COMMA)
                self.state = 159
                self.formalParameter()
                self.state = 164
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
        self.enterRule(localctx, 18, self.RULE_formalParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 165
                self.unionType()


            self.state = 168
            self.match(BSParser.IDENTIFIER)
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
        self.enterRule(localctx, 20, self.RULE_functionTyping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(BSParser.COLON)
            self.state = 171
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

        def primary(self):
            return self.getTypedRuleContext(BSParser.PrimaryContext,0)


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
        self.enterRule(localctx, 22, self.RULE_returnStatement)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(BSParser.RETURN)
                self.state = 174
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(BSParser.RETURN)
                self.state = 176
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
        self.enterRule(localctx, 24, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(BSParser.LBRACE)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN:
                self.state = 180
                self.statements()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
            self.match(BSParser.RBRACE)
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


        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def repeat(self):
            return self.getTypedRuleContext(BSParser.RepeatContext,0)


        def heat(self):
            return self.getTypedRuleContext(BSParser.HeatContext,0)


        def dispose(self):
            return self.getTypedRuleContext(BSParser.DisposeContext,0)


        def mix(self):
            return self.getTypedRuleContext(BSParser.MixContext,0)


        def dispense(self):
            return self.getTypedRuleContext(BSParser.DispenseContext,0)


        def split(self):
            return self.getTypedRuleContext(BSParser.SplitContext,0)


        def methodInvocation(self):
            return self.getTypedRuleContext(BSParser.MethodInvocationContext,0)


        def gradient(self):
            return self.getTypedRuleContext(BSParser.GradientContext,0)


        def detect(self):
            return self.getTypedRuleContext(BSParser.DetectContext,0)


        def store(self):
            return self.getTypedRuleContext(BSParser.StoreContext,0)


        def math(self):
            return self.getTypedRuleContext(BSParser.MathContext,0)


        def numberAssignment(self):
            return self.getTypedRuleContext(BSParser.NumberAssignmentContext,0)


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
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.variableDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.repeat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 192
                self.heat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 193
                self.dispose()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 194
                self.mix()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 195
                self.dispense()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 196
                self.split()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 197
                self.methodInvocation()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 198
                self.gradient()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 199
                self.detect()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 200
                self.store()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 201
                self.math()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 202
                self.numberAssignment()
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
            self.state = 205
            self.match(BSParser.IF)
            self.state = 206
            self.parExpression()
            self.state = 207
            self.blockStatement()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ELSE:
                self.state = 208
                self.match(BSParser.ELSE)
                self.state = 209
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
            self.state = 212
            self.match(BSParser.WHILE)
            self.state = 213
            self.parExpression()
            self.state = 214
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

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def TIMES(self):
            return self.getToken(BSParser.TIMES, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(BSParser.BlockStatementContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(BSParser.REPEAT)
            self.state = 217
            self.match(BSParser.INTEGER_LITERAL)
            self.state = 218
            self.match(BSParser.TIMES)
            self.state = 219
            self.blockStatement()
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

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


        def AT(self):
            return self.getToken(BSParser.AT, 0)

        def temperatureIdentifier(self):
            return self.getTypedRuleContext(BSParser.TemperatureIdentifierContext,0)


        def usein(self):
            return self.getTypedRuleContext(BSParser.UseinContext,0)


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
        self.enterRule(localctx, 34, self.RULE_heat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ATSIGN:
                self.state = 221
                self.usein()


            self.state = 224
            self.match(BSParser.HEAT)
            self.state = 225
            self.variable()
            self.state = 226
            self.match(BSParser.AT)
            self.state = 227
            self.temperatureIdentifier()
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 228
                self.match(BSParser.FOR)
                self.state = 229
                self.timeIdentifier()


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

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


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
        self.enterRule(localctx, 36, self.RULE_dispose)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.DRAIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(BSParser.DRAIN)
                self.state = 233
                self.variable()
                pass
            elif token in [BSParser.DISPOSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(BSParser.DISPOSE)
                self.state = 235
                self.variable()
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


    class MixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def MIX(self):
            return self.getToken(BSParser.MIX, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.VariableContext)
            else:
                return self.getTypedRuleContext(BSParser.VariableContext,i)


        def WITH(self):
            return self.getToken(BSParser.WITH, 0)

        def usein(self):
            return self.getTypedRuleContext(BSParser.UseinContext,0)


        def unitTracker(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.UnitTrackerContext)
            else:
                return self.getTypedRuleContext(BSParser.UnitTrackerContext,i)


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
        self.enterRule(localctx, 38, self.RULE_mix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ATSIGN:
                self.state = 238
                self.usein()


            self.state = 241
            self.variableDefinition()
            self.state = 242
            self.match(BSParser.MIX)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 243
                self.unitTracker()


            self.state = 246
            self.variable()
            self.state = 247
            self.match(BSParser.WITH)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 248
                self.unitTracker()


            self.state = 251
            self.variable()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 252
                self.match(BSParser.FOR)
                self.state = 253
                self.timeIdentifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATSIGN(self):
            return self.getToken(BSParser.ATSIGN, 0)

        def USEIN(self):
            return self.getToken(BSParser.USEIN, 0)

        def timeIdentifier(self):
            return self.getTypedRuleContext(BSParser.TimeIdentifierContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_usein

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsein" ):
                listener.enterUsein(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsein" ):
                listener.exitUsein(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsein" ):
                return visitor.visitUsein(self)
            else:
                return visitor.visitChildren(self)




    def usein(self):

        localctx = BSParser.UseinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_usein)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(BSParser.ATSIGN)
            self.state = 257
            self.match(BSParser.USEIN)
            self.state = 258
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

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def DETECT(self):
            return self.getToken(BSParser.DETECT, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def ON(self):
            return self.getToken(BSParser.ON, 0)

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


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
        self.enterRule(localctx, 42, self.RULE_detect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.variableDefinition()
            self.state = 261
            self.match(BSParser.DETECT)
            self.state = 262
            self.match(BSParser.IDENTIFIER)
            self.state = 263
            self.match(BSParser.ON)
            self.state = 264
            self.variable()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 265
                self.match(BSParser.FOR)
                self.state = 266
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

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def SPLIT(self):
            return self.getToken(BSParser.SPLIT, 0)

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


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
        self.enterRule(localctx, 44, self.RULE_split)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.variableDefinition()
            self.state = 270
            self.match(BSParser.SPLIT)
            self.state = 271
            self.variable()
            self.state = 272
            self.match(BSParser.INTO)
            self.state = 273
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

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def DISPENSE(self):
            return self.getToken(BSParser.DISPENSE, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def unitTracker(self):
            return self.getTypedRuleContext(BSParser.UnitTrackerContext,0)


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
        self.enterRule(localctx, 46, self.RULE_dispense)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.variableDefinition()
            self.state = 276
            self.match(BSParser.DISPENSE)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 277
                self.unitTracker()


            self.state = 280
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GradientContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def GRADIENT(self):
            return self.getToken(BSParser.GRADIENT, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.VariableContext)
            else:
                return self.getTypedRuleContext(BSParser.VariableContext,i)


        def WITH(self):
            return self.getToken(BSParser.WITH, 0)

        def RANGE(self):
            return self.getToken(BSParser.RANGE, 0)

        def FLOAT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.FLOAT_LITERAL)
            else:
                return self.getToken(BSParser.FLOAT_LITERAL, i)

        def COMMA(self):
            return self.getToken(BSParser.COMMA, 0)

        def AT(self):
            return self.getToken(BSParser.AT, 0)

        def getRuleIndex(self):
            return BSParser.RULE_gradient

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGradient" ):
                listener.enterGradient(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGradient" ):
                listener.exitGradient(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGradient" ):
                return visitor.visitGradient(self)
            else:
                return visitor.visitChildren(self)




    def gradient(self):

        localctx = BSParser.GradientContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_gradient)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.variableDefinition()
            self.state = 283
            self.match(BSParser.GRADIENT)
            self.state = 284
            self.variable()
            self.state = 285
            self.match(BSParser.WITH)
            self.state = 286
            self.variable()
            self.state = 287
            self.match(BSParser.RANGE)
            self.state = 288
            self.match(BSParser.FLOAT_LITERAL)
            self.state = 289
            self.match(BSParser.COMMA)
            self.state = 290
            self.match(BSParser.FLOAT_LITERAL)
            self.state = 291
            self.match(BSParser.AT)
            self.state = 292
            self.match(BSParser.FLOAT_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STORE(self):
            return self.getToken(BSParser.STORE, 0)

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_store

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStore" ):
                listener.enterStore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStore" ):
                listener.exitStore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStore" ):
                return visitor.visitStore(self)
            else:
                return visitor.visitChildren(self)




    def store(self):

        localctx = BSParser.StoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_store)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(BSParser.STORE)
            self.state = 295
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def literal(self):
            return self.getTypedRuleContext(BSParser.LiteralContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_numberAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAssignment" ):
                listener.enterNumberAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAssignment" ):
                listener.exitNumberAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberAssignment" ):
                return visitor.visitNumberAssignment(self)
            else:
                return visitor.visitChildren(self)




    def numberAssignment(self):

        localctx = BSParser.NumberAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_numberAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.variableDefinition()
            self.state = 298
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bop = None # Token

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BSParser.PrimaryContext,i)


        def MULTIPLY(self):
            return self.getToken(BSParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(BSParser.DIVIDE, 0)

        def MOD(self):
            return self.getToken(BSParser.MOD, 0)

        def ADDITION(self):
            return self.getToken(BSParser.ADDITION, 0)

        def SUBTRACT(self):
            return self.getToken(BSParser.SUBTRACT, 0)

        def getRuleIndex(self):
            return BSParser.RULE_math

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath" ):
                listener.enterMath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath" ):
                listener.exitMath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath" ):
                return visitor.visitMath(self)
            else:
                return visitor.visitChildren(self)




    def math(self):

        localctx = BSParser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_math)
        self._la = 0 # Token type
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.variableDefinition()
                self.state = 301
                self.primary()
                self.state = 302
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (BSParser.MULTIPLY - 69)) | (1 << (BSParser.DIVIDE - 69)) | (1 << (BSParser.MOD - 69)))) != 0)):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 303
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.variableDefinition()
                self.state = 306
                self.primary()
                self.state = 307
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BSParser.ADDITION or _la==BSParser.SUBTRACT):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 308
                self.primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinopsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bop = None # Token

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BSParser.PrimaryContext,i)


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

        def getRuleIndex(self):
            return BSParser.RULE_binops

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinops" ):
                listener.enterBinops(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinops" ):
                listener.exitBinops(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinops" ):
                return visitor.visitBinops(self)
            else:
                return visitor.visitChildren(self)




    def binops(self):

        localctx = BSParser.BinopsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_binops)
        self._la = 0 # Token type
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.primary()
                self.state = 320
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 313
                    self.match(BSParser.LT)
                    self.state = 314
                    self.match(BSParser.LT)
                    pass

                elif la_ == 2:
                    self.state = 315
                    self.match(BSParser.GT)
                    self.state = 316
                    self.match(BSParser.GT)
                    self.state = 317
                    self.match(BSParser.GT)
                    pass

                elif la_ == 3:
                    self.state = 318
                    self.match(BSParser.GT)
                    self.state = 319
                    self.match(BSParser.GT)
                    pass


                self.state = 322
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.primary()
                self.state = 325
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.GT) | (1 << BSParser.LT) | (1 << BSParser.LTE) | (1 << BSParser.GTE))) != 0)):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 326
                self.primary()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.primary()
                self.state = 329
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BSParser.EQUALITY or _la==BSParser.NOTEQUAL):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 330
                self.primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BSParser.LPAREN, 0)

        def binops(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.BinopsContext)
            else:
                return self.getTypedRuleContext(BSParser.BinopsContext,i)


        def RPAREN(self):
            return self.getToken(BSParser.RPAREN, 0)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.AND)
            else:
                return self.getToken(BSParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.OR)
            else:
                return self.getToken(BSParser.OR, i)

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
        self.enterRule(localctx, 58, self.RULE_parExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(BSParser.LPAREN)
            self.state = 335
            self.binops()
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.AND or _la==BSParser.OR:
                self.state = 336
                _la = self._input.LA(1)
                if not(_la==BSParser.AND or _la==BSParser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 337
                self.binops()
                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 343
            self.match(BSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(BSParser.MethodCallContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_methodInvocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodInvocation" ):
                listener.enterMethodInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodInvocation" ):
                listener.exitMethodInvocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvocation" ):
                return visitor.visitMethodInvocation(self)
            else:
                return visitor.visitChildren(self)




    def methodInvocation(self):

        localctx = BSParser.MethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_methodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.variableDefinition()
            self.state = 346
            self.methodCall()
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
        self.enterRule(localctx, 62, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(BSParser.IDENTIFIER)
            self.state = 349
            self.match(BSParser.LPAREN)
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IDENTIFIER) | (1 << BSParser.STRING_LITERAL) | (1 << BSParser.BOOL_LITERAL) | (1 << BSParser.FLOAT_LITERAL) | (1 << BSParser.INTEGER_LITERAL))) != 0):
                self.state = 350
                self.expressionList()


            self.state = 353
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

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BSParser.PrimaryContext,i)


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
        self.enterRule(localctx, 64, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.primary()
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 356
                self.match(BSParser.COMMA)
                self.state = 357
                self.primary()
                self.state = 362
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


        def chemicalType(self):
            return self.getTypedRuleContext(BSParser.ChemicalTypeContext,0)


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
        self.enterRule(localctx, 66, self.RULE_typeType)
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.NAT, BSParser.REAL, BSParser.MAT, BSParser.BOOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.primitiveType()
                pass
            elif token in [BSParser.INTEGER_LITERAL, BSParser.ACIDS_STRONG_NON_OXIDIZING, BSParser.ACIDS_STRONG_OXIDIZING, BSParser.ACIDS_CARBOXYLIC, BSParser.ALCOHOLS_AND_POLYOLS, BSParser.ALDEHYDES, BSParser.AMIDES_AND_IMIDES, BSParser.AMINES_PHOSPHINES_AND_PYRIDINES, BSParser.AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS, BSParser.CARBAMATES, BSParser.BASES_STRONG, BSParser.CYANIDES_INORGANIC, BSParser.THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS, BSParser.ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS, BSParser.ETHERS, BSParser.FLUORIDES_INORGANIC, BSParser.HYDROCARBONS_AROMATIC, BSParser.HALOGENATED_ORGANIC_COMPOUNDS, BSParser.ISOCYANATES_AND_ISOTHIOCYANATES, BSParser.KETONES, BSParser.SULFIDES_ORGANIC, BSParser.METALS_ALKALI_VERY_ACTIVE, BSParser.METALS_ELEMENTAL_AND_POWDER_ACTIVE, BSParser.METALS_LESS_REACTIVE, BSParser.METALS_AND_METAL_COMPOUNDS_TOXIC, BSParser.DIAZONIUM_SALTS, BSParser.NITRILES, BSParser.NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC, BSParser.HYDROCARBONS_ALIPHATIC_UNSATURATED, BSParser.HYDROCARBONS_ALIPHATIC_SATURATED, BSParser.PEROXIDES_ORGANIC, BSParser.PHENOLS_AND_CRESOLS, BSParser.SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC, BSParser.SULFIDES_INORGANIC, BSParser.EPOXIDES, BSParser.METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES, BSParser.ANHYDRIDES, BSParser.SALTS_ACIDIC, BSParser.SALTS_BASIC, BSParser.ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES, BSParser.ORGANOMETALLICS, BSParser.OXIDIZING_AGENTS_STRONG, BSParser.REDUCING_AGENTS_STRONG, BSParser.NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS, BSParser.FLUORINATED_ORGANIC_COMPOUNDS, BSParser.FLUORIDE_SALTS_SOLUBLE, BSParser.OXIDIZING_AGENTS_WEAK, BSParser.REDUCING_AGENTS_WEAK, BSParser.NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES, BSParser.CHLOROSILANES, BSParser.SILOXANES, BSParser.HALOGENATING_AGENTS, BSParser.ACIDS_WEAK, BSParser.BASES_WEAK, BSParser.CARBONATE_SALTS, BSParser.ALKYNES_WITH_ACETYLENIC_HYDROGEN, BSParser.ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN, BSParser.CONJUGATED_DIENES, BSParser.ARYL_HALIDES, BSParser.AMINES_AROMATIC, BSParser.NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC, BSParser.ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS, BSParser.ACRYLATES_AND_ACRYLIC_ACIDS, BSParser.PHENOLIC_SALTS, BSParser.QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS, BSParser.SULFITE_AND_THIOSULFATE_SALTS, BSParser.OXIMES, BSParser.POLYMERIZABLE_COMPOUNDS, BSParser.NOT_CHEMICALLY_REACTIVE, BSParser.INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION, BSParser.WATER_AND_AQUEOUS_SOLUTIONS, BSParser.NULL, BSParser.UNKNOWN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.chemicalType()
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
        self.enterRule(localctx, 68, self.RULE_unionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(BSParser.LBRACKET)
            self.state = 368
            self.typesList()
            self.state = 369
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
        self.enterRule(localctx, 70, self.RULE_typesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.typeType()
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.SEMICOLON:
                self.state = 372
                self.match(BSParser.SEMICOLON)
                self.state = 373
                self.typeType()
                self.state = 378
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(BSParser.ASSIGN, 0)

        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_variableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDefinition" ):
                listener.enterVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDefinition" ):
                listener.exitVariableDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDefinition" ):
                return visitor.visitVariableDefinition(self)
            else:
                return visitor.visitChildren(self)




    def variableDefinition(self):

        localctx = BSParser.VariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_variableDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 379
                self.unionType()


            self.state = 382
            self.variable()
            self.state = 383
            self.match(BSParser.ASSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

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
            return BSParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BSParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(BSParser.IDENTIFIER)
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 386
                self.match(BSParser.LBRACKET)
                self.state = 387
                self.match(BSParser.INTEGER_LITERAL)
                self.state = 388
                self.match(BSParser.RBRACKET)


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

        def literal(self):
            return self.getTypedRuleContext(BSParser.LiteralContext,0)


        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


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
        self.enterRule(localctx, 76, self.RULE_primary)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.STRING_LITERAL, BSParser.BOOL_LITERAL, BSParser.FLOAT_LITERAL, BSParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.literal()
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.variable()
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
        self.enterRule(localctx, 78, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
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
        self.enterRule(localctx, 80, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
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


    class ChemicalTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def ACIDS_STRONG_NON_OXIDIZING(self):
            return self.getToken(BSParser.ACIDS_STRONG_NON_OXIDIZING, 0)

        def ACIDS_STRONG_OXIDIZING(self):
            return self.getToken(BSParser.ACIDS_STRONG_OXIDIZING, 0)

        def ACIDS_CARBOXYLIC(self):
            return self.getToken(BSParser.ACIDS_CARBOXYLIC, 0)

        def ALCOHOLS_AND_POLYOLS(self):
            return self.getToken(BSParser.ALCOHOLS_AND_POLYOLS, 0)

        def ALDEHYDES(self):
            return self.getToken(BSParser.ALDEHYDES, 0)

        def AMIDES_AND_IMIDES(self):
            return self.getToken(BSParser.AMIDES_AND_IMIDES, 0)

        def AMINES_PHOSPHINES_AND_PYRIDINES(self):
            return self.getToken(BSParser.AMINES_PHOSPHINES_AND_PYRIDINES, 0)

        def AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS(self):
            return self.getToken(BSParser.AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS, 0)

        def CARBAMATES(self):
            return self.getToken(BSParser.CARBAMATES, 0)

        def BASES_STRONG(self):
            return self.getToken(BSParser.BASES_STRONG, 0)

        def CYANIDES_INORGANIC(self):
            return self.getToken(BSParser.CYANIDES_INORGANIC, 0)

        def THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS(self):
            return self.getToken(BSParser.THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS, 0)

        def ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS(self):
            return self.getToken(BSParser.ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS, 0)

        def ETHERS(self):
            return self.getToken(BSParser.ETHERS, 0)

        def FLUORIDES_INORGANIC(self):
            return self.getToken(BSParser.FLUORIDES_INORGANIC, 0)

        def HYDROCARBONS_AROMATIC(self):
            return self.getToken(BSParser.HYDROCARBONS_AROMATIC, 0)

        def HALOGENATED_ORGANIC_COMPOUNDS(self):
            return self.getToken(BSParser.HALOGENATED_ORGANIC_COMPOUNDS, 0)

        def ISOCYANATES_AND_ISOTHIOCYANATES(self):
            return self.getToken(BSParser.ISOCYANATES_AND_ISOTHIOCYANATES, 0)

        def KETONES(self):
            return self.getToken(BSParser.KETONES, 0)

        def SULFIDES_ORGANIC(self):
            return self.getToken(BSParser.SULFIDES_ORGANIC, 0)

        def METALS_ALKALI_VERY_ACTIVE(self):
            return self.getToken(BSParser.METALS_ALKALI_VERY_ACTIVE, 0)

        def METALS_ELEMENTAL_AND_POWDER_ACTIVE(self):
            return self.getToken(BSParser.METALS_ELEMENTAL_AND_POWDER_ACTIVE, 0)

        def METALS_LESS_REACTIVE(self):
            return self.getToken(BSParser.METALS_LESS_REACTIVE, 0)

        def METALS_AND_METAL_COMPOUNDS_TOXIC(self):
            return self.getToken(BSParser.METALS_AND_METAL_COMPOUNDS_TOXIC, 0)

        def DIAZONIUM_SALTS(self):
            return self.getToken(BSParser.DIAZONIUM_SALTS, 0)

        def NITRILES(self):
            return self.getToken(BSParser.NITRILES, 0)

        def NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC(self):
            return self.getToken(BSParser.NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC, 0)

        def HYDROCARBONS_ALIPHATIC_UNSATURATED(self):
            return self.getToken(BSParser.HYDROCARBONS_ALIPHATIC_UNSATURATED, 0)

        def HYDROCARBONS_ALIPHATIC_SATURATED(self):
            return self.getToken(BSParser.HYDROCARBONS_ALIPHATIC_SATURATED, 0)

        def PEROXIDES_ORGANIC(self):
            return self.getToken(BSParser.PEROXIDES_ORGANIC, 0)

        def PHENOLS_AND_CRESOLS(self):
            return self.getToken(BSParser.PHENOLS_AND_CRESOLS, 0)

        def SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC(self):
            return self.getToken(BSParser.SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC, 0)

        def SULFIDES_INORGANIC(self):
            return self.getToken(BSParser.SULFIDES_INORGANIC, 0)

        def EPOXIDES(self):
            return self.getToken(BSParser.EPOXIDES, 0)

        def METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES(self):
            return self.getToken(BSParser.METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES, 0)

        def ANHYDRIDES(self):
            return self.getToken(BSParser.ANHYDRIDES, 0)

        def SALTS_ACIDIC(self):
            return self.getToken(BSParser.SALTS_ACIDIC, 0)

        def SALTS_BASIC(self):
            return self.getToken(BSParser.SALTS_BASIC, 0)

        def ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES(self):
            return self.getToken(BSParser.ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES, 0)

        def ORGANOMETALLICS(self):
            return self.getToken(BSParser.ORGANOMETALLICS, 0)

        def OXIDIZING_AGENTS_STRONG(self):
            return self.getToken(BSParser.OXIDIZING_AGENTS_STRONG, 0)

        def REDUCING_AGENTS_STRONG(self):
            return self.getToken(BSParser.REDUCING_AGENTS_STRONG, 0)

        def NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS(self):
            return self.getToken(BSParser.NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS, 0)

        def FLUORINATED_ORGANIC_COMPOUNDS(self):
            return self.getToken(BSParser.FLUORINATED_ORGANIC_COMPOUNDS, 0)

        def FLUORIDE_SALTS_SOLUBLE(self):
            return self.getToken(BSParser.FLUORIDE_SALTS_SOLUBLE, 0)

        def OXIDIZING_AGENTS_WEAK(self):
            return self.getToken(BSParser.OXIDIZING_AGENTS_WEAK, 0)

        def REDUCING_AGENTS_WEAK(self):
            return self.getToken(BSParser.REDUCING_AGENTS_WEAK, 0)

        def NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES(self):
            return self.getToken(BSParser.NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES, 0)

        def CHLOROSILANES(self):
            return self.getToken(BSParser.CHLOROSILANES, 0)

        def SILOXANES(self):
            return self.getToken(BSParser.SILOXANES, 0)

        def HALOGENATING_AGENTS(self):
            return self.getToken(BSParser.HALOGENATING_AGENTS, 0)

        def ACIDS_WEAK(self):
            return self.getToken(BSParser.ACIDS_WEAK, 0)

        def BASES_WEAK(self):
            return self.getToken(BSParser.BASES_WEAK, 0)

        def CARBONATE_SALTS(self):
            return self.getToken(BSParser.CARBONATE_SALTS, 0)

        def ALKYNES_WITH_ACETYLENIC_HYDROGEN(self):
            return self.getToken(BSParser.ALKYNES_WITH_ACETYLENIC_HYDROGEN, 0)

        def ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN(self):
            return self.getToken(BSParser.ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN, 0)

        def CONJUGATED_DIENES(self):
            return self.getToken(BSParser.CONJUGATED_DIENES, 0)

        def ARYL_HALIDES(self):
            return self.getToken(BSParser.ARYL_HALIDES, 0)

        def AMINES_AROMATIC(self):
            return self.getToken(BSParser.AMINES_AROMATIC, 0)

        def NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC(self):
            return self.getToken(BSParser.NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC, 0)

        def ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS(self):
            return self.getToken(BSParser.ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS, 0)

        def ACRYLATES_AND_ACRYLIC_ACIDS(self):
            return self.getToken(BSParser.ACRYLATES_AND_ACRYLIC_ACIDS, 0)

        def PHENOLIC_SALTS(self):
            return self.getToken(BSParser.PHENOLIC_SALTS, 0)

        def QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS(self):
            return self.getToken(BSParser.QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS, 0)

        def SULFITE_AND_THIOSULFATE_SALTS(self):
            return self.getToken(BSParser.SULFITE_AND_THIOSULFATE_SALTS, 0)

        def OXIMES(self):
            return self.getToken(BSParser.OXIMES, 0)

        def POLYMERIZABLE_COMPOUNDS(self):
            return self.getToken(BSParser.POLYMERIZABLE_COMPOUNDS, 0)

        def NOT_CHEMICALLY_REACTIVE(self):
            return self.getToken(BSParser.NOT_CHEMICALLY_REACTIVE, 0)

        def INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION(self):
            return self.getToken(BSParser.INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION, 0)

        def WATER_AND_AQUEOUS_SOLUTIONS(self):
            return self.getToken(BSParser.WATER_AND_AQUEOUS_SOLUTIONS, 0)

        def NULL(self):
            return self.getToken(BSParser.NULL, 0)

        def UNKNOWN(self):
            return self.getToken(BSParser.UNKNOWN, 0)

        def getRuleIndex(self):
            return BSParser.RULE_chemicalType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChemicalType" ):
                listener.enterChemicalType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChemicalType" ):
                listener.exitChemicalType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChemicalType" ):
                return visitor.visitChemicalType(self)
            else:
                return visitor.visitChildren(self)




    def chemicalType(self):

        localctx = BSParser.ChemicalTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_chemicalType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            _la = self._input.LA(1)
            if not(_la==BSParser.INTEGER_LITERAL or ((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (BSParser.ACIDS_STRONG_NON_OXIDIZING - 99)) | (1 << (BSParser.ACIDS_STRONG_OXIDIZING - 99)) | (1 << (BSParser.ACIDS_CARBOXYLIC - 99)) | (1 << (BSParser.ALCOHOLS_AND_POLYOLS - 99)) | (1 << (BSParser.ALDEHYDES - 99)) | (1 << (BSParser.AMIDES_AND_IMIDES - 99)) | (1 << (BSParser.AMINES_PHOSPHINES_AND_PYRIDINES - 99)) | (1 << (BSParser.AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS - 99)) | (1 << (BSParser.CARBAMATES - 99)) | (1 << (BSParser.BASES_STRONG - 99)) | (1 << (BSParser.CYANIDES_INORGANIC - 99)) | (1 << (BSParser.THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS - 99)) | (1 << (BSParser.ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS - 99)) | (1 << (BSParser.ETHERS - 99)) | (1 << (BSParser.FLUORIDES_INORGANIC - 99)) | (1 << (BSParser.HYDROCARBONS_AROMATIC - 99)) | (1 << (BSParser.HALOGENATED_ORGANIC_COMPOUNDS - 99)) | (1 << (BSParser.ISOCYANATES_AND_ISOTHIOCYANATES - 99)) | (1 << (BSParser.KETONES - 99)) | (1 << (BSParser.SULFIDES_ORGANIC - 99)) | (1 << (BSParser.METALS_ALKALI_VERY_ACTIVE - 99)) | (1 << (BSParser.METALS_ELEMENTAL_AND_POWDER_ACTIVE - 99)) | (1 << (BSParser.METALS_LESS_REACTIVE - 99)) | (1 << (BSParser.METALS_AND_METAL_COMPOUNDS_TOXIC - 99)) | (1 << (BSParser.DIAZONIUM_SALTS - 99)) | (1 << (BSParser.NITRILES - 99)) | (1 << (BSParser.NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC - 99)) | (1 << (BSParser.HYDROCARBONS_ALIPHATIC_UNSATURATED - 99)) | (1 << (BSParser.HYDROCARBONS_ALIPHATIC_SATURATED - 99)) | (1 << (BSParser.PEROXIDES_ORGANIC - 99)) | (1 << (BSParser.PHENOLS_AND_CRESOLS - 99)) | (1 << (BSParser.SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC - 99)) | (1 << (BSParser.SULFIDES_INORGANIC - 99)) | (1 << (BSParser.EPOXIDES - 99)) | (1 << (BSParser.METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES - 99)) | (1 << (BSParser.ANHYDRIDES - 99)) | (1 << (BSParser.SALTS_ACIDIC - 99)) | (1 << (BSParser.SALTS_BASIC - 99)) | (1 << (BSParser.ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES - 99)) | (1 << (BSParser.ORGANOMETALLICS - 99)) | (1 << (BSParser.OXIDIZING_AGENTS_STRONG - 99)) | (1 << (BSParser.REDUCING_AGENTS_STRONG - 99)) | (1 << (BSParser.NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS - 99)) | (1 << (BSParser.FLUORINATED_ORGANIC_COMPOUNDS - 99)) | (1 << (BSParser.FLUORIDE_SALTS_SOLUBLE - 99)) | (1 << (BSParser.OXIDIZING_AGENTS_WEAK - 99)) | (1 << (BSParser.REDUCING_AGENTS_WEAK - 99)) | (1 << (BSParser.NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES - 99)) | (1 << (BSParser.CHLOROSILANES - 99)) | (1 << (BSParser.SILOXANES - 99)) | (1 << (BSParser.HALOGENATING_AGENTS - 99)) | (1 << (BSParser.ACIDS_WEAK - 99)) | (1 << (BSParser.BASES_WEAK - 99)) | (1 << (BSParser.CARBONATE_SALTS - 99)) | (1 << (BSParser.ALKYNES_WITH_ACETYLENIC_HYDROGEN - 99)) | (1 << (BSParser.ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN - 99)) | (1 << (BSParser.CONJUGATED_DIENES - 99)) | (1 << (BSParser.ARYL_HALIDES - 99)) | (1 << (BSParser.AMINES_AROMATIC - 99)) | (1 << (BSParser.NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC - 99)) | (1 << (BSParser.ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS - 99)) | (1 << (BSParser.ACRYLATES_AND_ACRYLIC_ACIDS - 99)) | (1 << (BSParser.PHENOLIC_SALTS - 99)) | (1 << (BSParser.QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS - 99)))) != 0) or ((((_la - 163)) & ~0x3f) == 0 and ((1 << (_la - 163)) & ((1 << (BSParser.SULFITE_AND_THIOSULFATE_SALTS - 163)) | (1 << (BSParser.OXIMES - 163)) | (1 << (BSParser.POLYMERIZABLE_COMPOUNDS - 163)) | (1 << (BSParser.NOT_CHEMICALLY_REACTIVE - 163)) | (1 << (BSParser.INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION - 163)) | (1 << (BSParser.WATER_AND_AQUEOUS_SOLUTIONS - 163)) | (1 << (BSParser.NULL - 163)) | (1 << (BSParser.UNKNOWN - 163)))) != 0)):
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
        self.enterRule(localctx, 84, self.RULE_timeIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
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
        self.enterRule(localctx, 86, self.RULE_temperatureIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(BSParser.TEMP_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitTrackerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def UNITS(self):
            return self.getToken(BSParser.UNITS, 0)

        def OF(self):
            return self.getToken(BSParser.OF, 0)

        def getRuleIndex(self):
            return BSParser.RULE_unitTracker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnitTracker" ):
                listener.enterUnitTracker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnitTracker" ):
                listener.exitUnitTracker(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnitTracker" ):
                return visitor.visitUnitTracker(self)
            else:
                return visitor.visitChildren(self)




    def unitTracker(self):

        localctx = BSParser.UnitTrackerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_unitTracker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(BSParser.INTEGER_LITERAL)
            self.state = 406
            self.match(BSParser.UNITS)
            self.state = 407
            self.match(BSParser.OF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





