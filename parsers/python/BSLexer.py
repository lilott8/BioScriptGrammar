from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2b")
        buf.write("\u02b9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("g\tg\4h\th\4i\ti\4j\tj\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \7 \u0194\n \f \16 \u0197\13 \3!\3!\3")
        buf.write("!\7!\u019c\n!\f!\16!\u019f\13!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\5\"\u01ac\n\"\3#\3#\3#\5#\u01b1\n#")
        buf.write("\3#\3#\5#\u01b5\n#\3$\3$\7$\u01b9\n$\f$\16$\u01bc\13$")
        buf.write("\3%\3%\5%\u01c0\n%\3%\3%\3&\3&\5&\u01c6\n&\3&\3&\3\'\3")
        buf.write("\'\5\'\u01cc\n\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("8\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3")
        buf.write(">\3?\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("G\3G\3H\3H\3I\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3L\3M\3M\3")
        buf.write("M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3S\3T\3T\3U\3U\3")
        buf.write("U\3V\3V\3V\3W\3W\3W\3X\3X\3X\3Y\3Y\3Y\3Z\3Z\3[\3[\3[\3")
        buf.write("[\3\\\3\\\3]\3]\3^\3^\3_\6_\u0254\n_\r_\16_\u0255\3_\3")
        buf.write("_\3`\3`\3`\3`\7`\u025e\n`\f`\16`\u0261\13`\3`\3`\3`\3")
        buf.write("`\3`\3a\3a\3a\3a\7a\u026c\na\fa\16a\u026f\13a\3a\3a\3")
        buf.write("b\3b\3b\3b\3b\3b\3b\3b\3b\3b\3b\3b\5b\u027f\nb\3c\3c\3")
        buf.write("c\3c\3c\3c\5c\u0287\nc\3d\3d\3d\5d\u028c\nd\3e\3e\7e\u0290")
        buf.write("\ne\fe\16e\u0293\13e\3e\5e\u0296\ne\3f\3f\5f\u029a\nf")
        buf.write("\3g\3g\3g\3g\5g\u02a0\ng\3h\3h\3h\3h\5h\u02a6\nh\3h\5")
        buf.write("h\u02a9\nh\3h\5h\u02ac\nh\3i\6i\u02af\ni\ri\16i\u02b0")
        buf.write("\3j\5j\u02b4\nj\3j\3j\5j\u02b8\nj\3\u025f\2k\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}")
        buf.write("@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008d")
        buf.write("H\u008fI\u0091J\u0093K\u0095L\u0097M\u0099N\u009bO\u009d")
        buf.write("P\u009fQ\u00a1R\u00a3S\u00a5T\u00a7U\u00a9V\u00abW\u00ad")
        buf.write("X\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7]\u00b9^\u00bb_\u00bd")
        buf.write("`\u00bfa\u00c1b\u00c3\2\u00c5\2\u00c7\2\u00c9\2\u00cb")
        buf.write("\2\u00cd\2\u00cf\2\u00d1\2\u00d3\2\3\2\17\6\2\f\f\17\17")
        buf.write("$$^^\5\2\13\f\16\17\"\"\4\2\f\f\17\17\3\2\62;\4\2\62;")
        buf.write("aa\6\2&&C\\aac|\4\2\2\u0081\ud802\udc01\3\2\ud802\udc01")
        buf.write("\3\2\udc02\ue001\n\2$$))^^ddhhppttvv\3\2\62\65\3\2\62")
        buf.write("9\4\2\13\13\"\"\2\u02d9\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9")
        buf.write("\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2")
        buf.write("\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7")
        buf.write("\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2")
        buf.write("\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\3\u00d5\3\2\2\2\5\u00d8")
        buf.write("\3\2\2\2\7\u00dd\3\2\2\2\t\u00e4\3\2\2\2\13\u00ea\3\2")
        buf.write("\2\2\r\u00f3\3\2\2\2\17\u00fa\3\2\2\2\21\u0103\3\2\2\2")
        buf.write("\23\u010a\3\2\2\2\25\u0115\3\2\2\2\27\u011f\3\2\2\2\31")
        buf.write("\u012c\3\2\2\2\33\u0133\3\2\2\2\35\u0137\3\2\2\2\37\u013d")
        buf.write("\3\2\2\2!\u0142\3\2\2\2#\u0148\3\2\2\2%\u0151\3\2\2\2")
        buf.write("\'\u0159\3\2\2\2)\u0162\3\2\2\2+\u0165\3\2\2\2-\u016a")
        buf.write("\3\2\2\2/\u016e\3\2\2\2\61\u0173\3\2\2\2\63\u0179\3\2")
        buf.write("\2\2\65\u017c\3\2\2\2\67\u017f\3\2\2\29\u0183\3\2\2\2")
        buf.write(";\u0188\3\2\2\2=\u018c\3\2\2\2?\u0191\3\2\2\2A\u0198\3")
        buf.write("\2\2\2C\u01ab\3\2\2\2E\u01b4\3\2\2\2G\u01b6\3\2\2\2I\u01bf")
        buf.write("\3\2\2\2K\u01c5\3\2\2\2M\u01cb\3\2\2\2O\u01cf\3\2\2\2")
        buf.write("Q\u01d1\3\2\2\2S\u01d3\3\2\2\2U\u01d5\3\2\2\2W\u01d7\3")
        buf.write("\2\2\2Y\u01d9\3\2\2\2[\u01db\3\2\2\2]\u01dd\3\2\2\2_\u01df")
        buf.write("\3\2\2\2a\u01e1\3\2\2\2c\u01e3\3\2\2\2e\u01e5\3\2\2\2")
        buf.write("g\u01e7\3\2\2\2i\u01e9\3\2\2\2k\u01eb\3\2\2\2m\u01ed\3")
        buf.write("\2\2\2o\u01ef\3\2\2\2q\u01f2\3\2\2\2s\u01f5\3\2\2\2u\u01f8")
        buf.write("\3\2\2\2w\u01fb\3\2\2\2y\u01fe\3\2\2\2{\u0201\3\2\2\2")
        buf.write("}\u0204\3\2\2\2\177\u0207\3\2\2\2\u0081\u0209\3\2\2\2")
        buf.write("\u0083\u020b\3\2\2\2\u0085\u020d\3\2\2\2\u0087\u020f\3")
        buf.write("\2\2\2\u0089\u0211\3\2\2\2\u008b\u0213\3\2\2\2\u008d\u0215")
        buf.write("\3\2\2\2\u008f\u0217\3\2\2\2\u0091\u0219\3\2\2\2\u0093")
        buf.write("\u021c\3\2\2\2\u0095\u021f\3\2\2\2\u0097\u0222\3\2\2\2")
        buf.write("\u0099\u0225\3\2\2\2\u009b\u0228\3\2\2\2\u009d\u022a\3")
        buf.write("\2\2\2\u009f\u022c\3\2\2\2\u00a1\u022e\3\2\2\2\u00a3\u0230")
        buf.write("\3\2\2\2\u00a5\u0232\3\2\2\2\u00a7\u0235\3\2\2\2\u00a9")
        buf.write("\u0237\3\2\2\2\u00ab\u023a\3\2\2\2\u00ad\u023d\3\2\2\2")
        buf.write("\u00af\u0240\3\2\2\2\u00b1\u0243\3\2\2\2\u00b3\u0246\3")
        buf.write("\2\2\2\u00b5\u0248\3\2\2\2\u00b7\u024c\3\2\2\2\u00b9\u024e")
        buf.write("\3\2\2\2\u00bb\u0250\3\2\2\2\u00bd\u0253\3\2\2\2\u00bf")
        buf.write("\u0259\3\2\2\2\u00c1\u0267\3\2\2\2\u00c3\u027e\3\2\2\2")
        buf.write("\u00c5\u0286\3\2\2\2\u00c7\u028b\3\2\2\2\u00c9\u028d\3")
        buf.write("\2\2\2\u00cb\u0299\3\2\2\2\u00cd\u029f\3\2\2\2\u00cf\u02ab")
        buf.write("\3\2\2\2\u00d1\u02ae\3\2\2\2\u00d3\u02b7\3\2\2\2\u00d5")
        buf.write("\u00d6\7k\2\2\u00d6\u00d7\7h\2\2\u00d7\4\3\2\2\2\u00d8")
        buf.write("\u00d9\7g\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7u\2\2\u00db")
        buf.write("\u00dc\7g\2\2\u00dc\6\3\2\2\2\u00dd\u00de\7t\2\2\u00de")
        buf.write("\u00df\7g\2\2\u00df\u00e0\7r\2\2\u00e0\u00e1\7g\2\2\u00e1")
        buf.write("\u00e2\7c\2\2\u00e2\u00e3\7v\2\2\u00e3\b\3\2\2\2\u00e4")
        buf.write("\u00e5\7y\2\2\u00e5\u00e6\7j\2\2\u00e6\u00e7\7k\2\2\u00e7")
        buf.write("\u00e8\7n\2\2\u00e8\u00e9\7g\2\2\u00e9\n\3\2\2\2\u00ea")
        buf.write("\u00eb\7h\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7p\2\2\u00ed")
        buf.write("\u00ee\7e\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7k\2\2\u00f0")
        buf.write("\u00f1\7q\2\2\u00f1\u00f2\7p\2\2\u00f2\f\3\2\2\2\u00f3")
        buf.write("\u00f4\7t\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7v\2\2\u00f6")
        buf.write("\u00f7\7w\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7p\2\2\u00f9")
        buf.write("\16\3\2\2\2\u00fa\u00fb\7o\2\2\u00fb\u00fc\7c\2\2\u00fc")
        buf.write("\u00fd\7p\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7h\2\2\u00ff")
        buf.write("\u0100\7g\2\2\u0100\u0101\7u\2\2\u0101\u0102\7v\2\2\u0102")
        buf.write("\20\3\2\2\2\u0103\u0104\7o\2\2\u0104\u0105\7q\2\2\u0105")
        buf.write("\u0106\7f\2\2\u0106\u0107\7w\2\2\u0107\u0108\7n\2\2\u0108")
        buf.write("\u0109\7g\2\2\u0109\22\3\2\2\2\u010a\u010b\7u\2\2\u010b")
        buf.write("\u010c\7v\2\2\u010c\u010d\7c\2\2\u010d\u010e\7v\2\2\u010e")
        buf.write("\u010f\7k\2\2\u010f\u0110\7q\2\2\u0110\u0111\7p\2\2\u0111")
        buf.write("\u0112\7c\2\2\u0112\u0113\7t\2\2\u0113\u0114\7{\2\2\u0114")
        buf.write("\24\3\2\2\2\u0115\u0116\7h\2\2\u0116\u0117\7w\2\2\u0117")
        buf.write("\u0118\7p\2\2\u0118\u0119\7e\2\2\u0119\u011a\7v\2\2\u011a")
        buf.write("\u011b\7k\2\2\u011b\u011c\7q\2\2\u011c\u011d\7p\2\2\u011d")
        buf.write("\u011e\7u\2\2\u011e\26\3\2\2\2\u011f\u0120\7k\2\2\u0120")
        buf.write("\u0121\7p\2\2\u0121\u0122\7u\2\2\u0122\u0123\7v\2\2\u0123")
        buf.write("\u0124\7t\2\2\u0124\u0125\7w\2\2\u0125\u0126\7e\2\2\u0126")
        buf.write("\u0127\7v\2\2\u0127\u0128\7k\2\2\u0128\u0129\7q\2\2\u0129")
        buf.write("\u012a\7p\2\2\u012a\u012b\7u\2\2\u012b\30\3\2\2\2\u012c")
        buf.write("\u012d\7f\2\2\u012d\u012e\7g\2\2\u012e\u012f\7v\2\2\u012f")
        buf.write("\u0130\7g\2\2\u0130\u0131\7e\2\2\u0131\u0132\7v\2\2\u0132")
        buf.write("\32\3\2\2\2\u0133\u0134\7o\2\2\u0134\u0135\7k\2\2\u0135")
        buf.write("\u0136\7z\2\2\u0136\34\3\2\2\2\u0137\u0138\7u\2\2\u0138")
        buf.write("\u0139\7r\2\2\u0139\u013a\7n\2\2\u013a\u013b\7k\2\2\u013b")
        buf.write("\u013c\7v\2\2\u013c\36\3\2\2\2\u013d\u013e\7j\2\2\u013e")
        buf.write("\u013f\7g\2\2\u013f\u0140\7c\2\2\u0140\u0141\7v\2\2\u0141")
        buf.write(" \3\2\2\2\u0142\u0143\7f\2\2\u0143\u0144\7t\2\2\u0144")
        buf.write("\u0145\7c\2\2\u0145\u0146\7k\2\2\u0146\u0147\7p\2\2\u0147")
        buf.write("\"\3\2\2\2\u0148\u0149\7f\2\2\u0149\u014a\7k\2\2\u014a")
        buf.write("\u014b\7u\2\2\u014b\u014c\7r\2\2\u014c\u014d\7g\2\2\u014d")
        buf.write("\u014e\7p\2\2\u014e\u014f\7u\2\2\u014f\u0150\7g\2\2\u0150")
        buf.write("$\3\2\2\2\u0151\u0152\7f\2\2\u0152\u0153\7k\2\2\u0153")
        buf.write("\u0154\7u\2\2\u0154\u0155\7r\2\2\u0155\u0156\7q\2\2\u0156")
        buf.write("\u0157\7u\2\2\u0157\u0158\7g\2\2\u0158&\3\2\2\2\u0159")
        buf.write("\u015a\7i\2\2\u015a\u015b\7t\2\2\u015b\u015c\7c\2\2\u015c")
        buf.write("\u015d\7f\2\2\u015d\u015e\7k\2\2\u015e\u015f\7g\2\2\u015f")
        buf.write("\u0160\7p\2\2\u0160\u0161\7v\2\2\u0161(\3\2\2\2\u0162")
        buf.write("\u0163\7c\2\2\u0163\u0164\7v\2\2\u0164*\3\2\2\2\u0165")
        buf.write("\u0166\7y\2\2\u0166\u0167\7k\2\2\u0167\u0168\7v\2\2\u0168")
        buf.write("\u0169\7j\2\2\u0169,\3\2\2\2\u016a\u016b\7h\2\2\u016b")
        buf.write("\u016c\7q\2\2\u016c\u016d\7t\2\2\u016d.\3\2\2\2\u016e")
        buf.write("\u016f\7k\2\2\u016f\u0170\7p\2\2\u0170\u0171\7v\2\2\u0171")
        buf.write("\u0172\7q\2\2\u0172\60\3\2\2\2\u0173\u0174\7v\2\2\u0174")
        buf.write("\u0175\7k\2\2\u0175\u0176\7o\2\2\u0176\u0177\7g\2\2\u0177")
        buf.write("\u0178\7u\2\2\u0178\62\3\2\2\2\u0179\u017a\7q\2\2\u017a")
        buf.write("\u017b\7p\2\2\u017b\64\3\2\2\2\u017c\u017d\7q\2\2\u017d")
        buf.write("\u017e\7h\2\2\u017e\66\3\2\2\2\u017f\u0180\7p\2\2\u0180")
        buf.write("\u0181\7c\2\2\u0181\u0182\7v\2\2\u01828\3\2\2\2\u0183")
        buf.write("\u0184\7t\2\2\u0184\u0185\7g\2\2\u0185\u0186\7c\2\2\u0186")
        buf.write("\u0187\7n\2\2\u0187:\3\2\2\2\u0188\u0189\7o\2\2\u0189")
        buf.write("\u018a\7c\2\2\u018a\u018b\7v\2\2\u018b<\3\2\2\2\u018c")
        buf.write("\u018d\7d\2\2\u018d\u018e\7q\2\2\u018e\u018f\7q\2\2\u018f")
        buf.write("\u0190\7n\2\2\u0190>\3\2\2\2\u0191\u0195\5\u00cdg\2\u0192")
        buf.write("\u0194\5\u00cbf\2\u0193\u0192\3\2\2\2\u0194\u0197\3\2")
        buf.write("\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196@\3")
        buf.write("\2\2\2\u0197\u0195\3\2\2\2\u0198\u019d\7$\2\2\u0199\u019c")
        buf.write("\n\2\2\2\u019a\u019c\5\u00cfh\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019a\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019e\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u019d\3")
        buf.write("\2\2\2\u01a0\u01a1\7$\2\2\u01a1B\3\2\2\2\u01a2\u01a3\7")
        buf.write("v\2\2\u01a3\u01a4\7t\2\2\u01a4\u01a5\7w\2\2\u01a5\u01ac")
        buf.write("\7g\2\2\u01a6\u01a7\7h\2\2\u01a7\u01a8\7c\2\2\u01a8\u01a9")
        buf.write("\7n\2\2\u01a9\u01aa\7u\2\2\u01aa\u01ac\7g\2\2\u01ab\u01a2")
        buf.write("\3\2\2\2\u01ab\u01a6\3\2\2\2\u01acD\3\2\2\2\u01ad\u01ae")
        buf.write("\5\u00c9e\2\u01ae\u01b0\7\60\2\2\u01af\u01b1\5\u00c9e")
        buf.write("\2\u01b0\u01af\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b5")
        buf.write("\3\2\2\2\u01b2\u01b3\7\60\2\2\u01b3\u01b5\5\u00c9e\2\u01b4")
        buf.write("\u01ad\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5F\3\2\2\2\u01b6")
        buf.write("\u01ba\5\u00c9e\2\u01b7\u01b9\5\u00c9e\2\u01b8\u01b7\3")
        buf.write("\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb")
        buf.write("\3\2\2\2\u01bbH\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01c0")
        buf.write("\5E#\2\u01be\u01c0\5G$\2\u01bf\u01bd\3\2\2\2\u01bf\u01be")
        buf.write("\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\5\u00c3b\2\u01c2")
        buf.write("J\3\2\2\2\u01c3\u01c6\5E#\2\u01c4\u01c6\5G$\2\u01c5\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7")
        buf.write("\u01c8\5\u00c5c\2\u01c8L\3\2\2\2\u01c9\u01cc\5E#\2\u01ca")
        buf.write("\u01cc\5G$\2\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01ce\5\u00c7d\2\u01ceN\3\2\2\2\u01cf")
        buf.write("\u01d0\7*\2\2\u01d0P\3\2\2\2\u01d1\u01d2\7+\2\2\u01d2")
        buf.write("R\3\2\2\2\u01d3\u01d4\7}\2\2\u01d4T\3\2\2\2\u01d5\u01d6")
        buf.write("\7\177\2\2\u01d6V\3\2\2\2\u01d7\u01d8\7]\2\2\u01d8X\3")
        buf.write("\2\2\2\u01d9\u01da\7_\2\2\u01daZ\3\2\2\2\u01db\u01dc\7")
        buf.write("=\2\2\u01dc\\\3\2\2\2\u01dd\u01de\7.\2\2\u01de^\3\2\2")
        buf.write("\2\u01df\u01e0\7\60\2\2\u01e0`\3\2\2\2\u01e1\u01e2\7?")
        buf.write("\2\2\u01e2b\3\2\2\2\u01e3\u01e4\7@\2\2\u01e4d\3\2\2\2")
        buf.write("\u01e5\u01e6\7>\2\2\u01e6f\3\2\2\2\u01e7\u01e8\7#\2\2")
        buf.write("\u01e8h\3\2\2\2\u01e9\u01ea\7\u0080\2\2\u01eaj\3\2\2\2")
        buf.write("\u01eb\u01ec\7A\2\2\u01ecl\3\2\2\2\u01ed\u01ee\7<\2\2")
        buf.write("\u01een\3\2\2\2\u01ef\u01f0\7?\2\2\u01f0\u01f1\7?\2\2")
        buf.write("\u01f1p\3\2\2\2\u01f2\u01f3\7>\2\2\u01f3\u01f4\7?\2\2")
        buf.write("\u01f4r\3\2\2\2\u01f5\u01f6\7@\2\2\u01f6\u01f7\7?\2\2")
        buf.write("\u01f7t\3\2\2\2\u01f8\u01f9\7#\2\2\u01f9\u01fa\7?\2\2")
        buf.write("\u01fav\3\2\2\2\u01fb\u01fc\7(\2\2\u01fc\u01fd\7(\2\2")
        buf.write("\u01fdx\3\2\2\2\u01fe\u01ff\7~\2\2\u01ff\u0200\7~\2\2")
        buf.write("\u0200z\3\2\2\2\u0201\u0202\7-\2\2\u0202\u0203\7-\2\2")
        buf.write("\u0203|\3\2\2\2\u0204\u0205\7/\2\2\u0205\u0206\7/\2\2")
        buf.write("\u0206~\3\2\2\2\u0207\u0208\7-\2\2\u0208\u0080\3\2\2\2")
        buf.write("\u0209\u020a\7/\2\2\u020a\u0082\3\2\2\2\u020b\u020c\7")
        buf.write(",\2\2\u020c\u0084\3\2\2\2\u020d\u020e\7\61\2\2\u020e\u0086")
        buf.write("\3\2\2\2\u020f\u0210\7(\2\2\u0210\u0088\3\2\2\2\u0211")
        buf.write("\u0212\7~\2\2\u0212\u008a\3\2\2\2\u0213\u0214\7`\2\2\u0214")
        buf.write("\u008c\3\2\2\2\u0215\u0216\7\'\2\2\u0216\u008e\3\2\2\2")
        buf.write("\u0217\u0218\7a\2\2\u0218\u0090\3\2\2\2\u0219\u021a\7")
        buf.write("p\2\2\u021a\u021b\7u\2\2\u021b\u0092\3\2\2\2\u021c\u021d")
        buf.write("\7w\2\2\u021d\u021e\7u\2\2\u021e\u0094\3\2\2\2\u021f\u0220")
        buf.write("\7o\2\2\u0220\u0221\7u\2\2\u0221\u0096\3\2\2\2\u0222\u0223")
        buf.write("\7e\2\2\u0223\u0224\7u\2\2\u0224\u0098\3\2\2\2\u0225\u0226")
        buf.write("\7f\2\2\u0226\u0227\7u\2\2\u0227\u009a\3\2\2\2\u0228\u0229")
        buf.write("\7u\2\2\u0229\u009c\3\2\2\2\u022a\u022b\7o\2\2\u022b\u009e")
        buf.write("\3\2\2\2\u022c\u022d\7j\2\2\u022d\u00a0\3\2\2\2\u022e")
        buf.write("\u022f\7f\2\2\u022f\u00a2\3\2\2\2\u0230\u0231\7y\2\2\u0231")
        buf.write("\u00a4\3\2\2\2\u0232\u0233\7o\2\2\u0233\u0234\7q\2\2\u0234")
        buf.write("\u00a6\3\2\2\2\u0235\u0236\7{\2\2\u0236\u00a8\3\2\2\2")
        buf.write("\u0237\u0238\7p\2\2\u0238\u0239\7N\2\2\u0239\u00aa\3\2")
        buf.write("\2\2\u023a\u023b\7w\2\2\u023b\u023c\7N\2\2\u023c\u00ac")
        buf.write("\3\2\2\2\u023d\u023e\7o\2\2\u023e\u023f\7N\2\2\u023f\u00ae")
        buf.write("\3\2\2\2\u0240\u0241\7e\2\2\u0241\u0242\7N\2\2\u0242\u00b0")
        buf.write("\3\2\2\2\u0243\u0244\7f\2\2\u0244\u0245\7N\2\2\u0245\u00b2")
        buf.write("\3\2\2\2\u0246\u0247\7N\2\2\u0247\u00b4\3\2\2\2\u0248")
        buf.write("\u0249\7f\2\2\u0249\u024a\7c\2\2\u024a\u024b\7N\2\2\u024b")
        buf.write("\u00b6\3\2\2\2\u024c\u024d\7e\2\2\u024d\u00b8\3\2\2\2")
        buf.write("\u024e\u024f\7h\2\2\u024f\u00ba\3\2\2\2\u0250\u0251\7")
        buf.write("m\2\2\u0251\u00bc\3\2\2\2\u0252\u0254\t\3\2\2\u0253\u0252")
        buf.write("\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0253\3\2\2\2\u0255")
        buf.write("\u0256\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0258\b_\2\2")
        buf.write("\u0258\u00be\3\2\2\2\u0259\u025a\7\61\2\2\u025a\u025b")
        buf.write("\7,\2\2\u025b\u025f\3\2\2\2\u025c\u025e\13\2\2\2\u025d")
        buf.write("\u025c\3\2\2\2\u025e\u0261\3\2\2\2\u025f\u0260\3\2\2\2")
        buf.write("\u025f\u025d\3\2\2\2\u0260\u0262\3\2\2\2\u0261\u025f\3")
        buf.write("\2\2\2\u0262\u0263\7,\2\2\u0263\u0264\7\61\2\2\u0264\u0265")
        buf.write("\3\2\2\2\u0265\u0266\b`\2\2\u0266\u00c0\3\2\2\2\u0267")
        buf.write("\u0268\7\61\2\2\u0268\u0269\7\61\2\2\u0269\u026d\3\2\2")
        buf.write("\2\u026a\u026c\n\4\2\2\u026b\u026a\3\2\2\2\u026c\u026f")
        buf.write("\3\2\2\2\u026d\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e")
        buf.write("\u0270\3\2\2\2\u026f\u026d\3\2\2\2\u0270\u0271\ba\2\2")
        buf.write("\u0271\u00c2\3\2\2\2\u0272\u027f\5\u0091I\2\u0273\u027f")
        buf.write("\5\u0093J\2\u0274\u027f\5\u0095K\2\u0275\u027f\5\u0097")
        buf.write("L\2\u0276\u027f\5\u0099M\2\u0277\u027f\5\u009bN\2\u0278")
        buf.write("\u027f\5\u009dO\2\u0279\u027f\5\u009fP\2\u027a\u027f\5")
        buf.write("\u00a1Q\2\u027b\u027f\5\u00a3R\2\u027c\u027f\5\u00a5S")
        buf.write("\2\u027d\u027f\5\u00a7T\2\u027e\u0272\3\2\2\2\u027e\u0273")
        buf.write("\3\2\2\2\u027e\u0274\3\2\2\2\u027e\u0275\3\2\2\2\u027e")
        buf.write("\u0276\3\2\2\2\u027e\u0277\3\2\2\2\u027e\u0278\3\2\2\2")
        buf.write("\u027e\u0279\3\2\2\2\u027e\u027a\3\2\2\2\u027e\u027b\3")
        buf.write("\2\2\2\u027e\u027c\3\2\2\2\u027e\u027d\3\2\2\2\u027f\u00c4")
        buf.write("\3\2\2\2\u0280\u0287\5\u00a9U\2\u0281\u0287\5\u00abV\2")
        buf.write("\u0282\u0287\5\u00adW\2\u0283\u0287\5\u00afX\2\u0284\u0287")
        buf.write("\5\u00b3Z\2\u0285\u0287\5\u00b5[\2\u0286\u0280\3\2\2\2")
        buf.write("\u0286\u0281\3\2\2\2\u0286\u0282\3\2\2\2\u0286\u0283\3")
        buf.write("\2\2\2\u0286\u0284\3\2\2\2\u0286\u0285\3\2\2\2\u0287\u00c6")
        buf.write("\3\2\2\2\u0288\u028c\5\u00b9]\2\u0289\u028c\5\u00b7\\")
        buf.write("\2\u028a\u028c\5\u00bb^\2\u028b\u0288\3\2\2\2\u028b\u0289")
        buf.write("\3\2\2\2\u028b\u028a\3\2\2\2\u028c\u00c8\3\2\2\2\u028d")
        buf.write("\u0295\t\5\2\2\u028e\u0290\t\6\2\2\u028f\u028e\3\2\2\2")
        buf.write("\u0290\u0293\3\2\2\2\u0291\u028f\3\2\2\2\u0291\u0292\3")
        buf.write("\2\2\2\u0292\u0294\3\2\2\2\u0293\u0291\3\2\2\2\u0294\u0296")
        buf.write("\t\5\2\2\u0295\u0291\3\2\2\2\u0295\u0296\3\2\2\2\u0296")
        buf.write("\u00ca\3\2\2\2\u0297\u029a\5\u00cdg\2\u0298\u029a\t\5")
        buf.write("\2\2\u0299\u0297\3\2\2\2\u0299\u0298\3\2\2\2\u029a\u00cc")
        buf.write("\3\2\2\2\u029b\u02a0\t\7\2\2\u029c\u02a0\n\b\2\2\u029d")
        buf.write("\u029e\t\t\2\2\u029e\u02a0\t\n\2\2\u029f\u029b\3\2\2\2")
        buf.write("\u029f\u029c\3\2\2\2\u029f\u029d\3\2\2\2\u02a0\u00ce\3")
        buf.write("\2\2\2\u02a1\u02a2\7^\2\2\u02a2\u02ac\t\13\2\2\u02a3\u02a8")
        buf.write("\7^\2\2\u02a4\u02a6\t\f\2\2\u02a5\u02a4\3\2\2\2\u02a5")
        buf.write("\u02a6\3\2\2\2\u02a6\u02a7\3\2\2\2\u02a7\u02a9\t\r\2\2")
        buf.write("\u02a8\u02a5\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02aa\3")
        buf.write("\2\2\2\u02aa\u02ac\t\r\2\2\u02ab\u02a1\3\2\2\2\u02ab\u02a3")
        buf.write("\3\2\2\2\u02ac\u00d0\3\2\2\2\u02ad\u02af\t\16\2\2\u02ae")
        buf.write("\u02ad\3\2\2\2\u02af\u02b0\3\2\2\2\u02b0\u02ae\3\2\2\2")
        buf.write("\u02b0\u02b1\3\2\2\2\u02b1\u00d2\3\2\2\2\u02b2\u02b4\7")
        buf.write("\17\2\2\u02b3\u02b2\3\2\2\2\u02b3\u02b4\3\2\2\2\u02b4")
        buf.write("\u02b5\3\2\2\2\u02b5\u02b8\7\f\2\2\u02b6\u02b8\4\16\17")
        buf.write("\2\u02b7\u02b3\3\2\2\2\u02b7\u02b6\3\2\2\2\u02b8\u00d4")
        buf.write("\3\2\2\2\35\2\u0195\u019b\u019d\u01ab\u01b0\u01b4\u01ba")
        buf.write("\u01bf\u01c5\u01cb\u0255\u025f\u026d\u027e\u0286\u028b")
        buf.write("\u0291\u0295\u0299\u029f\u02a5\u02a8\u02ab\u02b0\u02b3")
        buf.write("\u02b7\3\2\3\2")
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
    AT = 20
    WITH = 21
    FOR = 22
    INTO = 23
    TIMES = 24
    ON = 25
    OF = 26
    NAT = 27
    REAL = 28
    MAT = 29
    BOOL = 30
    IDENTIFIER = 31
    STRING_LITERAL = 32
    BOOL_LITERAL = 33
    FLOAT_LITERAL = 34
    INTEGER_LITERAL = 35
    TIME_NUMBER = 36
    VOLUME_NUMBER = 37
    TEMP_NUMBER = 38
    LPAREN = 39
    RPAREN = 40
    LBRACE = 41
    RBRACE = 42
    LBRACKET = 43
    RBRACKET = 44
    SEMICOLON = 45
    COMMA = 46
    DOT = 47
    ASSIGN = 48
    GT = 49
    LT = 50
    BANG = 51
    TILDE = 52
    QUESTION = 53
    COLON = 54
    EQUALITY = 55
    LTE = 56
    GTE = 57
    NOTEQUAL = 58
    AND = 59
    OR = 60
    INC = 61
    DEC = 62
    ADDITION = 63
    SUBTRACT = 64
    MULTIPLY = 65
    DIVIDE = 66
    BITAND = 67
    BITOR = 68
    CARET = 69
    MOD = 70
    UNDERSCORE = 71
    NANOSECOND = 72
    MICROSECOND = 73
    MILLISECOND = 74
    CENTISECOND = 75
    DECISECOND = 76
    SECOND = 77
    MINUTE = 78
    HOUR = 79
    DAY = 80
    WEEK = 81
    MONTH = 82
    YEAR = 83
    NANOLITRE = 84
    MICROLITRE = 85
    MILLILITRE = 86
    CENTILITRE = 87
    DECILITRE = 88
    LITRE = 89
    DECALITRE = 90
    CELSIUS = 91
    FAHRENHEIT = 92
    KELVIN = 93
    WS = 94
    COMMENT = 95
    LINE_COMMENT = 96

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'repeat'", "'while'", "'function'", "'return'", 
            "'manifest'", "'module'", "'stationary'", "'functions'", "'instructions'", 
            "'detect'", "'mix'", "'split'", "'heat'", "'drain'", "'dispense'", 
            "'dispose'", "'gradient'", "'at'", "'with'", "'for'", "'into'", 
            "'times'", "'on'", "'of'", "'nat'", "'real'", "'mat'", "'bool'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", 
            "'='", "'>'", "'<'", "'!'", "'~'", "'?'", "':'", "'=='", "'<='", 
            "'>='", "'!='", "'&&'", "'||'", "'++'", "'--'", "'+'", "'-'", 
            "'*'", "'/'", "'&'", "'|'", "'^'", "'%'", "'_'", "'ns'", "'us'", 
            "'ms'", "'cs'", "'ds'", "'s'", "'m'", "'h'", "'d'", "'w'", "'mo'", 
            "'y'", "'nL'", "'uL'", "'mL'", "'cL'", "'dL'", "'L'", "'daL'", 
            "'c'", "'f'", "'k'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", "RETURN", "MANIFEST", 
            "MODULE", "STATIONARY", "FUNCTIONS", "INSTRUCTIONS", "DETECT", 
            "MIX", "SPLIT", "HEAT", "DRAIN", "DISPENSE", "DISPOSE", "GRADIENT", 
            "AT", "WITH", "FOR", "INTO", "TIMES", "ON", "OF", "NAT", "REAL", 
            "MAT", "BOOL", "IDENTIFIER", "STRING_LITERAL", "BOOL_LITERAL", 
            "FLOAT_LITERAL", "INTEGER_LITERAL", "TIME_NUMBER", "VOLUME_NUMBER", 
            "TEMP_NUMBER", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
            "RBRACKET", "SEMICOLON", "COMMA", "DOT", "ASSIGN", "GT", "LT", 
            "BANG", "TILDE", "QUESTION", "COLON", "EQUALITY", "LTE", "GTE", 
            "NOTEQUAL", "AND", "OR", "INC", "DEC", "ADDITION", "SUBTRACT", 
            "MULTIPLY", "DIVIDE", "BITAND", "BITOR", "CARET", "MOD", "UNDERSCORE", 
            "NANOSECOND", "MICROSECOND", "MILLISECOND", "CENTISECOND", "DECISECOND", 
            "SECOND", "MINUTE", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", 
            "NANOLITRE", "MICROLITRE", "MILLILITRE", "CENTILITRE", "DECILITRE", 
            "LITRE", "DECALITRE", "CELSIUS", "FAHRENHEIT", "KELVIN", "WS", 
            "COMMENT", "LINE_COMMENT" ]

    ruleNames = [ "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", "RETURN", 
                  "MANIFEST", "MODULE", "STATIONARY", "FUNCTIONS", "INSTRUCTIONS", 
                  "DETECT", "MIX", "SPLIT", "HEAT", "DRAIN", "DISPENSE", 
                  "DISPOSE", "GRADIENT", "AT", "WITH", "FOR", "INTO", "TIMES", 
                  "ON", "OF", "NAT", "REAL", "MAT", "BOOL", "IDENTIFIER", 
                  "STRING_LITERAL", "BOOL_LITERAL", "FLOAT_LITERAL", "INTEGER_LITERAL", 
                  "TIME_NUMBER", "VOLUME_NUMBER", "TEMP_NUMBER", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                  "SEMICOLON", "COMMA", "DOT", "ASSIGN", "GT", "LT", "BANG", 
                  "TILDE", "QUESTION", "COLON", "EQUALITY", "LTE", "GTE", 
                  "NOTEQUAL", "AND", "OR", "INC", "DEC", "ADDITION", "SUBTRACT", 
                  "MULTIPLY", "DIVIDE", "BITAND", "BITOR", "CARET", "MOD", 
                  "UNDERSCORE", "NANOSECOND", "MICROSECOND", "MILLISECOND", 
                  "CENTISECOND", "DECISECOND", "SECOND", "MINUTE", "HOUR", 
                  "DAY", "WEEK", "MONTH", "YEAR", "NANOLITRE", "MICROLITRE", 
                  "MILLILITRE", "CENTILITRE", "DECILITRE", "LITRE", "DECALITRE", 
                  "CELSIUS", "FAHRENHEIT", "KELVIN", "WS", "COMMENT", "LINE_COMMENT", 
                  "TimeUnits", "VolumeUnits", "TempUnits", "Digits", "LetterOrDigit", 
                  "Letter", "EscapeSequence", "SPACES", "NEWLINE" ]

    grammarFileName = "BSLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


