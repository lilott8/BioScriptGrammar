# Generated from /home/warfield/Github/BioScriptGrammar/grammar/BSParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

/* parser/listener/visitor header section */

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3j")
        buf.write("\u0184\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\3\2\3\2\3\2\3\2\3\2\7\2U\n\2\f\2\16\2X\13")
        buf.write("\2\3\2\3\2\3\2\7\2]\n\2\f\2\16\2`\13\2\3\2\3\2\3\3\3\3")
        buf.write("\7\3f\n\3\f\3\16\3i\13\3\3\4\3\4\6\4m\n\4\r\4\16\4n\3")
        buf.write("\5\3\5\7\5s\n\5\f\5\16\5v\13\5\3\6\3\6\3\6\3\6\5\6|\n")
        buf.write("\6\3\6\3\6\7\6\u0080\n\6\f\6\16\6\u0083\13\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\5\7\u008a\n\7\3\7\3\7\3\b\3\b\3\b\7\b\u0091")
        buf.write("\n\b\f\b\16\b\u0094\13\b\3\t\5\t\u0097\n\t\3\t\3\t\3\t")
        buf.write("\5\t\u009c\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\5\13\u00a7\n\13\3\f\3\f\7\f\u00ab\n\f\f\f\16\f\u00ae")
        buf.write("\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b9\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00c2\n\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00c9\n\17\3\20\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u00da\n\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u00e2\n\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u00ea\n\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3")
        buf.write("\27\3\27\3\27\3\27\5\27\u00f8\n\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u0116\n\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\7\31\u012a\n\31\f\31\16\31\u012d\13\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u013d\n\32\3\33\3\33\3\33\3\33\3\34\3")
        buf.write("\34\3\34\5\34\u0146\n\34\3\34\3\34\3\35\3\35\3\35\7\35")
        buf.write("\u014d\n\35\f\35\16\35\u0150\13\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \7 \u015b\n \f \16 \u015e\13 \3!\5")
        buf.write("!\u0161\n!\3!\3!\3!\5!\u0166\n!\3!\5!\u0169\n!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0174\n\"\3#\3#\3$\3$\3")
        buf.write("%\3%\5%\u017c\n%\3%\3%\3&\3&\3\'\3\'\3\'\2\3\60(\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJL\2\n\4\2!!%%\4\2JKOO\3\2HI\4\2:;AB\4\2@@CC")
        buf.write("\3\2$%\3\2\"%\3\2\35 \2\u0195\2N\3\2\2\2\4g\3\2\2\2\6")
        buf.write("l\3\2\2\2\bt\3\2\2\2\nw\3\2\2\2\f\u0087\3\2\2\2\16\u008d")
        buf.write("\3\2\2\2\20\u0096\3\2\2\2\22\u009d\3\2\2\2\24\u00a6\3")
        buf.write("\2\2\2\26\u00a8\3\2\2\2\30\u00b8\3\2\2\2\32\u00c1\3\2")
        buf.write("\2\2\34\u00c3\3\2\2\2\36\u00ca\3\2\2\2 \u00ce\3\2\2\2")
        buf.write("\"\u00d3\3\2\2\2$\u00db\3\2\2\2&\u00e3\3\2\2\2(\u00eb")
        buf.write("\3\2\2\2*\u00f0\3\2\2\2,\u00f7\3\2\2\2.\u00f9\3\2\2\2")
        buf.write("\60\u0104\3\2\2\2\62\u013c\3\2\2\2\64\u013e\3\2\2\2\66")
        buf.write("\u0142\3\2\2\28\u0149\3\2\2\2:\u0151\3\2\2\2<\u0153\3")
        buf.write("\2\2\2>\u0157\3\2\2\2@\u0160\3\2\2\2B\u0173\3\2\2\2D\u0175")
        buf.write("\3\2\2\2F\u0177\3\2\2\2H\u017b\3\2\2\2J\u017f\3\2\2\2")
        buf.write("L\u0181\3\2\2\2NO\5\4\3\2OP\5\b\5\2PQ\5\6\4\2QR\7\f\2")
        buf.write("\2RV\7?\2\2SU\5\n\6\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW")
        buf.write("\3\2\2\2WY\3\2\2\2XV\3\2\2\2YZ\7\r\2\2Z^\7?\2\2[]\5\32")
        buf.write("\16\2\\[\3\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_a\3\2")
        buf.write("\2\2`^\3\2\2\2ab\7\2\2\3b\3\3\2\2\2cd\7\n\2\2df\7!\2\2")
        buf.write("ec\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\5\3\2\2\2ig")
        buf.write("\3\2\2\2jk\7\t\2\2km\7!\2\2lj\3\2\2\2mn\3\2\2\2nl\3\2")
        buf.write("\2\2no\3\2\2\2o\7\3\2\2\2pq\7\13\2\2qs\7!\2\2rp\3\2\2")
        buf.write("\2sv\3\2\2\2tr\3\2\2\2tu\3\2\2\2u\t\3\2\2\2vt\3\2\2\2")
        buf.write("wx\7\7\2\2xy\7!\2\2y{\5\f\7\2z|\5\22\n\2{z\3\2\2\2{|\3")
        buf.write("\2\2\2|}\3\2\2\2}\u0081\7\62\2\2~\u0080\5\32\16\2\177")
        buf.write("~\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3\2\2\2\u0081")
        buf.write("\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081\3\2\2\2")
        buf.write("\u0084\u0085\5\24\13\2\u0085\u0086\7\63\2\2\u0086\13\3")
        buf.write("\2\2\2\u0087\u0089\7\60\2\2\u0088\u008a\5\16\b\2\u0089")
        buf.write("\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\3\2\2\2")
        buf.write("\u008b\u008c\7\61\2\2\u008c\r\3\2\2\2\u008d\u0092\5\20")
        buf.write("\t\2\u008e\u008f\7\67\2\2\u008f\u0091\5\20\t\2\u0090\u008e")
        buf.write("\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\17\3\2\2\2\u0094\u0092\3\2\2\2\u0095")
        buf.write("\u0097\5<\37\2\u0096\u0095\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\u009b\7!\2\2\u0099\u009a\7")
        buf.write("\64\2\2\u009a\u009c\7\65\2\2\u009b\u0099\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c\21\3\2\2\2\u009d\u009e\7?\2\2\u009e")
        buf.write("\u009f\5<\37\2\u009f\23\3\2\2\2\u00a0\u00a1\7\b\2\2\u00a1")
        buf.write("\u00a7\7!\2\2\u00a2\u00a3\7\b\2\2\u00a3\u00a7\5D#\2\u00a4")
        buf.write("\u00a5\7\b\2\2\u00a5\u00a7\5\66\34\2\u00a6\u00a0\3\2\2")
        buf.write("\2\u00a6\u00a2\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\25\3")
        buf.write("\2\2\2\u00a8\u00ac\7\62\2\2\u00a9\u00ab\5\32\16\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00ac\3")
        buf.write("\2\2\2\u00af\u00b0\7\63\2\2\u00b0\27\3\2\2\2\u00b1\u00b9")
        buf.write("\5\"\22\2\u00b2\u00b9\5*\26\2\u00b3\u00b9\5(\25\2\u00b4")
        buf.write("\u00b9\5\66\34\2\u00b5\u00b9\5$\23\2\u00b6\u00b9\5\60")
        buf.write("\31\2\u00b7\u00b9\5.\30\2\u00b8\u00b1\3\2\2\2\u00b8\u00b2")
        buf.write("\3\2\2\2\u00b8\u00b3\3\2\2\2\u00b8\u00b4\3\2\2\2\u00b8")
        buf.write("\u00b5\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2")
        buf.write("\u00b9\31\3\2\2\2\u00ba\u00c2\5\34\17\2\u00bb\u00c2\5")
        buf.write("\36\20\2\u00bc\u00c2\5@!\2\u00bd\u00c2\5 \21\2\u00be\u00c2")
        buf.write("\5&\24\2\u00bf\u00c2\5,\27\2\u00c0\u00c2\5\62\32\2\u00c1")
        buf.write("\u00ba\3\2\2\2\u00c1\u00bb\3\2\2\2\u00c1\u00bc\3\2\2\2")
        buf.write("\u00c1\u00bd\3\2\2\2\u00c1\u00be\3\2\2\2\u00c1\u00bf\3")
        buf.write("\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\33\3\2\2\2\u00c3\u00c4")
        buf.write("\7\3\2\2\u00c4\u00c5\5\64\33\2\u00c5\u00c8\5\26\f\2\u00c6")
        buf.write("\u00c7\7\4\2\2\u00c7\u00c9\5\26\f\2\u00c8\u00c6\3\2\2")
        buf.write("\2\u00c8\u00c9\3\2\2\2\u00c9\35\3\2\2\2\u00ca\u00cb\7")
        buf.write("\6\2\2\u00cb\u00cc\5\64\33\2\u00cc\u00cd\5\26\f\2\u00cd")
        buf.write("\37\3\2\2\2\u00ce\u00cf\7\5\2\2\u00cf\u00d0\t\2\2\2\u00d0")
        buf.write("\u00d1\7\32\2\2\u00d1\u00d2\5\26\f\2\u00d2!\3\2\2\2\u00d3")
        buf.write("\u00d4\7\17\2\2\u00d4\u00d5\5H%\2\u00d5\u00d6\7\27\2\2")
        buf.write("\u00d6\u00d9\5H%\2\u00d7\u00d8\7\30\2\2\u00d8\u00da\5")
        buf.write("J&\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da#\3")
        buf.write("\2\2\2\u00db\u00dc\7\16\2\2\u00dc\u00dd\7!\2\2\u00dd\u00de")
        buf.write("\7\33\2\2\u00de\u00e1\7!\2\2\u00df\u00e0\7\30\2\2\u00e0")
        buf.write("\u00e2\5J&\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("%\3\2\2\2\u00e3\u00e4\7\21\2\2\u00e4\u00e5\7!\2\2\u00e5")
        buf.write("\u00e6\7\26\2\2\u00e6\u00e9\5L\'\2\u00e7\u00e8\7\30\2")
        buf.write("\2\u00e8\u00ea\5J&\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3")
        buf.write("\2\2\2\u00ea\'\3\2\2\2\u00eb\u00ec\7\20\2\2\u00ec\u00ed")
        buf.write("\7!\2\2\u00ed\u00ee\7\31\2\2\u00ee\u00ef\7%\2\2\u00ef")
        buf.write(")\3\2\2\2\u00f0\u00f1\7\23\2\2\u00f1\u00f2\7!\2\2\u00f2")
        buf.write("+\3\2\2\2\u00f3\u00f4\7\22\2\2\u00f4\u00f8\7!\2\2\u00f5")
        buf.write("\u00f6\7\24\2\2\u00f6\u00f8\7!\2\2\u00f7\u00f3\3\2\2\2")
        buf.write("\u00f7\u00f5\3\2\2\2\u00f8-\3\2\2\2\u00f9\u00fa\7\25\2")
        buf.write("\2\u00fa\u00fb\7!\2\2\u00fb\u00fc\7\27\2\2\u00fc\u00fd")
        buf.write("\7!\2\2\u00fd\u00fe\7\30\2\2\u00fe\u00ff\7$\2\2\u00ff")
        buf.write("\u0100\7\67\2\2\u0100\u0101\7$\2\2\u0101\u0102\7\26\2")
        buf.write("\2\u0102\u0103\7$\2\2\u0103/\3\2\2\2\u0104\u0105\b\31")
        buf.write("\1\2\u0105\u0106\5B\"\2\u0106\u012b\3\2\2\2\u0107\u0108")
        buf.write("\f\t\2\2\u0108\u0109\t\3\2\2\u0109\u012a\5\60\31\n\u010a")
        buf.write("\u010b\f\b\2\2\u010b\u010c\t\4\2\2\u010c\u012a\5\60\31")
        buf.write("\t\u010d\u0115\f\7\2\2\u010e\u010f\7;\2\2\u010f\u0116")
        buf.write("\7;\2\2\u0110\u0111\7:\2\2\u0111\u0112\7:\2\2\u0112\u0116")
        buf.write("\7:\2\2\u0113\u0114\7:\2\2\u0114\u0116\7:\2\2\u0115\u010e")
        buf.write("\3\2\2\2\u0115\u0110\3\2\2\2\u0115\u0113\3\2\2\2\u0116")
        buf.write("\u0117\3\2\2\2\u0117\u012a\5\60\31\b\u0118\u0119\f\6\2")
        buf.write("\2\u0119\u011a\t\5\2\2\u011a\u012a\5\60\31\7\u011b\u011c")
        buf.write("\f\5\2\2\u011c\u011d\t\6\2\2\u011d\u012a\5\60\31\6\u011e")
        buf.write("\u011f\f\4\2\2\u011f\u0120\7D\2\2\u0120\u012a\5\60\31")
        buf.write("\5\u0121\u0122\f\3\2\2\u0122\u0123\7E\2\2\u0123\u012a")
        buf.write("\5\60\31\4\u0124\u0125\f\n\2\2\u0125\u0126\7\64\2\2\u0126")
        buf.write("\u0127\5\60\31\2\u0127\u0128\7\65\2\2\u0128\u012a\3\2")
        buf.write("\2\2\u0129\u0107\3\2\2\2\u0129\u010a\3\2\2\2\u0129\u010d")
        buf.write("\3\2\2\2\u0129\u0118\3\2\2\2\u0129\u011b\3\2\2\2\u0129")
        buf.write("\u011e\3\2\2\2\u0129\u0121\3\2\2\2\u0129\u0124\3\2\2\2")
        buf.write("\u012a\u012d\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3")
        buf.write("\2\2\2\u012c\61\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u012f")
        buf.write("\7)\2\2\u012f\u013d\t\7\2\2\u0130\u0131\7*\2\2\u0131\u013d")
        buf.write("\t\7\2\2\u0132\u0133\7+\2\2\u0133\u013d\t\7\2\2\u0134")
        buf.write("\u0135\7,\2\2\u0135\u013d\t\7\2\2\u0136\u0137\7-\2\2\u0137")
        buf.write("\u013d\t\7\2\2\u0138\u0139\7.\2\2\u0139\u013d\t\7\2\2")
        buf.write("\u013a\u013b\7/\2\2\u013b\u013d\t\7\2\2\u013c\u012e\3")
        buf.write("\2\2\2\u013c\u0130\3\2\2\2\u013c\u0132\3\2\2\2\u013c\u0134")
        buf.write("\3\2\2\2\u013c\u0136\3\2\2\2\u013c\u0138\3\2\2\2\u013c")
        buf.write("\u013a\3\2\2\2\u013d\63\3\2\2\2\u013e\u013f\7\60\2\2\u013f")
        buf.write("\u0140\5\60\31\2\u0140\u0141\7\61\2\2\u0141\65\3\2\2\2")
        buf.write("\u0142\u0143\7!\2\2\u0143\u0145\7\60\2\2\u0144\u0146\5")
        buf.write("8\35\2\u0145\u0144\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147")
        buf.write("\3\2\2\2\u0147\u0148\7\61\2\2\u0148\67\3\2\2\2\u0149\u014e")
        buf.write("\5\60\31\2\u014a\u014b\7\67\2\2\u014b\u014d\5\60\31\2")
        buf.write("\u014c\u014a\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3")
        buf.write("\2\2\2\u014e\u014f\3\2\2\2\u014f9\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0151\u0152\5F$\2\u0152;\3\2\2\2\u0153\u0154")
        buf.write("\7\64\2\2\u0154\u0155\5> \2\u0155\u0156\7\65\2\2\u0156")
        buf.write("=\3\2\2\2\u0157\u015c\5:\36\2\u0158\u0159\7\66\2\2\u0159")
        buf.write("\u015b\5:\36\2\u015a\u0158\3\2\2\2\u015b\u015e\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d?\3\2\2")
        buf.write("\2\u015e\u015c\3\2\2\2\u015f\u0161\5<\37\2\u0160\u015f")
        buf.write("\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0168\7!\2\2\u0163\u0165\7\64\2\2\u0164\u0166\7%\2\2")
        buf.write("\u0165\u0164\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\3")
        buf.write("\2\2\2\u0167\u0169\7\65\2\2\u0168\u0163\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\79\2\2")
        buf.write("\u016b\u016c\5\30\r\2\u016cA\3\2\2\2\u016d\u016e\7\60")
        buf.write("\2\2\u016e\u016f\5\60\31\2\u016f\u0170\7\61\2\2\u0170")
        buf.write("\u0174\3\2\2\2\u0171\u0174\5D#\2\u0172\u0174\7!\2\2\u0173")
        buf.write("\u016d\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0172\3\2\2\2")
        buf.write("\u0174C\3\2\2\2\u0175\u0176\t\b\2\2\u0176E\3\2\2\2\u0177")
        buf.write("\u0178\t\t\2\2\u0178G\3\2\2\2\u0179\u017a\7\'\2\2\u017a")
        buf.write("\u017c\7\34\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2")
        buf.write("\2\u017c\u017d\3\2\2\2\u017d\u017e\7!\2\2\u017eI\3\2\2")
        buf.write("\2\u017f\u0180\7&\2\2\u0180K\3\2\2\2\u0181\u0182\7(\2")
        buf.write("\2\u0182M\3\2\2\2\"V^gnt{\u0081\u0089\u0092\u0096\u009b")
        buf.write("\u00a6\u00ac\u00b8\u00c1\u00c8\u00d9\u00e1\u00e9\u00f7")
        buf.write("\u0115\u0129\u012b\u013c\u0145\u014e\u015c\u0160\u0165")
        buf.write("\u0168\u0173\u017b")
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
                     "'dispose'", "'gradient'", "'at'", "'with'", "'for'", 
                     "'into'", "'times'", "'on'", "'of'", "'nat'", "'real'", 
                     "'mat'", "'bool'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'mass'", "'efficiency'", "'pressure'", 
                     "'force'", "'speed'", "'friction'", "'useby'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", 
                     "'='", "'>'", "'<'", "'!'", "'~'", "'?'", "':'", "'=='", 
                     "'<='", "'>='", "'!='", "'&&'", "'||'", "'++'", "'--'", 
                     "'+'", "'-'", "'*'", "'/'", "'&'", "'|'", "'^'", "'%'", 
                     "'_'", "'@'", "'ns'", "'us'", "'ms'", "'cs'", "'ds'", 
                     "'s'", "'m'", "'h'", "'d'", "'w'", "'mo'", "'y'", "'nL'", 
                     "'uL'", "'mL'", "'cL'", "'dL'", "'L'", "'daL'", "'c'", 
                     "'f'", "'k'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", 
                      "RETURN", "MANIFEST", "MODULE", "STATIONARY", "FUNCTIONS", 
                      "INSTRUCTIONS", "DETECT", "MIX", "SPLIT", "HEAT", 
                      "DRAIN", "DISPENSE", "DISPOSE", "GRADIENT", "AT", 
                      "WITH", "FOR", "INTO", "TIMES", "ON", "OF", "NAT", 
                      "REAL", "MAT", "BOOL", "IDENTIFIER", "STRING_LITERAL", 
                      "BOOL_LITERAL", "FLOAT_LITERAL", "INTEGER_LITERAL", 
                      "TIME_NUMBER", "VOLUME_NUMBER", "TEMP_NUMBER", "MASS_NUMBER", 
                      "EFFICIENCY_NUMBER", "PRESSURE_NUMBER", "FORCE_NUMBER", 
                      "SPEED_NUMBER", "FRICTION_NUMBER", "USEBY", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                      "SEMICOLON", "COMMA", "DOT", "ASSIGN", "GT", "LT", 
                      "BANG", "TILDE", "QUESTION", "COLON", "EQUALITY", 
                      "LTE", "GTE", "NOTEQUAL", "AND", "OR", "INC", "DEC", 
                      "ADDITION", "SUBTRACT", "MULTIPLY", "DIVIDE", "BITAND", 
                      "BITOR", "CARET", "MOD", "UNDERSCORE", "AT_SYMBOL", 
                      "NANOSECOND", "MICROSECOND", "MILLISECOND", "CENTISECOND", 
                      "DECISECOND", "SECOND", "MINUTE", "HOUR", "DAY", "WEEK", 
                      "MONTH", "YEAR", "NANOLITRE", "MICROLITRE", "MILLILITRE", 
                      "CENTILITRE", "DECILITRE", "LITRE", "DECALITRE", "CELSIUS", 
                      "FAHRENHEIT", "KELVIN", "WS", "COMMENT", "LINE_COMMENT" ]

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
    RULE_variableDeclaration = 11
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
    RULE_gradient = 22
    RULE_expression = 23
    RULE_physic_annotation = 24
    RULE_parExpression = 25
    RULE_methodCall = 26
    RULE_expressionList = 27
    RULE_typeType = 28
    RULE_unionType = 29
    RULE_typesList = 30
    RULE_variableDefinition = 31
    RULE_primary = 32
    RULE_literal = 33
    RULE_primitiveType = 34
    RULE_volumeIdentifier = 35
    RULE_timeIdentifier = 36
    RULE_temperatureIdentifier = 37

    ruleNames =  [ "program", "moduleDeclaration", "manifestDeclaration", 
                   "stationaryDeclaration", "functionDeclaration", "formalParameters", 
                   "formalParameterList", "formalParameter", "functionTyping", 
                   "returnStatement", "blockStatement", "variableDeclaration", 
                   "statements", "ifStatement", "whileStatement", "repeat", 
                   "mix", "detect", "heat", "split", "dispense", "dispose", 
                   "gradient", "expression", "physic_annotation", "parExpression", 
                   "methodCall", "expressionList", "typeType", "unionType", 
                   "typesList", "variableDefinition", "primary", "literal", 
                   "primitiveType", "volumeIdentifier", "timeIdentifier", 
                   "temperatureIdentifier" ]

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
    AT=20
    WITH=21
    FOR=22
    INTO=23
    TIMES=24
    ON=25
    OF=26
    NAT=27
    REAL=28
    MAT=29
    BOOL=30
    IDENTIFIER=31
    STRING_LITERAL=32
    BOOL_LITERAL=33
    FLOAT_LITERAL=34
    INTEGER_LITERAL=35
    TIME_NUMBER=36
    VOLUME_NUMBER=37
    TEMP_NUMBER=38
    MASS_NUMBER=39
    EFFICIENCY_NUMBER=40
    PRESSURE_NUMBER=41
    FORCE_NUMBER=42
    SPEED_NUMBER=43
    FRICTION_NUMBER=44
    USEBY=45
    LPAREN=46
    RPAREN=47
    LBRACE=48
    RBRACE=49
    LBRACKET=50
    RBRACKET=51
    SEMICOLON=52
    COMMA=53
    DOT=54
    ASSIGN=55
    GT=56
    LT=57
    BANG=58
    TILDE=59
    QUESTION=60
    COLON=61
    EQUALITY=62
    LTE=63
    GTE=64
    NOTEQUAL=65
    AND=66
    OR=67
    INC=68
    DEC=69
    ADDITION=70
    SUBTRACT=71
    MULTIPLY=72
    DIVIDE=73
    BITAND=74
    BITOR=75
    CARET=76
    MOD=77
    UNDERSCORE=78
    AT_SYMBOL=79
    NANOSECOND=80
    MICROSECOND=81
    MILLISECOND=82
    CENTISECOND=83
    DECISECOND=84
    SECOND=85
    MINUTE=86
    HOUR=87
    DAY=88
    WEEK=89
    MONTH=90
    YEAR=91
    NANOLITRE=92
    MICROLITRE=93
    MILLILITRE=94
    CENTILITRE=95
    DECILITRE=96
    LITRE=97
    DECALITRE=98
    CELSIUS=99
    FAHRENHEIT=100
    KELVIN=101
    WS=102
    COMMENT=103
    LINE_COMMENT=104

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.MASS_NUMBER) | (1 << BSParser.EFFICIENCY_NUMBER) | (1 << BSParser.PRESSURE_NUMBER) | (1 << BSParser.FORCE_NUMBER) | (1 << BSParser.SPEED_NUMBER) | (1 << BSParser.FRICTION_NUMBER) | (1 << BSParser.USEBY) | (1 << BSParser.LBRACKET))) != 0):
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
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.MASS_NUMBER) | (1 << BSParser.EFFICIENCY_NUMBER) | (1 << BSParser.PRESSURE_NUMBER) | (1 << BSParser.FORCE_NUMBER) | (1 << BSParser.SPEED_NUMBER) | (1 << BSParser.FRICTION_NUMBER) | (1 << BSParser.USEBY) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 124
                self.statements()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self.returnStatement()
            self.state = 131
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
            self.state = 133
            self.match(BSParser.LPAREN)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.IDENTIFIER or _la==BSParser.LBRACKET:
                self.state = 134
                self.formalParameterList()


            self.state = 137
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
            self.state = 139
            self.formalParameter()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 140
                self.match(BSParser.COMMA)
                self.state = 141
                self.formalParameter()
                self.state = 146
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
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 147
                self.unionType()


            self.state = 150
            self.match(BSParser.IDENTIFIER)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 151
                self.match(BSParser.LBRACKET)
                self.state = 152
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
            self.state = 155
            self.match(BSParser.COLON)
            self.state = 156
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




    def returnStatement(self):

        localctx = BSParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_returnStatement)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(BSParser.RETURN)
                self.state = 159
                self.match(BSParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(BSParser.RETURN)
                self.state = 161
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.match(BSParser.RETURN)
                self.state = 163
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




    def blockStatement(self):

        localctx = BSParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(BSParser.LBRACE)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.MASS_NUMBER) | (1 << BSParser.EFFICIENCY_NUMBER) | (1 << BSParser.PRESSURE_NUMBER) | (1 << BSParser.FORCE_NUMBER) | (1 << BSParser.SPEED_NUMBER) | (1 << BSParser.FRICTION_NUMBER) | (1 << BSParser.USEBY) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 167
                self.statements()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
            self.match(BSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):

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


        def detect(self):
            return self.getTypedRuleContext(BSParser.DetectContext,0)


        def expression(self):
            return self.getTypedRuleContext(BSParser.ExpressionContext,0)


        def gradient(self):
            return self.getTypedRuleContext(BSParser.GradientContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = BSParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_variableDeclaration)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.mix()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.dispense()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.split()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.methodCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 179
                self.detect()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 180
                self.expression(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 181
                self.gradient()
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


        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def repeat(self):
            return self.getTypedRuleContext(BSParser.RepeatContext,0)


        def heat(self):
            return self.getTypedRuleContext(BSParser.HeatContext,0)


        def dispose(self):
            return self.getTypedRuleContext(BSParser.DisposeContext,0)


        def physic_annotation(self):
            return self.getTypedRuleContext(BSParser.Physic_annotationContext,0)


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
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.ifStatement()
                pass
            elif token in [BSParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.whileStatement()
                pass
            elif token in [BSParser.IDENTIFIER, BSParser.LBRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.variableDefinition()
                pass
            elif token in [BSParser.REPEAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.repeat()
                pass
            elif token in [BSParser.HEAT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 188
                self.heat()
                pass
            elif token in [BSParser.DRAIN, BSParser.DISPOSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 189
                self.dispose()
                pass
            elif token in [BSParser.MASS_NUMBER, BSParser.EFFICIENCY_NUMBER, BSParser.PRESSURE_NUMBER, BSParser.FORCE_NUMBER, BSParser.SPEED_NUMBER, BSParser.FRICTION_NUMBER, BSParser.USEBY]:
                self.enterOuterAlt(localctx, 7)
                self.state = 190
                self.physic_annotation()
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
            self.state = 193
            self.match(BSParser.IF)
            self.state = 194
            self.parExpression()
            self.state = 195
            self.blockStatement()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ELSE:
                self.state = 196
                self.match(BSParser.ELSE)
                self.state = 197
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
            self.state = 200
            self.match(BSParser.WHILE)
            self.state = 201
            self.parExpression()
            self.state = 202
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
            self.state = 204
            self.match(BSParser.REPEAT)
            self.state = 205
            _la = self._input.LA(1)
            if not(_la==BSParser.IDENTIFIER or _la==BSParser.INTEGER_LITERAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 206
            self.match(BSParser.TIMES)
            self.state = 207
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
            self.state = 209
            self.match(BSParser.MIX)
            self.state = 210
            self.volumeIdentifier()
            self.state = 211
            self.match(BSParser.WITH)
            self.state = 212
            self.volumeIdentifier()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 213
                self.match(BSParser.FOR)
                self.state = 214
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
            self.state = 217
            self.match(BSParser.DETECT)
            self.state = 218
            self.match(BSParser.IDENTIFIER)
            self.state = 219
            self.match(BSParser.ON)
            self.state = 220
            self.match(BSParser.IDENTIFIER)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 221
                self.match(BSParser.FOR)
                self.state = 222
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
            self.state = 225
            self.match(BSParser.HEAT)
            self.state = 226
            self.match(BSParser.IDENTIFIER)
            self.state = 227
            self.match(BSParser.AT)
            self.state = 228
            self.temperatureIdentifier()
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 229
                self.match(BSParser.FOR)
                self.state = 230
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
            self.state = 233
            self.match(BSParser.SPLIT)
            self.state = 234
            self.match(BSParser.IDENTIFIER)
            self.state = 235
            self.match(BSParser.INTO)
            self.state = 236
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
            self.state = 238
            self.match(BSParser.DISPENSE)
            self.state = 239
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
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.DRAIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(BSParser.DRAIN)
                self.state = 242
                self.match(BSParser.IDENTIFIER)
                pass
            elif token in [BSParser.DISPOSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(BSParser.DISPOSE)
                self.state = 244
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


    class GradientContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRADIENT(self):
            return self.getToken(BSParser.GRADIENT, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.IDENTIFIER)
            else:
                return self.getToken(BSParser.IDENTIFIER, i)

        def WITH(self):
            return self.getToken(BSParser.WITH, 0)

        def FOR(self):
            return self.getToken(BSParser.FOR, 0)

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




    def gradient(self):

        localctx = BSParser.GradientContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_gradient)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(BSParser.GRADIENT)
            self.state = 248
            self.match(BSParser.IDENTIFIER)
            self.state = 249
            self.match(BSParser.WITH)
            self.state = 250
            self.match(BSParser.IDENTIFIER)
            self.state = 251
            self.match(BSParser.FOR)
            self.state = 252
            self.match(BSParser.FLOAT_LITERAL)
            self.state = 253
            self.match(BSParser.COMMA)
            self.state = 254
            self.match(BSParser.FLOAT_LITERAL)
            self.state = 255
            self.match(BSParser.AT)
            self.state = 256
            self.match(BSParser.FLOAT_LITERAL)
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

        def MOD(self):
            return self.getToken(BSParser.MOD, 0)

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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.primary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 295
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 261
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 262
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & ((1 << (BSParser.MULTIPLY - 72)) | (1 << (BSParser.DIVIDE - 72)) | (1 << (BSParser.MOD - 72)))) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 263
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 264
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 265
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BSParser.ADDITION or _la==BSParser.SUBTRACT):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 266
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 267
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 275
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                        if la_ == 1:
                            self.state = 268
                            self.match(BSParser.LT)
                            self.state = 269
                            self.match(BSParser.LT)
                            pass

                        elif la_ == 2:
                            self.state = 270
                            self.match(BSParser.GT)
                            self.state = 271
                            self.match(BSParser.GT)
                            self.state = 272
                            self.match(BSParser.GT)
                            pass

                        elif la_ == 3:
                            self.state = 273
                            self.match(BSParser.GT)
                            self.state = 274
                            self.match(BSParser.GT)
                            pass


                        self.state = 277
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 278
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 279
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((((_la - 56)) & ~0x3f) == 0 and ((1 << (_la - 56)) & ((1 << (BSParser.GT - 56)) | (1 << (BSParser.LT - 56)) | (1 << (BSParser.LTE - 56)) | (1 << (BSParser.GTE - 56)))) != 0)):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 280
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 281
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 282
                        localctx.bop = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BSParser.EQUALITY or _la==BSParser.NOTEQUAL):
                            localctx.bop = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 283
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 284
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 285
                        localctx.bop = self.match(BSParser.AND)
                        self.state = 286
                        self.expression(3)
                        pass

                    elif la_ == 7:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 287
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 288
                        localctx.bop = self.match(BSParser.OR)
                        self.state = 289
                        self.expression(2)
                        pass

                    elif la_ == 8:
                        localctx = BSParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 290
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 291
                        self.match(BSParser.LBRACKET)
                        self.state = 292
                        self.expression(0)
                        self.state = 293
                        self.match(BSParser.RBRACKET)
                        pass

             
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Physic_annotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MASS_NUMBER(self):
            return self.getToken(BSParser.MASS_NUMBER, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(BSParser.FLOAT_LITERAL, 0)

        def EFFICIENCY_NUMBER(self):
            return self.getToken(BSParser.EFFICIENCY_NUMBER, 0)

        def PRESSURE_NUMBER(self):
            return self.getToken(BSParser.PRESSURE_NUMBER, 0)

        def FORCE_NUMBER(self):
            return self.getToken(BSParser.FORCE_NUMBER, 0)

        def SPEED_NUMBER(self):
            return self.getToken(BSParser.SPEED_NUMBER, 0)

        def FRICTION_NUMBER(self):
            return self.getToken(BSParser.FRICTION_NUMBER, 0)

        def USEBY(self):
            return self.getToken(BSParser.USEBY, 0)

        def getRuleIndex(self):
            return BSParser.RULE_physic_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhysic_annotation" ):
                listener.enterPhysic_annotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhysic_annotation" ):
                listener.exitPhysic_annotation(self)




    def physic_annotation(self):

        localctx = BSParser.Physic_annotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_physic_annotation)
        self._la = 0 # Token type
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.MASS_NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(BSParser.MASS_NUMBER)
                self.state = 301
                _la = self._input.LA(1)
                if not(_la==BSParser.FLOAT_LITERAL or _la==BSParser.INTEGER_LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [BSParser.EFFICIENCY_NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.match(BSParser.EFFICIENCY_NUMBER)
                self.state = 303
                _la = self._input.LA(1)
                if not(_la==BSParser.FLOAT_LITERAL or _la==BSParser.INTEGER_LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [BSParser.PRESSURE_NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.match(BSParser.PRESSURE_NUMBER)
                self.state = 305
                _la = self._input.LA(1)
                if not(_la==BSParser.FLOAT_LITERAL or _la==BSParser.INTEGER_LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [BSParser.FORCE_NUMBER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 306
                self.match(BSParser.FORCE_NUMBER)
                self.state = 307
                _la = self._input.LA(1)
                if not(_la==BSParser.FLOAT_LITERAL or _la==BSParser.INTEGER_LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [BSParser.SPEED_NUMBER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 308
                self.match(BSParser.SPEED_NUMBER)
                self.state = 309
                _la = self._input.LA(1)
                if not(_la==BSParser.FLOAT_LITERAL or _la==BSParser.INTEGER_LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [BSParser.FRICTION_NUMBER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 310
                self.match(BSParser.FRICTION_NUMBER)
                self.state = 311
                _la = self._input.LA(1)
                if not(_la==BSParser.FLOAT_LITERAL or _la==BSParser.INTEGER_LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [BSParser.USEBY]:
                self.enterOuterAlt(localctx, 7)
                self.state = 312
                self.match(BSParser.USEBY)
                self.state = 313
                _la = self._input.LA(1)
                if not(_la==BSParser.FLOAT_LITERAL or _la==BSParser.INTEGER_LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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
        self.enterRule(localctx, 50, self.RULE_parExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(BSParser.LPAREN)
            self.state = 317
            self.expression(0)
            self.state = 318
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
        self.enterRule(localctx, 52, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(BSParser.IDENTIFIER)
            self.state = 321
            self.match(BSParser.LPAREN)
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IDENTIFIER) | (1 << BSParser.STRING_LITERAL) | (1 << BSParser.BOOL_LITERAL) | (1 << BSParser.FLOAT_LITERAL) | (1 << BSParser.INTEGER_LITERAL) | (1 << BSParser.LPAREN))) != 0):
                self.state = 322
                self.expressionList()


            self.state = 325
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
        self.enterRule(localctx, 54, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.expression(0)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 328
                self.match(BSParser.COMMA)
                self.state = 329
                self.expression(0)
                self.state = 334
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
        self.enterRule(localctx, 56, self.RULE_typeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
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
        self.enterRule(localctx, 58, self.RULE_unionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(BSParser.LBRACKET)
            self.state = 338
            self.typesList()
            self.state = 339
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
        self.enterRule(localctx, 60, self.RULE_typesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.typeType()
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.SEMICOLON:
                self.state = 342
                self.match(BSParser.SEMICOLON)
                self.state = 343
                self.typeType()
                self.state = 348
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

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(BSParser.ASSIGN, 0)

        def variableDeclaration(self):
            return self.getTypedRuleContext(BSParser.VariableDeclarationContext,0)


        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def getRuleIndex(self):
            return BSParser.RULE_variableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDefinition" ):
                listener.enterVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDefinition" ):
                listener.exitVariableDefinition(self)




    def variableDefinition(self):

        localctx = BSParser.VariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_variableDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 349
                self.unionType()


            self.state = 352
            self.match(BSParser.IDENTIFIER)
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 353
                self.match(BSParser.LBRACKET)
                self.state = 355
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.INTEGER_LITERAL:
                    self.state = 354
                    self.match(BSParser.INTEGER_LITERAL)


                self.state = 357
                self.match(BSParser.RBRACKET)


            self.state = 360
            self.match(BSParser.ASSIGN)
            self.state = 361
            self.variableDeclaration()
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
        self.enterRule(localctx, 64, self.RULE_primary)
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(BSParser.LPAREN)
                self.state = 364
                self.expression(0)
                self.state = 365
                self.match(BSParser.RPAREN)
                pass
            elif token in [BSParser.STRING_LITERAL, BSParser.BOOL_LITERAL, BSParser.FLOAT_LITERAL, BSParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.literal()
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
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
        self.enterRule(localctx, 66, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
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
        self.enterRule(localctx, 68, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
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
        self.enterRule(localctx, 70, self.RULE_volumeIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.VOLUME_NUMBER:
                self.state = 375
                self.match(BSParser.VOLUME_NUMBER)
                self.state = 376
                self.match(BSParser.OF)


            self.state = 379
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
        self.enterRule(localctx, 72, self.RULE_timeIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
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
        self.enterRule(localctx, 74, self.RULE_temperatureIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
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
         




