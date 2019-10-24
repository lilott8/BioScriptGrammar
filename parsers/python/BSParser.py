# Generated from /bioscriptgrammar/grammar/BSParser.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

# /* parser/listener/visitor header section */
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3e")
        buf.write("\u0184\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\6\2Z\n\2\r")
        buf.write("\2\16\2[\3\2\5\2_\n\2\3\2\3\2\3\2\7\2d\n\2\f\2\16\2g\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\5\3n\n\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\7\3\7\3\7\6\7|\n\7\r\7\16\7}\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u0084\n\b\3\b\3\b\7\b\u0088\n\b\f\b\16\b")
        buf.write("\u008b\13\b\3\b\3\b\3\b\3\t\3\t\5\t\u0092\n\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\7\n\u0099\n\n\f\n\16\n\u009c\13\n\3\13\5")
        buf.write("\13\u009f\n\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u00aa\n\r\3\16\3\16\7\16\u00ae\n\16\f\16\16\16\u00b1")
        buf.write("\13\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00c4\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\5\20\u00cb\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00dc\n\23\3\24\3\24\3\24\3\24\5\24\u00e2")
        buf.write("\n\24\3\25\3\25\3\25\5\25\u00e7\n\25\3\25\3\25\3\25\5")
        buf.write("\25\u00ec\n\25\3\25\3\25\3\25\5\25\u00f1\n\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\5\26\u00fa\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\30\3\30\3\30\5\30\u0105\n\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0125\n\34\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u012f\n\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u013b\n\35\3\36\3\36\3\36\3\36\7\36\u0141\n\36\f\36\16")
        buf.write("\36\u0144\13\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \5 \u014e")
        buf.write("\n \3 \3 \3!\3!\3!\7!\u0155\n!\f!\16!\u0158\13!\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3$\3$\3$\7$\u0163\n$\f$\16$\u0166\13$\3")
        buf.write("%\5%\u0169\n%\3%\3%\3%\3&\3&\3&\3&\5&\u0172\n&\3\'\3\'")
        buf.write("\5\'\u0176\n\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3,\3,")
        buf.write("\2\2-\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.")
        buf.write("\60\62\64\668:<>@BDFHJLNPRTV\2\t\4\2FGKK\3\2DE\4\2\66")
        buf.write("\67=>\4\2<<??\3\2@A\3\2%(\3\2 #\2\u0187\2Y\3\2\2\2\4m")
        buf.write("\3\2\2\2\6o\3\2\2\2\br\3\2\2\2\nu\3\2\2\2\fx\3\2\2\2\16")
        buf.write("\177\3\2\2\2\20\u008f\3\2\2\2\22\u0095\3\2\2\2\24\u009e")
        buf.write("\3\2\2\2\26\u00a2\3\2\2\2\30\u00a9\3\2\2\2\32\u00ab\3")
        buf.write("\2\2\2\34\u00c3\3\2\2\2\36\u00c5\3\2\2\2 \u00cc\3\2\2")
        buf.write("\2\"\u00d0\3\2\2\2$\u00d5\3\2\2\2&\u00e1\3\2\2\2(\u00e3")
        buf.write("\3\2\2\2*\u00f2\3\2\2\2,\u00fb\3\2\2\2.\u0101\3\2\2\2")
        buf.write("\60\u0108\3\2\2\2\62\u0114\3\2\2\2\64\u0117\3\2\2\2\66")
        buf.write("\u0124\3\2\2\28\u013a\3\2\2\2:\u013c\3\2\2\2<\u0147\3")
        buf.write("\2\2\2>\u014a\3\2\2\2@\u0151\3\2\2\2B\u0159\3\2\2\2D\u015b")
        buf.write("\3\2\2\2F\u015f\3\2\2\2H\u0168\3\2\2\2J\u016d\3\2\2\2")
        buf.write("L\u0175\3\2\2\2N\u0177\3\2\2\2P\u0179\3\2\2\2R\u017b\3")
        buf.write("\2\2\2T\u017d\3\2\2\2V\u017f\3\2\2\2XZ\5\4\3\2YX\3\2\2")
        buf.write("\2Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2]_\5\f\7\2")
        buf.write("^]\3\2\2\2^_\3\2\2\2_`\3\2\2\2`a\7\r\2\2ae\7;\2\2bd\5")
        buf.write("\34\17\2cb\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2fh\3\2")
        buf.write("\2\2ge\3\2\2\2hi\7\2\2\3i\3\3\2\2\2jn\5\6\4\2kn\5\b\5")
        buf.write("\2ln\5\n\6\2mj\3\2\2\2mk\3\2\2\2ml\3\2\2\2n\5\3\2\2\2")
        buf.write("op\7\n\2\2pq\7$\2\2q\7\3\2\2\2rs\7\t\2\2st\7$\2\2t\t\3")
        buf.write("\2\2\2uv\7\13\2\2vw\7$\2\2w\13\3\2\2\2xy\7\f\2\2y{\7;")
        buf.write("\2\2z|\5\16\b\2{z\3\2\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2")
        buf.write("\2~\r\3\2\2\2\177\u0080\7\7\2\2\u0080\u0081\7$\2\2\u0081")
        buf.write("\u0083\5\20\t\2\u0082\u0084\5\26\f\2\u0083\u0082\3\2\2")
        buf.write("\2\u0083\u0084\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0089")
        buf.write("\7.\2\2\u0086\u0088\5\34\17\2\u0087\u0086\3\2\2\2\u0088")
        buf.write("\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2")
        buf.write("\u008a\u008c\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d\5")
        buf.write("\30\r\2\u008d\u008e\7/\2\2\u008e\17\3\2\2\2\u008f\u0091")
        buf.write("\7,\2\2\u0090\u0092\5\22\n\2\u0091\u0090\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\7-\2\2")
        buf.write("\u0094\21\3\2\2\2\u0095\u009a\5\24\13\2\u0096\u0097\7")
        buf.write("\63\2\2\u0097\u0099\5\24\13\2\u0098\u0096\3\2\2\2\u0099")
        buf.write("\u009c\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\23\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009f\5D#")
        buf.write("\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0")
        buf.write("\3\2\2\2\u00a0\u00a1\7$\2\2\u00a1\25\3\2\2\2\u00a2\u00a3")
        buf.write("\7;\2\2\u00a3\u00a4\5D#\2\u00a4\27\3\2\2\2\u00a5\u00a6")
        buf.write("\7\b\2\2\u00a6\u00aa\5L\'\2\u00a7\u00a8\7\b\2\2\u00a8")
        buf.write("\u00aa\5> \2\u00a9\u00a5\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa")
        buf.write("\31\3\2\2\2\u00ab\u00af\7.\2\2\u00ac\u00ae\5\34\17\2\u00ad")
        buf.write("\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3")
        buf.write("\2\2\2\u00b2\u00b3\7/\2\2\u00b3\33\3\2\2\2\u00b4\u00c4")
        buf.write("\5\36\20\2\u00b5\u00c4\5 \21\2\u00b6\u00c4\5H%\2\u00b7")
        buf.write("\u00c4\5\"\22\2\u00b8\u00c4\5$\23\2\u00b9\u00c4\5&\24")
        buf.write("\2\u00ba\u00c4\5(\25\2\u00bb\u00c4\5.\30\2\u00bc\u00c4")
        buf.write("\5,\27\2\u00bd\u00c4\5<\37\2\u00be\u00c4\5\60\31\2\u00bf")
        buf.write("\u00c4\5*\26\2\u00c0\u00c4\5\62\32\2\u00c1\u00c4\5\66")
        buf.write("\34\2\u00c2\u00c4\5\64\33\2\u00c3\u00b4\3\2\2\2\u00c3")
        buf.write("\u00b5\3\2\2\2\u00c3\u00b6\3\2\2\2\u00c3\u00b7\3\2\2\2")
        buf.write("\u00c3\u00b8\3\2\2\2\u00c3\u00b9\3\2\2\2\u00c3\u00ba\3")
        buf.write("\2\2\2\u00c3\u00bb\3\2\2\2\u00c3\u00bc\3\2\2\2\u00c3\u00bd")
        buf.write("\3\2\2\2\u00c3\u00be\3\2\2\2\u00c3\u00bf\3\2\2\2\u00c3")
        buf.write("\u00c0\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2")
        buf.write("\u00c4\35\3\2\2\2\u00c5\u00c6\7\3\2\2\u00c6\u00c7\5:\36")
        buf.write("\2\u00c7\u00ca\5\32\16\2\u00c8\u00c9\7\4\2\2\u00c9\u00cb")
        buf.write("\5\32\16\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\37\3\2\2\2\u00cc\u00cd\7\6\2\2\u00cd\u00ce\5:\36\2\u00ce")
        buf.write("\u00cf\5\32\16\2\u00cf!\3\2\2\2\u00d0\u00d1\7\5\2\2\u00d1")
        buf.write("\u00d2\7(\2\2\u00d2\u00d3\7\34\2\2\u00d3\u00d4\5\32\16")
        buf.write("\2\u00d4#\3\2\2\2\u00d5\u00d6\7\21\2\2\u00d6\u00d7\5J")
        buf.write("&\2\u00d7\u00d8\7\30\2\2\u00d8\u00db\5T+\2\u00d9\u00da")
        buf.write("\7\32\2\2\u00da\u00dc\5R*\2\u00db\u00d9\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc%\3\2\2\2\u00dd\u00de\7\22\2\2\u00de")
        buf.write("\u00e2\5J&\2\u00df\u00e0\7\24\2\2\u00e0\u00e2\5J&\2\u00e1")
        buf.write("\u00dd\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\'\3\2\2\2\u00e3")
        buf.write("\u00e4\5H%\2\u00e4\u00e6\7\17\2\2\u00e5\u00e7\5V,\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e9\5J&\2\u00e9\u00eb\7\31\2\2\u00ea\u00ec\5")
        buf.write("V,\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed")
        buf.write("\3\2\2\2\u00ed\u00f0\5J&\2\u00ee\u00ef\7\32\2\2\u00ef")
        buf.write("\u00f1\5R*\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1")
        buf.write(")\3\2\2\2\u00f2\u00f3\5H%\2\u00f3\u00f4\7\16\2\2\u00f4")
        buf.write("\u00f5\7$\2\2\u00f5\u00f6\7\35\2\2\u00f6\u00f9\5J&\2\u00f7")
        buf.write("\u00f8\7\32\2\2\u00f8\u00fa\5R*\2\u00f9\u00f7\3\2\2\2")
        buf.write("\u00f9\u00fa\3\2\2\2\u00fa+\3\2\2\2\u00fb\u00fc\5H%\2")
        buf.write("\u00fc\u00fd\7\20\2\2\u00fd\u00fe\5J&\2\u00fe\u00ff\7")
        buf.write("\33\2\2\u00ff\u0100\7(\2\2\u0100-\3\2\2\2\u0101\u0102")
        buf.write("\5H%\2\u0102\u0104\7\23\2\2\u0103\u0105\5V,\2\u0104\u0103")
        buf.write("\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106\3\2\2\2\u0106")
        buf.write("\u0107\7$\2\2\u0107/\3\2\2\2\u0108\u0109\5H%\2\u0109\u010a")
        buf.write("\7\25\2\2\u010a\u010b\7$\2\2\u010b\u010c\7\31\2\2\u010c")
        buf.write("\u010d\7$\2\2\u010d\u010e\7\27\2\2\u010e\u010f\7(\2\2")
        buf.write("\u010f\u0110\7\63\2\2\u0110\u0111\7(\2\2\u0111\u0112\7")
        buf.write("\30\2\2\u0112\u0113\7(\2\2\u0113\61\3\2\2\2\u0114\u0115")
        buf.write("\7\26\2\2\u0115\u0116\5J&\2\u0116\63\3\2\2\2\u0117\u0118")
        buf.write("\5H%\2\u0118\u0119\5N(\2\u0119\65\3\2\2\2\u011a\u011b")
        buf.write("\5H%\2\u011b\u011c\5L\'\2\u011c\u011d\t\2\2\2\u011d\u011e")
        buf.write("\5L\'\2\u011e\u0125\3\2\2\2\u011f\u0120\5H%\2\u0120\u0121")
        buf.write("\5L\'\2\u0121\u0122\t\3\2\2\u0122\u0123\5L\'\2\u0123\u0125")
        buf.write("\3\2\2\2\u0124\u011a\3\2\2\2\u0124\u011f\3\2\2\2\u0125")
        buf.write("\67\3\2\2\2\u0126\u012e\5L\'\2\u0127\u0128\7\67\2\2\u0128")
        buf.write("\u012f\7\67\2\2\u0129\u012a\7\66\2\2\u012a\u012b\7\66")
        buf.write("\2\2\u012b\u012f\7\66\2\2\u012c\u012d\7\66\2\2\u012d\u012f")
        buf.write("\7\66\2\2\u012e\u0127\3\2\2\2\u012e\u0129\3\2\2\2\u012e")
        buf.write("\u012c\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131\5L\'\2")
        buf.write("\u0131\u013b\3\2\2\2\u0132\u0133\5L\'\2\u0133\u0134\t")
        buf.write("\4\2\2\u0134\u0135\5L\'\2\u0135\u013b\3\2\2\2\u0136\u0137")
        buf.write("\5L\'\2\u0137\u0138\t\5\2\2\u0138\u0139\5L\'\2\u0139\u013b")
        buf.write("\3\2\2\2\u013a\u0126\3\2\2\2\u013a\u0132\3\2\2\2\u013a")
        buf.write("\u0136\3\2\2\2\u013b9\3\2\2\2\u013c\u013d\7,\2\2\u013d")
        buf.write("\u0142\58\35\2\u013e\u013f\t\6\2\2\u013f\u0141\58\35\2")
        buf.write("\u0140\u013e\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140\3")
        buf.write("\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0145\u0146\7-\2\2\u0146;\3\2\2\2\u0147\u0148")
        buf.write("\5H%\2\u0148\u0149\5> \2\u0149=\3\2\2\2\u014a\u014b\7")
        buf.write("$\2\2\u014b\u014d\7,\2\2\u014c\u014e\5@!\2\u014d\u014c")
        buf.write("\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u0150\7-\2\2\u0150?\3\2\2\2\u0151\u0156\5L\'\2\u0152")
        buf.write("\u0153\7\63\2\2\u0153\u0155\5L\'\2\u0154\u0152\3\2\2\2")
        buf.write("\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3")
        buf.write("\2\2\2\u0157A\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a")
        buf.write("\5P)\2\u015aC\3\2\2\2\u015b\u015c\7\60\2\2\u015c\u015d")
        buf.write("\5F$\2\u015d\u015e\7\61\2\2\u015eE\3\2\2\2\u015f\u0164")
        buf.write("\5B\"\2\u0160\u0161\7\62\2\2\u0161\u0163\5B\"\2\u0162")
        buf.write("\u0160\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165G\3\2\2\2\u0166\u0164\3\2\2")
        buf.write("\2\u0167\u0169\5D#\2\u0168\u0167\3\2\2\2\u0168\u0169\3")
        buf.write("\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\5J&\2\u016b\u016c")
        buf.write("\7\65\2\2\u016cI\3\2\2\2\u016d\u0171\7$\2\2\u016e\u016f")
        buf.write("\7\60\2\2\u016f\u0170\7(\2\2\u0170\u0172\7\61\2\2\u0171")
        buf.write("\u016e\3\2\2\2\u0171\u0172\3\2\2\2\u0172K\3\2\2\2\u0173")
        buf.write("\u0176\5N(\2\u0174\u0176\5J&\2\u0175\u0173\3\2\2\2\u0175")
        buf.write("\u0174\3\2\2\2\u0176M\3\2\2\2\u0177\u0178\t\7\2\2\u0178")
        buf.write("O\3\2\2\2\u0179\u017a\t\b\2\2\u017aQ\3\2\2\2\u017b\u017c")
        buf.write("\7)\2\2\u017cS\3\2\2\2\u017d\u017e\7+\2\2\u017eU\3\2\2")
        buf.write("\2\u017f\u0180\7(\2\2\u0180\u0181\7\37\2\2\u0181\u0182")
        buf.write("\7\36\2\2\u0182W\3\2\2\2![^em}\u0083\u0089\u0091\u009a")
        buf.write("\u009e\u00a9\u00af\u00c3\u00ca\u00db\u00e1\u00e6\u00eb")
        buf.write("\u00f0\u00f9\u0104\u0124\u012e\u013a\u0142\u014d\u0156")
        buf.write("\u0164\u0168\u0171\u0175")
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
                     "'units'", "'nat'", "'real'", "'mat'", "'bool'", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'",
                     "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", "'='",
                     "'>'", "'<'", "'!'", "'~'", "'?'", "':'", "'=='", "'<='",
                     "'>='", "'!='", "'&&'", "'||'", "'++'", "'--'", "'+'",
                     "'-'", "'*'", "'/'", "'&'", "'|'", "'^'", "'%'", "'_'",
                     "'ns'", "'us'", "'ms'", "'cs'", "'ds'", "'s'", "'m'",
                     "'h'", "'d'", "'w'", "'mo'", "'y'", "'nL'", "'uL'",
                     "'mL'", "'cL'", "'dL'", "'L'", "'daL'", "'c'", "'f'",
                     "'k'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION",
                      "RETURN", "MANIFEST", "MODULE", "STATIONARY", "FUNCTIONS",
                      "INSTRUCTIONS", "DETECT", "MIX", "SPLIT", "HEAT",
                      "DRAIN", "DISPENSE", "DISPOSE", "GRADIENT", "STORE",
                      "RANGE", "AT", "WITH", "FOR", "INTO", "TIMES", "ON",
                      "OF", "UNITS", "NAT", "REAL", "MAT", "BOOL", "IDENTIFIER",
                      "STRING_LITERAL", "BOOL_LITERAL", "FLOAT_LITERAL",
                      "INTEGER_LITERAL", "TIME_NUMBER", "VOLUME_NUMBER",
                      "TEMP_NUMBER", "LPAREN", "RPAREN", "LBRACE", "RBRACE",
                      "LBRACKET", "RBRACKET", "SEMICOLON", "COMMA", "DOT",
                      "ASSIGN", "GT", "LT", "BANG", "TILDE", "QUESTION",
                      "COLON", "EQUALITY", "LTE", "GTE", "NOTEQUAL", "AND",
                      "OR", "INC", "DEC", "ADDITION", "SUBTRACT", "MULTIPLY",
                      "DIVIDE", "BITAND", "BITOR", "CARET", "MOD", "UNDERSCORE",
                      "NANOSECOND", "MICROSECOND", "MILLISECOND", "CENTISECOND",
                      "DECISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK",
                      "MONTH", "YEAR", "NANOLITRE", "MICROLITRE", "MILLILITRE",
                      "CENTILITRE", "DECILITRE", "LITRE", "DECALITRE", "CELSIUS",
                      "FAHRENHEIT", "KELVIN", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_progmaram = 0
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
    RULE_detect = 20
    RULE_split = 21
    RULE_dispense = 22
    RULE_gradient = 23
    RULE_store = 24
    RULE_numberAssignment = 25
    RULE_math = 26
    RULE_binops = 27
    RULE_parExpression = 28
    RULE_methodInvocation = 29
    RULE_methodCall = 30
    RULE_expressionList = 31
    RULE_typeType = 32
    RULE_unionType = 33
    RULE_typesList = 34
    RULE_variableDefinition = 35
    RULE_variable = 36
    RULE_primary = 37
    RULE_literal = 38
    RULE_primitiveType = 39
    RULE_timeIdentifier = 40
    RULE_temperatureIdentifier = 41
    RULE_unitTracker = 42

    ruleNames =  [ "progmaram", "globalDeclarations", "moduleDeclaration",
                   "manifestDeclaration", "stationaryDeclaration", "functions",
                   "functionDeclaration", "formalParameters", "formalParameterList",
                   "formalParameter", "functionTyping", "returnStatement",
                   "blockStatement", "statements", "ifStatement", "whileStatement",
                   "repeat", "heat", "dispose", "mix", "detect", "split",
                   "dispense", "gradient", "store", "numberAssignment",
                   "math", "binops", "parExpression", "methodInvocation",
                   "methodCall", "expressionList", "typeType", "unionType",
                   "typesList", "variableDefinition", "variable", "primary",
                   "literal", "primitiveType", "timeIdentifier", "temperatureIdentifier",
                   "unitTracker" ]

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
    NAT=30
    REAL=31
    MAT=32
    BOOL=33
    IDENTIFIER=34
    STRING_LITERAL=35
    BOOL_LITERAL=36
    FLOAT_LITERAL=37
    INTEGER_LITERAL=38
    TIME_NUMBER=39
    VOLUME_NUMBER=40
    TEMP_NUMBER=41
    LPAREN=42
    RPAREN=43
    LBRACE=44
    RBRACE=45
    LBRACKET=46
    RBRACKET=47
    SEMICOLON=48
    COMMA=49
    DOT=50
    ASSIGN=51
    GT=52
    LT=53
    BANG=54
    TILDE=55
    QUESTION=56
    COLON=57
    EQUALITY=58
    LTE=59
    GTE=60
    NOTEQUAL=61
    AND=62
    OR=63
    INC=64
    DEC=65
    ADDITION=66
    SUBTRACT=67
    MULTIPLY=68
    DIVIDE=69
    BITAND=70
    BITOR=71
    CARET=72
    MOD=73
    UNDERSCORE=74
    NANOSECOND=75
    MICROSECOND=76
    MILLISECOND=77
    CENTISECOND=78
    DECISECOND=79
    SECOND=80
    MINUTE=81
    HOUR=82
    DAY=83
    WEEK=84
    MONTH=85
    YEAR=86
    NANOLITRE=87
    MICROLITRE=88
    MILLILITRE=89
    CENTILITRE=90
    DECILITRE=91
    LITRE=92
    DECALITRE=93
    CELSIUS=94
    FAHRENHEIT=95
    KELVIN=96
    WS=97
    COMMENT=98
    LINE_COMMENT=99

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgmaramContext(ParserRuleContext):

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
            return BSParser.RULE_progmaram

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgmaram" ):
                listener.enterProgmaram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgmaram" ):
                listener.exitProgmaram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgmaram" ):
                return visitor.visitProgmaram(self)
            else:
                return visitor.visitChildren(self)




    def progmaram(self):

        localctx = BSParser.ProgmaramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_progmaram)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.globalDeclarations()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.MANIFEST) | (1 << BSParser.MODULE) | (1 << BSParser.STATIONARY))) != 0)):
                    break

            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FUNCTIONS:
                self.state = 91
                self.functions()


            self.state = 94
            self.match(BSParser.INSTRUCTIONS)
            self.state = 95
            self.match(BSParser.COLON)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 96
                self.statements()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
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
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.MODULE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.moduleDeclaration()
                pass
            elif token in [BSParser.MANIFEST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.manifestDeclaration()
                pass
            elif token in [BSParser.STATIONARY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.stationaryDeclaration()
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
            self.state = 109
            self.match(BSParser.MODULE)
            self.state = 110
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(BSParser.MANIFEST)
            self.state = 113
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(BSParser.STATIONARY)
            self.state = 116
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
            self.state = 118
            self.match(BSParser.FUNCTIONS)
            self.state = 119
            self.match(BSParser.COLON)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 120
                self.functionDeclaration()
                self.state = 123
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
            self.state = 125
            self.match(BSParser.FUNCTION)
            self.state = 126
            self.match(BSParser.IDENTIFIER)
            self.state = 127
            self.formalParameters()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.COLON:
                self.state = 128
                self.functionTyping()


            self.state = 131
            self.match(BSParser.LBRACE)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 132
                self.statements()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self.returnStatement()
            self.state = 139
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
            self.state = 141
            self.match(BSParser.LPAREN)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.IDENTIFIER or _la==BSParser.LBRACKET:
                self.state = 142
                self.formalParameterList()


            self.state = 145
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
            self.state = 147
            self.formalParameter()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 148
                self.match(BSParser.COMMA)
                self.state = 149
                self.formalParameter()
                self.state = 154
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
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 155
                self.unionType()


            self.state = 158
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
            self.state = 160
            self.match(BSParser.COLON)
            self.state = 161
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
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(BSParser.RETURN)
                self.state = 164
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(BSParser.RETURN)
                self.state = 166
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
            self.state = 169
            self.match(BSParser.LBRACE)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 170
                self.statements()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
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
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.variableDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.repeat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.heat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 183
                self.dispose()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.mix()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 185
                self.dispense()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 186
                self.split()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 187
                self.methodInvocation()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 188
                self.gradient()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 189
                self.detect()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 190
                self.store()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 191
                self.math()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 192
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
            self.state = 195
            self.match(BSParser.IF)
            self.state = 196
            self.parExpression()
            self.state = 197
            self.blockStatement()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ELSE:
                self.state = 198
                self.match(BSParser.ELSE)
                self.state = 199
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
            self.state = 202
            self.match(BSParser.WHILE)
            self.state = 203
            self.parExpression()
            self.state = 204
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
            self.state = 206
            self.match(BSParser.REPEAT)
            self.state = 207
            self.match(BSParser.INTEGER_LITERAL)
            self.state = 208
            self.match(BSParser.TIMES)
            self.state = 209
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
            self.state = 211
            self.match(BSParser.HEAT)
            self.state = 212
            self.variable()
            self.state = 213
            self.match(BSParser.AT)
            self.state = 214
            self.temperatureIdentifier()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 215
                self.match(BSParser.FOR)
                self.state = 216
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
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.DRAIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(BSParser.DRAIN)
                self.state = 220
                self.variable()
                pass
            elif token in [BSParser.DISPOSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(BSParser.DISPOSE)
                self.state = 222
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
            self.state = 225
            self.variableDefinition()
            self.state = 226
            self.match(BSParser.MIX)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 227
                self.unitTracker()


            self.state = 230
            self.variable()
            self.state = 231
            self.match(BSParser.WITH)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 232
                self.unitTracker()


            self.state = 235
            self.variable()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 236
                self.match(BSParser.FOR)
                self.state = 237
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
        self.enterRule(localctx, 40, self.RULE_detect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.variableDefinition()
            self.state = 241
            self.match(BSParser.DETECT)
            self.state = 242
            self.match(BSParser.IDENTIFIER)
            self.state = 243
            self.match(BSParser.ON)
            self.state = 244
            self.variable()
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 245
                self.match(BSParser.FOR)
                self.state = 246
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
        self.enterRule(localctx, 42, self.RULE_split)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.variableDefinition()
            self.state = 250
            self.match(BSParser.SPLIT)
            self.state = 251
            self.variable()
            self.state = 252
            self.match(BSParser.INTO)
            self.state = 253
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
        self.enterRule(localctx, 44, self.RULE_dispense)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.variableDefinition()
            self.state = 256
            self.match(BSParser.DISPENSE)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 257
                self.unitTracker()


            self.state = 260
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.IDENTIFIER)
            else:
                return self.getToken(BSParser.IDENTIFIER, i)

        def WITH(self):
            return self.getToken(BSParser.WITH, 0)

        def RANGE(self):
            return self.getToken(BSParser.RANGE, 0)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.INTEGER_LITERAL)
            else:
                return self.getToken(BSParser.INTEGER_LITERAL, i)

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
        self.enterRule(localctx, 46, self.RULE_gradient)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.variableDefinition()
            self.state = 263
            self.match(BSParser.GRADIENT)
            self.state = 264
            self.match(BSParser.IDENTIFIER)
            self.state = 265
            self.match(BSParser.WITH)
            self.state = 266
            self.match(BSParser.IDENTIFIER)
            self.state = 267
            self.match(BSParser.RANGE)
            self.state = 268
            self.match(BSParser.INTEGER_LITERAL)
            self.state = 269
            self.match(BSParser.COMMA)
            self.state = 270
            self.match(BSParser.INTEGER_LITERAL)
            self.state = 271
            self.match(BSParser.AT)
            self.state = 272
            self.match(BSParser.INTEGER_LITERAL)
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
        self.enterRule(localctx, 48, self.RULE_store)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(BSParser.STORE)
            self.state = 275
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
        self.enterRule(localctx, 50, self.RULE_numberAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.variableDefinition()
            self.state = 278
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
        self.enterRule(localctx, 52, self.RULE_math)
        self._la = 0 # Token type
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.variableDefinition()
                self.state = 281
                self.primary()
                self.state = 282
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (BSParser.MULTIPLY - 68)) | (1 << (BSParser.DIVIDE - 68)) | (1 << (BSParser.MOD - 68)))) != 0)):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 283
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.variableDefinition()
                self.state = 286
                self.primary()
                self.state = 287
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BSParser.ADDITION or _la==BSParser.SUBTRACT):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 288
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
        self.enterRule(localctx, 54, self.RULE_binops)
        self._la = 0 # Token type
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.primary()
                self.state = 300
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 293
                    self.match(BSParser.LT)
                    self.state = 294
                    self.match(BSParser.LT)
                    pass

                elif la_ == 2:
                    self.state = 295
                    self.match(BSParser.GT)
                    self.state = 296
                    self.match(BSParser.GT)
                    self.state = 297
                    self.match(BSParser.GT)
                    pass

                elif la_ == 3:
                    self.state = 298
                    self.match(BSParser.GT)
                    self.state = 299
                    self.match(BSParser.GT)
                    pass


                self.state = 302
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.primary()
                self.state = 305
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.GT) | (1 << BSParser.LT) | (1 << BSParser.LTE) | (1 << BSParser.GTE))) != 0)):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 306
                self.primary()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 308
                self.primary()
                self.state = 309
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BSParser.EQUALITY or _la==BSParser.NOTEQUAL):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 310
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
        self.enterRule(localctx, 56, self.RULE_parExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(BSParser.LPAREN)
            self.state = 315
            self.binops()
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.AND or _la==BSParser.OR:
                self.state = 316
                _la = self._input.LA(1)
                if not(_la==BSParser.AND or _la==BSParser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 317
                self.binops()
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 323
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
        self.enterRule(localctx, 58, self.RULE_methodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.variableDefinition()
            self.state = 326
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
        self.enterRule(localctx, 60, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(BSParser.IDENTIFIER)
            self.state = 329
            self.match(BSParser.LPAREN)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IDENTIFIER) | (1 << BSParser.STRING_LITERAL) | (1 << BSParser.BOOL_LITERAL) | (1 << BSParser.FLOAT_LITERAL) | (1 << BSParser.INTEGER_LITERAL))) != 0):
                self.state = 330
                self.expressionList()


            self.state = 333
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
        self.enterRule(localctx, 62, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.primary()
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 336
                self.match(BSParser.COMMA)
                self.state = 337
                self.primary()
                self.state = 342
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
        self.enterRule(localctx, 64, self.RULE_typeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
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
        self.enterRule(localctx, 66, self.RULE_unionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(BSParser.LBRACKET)
            self.state = 346
            self.typesList()
            self.state = 347
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
        self.enterRule(localctx, 68, self.RULE_typesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.typeType()
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.SEMICOLON:
                self.state = 350
                self.match(BSParser.SEMICOLON)
                self.state = 351
                self.typeType()
                self.state = 356
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
        self.enterRule(localctx, 70, self.RULE_variableDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 357
                self.unionType()


            self.state = 360
            self.variable()
            self.state = 361
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
        self.enterRule(localctx, 72, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(BSParser.IDENTIFIER)
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 364
                self.match(BSParser.LBRACKET)
                self.state = 365
                self.match(BSParser.INTEGER_LITERAL)
                self.state = 366
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
        self.enterRule(localctx, 74, self.RULE_primary)
        try:
            self.state = 371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.STRING_LITERAL, BSParser.BOOL_LITERAL, BSParser.FLOAT_LITERAL, BSParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.literal()
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
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
        self.enterRule(localctx, 76, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
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
        self.enterRule(localctx, 78, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
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
        self.enterRule(localctx, 80, self.RULE_timeIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
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
        self.enterRule(localctx, 82, self.RULE_temperatureIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
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
        self.enterRule(localctx, 84, self.RULE_unitTracker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(BSParser.INTEGER_LITERAL)
            self.state = 382
            self.match(BSParser.UNITS)
            self.state = 383
            self.match(BSParser.OF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





