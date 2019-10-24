# Generated from /bioscriptgrammar/grammar/BSLexer.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2e")
        buf.write("\u02d1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\7#\u01ac")
        buf.write("\n#\f#\16#\u01af\13#\3$\3$\3$\7$\u01b4\n$\f$\16$\u01b7")
        buf.write("\13$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01c4\n%\3&\3")
        buf.write("&\3&\5&\u01c9\n&\3&\3&\5&\u01cd\n&\3\'\3\'\7\'\u01d1\n")
        buf.write("\'\f\'\16\'\u01d4\13\'\3(\3(\5(\u01d8\n(\3(\3(\3)\3)\5")
        buf.write(")\u01de\n)\3)\3)\3*\3*\5*\u01e4\n*\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\3")
        buf.write("9\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3")
        buf.write("@\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3")
        buf.write("G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3L\3M\3M\3M\3N\3N\3N\3")
        buf.write("O\3O\3O\3P\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3")
        buf.write("V\3W\3W\3X\3X\3X\3Y\3Y\3Y\3Z\3Z\3Z\3[\3[\3[\3\\\3\\\3")
        buf.write("\\\3]\3]\3^\3^\3^\3^\3_\3_\3`\3`\3a\3a\3b\6b\u026c\nb")
        buf.write("\rb\16b\u026d\3b\3b\3c\3c\3c\3c\7c\u0276\nc\fc\16c\u0279")
        buf.write("\13c\3c\3c\3c\3c\3c\3d\3d\3d\3d\7d\u0284\nd\fd\16d\u0287")
        buf.write("\13d\3d\3d\3e\3e\3e\3e\3e\3e\3e\3e\3e\3e\3e\3e\5e\u0297")
        buf.write("\ne\3f\3f\3f\3f\3f\3f\5f\u029f\nf\3g\3g\3g\5g\u02a4\n")
        buf.write("g\3h\3h\7h\u02a8\nh\fh\16h\u02ab\13h\3h\5h\u02ae\nh\3")
        buf.write("i\3i\5i\u02b2\ni\3j\3j\3j\3j\5j\u02b8\nj\3k\3k\3k\3k\5")
        buf.write("k\u02be\nk\3k\5k\u02c1\nk\3k\5k\u02c4\nk\3l\6l\u02c7\n")
        buf.write("l\rl\16l\u02c8\3m\5m\u02cc\nm\3m\3m\5m\u02d0\nm\3\u0277")
        buf.write("\2n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F")
        buf.write("\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099")
        buf.write("N\u009bO\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7U\u00a9")
        buf.write("V\u00abW\u00adX\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7]\u00b9")
        buf.write("^\u00bb_\u00bd`\u00bfa\u00c1b\u00c3c\u00c5d\u00c7e\u00c9")
        buf.write("\2\u00cb\2\u00cd\2\u00cf\2\u00d1\2\u00d3\2\u00d5\2\u00d7")
        buf.write("\2\u00d9\2\3\2\17\6\2\f\f\17\17$$^^\5\2\13\f\16\17\"\"")
        buf.write("\4\2\f\f\17\17\3\2\62;\4\2\62;aa\6\2&&C\\aac|\4\2\2\u0081")
        buf.write("\ud802\udc01\3\2\ud802\udc01\3\2\udc02\ue001\n\2$$))^")
        buf.write("^ddhhppttvv\3\2\62\65\3\2\629\4\2\13\13\"\"\2\u02f1\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2")
        buf.write("\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\3\u00db")
        buf.write("\3\2\2\2\5\u00de\3\2\2\2\7\u00e3\3\2\2\2\t\u00ea\3\2\2")
        buf.write("\2\13\u00f0\3\2\2\2\r\u00f9\3\2\2\2\17\u0100\3\2\2\2\21")
        buf.write("\u0109\3\2\2\2\23\u0110\3\2\2\2\25\u011b\3\2\2\2\27\u0125")
        buf.write("\3\2\2\2\31\u0132\3\2\2\2\33\u0139\3\2\2\2\35\u013d\3")
        buf.write("\2\2\2\37\u0143\3\2\2\2!\u0148\3\2\2\2#\u014e\3\2\2\2")
        buf.write("%\u0157\3\2\2\2\'\u015f\3\2\2\2)\u0168\3\2\2\2+\u016e")
        buf.write("\3\2\2\2-\u0174\3\2\2\2/\u0177\3\2\2\2\61\u017c\3\2\2")
        buf.write("\2\63\u0180\3\2\2\2\65\u0185\3\2\2\2\67\u018b\3\2\2\2")
        buf.write("9\u018e\3\2\2\2;\u0191\3\2\2\2=\u0197\3\2\2\2?\u019b\3")
        buf.write("\2\2\2A\u01a0\3\2\2\2C\u01a4\3\2\2\2E\u01a9\3\2\2\2G\u01b0")
        buf.write("\3\2\2\2I\u01c3\3\2\2\2K\u01cc\3\2\2\2M\u01ce\3\2\2\2")
        buf.write("O\u01d7\3\2\2\2Q\u01dd\3\2\2\2S\u01e3\3\2\2\2U\u01e7\3")
        buf.write("\2\2\2W\u01e9\3\2\2\2Y\u01eb\3\2\2\2[\u01ed\3\2\2\2]\u01ef")
        buf.write("\3\2\2\2_\u01f1\3\2\2\2a\u01f3\3\2\2\2c\u01f5\3\2\2\2")
        buf.write("e\u01f7\3\2\2\2g\u01f9\3\2\2\2i\u01fb\3\2\2\2k\u01fd\3")
        buf.write("\2\2\2m\u01ff\3\2\2\2o\u0201\3\2\2\2q\u0203\3\2\2\2s\u0205")
        buf.write("\3\2\2\2u\u0207\3\2\2\2w\u020a\3\2\2\2y\u020d\3\2\2\2")
        buf.write("{\u0210\3\2\2\2}\u0213\3\2\2\2\177\u0216\3\2\2\2\u0081")
        buf.write("\u0219\3\2\2\2\u0083\u021c\3\2\2\2\u0085\u021f\3\2\2\2")
        buf.write("\u0087\u0221\3\2\2\2\u0089\u0223\3\2\2\2\u008b\u0225\3")
        buf.write("\2\2\2\u008d\u0227\3\2\2\2\u008f\u0229\3\2\2\2\u0091\u022b")
        buf.write("\3\2\2\2\u0093\u022d\3\2\2\2\u0095\u022f\3\2\2\2\u0097")
        buf.write("\u0231\3\2\2\2\u0099\u0234\3\2\2\2\u009b\u0237\3\2\2\2")
        buf.write("\u009d\u023a\3\2\2\2\u009f\u023d\3\2\2\2\u00a1\u0240\3")
        buf.write("\2\2\2\u00a3\u0242\3\2\2\2\u00a5\u0244\3\2\2\2\u00a7\u0246")
        buf.write("\3\2\2\2\u00a9\u0248\3\2\2\2\u00ab\u024a\3\2\2\2\u00ad")
        buf.write("\u024d\3\2\2\2\u00af\u024f\3\2\2\2\u00b1\u0252\3\2\2\2")
        buf.write("\u00b3\u0255\3\2\2\2\u00b5\u0258\3\2\2\2\u00b7\u025b\3")
        buf.write("\2\2\2\u00b9\u025e\3\2\2\2\u00bb\u0260\3\2\2\2\u00bd\u0264")
        buf.write("\3\2\2\2\u00bf\u0266\3\2\2\2\u00c1\u0268\3\2\2\2\u00c3")
        buf.write("\u026b\3\2\2\2\u00c5\u0271\3\2\2\2\u00c7\u027f\3\2\2\2")
        buf.write("\u00c9\u0296\3\2\2\2\u00cb\u029e\3\2\2\2\u00cd\u02a3\3")
        buf.write("\2\2\2\u00cf\u02a5\3\2\2\2\u00d1\u02b1\3\2\2\2\u00d3\u02b7")
        buf.write("\3\2\2\2\u00d5\u02c3\3\2\2\2\u00d7\u02c6\3\2\2\2\u00d9")
        buf.write("\u02cf\3\2\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7h\2\2\u00dd")
        buf.write("\4\3\2\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7n\2\2\u00e0")
        buf.write("\u00e1\7u\2\2\u00e1\u00e2\7g\2\2\u00e2\6\3\2\2\2\u00e3")
        buf.write("\u00e4\7t\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7r\2\2\u00e6")
        buf.write("\u00e7\7g\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7v\2\2\u00e9")
        buf.write("\b\3\2\2\2\u00ea\u00eb\7y\2\2\u00eb\u00ec\7j\2\2\u00ec")
        buf.write("\u00ed\7k\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef\7g\2\2\u00ef")
        buf.write("\n\3\2\2\2\u00f0\u00f1\7h\2\2\u00f1\u00f2\7w\2\2\u00f2")
        buf.write("\u00f3\7p\2\2\u00f3\u00f4\7e\2\2\u00f4\u00f5\7v\2\2\u00f5")
        buf.write("\u00f6\7k\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7p\2\2\u00f8")
        buf.write("\f\3\2\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb\7g\2\2\u00fb")
        buf.write("\u00fc\7v\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe\7t\2\2\u00fe")
        buf.write("\u00ff\7p\2\2\u00ff\16\3\2\2\2\u0100\u0101\7o\2\2\u0101")
        buf.write("\u0102\7c\2\2\u0102\u0103\7p\2\2\u0103\u0104\7k\2\2\u0104")
        buf.write("\u0105\7h\2\2\u0105\u0106\7g\2\2\u0106\u0107\7u\2\2\u0107")
        buf.write("\u0108\7v\2\2\u0108\20\3\2\2\2\u0109\u010a\7o\2\2\u010a")
        buf.write("\u010b\7q\2\2\u010b\u010c\7f\2\2\u010c\u010d\7w\2\2\u010d")
        buf.write("\u010e\7n\2\2\u010e\u010f\7g\2\2\u010f\22\3\2\2\2\u0110")
        buf.write("\u0111\7u\2\2\u0111\u0112\7v\2\2\u0112\u0113\7c\2\2\u0113")
        buf.write("\u0114\7v\2\2\u0114\u0115\7k\2\2\u0115\u0116\7q\2\2\u0116")
        buf.write("\u0117\7p\2\2\u0117\u0118\7c\2\2\u0118\u0119\7t\2\2\u0119")
        buf.write("\u011a\7{\2\2\u011a\24\3\2\2\2\u011b\u011c\7h\2\2\u011c")
        buf.write("\u011d\7w\2\2\u011d\u011e\7p\2\2\u011e\u011f\7e\2\2\u011f")
        buf.write("\u0120\7v\2\2\u0120\u0121\7k\2\2\u0121\u0122\7q\2\2\u0122")
        buf.write("\u0123\7p\2\2\u0123\u0124\7u\2\2\u0124\26\3\2\2\2\u0125")
        buf.write("\u0126\7k\2\2\u0126\u0127\7p\2\2\u0127\u0128\7u\2\2\u0128")
        buf.write("\u0129\7v\2\2\u0129\u012a\7t\2\2\u012a\u012b\7w\2\2\u012b")
        buf.write("\u012c\7e\2\2\u012c\u012d\7v\2\2\u012d\u012e\7k\2\2\u012e")
        buf.write("\u012f\7q\2\2\u012f\u0130\7p\2\2\u0130\u0131\7u\2\2\u0131")
        buf.write("\30\3\2\2\2\u0132\u0133\7f\2\2\u0133\u0134\7g\2\2\u0134")
        buf.write("\u0135\7v\2\2\u0135\u0136\7g\2\2\u0136\u0137\7e\2\2\u0137")
        buf.write("\u0138\7v\2\2\u0138\32\3\2\2\2\u0139\u013a\7o\2\2\u013a")
        buf.write("\u013b\7k\2\2\u013b\u013c\7z\2\2\u013c\34\3\2\2\2\u013d")
        buf.write("\u013e\7u\2\2\u013e\u013f\7r\2\2\u013f\u0140\7n\2\2\u0140")
        buf.write("\u0141\7k\2\2\u0141\u0142\7v\2\2\u0142\36\3\2\2\2\u0143")
        buf.write("\u0144\7j\2\2\u0144\u0145\7g\2\2\u0145\u0146\7c\2\2\u0146")
        buf.write("\u0147\7v\2\2\u0147 \3\2\2\2\u0148\u0149\7f\2\2\u0149")
        buf.write("\u014a\7t\2\2\u014a\u014b\7c\2\2\u014b\u014c\7k\2\2\u014c")
        buf.write("\u014d\7p\2\2\u014d\"\3\2\2\2\u014e\u014f\7f\2\2\u014f")
        buf.write("\u0150\7k\2\2\u0150\u0151\7u\2\2\u0151\u0152\7r\2\2\u0152")
        buf.write("\u0153\7g\2\2\u0153\u0154\7p\2\2\u0154\u0155\7u\2\2\u0155")
        buf.write("\u0156\7g\2\2\u0156$\3\2\2\2\u0157\u0158\7f\2\2\u0158")
        buf.write("\u0159\7k\2\2\u0159\u015a\7u\2\2\u015a\u015b\7r\2\2\u015b")
        buf.write("\u015c\7q\2\2\u015c\u015d\7u\2\2\u015d\u015e\7g\2\2\u015e")
        buf.write("&\3\2\2\2\u015f\u0160\7i\2\2\u0160\u0161\7t\2\2\u0161")
        buf.write("\u0162\7c\2\2\u0162\u0163\7f\2\2\u0163\u0164\7k\2\2\u0164")
        buf.write("\u0165\7g\2\2\u0165\u0166\7p\2\2\u0166\u0167\7v\2\2\u0167")
        buf.write("(\3\2\2\2\u0168\u0169\7u\2\2\u0169\u016a\7v\2\2\u016a")
        buf.write("\u016b\7q\2\2\u016b\u016c\7t\2\2\u016c\u016d\7g\2\2\u016d")
        buf.write("*\3\2\2\2\u016e\u016f\7t\2\2\u016f\u0170\7c\2\2\u0170")
        buf.write("\u0171\7p\2\2\u0171\u0172\7i\2\2\u0172\u0173\7g\2\2\u0173")
        buf.write(",\3\2\2\2\u0174\u0175\7c\2\2\u0175\u0176\7v\2\2\u0176")
        buf.write(".\3\2\2\2\u0177\u0178\7y\2\2\u0178\u0179\7k\2\2\u0179")
        buf.write("\u017a\7v\2\2\u017a\u017b\7j\2\2\u017b\60\3\2\2\2\u017c")
        buf.write("\u017d\7h\2\2\u017d\u017e\7q\2\2\u017e\u017f\7t\2\2\u017f")
        buf.write("\62\3\2\2\2\u0180\u0181\7k\2\2\u0181\u0182\7p\2\2\u0182")
        buf.write("\u0183\7v\2\2\u0183\u0184\7q\2\2\u0184\64\3\2\2\2\u0185")
        buf.write("\u0186\7v\2\2\u0186\u0187\7k\2\2\u0187\u0188\7o\2\2\u0188")
        buf.write("\u0189\7g\2\2\u0189\u018a\7u\2\2\u018a\66\3\2\2\2\u018b")
        buf.write("\u018c\7q\2\2\u018c\u018d\7p\2\2\u018d8\3\2\2\2\u018e")
        buf.write("\u018f\7q\2\2\u018f\u0190\7h\2\2\u0190:\3\2\2\2\u0191")
        buf.write("\u0192\7w\2\2\u0192\u0193\7p\2\2\u0193\u0194\7k\2\2\u0194")
        buf.write("\u0195\7v\2\2\u0195\u0196\7u\2\2\u0196<\3\2\2\2\u0197")
        buf.write("\u0198\7p\2\2\u0198\u0199\7c\2\2\u0199\u019a\7v\2\2\u019a")
        buf.write(">\3\2\2\2\u019b\u019c\7t\2\2\u019c\u019d\7g\2\2\u019d")
        buf.write("\u019e\7c\2\2\u019e\u019f\7n\2\2\u019f@\3\2\2\2\u01a0")
        buf.write("\u01a1\7o\2\2\u01a1\u01a2\7c\2\2\u01a2\u01a3\7v\2\2\u01a3")
        buf.write("B\3\2\2\2\u01a4\u01a5\7d\2\2\u01a5\u01a6\7q\2\2\u01a6")
        buf.write("\u01a7\7q\2\2\u01a7\u01a8\7n\2\2\u01a8D\3\2\2\2\u01a9")
        buf.write("\u01ad\5\u00d3j\2\u01aa\u01ac\5\u00d1i\2\u01ab\u01aa\3")
        buf.write("\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01aeF\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b5")
        buf.write("\7$\2\2\u01b1\u01b4\n\2\2\2\u01b2\u01b4\5\u00d5k\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2")
        buf.write("\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3")
        buf.write("\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01b9\7$\2\2\u01b9H\3")
        buf.write("\2\2\2\u01ba\u01bb\7v\2\2\u01bb\u01bc\7t\2\2\u01bc\u01bd")
        buf.write("\7w\2\2\u01bd\u01c4\7g\2\2\u01be\u01bf\7h\2\2\u01bf\u01c0")
        buf.write("\7c\2\2\u01c0\u01c1\7n\2\2\u01c1\u01c2\7u\2\2\u01c2\u01c4")
        buf.write("\7g\2\2\u01c3\u01ba\3\2\2\2\u01c3\u01be\3\2\2\2\u01c4")
        buf.write("J\3\2\2\2\u01c5\u01c6\5\u00cfh\2\u01c6\u01c8\7\60\2\2")
        buf.write("\u01c7\u01c9\5\u00cfh\2\u01c8\u01c7\3\2\2\2\u01c8\u01c9")
        buf.write("\3\2\2\2\u01c9\u01cd\3\2\2\2\u01ca\u01cb\7\60\2\2\u01cb")
        buf.write("\u01cd\5\u00cfh\2\u01cc\u01c5\3\2\2\2\u01cc\u01ca\3\2")
        buf.write("\2\2\u01cdL\3\2\2\2\u01ce\u01d2\5\u00cfh\2\u01cf\u01d1")
        buf.write("\5\u00cfh\2\u01d0\u01cf\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3N\3\2\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d5\u01d8\5K&\2\u01d6\u01d8\5M\'\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2")
        buf.write("\u01d9\u01da\5\u00c9e\2\u01daP\3\2\2\2\u01db\u01de\5K")
        buf.write("&\2\u01dc\u01de\5M\'\2\u01dd\u01db\3\2\2\2\u01dd\u01dc")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\5\u00cbf\2\u01e0")
        buf.write("R\3\2\2\2\u01e1\u01e4\5K&\2\u01e2\u01e4\5M\'\2\u01e3\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5")
        buf.write("\u01e6\5\u00cdg\2\u01e6T\3\2\2\2\u01e7\u01e8\7*\2\2\u01e8")
        buf.write("V\3\2\2\2\u01e9\u01ea\7+\2\2\u01eaX\3\2\2\2\u01eb\u01ec")
        buf.write("\7}\2\2\u01ecZ\3\2\2\2\u01ed\u01ee\7\177\2\2\u01ee\\\3")
        buf.write("\2\2\2\u01ef\u01f0\7]\2\2\u01f0^\3\2\2\2\u01f1\u01f2\7")
        buf.write("_\2\2\u01f2`\3\2\2\2\u01f3\u01f4\7=\2\2\u01f4b\3\2\2\2")
        buf.write("\u01f5\u01f6\7.\2\2\u01f6d\3\2\2\2\u01f7\u01f8\7\60\2")
        buf.write("\2\u01f8f\3\2\2\2\u01f9\u01fa\7?\2\2\u01fah\3\2\2\2\u01fb")
        buf.write("\u01fc\7@\2\2\u01fcj\3\2\2\2\u01fd\u01fe\7>\2\2\u01fe")
        buf.write("l\3\2\2\2\u01ff\u0200\7#\2\2\u0200n\3\2\2\2\u0201\u0202")
        buf.write("\7\u0080\2\2\u0202p\3\2\2\2\u0203\u0204\7A\2\2\u0204r")
        buf.write("\3\2\2\2\u0205\u0206\7<\2\2\u0206t\3\2\2\2\u0207\u0208")
        buf.write("\7?\2\2\u0208\u0209\7?\2\2\u0209v\3\2\2\2\u020a\u020b")
        buf.write("\7>\2\2\u020b\u020c\7?\2\2\u020cx\3\2\2\2\u020d\u020e")
        buf.write("\7@\2\2\u020e\u020f\7?\2\2\u020fz\3\2\2\2\u0210\u0211")
        buf.write("\7#\2\2\u0211\u0212\7?\2\2\u0212|\3\2\2\2\u0213\u0214")
        buf.write("\7(\2\2\u0214\u0215\7(\2\2\u0215~\3\2\2\2\u0216\u0217")
        buf.write("\7~\2\2\u0217\u0218\7~\2\2\u0218\u0080\3\2\2\2\u0219\u021a")
        buf.write("\7-\2\2\u021a\u021b\7-\2\2\u021b\u0082\3\2\2\2\u021c\u021d")
        buf.write("\7/\2\2\u021d\u021e\7/\2\2\u021e\u0084\3\2\2\2\u021f\u0220")
        buf.write("\7-\2\2\u0220\u0086\3\2\2\2\u0221\u0222\7/\2\2\u0222\u0088")
        buf.write("\3\2\2\2\u0223\u0224\7,\2\2\u0224\u008a\3\2\2\2\u0225")
        buf.write("\u0226\7\61\2\2\u0226\u008c\3\2\2\2\u0227\u0228\7(\2\2")
        buf.write("\u0228\u008e\3\2\2\2\u0229\u022a\7~\2\2\u022a\u0090\3")
        buf.write("\2\2\2\u022b\u022c\7`\2\2\u022c\u0092\3\2\2\2\u022d\u022e")
        buf.write("\7\'\2\2\u022e\u0094\3\2\2\2\u022f\u0230\7a\2\2\u0230")
        buf.write("\u0096\3\2\2\2\u0231\u0232\7p\2\2\u0232\u0233\7u\2\2\u0233")
        buf.write("\u0098\3\2\2\2\u0234\u0235\7w\2\2\u0235\u0236\7u\2\2\u0236")
        buf.write("\u009a\3\2\2\2\u0237\u0238\7o\2\2\u0238\u0239\7u\2\2\u0239")
        buf.write("\u009c\3\2\2\2\u023a\u023b\7e\2\2\u023b\u023c\7u\2\2\u023c")
        buf.write("\u009e\3\2\2\2\u023d\u023e\7f\2\2\u023e\u023f\7u\2\2\u023f")
        buf.write("\u00a0\3\2\2\2\u0240\u0241\7u\2\2\u0241\u00a2\3\2\2\2")
        buf.write("\u0242\u0243\7o\2\2\u0243\u00a4\3\2\2\2\u0244\u0245\7")
        buf.write("j\2\2\u0245\u00a6\3\2\2\2\u0246\u0247\7f\2\2\u0247\u00a8")
        buf.write("\3\2\2\2\u0248\u0249\7y\2\2\u0249\u00aa\3\2\2\2\u024a")
        buf.write("\u024b\7o\2\2\u024b\u024c\7q\2\2\u024c\u00ac\3\2\2\2\u024d")
        buf.write("\u024e\7{\2\2\u024e\u00ae\3\2\2\2\u024f\u0250\7p\2\2\u0250")
        buf.write("\u0251\7N\2\2\u0251\u00b0\3\2\2\2\u0252\u0253\7w\2\2\u0253")
        buf.write("\u0254\7N\2\2\u0254\u00b2\3\2\2\2\u0255\u0256\7o\2\2\u0256")
        buf.write("\u0257\7N\2\2\u0257\u00b4\3\2\2\2\u0258\u0259\7e\2\2\u0259")
        buf.write("\u025a\7N\2\2\u025a\u00b6\3\2\2\2\u025b\u025c\7f\2\2\u025c")
        buf.write("\u025d\7N\2\2\u025d\u00b8\3\2\2\2\u025e\u025f\7N\2\2\u025f")
        buf.write("\u00ba\3\2\2\2\u0260\u0261\7f\2\2\u0261\u0262\7c\2\2\u0262")
        buf.write("\u0263\7N\2\2\u0263\u00bc\3\2\2\2\u0264\u0265\7e\2\2\u0265")
        buf.write("\u00be\3\2\2\2\u0266\u0267\7h\2\2\u0267\u00c0\3\2\2\2")
        buf.write("\u0268\u0269\7m\2\2\u0269\u00c2\3\2\2\2\u026a\u026c\t")
        buf.write("\3\2\2\u026b\u026a\3\2\2\2\u026c\u026d\3\2\2\2\u026d\u026b")
        buf.write("\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u026f\3\2\2\2\u026f")
        buf.write("\u0270\bb\2\2\u0270\u00c4\3\2\2\2\u0271\u0272\7\61\2\2")
        buf.write("\u0272\u0273\7,\2\2\u0273\u0277\3\2\2\2\u0274\u0276\13")
        buf.write("\2\2\2\u0275\u0274\3\2\2\2\u0276\u0279\3\2\2\2\u0277\u0278")
        buf.write("\3\2\2\2\u0277\u0275\3\2\2\2\u0278\u027a\3\2\2\2\u0279")
        buf.write("\u0277\3\2\2\2\u027a\u027b\7,\2\2\u027b\u027c\7\61\2\2")
        buf.write("\u027c\u027d\3\2\2\2\u027d\u027e\bc\2\2\u027e\u00c6\3")
        buf.write("\2\2\2\u027f\u0280\7\61\2\2\u0280\u0281\7\61\2\2\u0281")
        buf.write("\u0285\3\2\2\2\u0282\u0284\n\4\2\2\u0283\u0282\3\2\2\2")
        buf.write("\u0284\u0287\3\2\2\2\u0285\u0283\3\2\2\2\u0285\u0286\3")
        buf.write("\2\2\2\u0286\u0288\3\2\2\2\u0287\u0285\3\2\2\2\u0288\u0289")
        buf.write("\bd\2\2\u0289\u00c8\3\2\2\2\u028a\u0297\5\u0097L\2\u028b")
        buf.write("\u0297\5\u0099M\2\u028c\u0297\5\u009bN\2\u028d\u0297\5")
        buf.write("\u009dO\2\u028e\u0297\5\u009fP\2\u028f\u0297\5\u00a1Q")
        buf.write("\2\u0290\u0297\5\u00a3R\2\u0291\u0297\5\u00a5S\2\u0292")
        buf.write("\u0297\5\u00a7T\2\u0293\u0297\5\u00a9U\2\u0294\u0297\5")
        buf.write("\u00abV\2\u0295\u0297\5\u00adW\2\u0296\u028a\3\2\2\2\u0296")
        buf.write("\u028b\3\2\2\2\u0296\u028c\3\2\2\2\u0296\u028d\3\2\2\2")
        buf.write("\u0296\u028e\3\2\2\2\u0296\u028f\3\2\2\2\u0296\u0290\3")
        buf.write("\2\2\2\u0296\u0291\3\2\2\2\u0296\u0292\3\2\2\2\u0296\u0293")
        buf.write("\3\2\2\2\u0296\u0294\3\2\2\2\u0296\u0295\3\2\2\2\u0297")
        buf.write("\u00ca\3\2\2\2\u0298\u029f\5\u00afX\2\u0299\u029f\5\u00b1")
        buf.write("Y\2\u029a\u029f\5\u00b3Z\2\u029b\u029f\5\u00b5[\2\u029c")
        buf.write("\u029f\5\u00b9]\2\u029d\u029f\5\u00bb^\2\u029e\u0298\3")
        buf.write("\2\2\2\u029e\u0299\3\2\2\2\u029e\u029a\3\2\2\2\u029e\u029b")
        buf.write("\3\2\2\2\u029e\u029c\3\2\2\2\u029e\u029d\3\2\2\2\u029f")
        buf.write("\u00cc\3\2\2\2\u02a0\u02a4\5\u00bf`\2\u02a1\u02a4\5\u00bd")
        buf.write("_\2\u02a2\u02a4\5\u00c1a\2\u02a3\u02a0\3\2\2\2\u02a3\u02a1")
        buf.write("\3\2\2\2\u02a3\u02a2\3\2\2\2\u02a4\u00ce\3\2\2\2\u02a5")
        buf.write("\u02ad\t\5\2\2\u02a6\u02a8\t\6\2\2\u02a7\u02a6\3\2\2\2")
        buf.write("\u02a8\u02ab\3\2\2\2\u02a9\u02a7\3\2\2\2\u02a9\u02aa\3")
        buf.write("\2\2\2\u02aa\u02ac\3\2\2\2\u02ab\u02a9\3\2\2\2\u02ac\u02ae")
        buf.write("\t\5\2\2\u02ad\u02a9\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae")
        buf.write("\u00d0\3\2\2\2\u02af\u02b2\5\u00d3j\2\u02b0\u02b2\t\5")
        buf.write("\2\2\u02b1\u02af\3\2\2\2\u02b1\u02b0\3\2\2\2\u02b2\u00d2")
        buf.write("\3\2\2\2\u02b3\u02b8\t\7\2\2\u02b4\u02b8\n\b\2\2\u02b5")
        buf.write("\u02b6\t\t\2\2\u02b6\u02b8\t\n\2\2\u02b7\u02b3\3\2\2\2")
        buf.write("\u02b7\u02b4\3\2\2\2\u02b7\u02b5\3\2\2\2\u02b8\u00d4\3")
        buf.write("\2\2\2\u02b9\u02ba\7^\2\2\u02ba\u02c4\t\13\2\2\u02bb\u02c0")
        buf.write("\7^\2\2\u02bc\u02be\t\f\2\2\u02bd\u02bc\3\2\2\2\u02bd")
        buf.write("\u02be\3\2\2\2\u02be\u02bf\3\2\2\2\u02bf\u02c1\t\r\2\2")
        buf.write("\u02c0\u02bd\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02c2\3")
        buf.write("\2\2\2\u02c2\u02c4\t\r\2\2\u02c3\u02b9\3\2\2\2\u02c3\u02bb")
        buf.write("\3\2\2\2\u02c4\u00d6\3\2\2\2\u02c5\u02c7\t\16\2\2\u02c6")
        buf.write("\u02c5\3\2\2\2\u02c7\u02c8\3\2\2\2\u02c8\u02c6\3\2\2\2")
        buf.write("\u02c8\u02c9\3\2\2\2\u02c9\u00d8\3\2\2\2\u02ca\u02cc\7")
        buf.write("\17\2\2\u02cb\u02ca\3\2\2\2\u02cb\u02cc\3\2\2\2\u02cc")
        buf.write("\u02cd\3\2\2\2\u02cd\u02d0\7\f\2\2\u02ce\u02d0\4\16\17")
        buf.write("\2\u02cf\u02cb\3\2\2\2\u02cf\u02ce\3\2\2\2\u02d0\u00da")
        buf.write("\3\2\2\2\35\2\u01ad\u01b3\u01b5\u01c3\u01c8\u01cc\u01d2")
        buf.write("\u01d7\u01dd\u01e3\u026d\u0277\u0285\u0296\u029e\u02a3")
        buf.write("\u02a9\u02ad\u02b1\u02b7\u02bd\u02c0\u02c3\u02c8\u02cb")
        buf.write("\u02cf\3\2\3\2")
        return buf.getvalue()


class BSLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    REPEAT = 3
    WHILE = 4
    FUNCTION = 5
    RETURN = 6
    MANIFEST = 7
    MODULE = 8
    STATIONARY = 9
    FUNCTIONS = 10
    INSTRUCTIONS = 11
    DETECT = 12
    MIX = 13
    SPLIT = 14
    HEAT = 15
    DRAIN = 16
    DISPENSE = 17
    DISPOSE = 18
    GRADIENT = 19
    STORE = 20
    RANGE = 21
    AT = 22
    WITH = 23
    FOR = 24
    INTO = 25
    TIMES = 26
    ON = 27
    OF = 28
    UNITS = 29
    NAT = 30
    REAL = 31
    MAT = 32
    BOOL = 33
    IDENTIFIER = 34
    STRING_LITERAL = 35
    BOOL_LITERAL = 36
    FLOAT_LITERAL = 37
    INTEGER_LITERAL = 38
    TIME_NUMBER = 39
    VOLUME_NUMBER = 40
    TEMP_NUMBER = 41
    LPAREN = 42
    RPAREN = 43
    LBRACE = 44
    RBRACE = 45
    LBRACKET = 46
    RBRACKET = 47
    SEMICOLON = 48
    COMMA = 49
    DOT = 50
    ASSIGN = 51
    GT = 52
    LT = 53
    BANG = 54
    TILDE = 55
    QUESTION = 56
    COLON = 57
    EQUALITY = 58
    LTE = 59
    GTE = 60
    NOTEQUAL = 61
    AND = 62
    OR = 63
    INC = 64
    DEC = 65
    ADDITION = 66
    SUBTRACT = 67
    MULTIPLY = 68
    DIVIDE = 69
    BITAND = 70
    BITOR = 71
    CARET = 72
    MOD = 73
    UNDERSCORE = 74
    NANOSECOND = 75
    MICROSECOND = 76
    MILLISECOND = 77
    CENTISECOND = 78
    DECISECOND = 79
    SECOND = 80
    MINUTE = 81
    HOUR = 82
    DAY = 83
    WEEK = 84
    MONTH = 85
    YEAR = 86
    NANOLITRE = 87
    MICROLITRE = 88
    MILLILITRE = 89
    CENTILITRE = 90
    DECILITRE = 91
    LITRE = 92
    DECALITRE = 93
    CELSIUS = 94
    FAHRENHEIT = 95
    KELVIN = 96
    WS = 97
    COMMENT = 98
    LINE_COMMENT = 99

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'repeat'", "'while'", "'function'", "'return'",
            "'manifest'", "'module'", "'stationary'", "'functions'", "'instructions'",
            "'detect'", "'mix'", "'split'", "'heat'", "'drain'", "'dispense'",
            "'dispose'", "'gradient'", "'store'", "'range'", "'at'", "'with'",
            "'for'", "'into'", "'times'", "'on'", "'of'", "'units'", "'nat'",
            "'real'", "'mat'", "'bool'", "'('", "')'", "'{'", "'}'", "'['",
            "']'", "';'", "','", "'.'", "'='", "'>'", "'<'", "'!'", "'~'",
            "'?'", "':'", "'=='", "'<='", "'>='", "'!='", "'&&'", "'||'",
            "'++'", "'--'", "'+'", "'-'", "'*'", "'/'", "'&'", "'|'", "'^'",
            "'%'", "'_'", "'ns'", "'us'", "'ms'", "'cs'", "'ds'", "'s'",
            "'m'", "'h'", "'d'", "'w'", "'mo'", "'y'", "'nL'", "'uL'", "'mL'",
            "'cL'", "'dL'", "'L'", "'daL'", "'c'", "'f'", "'k'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", "RETURN", "MANIFEST",
            "MODULE", "STATIONARY", "FUNCTIONS", "INSTRUCTIONS", "DETECT",
            "MIX", "SPLIT", "HEAT", "DRAIN", "DISPENSE", "DISPOSE", "GRADIENT",
            "STORE", "RANGE", "AT", "WITH", "FOR", "INTO", "TIMES", "ON",
            "OF", "UNITS", "NAT", "REAL", "MAT", "BOOL", "IDENTIFIER", "STRING_LITERAL",
            "BOOL_LITERAL", "FLOAT_LITERAL", "INTEGER_LITERAL", "TIME_NUMBER",
            "VOLUME_NUMBER", "TEMP_NUMBER", "LPAREN", "RPAREN", "LBRACE",
            "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON", "COMMA", "DOT",
            "ASSIGN", "GT", "LT", "BANG", "TILDE", "QUESTION", "COLON",
            "EQUALITY", "LTE", "GTE", "NOTEQUAL", "AND", "OR", "INC", "DEC",
            "ADDITION", "SUBTRACT", "MULTIPLY", "DIVIDE", "BITAND", "BITOR",
            "CARET", "MOD", "UNDERSCORE", "NANOSECOND", "MICROSECOND", "MILLISECOND",
            "CENTISECOND", "DECISECOND", "SECOND", "MINUTE", "HOUR", "DAY",
            "WEEK", "MONTH", "YEAR", "NANOLITRE", "MICROLITRE", "MILLILITRE",
            "CENTILITRE", "DECILITRE", "LITRE", "DECALITRE", "CELSIUS",
            "FAHRENHEIT", "KELVIN", "WS", "COMMENT", "LINE_COMMENT" ]

    ruleNames = [ "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", "RETURN",
                  "MANIFEST", "MODULE", "STATIONARY", "FUNCTIONS", "INSTRUCTIONS",
                  "DETECT", "MIX", "SPLIT", "HEAT", "DRAIN", "DISPENSE",
                  "DISPOSE", "GRADIENT", "STORE", "RANGE", "AT", "WITH",
                  "FOR", "INTO", "TIMES", "ON", "OF", "UNITS", "NAT", "REAL",
                  "MAT", "BOOL", "IDENTIFIER", "STRING_LITERAL", "BOOL_LITERAL",
                  "FLOAT_LITERAL", "INTEGER_LITERAL", "TIME_NUMBER", "VOLUME_NUMBER",
                  "TEMP_NUMBER", "LPAREN", "RPAREN", "LBRACE", "RBRACE",
                  "LBRACKET", "RBRACKET", "SEMICOLON", "COMMA", "DOT", "ASSIGN",
                  "GT", "LT", "BANG", "TILDE", "QUESTION", "COLON", "EQUALITY",
                  "LTE", "GTE", "NOTEQUAL", "AND", "OR", "INC", "DEC", "ADDITION",
                  "SUBTRACT", "MULTIPLY", "DIVIDE", "BITAND", "BITOR", "CARET",
                  "MOD", "UNDERSCORE", "NANOSECOND", "MICROSECOND", "MILLISECOND",
                  "CENTISECOND", "DECISECOND", "SECOND", "MINUTE", "HOUR",
                  "DAY", "WEEK", "MONTH", "YEAR", "NANOLITRE", "MICROLITRE",
                  "MILLILITRE", "CENTILITRE", "DECILITRE", "LITRE", "DECALITRE",
                  "CELSIUS", "FAHRENHEIT", "KELVIN", "WS", "COMMENT", "LINE_COMMENT",
                  "TimeUnits", "VolumeUnits", "TempUnits", "Digits", "LetterOrDigit",
                  "Letter", "EscapeSequence", "SPACES", "NEWLINE" ]

    grammarFileName = "BSLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


