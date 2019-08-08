# Generated from /home/warfield/Github/BioScriptGrammar/grammar/BSLexer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2j")
        buf.write("\u02ff\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \7 \u01a4\n \f \16 \u01a7\13 \3!\3!\3!\7!\u01ac")
        buf.write("\n!\f!\16!\u01af\13!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u01bc\n\"\3#\3#\3#\5#\u01c1\n#\3#\3#\5#\u01c5")
        buf.write("\n#\3$\3$\7$\u01c9\n$\f$\16$\u01cc\13$\3%\3%\5%\u01d0")
        buf.write("\n%\3%\3%\3&\3&\5&\u01d6\n&\3&\3&\3\'\3\'\5\'\u01dc\n")
        buf.write("\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:")
        buf.write("\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3")
        buf.write("B\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3H\3")
        buf.write("H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3")
        buf.write("Q\3Q\3R\3R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3U\3V\3V\3W\3W\3")
        buf.write("X\3X\3Y\3Y\3Z\3Z\3[\3[\3[\3\\\3\\\3]\3]\3]\3^\3^\3^\3")
        buf.write("_\3_\3_\3`\3`\3`\3a\3a\3a\3b\3b\3c\3c\3c\3c\3d\3d\3e\3")
        buf.write("e\3f\3f\3g\6g\u029a\ng\rg\16g\u029b\3g\3g\3h\3h\3h\3h")
        buf.write("\7h\u02a4\nh\fh\16h\u02a7\13h\3h\3h\3h\3h\3h\3i\3i\3i")
        buf.write("\3i\7i\u02b2\ni\fi\16i\u02b5\13i\3i\3i\3j\3j\3j\3j\3j")
        buf.write("\3j\3j\3j\3j\3j\3j\3j\5j\u02c5\nj\3k\3k\3k\3k\3k\3k\5")
        buf.write("k\u02cd\nk\3l\3l\3l\5l\u02d2\nl\3m\3m\7m\u02d6\nm\fm\16")
        buf.write("m\u02d9\13m\3m\5m\u02dc\nm\3n\3n\5n\u02e0\nn\3o\3o\3o")
        buf.write("\3o\5o\u02e6\no\3p\3p\3p\3p\5p\u02ec\np\3p\5p\u02ef\n")
        buf.write("p\3p\5p\u02f2\np\3q\6q\u02f5\nq\rq\16q\u02f6\3r\5r\u02fa")
        buf.write("\nr\3r\3r\5r\u02fe\nr\3\u02a5\2s\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091")
        buf.write("J\u0093K\u0095L\u0097M\u0099N\u009bO\u009dP\u009fQ\u00a1")
        buf.write("R\u00a3S\u00a5T\u00a7U\u00a9V\u00abW\u00adX\u00afY\u00b1")
        buf.write("Z\u00b3[\u00b5\\\u00b7]\u00b9^\u00bb_\u00bd`\u00bfa\u00c1")
        buf.write("b\u00c3c\u00c5d\u00c7e\u00c9f\u00cbg\u00cdh\u00cfi\u00d1")
        buf.write("j\u00d3\2\u00d5\2\u00d7\2\u00d9\2\u00db\2\u00dd\2\u00df")
        buf.write("\2\u00e1\2\u00e3\2\3\2\17\6\2\f\f\17\17$$^^\5\2\13\f\16")
        buf.write("\17\"\"\4\2\f\f\17\17\3\2\62;\4\2\62;aa\6\2&&C\\aac|\4")
        buf.write("\2\2\u0081\ud802\udc01\3\2\ud802\udc01\3\2\udc02\ue001")
        buf.write("\n\2$$))^^ddhhppttvv\3\2\62\65\3\2\629\4\2\13\13\"\"\2")
        buf.write("\u031f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3")
        buf.write("\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2")
        buf.write("\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1")
        buf.write("\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2")
        buf.write("\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf")
        buf.write("\3\2\2\2\2\u00d1\3\2\2\2\3\u00e5\3\2\2\2\5\u00e8\3\2\2")
        buf.write("\2\7\u00ed\3\2\2\2\t\u00f4\3\2\2\2\13\u00fa\3\2\2\2\r")
        buf.write("\u0103\3\2\2\2\17\u010a\3\2\2\2\21\u0113\3\2\2\2\23\u011a")
        buf.write("\3\2\2\2\25\u0125\3\2\2\2\27\u012f\3\2\2\2\31\u013c\3")
        buf.write("\2\2\2\33\u0143\3\2\2\2\35\u0147\3\2\2\2\37\u014d\3\2")
        buf.write("\2\2!\u0152\3\2\2\2#\u0158\3\2\2\2%\u0161\3\2\2\2\'\u0169")
        buf.write("\3\2\2\2)\u0172\3\2\2\2+\u0175\3\2\2\2-\u017a\3\2\2\2")
        buf.write("/\u017e\3\2\2\2\61\u0183\3\2\2\2\63\u0189\3\2\2\2\65\u018c")
        buf.write("\3\2\2\2\67\u018f\3\2\2\29\u0193\3\2\2\2;\u0198\3\2\2")
        buf.write("\2=\u019c\3\2\2\2?\u01a1\3\2\2\2A\u01a8\3\2\2\2C\u01bb")
        buf.write("\3\2\2\2E\u01c4\3\2\2\2G\u01c6\3\2\2\2I\u01cf\3\2\2\2")
        buf.write("K\u01d5\3\2\2\2M\u01db\3\2\2\2O\u01df\3\2\2\2Q\u01e4\3")
        buf.write("\2\2\2S\u01ef\3\2\2\2U\u01f8\3\2\2\2W\u01fe\3\2\2\2Y\u0204")
        buf.write("\3\2\2\2[\u020d\3\2\2\2]\u0213\3\2\2\2_\u0215\3\2\2\2")
        buf.write("a\u0217\3\2\2\2c\u0219\3\2\2\2e\u021b\3\2\2\2g\u021d\3")
        buf.write("\2\2\2i\u021f\3\2\2\2k\u0221\3\2\2\2m\u0223\3\2\2\2o\u0225")
        buf.write("\3\2\2\2q\u0227\3\2\2\2s\u0229\3\2\2\2u\u022b\3\2\2\2")
        buf.write("w\u022d\3\2\2\2y\u022f\3\2\2\2{\u0231\3\2\2\2}\u0233\3")
        buf.write("\2\2\2\177\u0236\3\2\2\2\u0081\u0239\3\2\2\2\u0083\u023c")
        buf.write("\3\2\2\2\u0085\u023f\3\2\2\2\u0087\u0242\3\2\2\2\u0089")
        buf.write("\u0245\3\2\2\2\u008b\u0248\3\2\2\2\u008d\u024b\3\2\2\2")
        buf.write("\u008f\u024d\3\2\2\2\u0091\u024f\3\2\2\2\u0093\u0251\3")
        buf.write("\2\2\2\u0095\u0253\3\2\2\2\u0097\u0255\3\2\2\2\u0099\u0257")
        buf.write("\3\2\2\2\u009b\u0259\3\2\2\2\u009d\u025b\3\2\2\2\u009f")
        buf.write("\u025d\3\2\2\2\u00a1\u025f\3\2\2\2\u00a3\u0262\3\2\2\2")
        buf.write("\u00a5\u0265\3\2\2\2\u00a7\u0268\3\2\2\2\u00a9\u026b\3")
        buf.write("\2\2\2\u00ab\u026e\3\2\2\2\u00ad\u0270\3\2\2\2\u00af\u0272")
        buf.write("\3\2\2\2\u00b1\u0274\3\2\2\2\u00b3\u0276\3\2\2\2\u00b5")
        buf.write("\u0278\3\2\2\2\u00b7\u027b\3\2\2\2\u00b9\u027d\3\2\2\2")
        buf.write("\u00bb\u0280\3\2\2\2\u00bd\u0283\3\2\2\2\u00bf\u0286\3")
        buf.write("\2\2\2\u00c1\u0289\3\2\2\2\u00c3\u028c\3\2\2\2\u00c5\u028e")
        buf.write("\3\2\2\2\u00c7\u0292\3\2\2\2\u00c9\u0294\3\2\2\2\u00cb")
        buf.write("\u0296\3\2\2\2\u00cd\u0299\3\2\2\2\u00cf\u029f\3\2\2\2")
        buf.write("\u00d1\u02ad\3\2\2\2\u00d3\u02c4\3\2\2\2\u00d5\u02cc\3")
        buf.write("\2\2\2\u00d7\u02d1\3\2\2\2\u00d9\u02d3\3\2\2\2\u00db\u02df")
        buf.write("\3\2\2\2\u00dd\u02e5\3\2\2\2\u00df\u02f1\3\2\2\2\u00e1")
        buf.write("\u02f4\3\2\2\2\u00e3\u02fd\3\2\2\2\u00e5\u00e6\7k\2\2")
        buf.write("\u00e6\u00e7\7h\2\2\u00e7\4\3\2\2\2\u00e8\u00e9\7g\2\2")
        buf.write("\u00e9\u00ea\7n\2\2\u00ea\u00eb\7u\2\2\u00eb\u00ec\7g")
        buf.write("\2\2\u00ec\6\3\2\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef\7")
        buf.write("g\2\2\u00ef\u00f0\7r\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7c\2\2\u00f2\u00f3\7v\2\2\u00f3\b\3\2\2\2\u00f4\u00f5")
        buf.write("\7y\2\2\u00f5\u00f6\7j\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8")
        buf.write("\7n\2\2\u00f8\u00f9\7g\2\2\u00f9\n\3\2\2\2\u00fa\u00fb")
        buf.write("\7h\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe")
        buf.write("\7e\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7k\2\2\u0100\u0101")
        buf.write("\7q\2\2\u0101\u0102\7p\2\2\u0102\f\3\2\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104\u0105\7g\2\2\u0105\u0106\7v\2\2\u0106\u0107")
        buf.write("\7w\2\2\u0107\u0108\7t\2\2\u0108\u0109\7p\2\2\u0109\16")
        buf.write("\3\2\2\2\u010a\u010b\7o\2\2\u010b\u010c\7c\2\2\u010c\u010d")
        buf.write("\7p\2\2\u010d\u010e\7k\2\2\u010e\u010f\7h\2\2\u010f\u0110")
        buf.write("\7g\2\2\u0110\u0111\7u\2\2\u0111\u0112\7v\2\2\u0112\20")
        buf.write("\3\2\2\2\u0113\u0114\7o\2\2\u0114\u0115\7q\2\2\u0115\u0116")
        buf.write("\7f\2\2\u0116\u0117\7w\2\2\u0117\u0118\7n\2\2\u0118\u0119")
        buf.write("\7g\2\2\u0119\22\3\2\2\2\u011a\u011b\7u\2\2\u011b\u011c")
        buf.write("\7v\2\2\u011c\u011d\7c\2\2\u011d\u011e\7v\2\2\u011e\u011f")
        buf.write("\7k\2\2\u011f\u0120\7q\2\2\u0120\u0121\7p\2\2\u0121\u0122")
        buf.write("\7c\2\2\u0122\u0123\7t\2\2\u0123\u0124\7{\2\2\u0124\24")
        buf.write("\3\2\2\2\u0125\u0126\7h\2\2\u0126\u0127\7w\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128\u0129\7e\2\2\u0129\u012a\7v\2\2\u012a\u012b")
        buf.write("\7k\2\2\u012b\u012c\7q\2\2\u012c\u012d\7p\2\2\u012d\u012e")
        buf.write("\7u\2\2\u012e\26\3\2\2\2\u012f\u0130\7k\2\2\u0130\u0131")
        buf.write("\7p\2\2\u0131\u0132\7u\2\2\u0132\u0133\7v\2\2\u0133\u0134")
        buf.write("\7t\2\2\u0134\u0135\7w\2\2\u0135\u0136\7e\2\2\u0136\u0137")
        buf.write("\7v\2\2\u0137\u0138\7k\2\2\u0138\u0139\7q\2\2\u0139\u013a")
        buf.write("\7p\2\2\u013a\u013b\7u\2\2\u013b\30\3\2\2\2\u013c\u013d")
        buf.write("\7f\2\2\u013d\u013e\7g\2\2\u013e\u013f\7v\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140\u0141\7e\2\2\u0141\u0142\7v\2\2\u0142\32")
        buf.write("\3\2\2\2\u0143\u0144\7o\2\2\u0144\u0145\7k\2\2\u0145\u0146")
        buf.write("\7z\2\2\u0146\34\3\2\2\2\u0147\u0148\7u\2\2\u0148\u0149")
        buf.write("\7r\2\2\u0149\u014a\7n\2\2\u014a\u014b\7k\2\2\u014b\u014c")
        buf.write("\7v\2\2\u014c\36\3\2\2\2\u014d\u014e\7j\2\2\u014e\u014f")
        buf.write("\7g\2\2\u014f\u0150\7c\2\2\u0150\u0151\7v\2\2\u0151 \3")
        buf.write("\2\2\2\u0152\u0153\7f\2\2\u0153\u0154\7t\2\2\u0154\u0155")
        buf.write("\7c\2\2\u0155\u0156\7k\2\2\u0156\u0157\7p\2\2\u0157\"")
        buf.write("\3\2\2\2\u0158\u0159\7f\2\2\u0159\u015a\7k\2\2\u015a\u015b")
        buf.write("\7u\2\2\u015b\u015c\7r\2\2\u015c\u015d\7g\2\2\u015d\u015e")
        buf.write("\7p\2\2\u015e\u015f\7u\2\2\u015f\u0160\7g\2\2\u0160$\3")
        buf.write("\2\2\2\u0161\u0162\7f\2\2\u0162\u0163\7k\2\2\u0163\u0164")
        buf.write("\7u\2\2\u0164\u0165\7r\2\2\u0165\u0166\7q\2\2\u0166\u0167")
        buf.write("\7u\2\2\u0167\u0168\7g\2\2\u0168&\3\2\2\2\u0169\u016a")
        buf.write("\7i\2\2\u016a\u016b\7t\2\2\u016b\u016c\7c\2\2\u016c\u016d")
        buf.write("\7f\2\2\u016d\u016e\7k\2\2\u016e\u016f\7g\2\2\u016f\u0170")
        buf.write("\7p\2\2\u0170\u0171\7v\2\2\u0171(\3\2\2\2\u0172\u0173")
        buf.write("\7c\2\2\u0173\u0174\7v\2\2\u0174*\3\2\2\2\u0175\u0176")
        buf.write("\7y\2\2\u0176\u0177\7k\2\2\u0177\u0178\7v\2\2\u0178\u0179")
        buf.write("\7j\2\2\u0179,\3\2\2\2\u017a\u017b\7h\2\2\u017b\u017c")
        buf.write("\7q\2\2\u017c\u017d\7t\2\2\u017d.\3\2\2\2\u017e\u017f")
        buf.write("\7k\2\2\u017f\u0180\7p\2\2\u0180\u0181\7v\2\2\u0181\u0182")
        buf.write("\7q\2\2\u0182\60\3\2\2\2\u0183\u0184\7v\2\2\u0184\u0185")
        buf.write("\7k\2\2\u0185\u0186\7o\2\2\u0186\u0187\7g\2\2\u0187\u0188")
        buf.write("\7u\2\2\u0188\62\3\2\2\2\u0189\u018a\7q\2\2\u018a\u018b")
        buf.write("\7p\2\2\u018b\64\3\2\2\2\u018c\u018d\7q\2\2\u018d\u018e")
        buf.write("\7h\2\2\u018e\66\3\2\2\2\u018f\u0190\7p\2\2\u0190\u0191")
        buf.write("\7c\2\2\u0191\u0192\7v\2\2\u01928\3\2\2\2\u0193\u0194")
        buf.write("\7t\2\2\u0194\u0195\7g\2\2\u0195\u0196\7c\2\2\u0196\u0197")
        buf.write("\7n\2\2\u0197:\3\2\2\2\u0198\u0199\7o\2\2\u0199\u019a")
        buf.write("\7c\2\2\u019a\u019b\7v\2\2\u019b<\3\2\2\2\u019c\u019d")
        buf.write("\7d\2\2\u019d\u019e\7q\2\2\u019e\u019f\7q\2\2\u019f\u01a0")
        buf.write("\7n\2\2\u01a0>\3\2\2\2\u01a1\u01a5\5\u00ddo\2\u01a2\u01a4")
        buf.write("\5\u00dbn\2\u01a3\u01a2\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6@\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a8\u01ad\7$\2\2\u01a9\u01ac\n\2\2\2")
        buf.write("\u01aa\u01ac\5\u00dfp\2\u01ab\u01a9\3\2\2\2\u01ab\u01aa")
        buf.write("\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad")
        buf.write("\u01ae\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u01ad\3\2\2\2")
        buf.write("\u01b0\u01b1\7$\2\2\u01b1B\3\2\2\2\u01b2\u01b3\7v\2\2")
        buf.write("\u01b3\u01b4\7t\2\2\u01b4\u01b5\7w\2\2\u01b5\u01bc\7g")
        buf.write("\2\2\u01b6\u01b7\7h\2\2\u01b7\u01b8\7c\2\2\u01b8\u01b9")
        buf.write("\7n\2\2\u01b9\u01ba\7u\2\2\u01ba\u01bc\7g\2\2\u01bb\u01b2")
        buf.write("\3\2\2\2\u01bb\u01b6\3\2\2\2\u01bcD\3\2\2\2\u01bd\u01be")
        buf.write("\5\u00d9m\2\u01be\u01c0\7\60\2\2\u01bf\u01c1\5\u00d9m")
        buf.write("\2\u01c0\u01bf\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c5")
        buf.write("\3\2\2\2\u01c2\u01c3\7\60\2\2\u01c3\u01c5\5\u00d9m\2\u01c4")
        buf.write("\u01bd\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5F\3\2\2\2\u01c6")
        buf.write("\u01ca\5\u00d9m\2\u01c7\u01c9\5\u00d9m\2\u01c8\u01c7\3")
        buf.write("\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb")
        buf.write("\3\2\2\2\u01cbH\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01d0")
        buf.write("\5E#\2\u01ce\u01d0\5G$\2\u01cf\u01cd\3\2\2\2\u01cf\u01ce")
        buf.write("\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2\5\u00d3j\2\u01d2")
        buf.write("J\3\2\2\2\u01d3\u01d6\5E#\2\u01d4\u01d6\5G$\2\u01d5\u01d3")
        buf.write("\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("\u01d8\5\u00d5k\2\u01d8L\3\2\2\2\u01d9\u01dc\5E#\2\u01da")
        buf.write("\u01dc\5G$\2\u01db\u01d9\3\2\2\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01dd\u01de\5\u00d7l\2\u01deN\3\2\2\2\u01df")
        buf.write("\u01e0\7o\2\2\u01e0\u01e1\7c\2\2\u01e1\u01e2\7u\2\2\u01e2")
        buf.write("\u01e3\7u\2\2\u01e3P\3\2\2\2\u01e4\u01e5\7g\2\2\u01e5")
        buf.write("\u01e6\7h\2\2\u01e6\u01e7\7h\2\2\u01e7\u01e8\7k\2\2\u01e8")
        buf.write("\u01e9\7e\2\2\u01e9\u01ea\7k\2\2\u01ea\u01eb\7g\2\2\u01eb")
        buf.write("\u01ec\7p\2\2\u01ec\u01ed\7e\2\2\u01ed\u01ee\7{\2\2\u01ee")
        buf.write("R\3\2\2\2\u01ef\u01f0\7r\2\2\u01f0\u01f1\7t\2\2\u01f1")
        buf.write("\u01f2\7g\2\2\u01f2\u01f3\7u\2\2\u01f3\u01f4\7u\2\2\u01f4")
        buf.write("\u01f5\7w\2\2\u01f5\u01f6\7t\2\2\u01f6\u01f7\7g\2\2\u01f7")
        buf.write("T\3\2\2\2\u01f8\u01f9\7h\2\2\u01f9\u01fa\7q\2\2\u01fa")
        buf.write("\u01fb\7t\2\2\u01fb\u01fc\7e\2\2\u01fc\u01fd\7g\2\2\u01fd")
        buf.write("V\3\2\2\2\u01fe\u01ff\7u\2\2\u01ff\u0200\7r\2\2\u0200")
        buf.write("\u0201\7g\2\2\u0201\u0202\7g\2\2\u0202\u0203\7f\2\2\u0203")
        buf.write("X\3\2\2\2\u0204\u0205\7h\2\2\u0205\u0206\7t\2\2\u0206")
        buf.write("\u0207\7k\2\2\u0207\u0208\7e\2\2\u0208\u0209\7v\2\2\u0209")
        buf.write("\u020a\7k\2\2\u020a\u020b\7q\2\2\u020b\u020c\7p\2\2\u020c")
        buf.write("Z\3\2\2\2\u020d\u020e\7w\2\2\u020e\u020f\7u\2\2\u020f")
        buf.write("\u0210\7g\2\2\u0210\u0211\7d\2\2\u0211\u0212\7{\2\2\u0212")
        buf.write("\\\3\2\2\2\u0213\u0214\7*\2\2\u0214^\3\2\2\2\u0215\u0216")
        buf.write("\7+\2\2\u0216`\3\2\2\2\u0217\u0218\7}\2\2\u0218b\3\2\2")
        buf.write("\2\u0219\u021a\7\177\2\2\u021ad\3\2\2\2\u021b\u021c\7")
        buf.write("]\2\2\u021cf\3\2\2\2\u021d\u021e\7_\2\2\u021eh\3\2\2\2")
        buf.write("\u021f\u0220\7=\2\2\u0220j\3\2\2\2\u0221\u0222\7.\2\2")
        buf.write("\u0222l\3\2\2\2\u0223\u0224\7\60\2\2\u0224n\3\2\2\2\u0225")
        buf.write("\u0226\7?\2\2\u0226p\3\2\2\2\u0227\u0228\7@\2\2\u0228")
        buf.write("r\3\2\2\2\u0229\u022a\7>\2\2\u022at\3\2\2\2\u022b\u022c")
        buf.write("\7#\2\2\u022cv\3\2\2\2\u022d\u022e\7\u0080\2\2\u022ex")
        buf.write("\3\2\2\2\u022f\u0230\7A\2\2\u0230z\3\2\2\2\u0231\u0232")
        buf.write("\7<\2\2\u0232|\3\2\2\2\u0233\u0234\7?\2\2\u0234\u0235")
        buf.write("\7?\2\2\u0235~\3\2\2\2\u0236\u0237\7>\2\2\u0237\u0238")
        buf.write("\7?\2\2\u0238\u0080\3\2\2\2\u0239\u023a\7@\2\2\u023a\u023b")
        buf.write("\7?\2\2\u023b\u0082\3\2\2\2\u023c\u023d\7#\2\2\u023d\u023e")
        buf.write("\7?\2\2\u023e\u0084\3\2\2\2\u023f\u0240\7(\2\2\u0240\u0241")
        buf.write("\7(\2\2\u0241\u0086\3\2\2\2\u0242\u0243\7~\2\2\u0243\u0244")
        buf.write("\7~\2\2\u0244\u0088\3\2\2\2\u0245\u0246\7-\2\2\u0246\u0247")
        buf.write("\7-\2\2\u0247\u008a\3\2\2\2\u0248\u0249\7/\2\2\u0249\u024a")
        buf.write("\7/\2\2\u024a\u008c\3\2\2\2\u024b\u024c\7-\2\2\u024c\u008e")
        buf.write("\3\2\2\2\u024d\u024e\7/\2\2\u024e\u0090\3\2\2\2\u024f")
        buf.write("\u0250\7,\2\2\u0250\u0092\3\2\2\2\u0251\u0252\7\61\2\2")
        buf.write("\u0252\u0094\3\2\2\2\u0253\u0254\7(\2\2\u0254\u0096\3")
        buf.write("\2\2\2\u0255\u0256\7~\2\2\u0256\u0098\3\2\2\2\u0257\u0258")
        buf.write("\7`\2\2\u0258\u009a\3\2\2\2\u0259\u025a\7\'\2\2\u025a")
        buf.write("\u009c\3\2\2\2\u025b\u025c\7a\2\2\u025c\u009e\3\2\2\2")
        buf.write("\u025d\u025e\7B\2\2\u025e\u00a0\3\2\2\2\u025f\u0260\7")
        buf.write("p\2\2\u0260\u0261\7u\2\2\u0261\u00a2\3\2\2\2\u0262\u0263")
        buf.write("\7w\2\2\u0263\u0264\7u\2\2\u0264\u00a4\3\2\2\2\u0265\u0266")
        buf.write("\7o\2\2\u0266\u0267\7u\2\2\u0267\u00a6\3\2\2\2\u0268\u0269")
        buf.write("\7e\2\2\u0269\u026a\7u\2\2\u026a\u00a8\3\2\2\2\u026b\u026c")
        buf.write("\7f\2\2\u026c\u026d\7u\2\2\u026d\u00aa\3\2\2\2\u026e\u026f")
        buf.write("\7u\2\2\u026f\u00ac\3\2\2\2\u0270\u0271\7o\2\2\u0271\u00ae")
        buf.write("\3\2\2\2\u0272\u0273\7j\2\2\u0273\u00b0\3\2\2\2\u0274")
        buf.write("\u0275\7f\2\2\u0275\u00b2\3\2\2\2\u0276\u0277\7y\2\2\u0277")
        buf.write("\u00b4\3\2\2\2\u0278\u0279\7o\2\2\u0279\u027a\7q\2\2\u027a")
        buf.write("\u00b6\3\2\2\2\u027b\u027c\7{\2\2\u027c\u00b8\3\2\2\2")
        buf.write("\u027d\u027e\7p\2\2\u027e\u027f\7N\2\2\u027f\u00ba\3\2")
        buf.write("\2\2\u0280\u0281\7w\2\2\u0281\u0282\7N\2\2\u0282\u00bc")
        buf.write("\3\2\2\2\u0283\u0284\7o\2\2\u0284\u0285\7N\2\2\u0285\u00be")
        buf.write("\3\2\2\2\u0286\u0287\7e\2\2\u0287\u0288\7N\2\2\u0288\u00c0")
        buf.write("\3\2\2\2\u0289\u028a\7f\2\2\u028a\u028b\7N\2\2\u028b\u00c2")
        buf.write("\3\2\2\2\u028c\u028d\7N\2\2\u028d\u00c4\3\2\2\2\u028e")
        buf.write("\u028f\7f\2\2\u028f\u0290\7c\2\2\u0290\u0291\7N\2\2\u0291")
        buf.write("\u00c6\3\2\2\2\u0292\u0293\7e\2\2\u0293\u00c8\3\2\2\2")
        buf.write("\u0294\u0295\7h\2\2\u0295\u00ca\3\2\2\2\u0296\u0297\7")
        buf.write("m\2\2\u0297\u00cc\3\2\2\2\u0298\u029a\t\3\2\2\u0299\u0298")
        buf.write("\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u0299\3\2\2\2\u029b")
        buf.write("\u029c\3\2\2\2\u029c\u029d\3\2\2\2\u029d\u029e\bg\2\2")
        buf.write("\u029e\u00ce\3\2\2\2\u029f\u02a0\7\61\2\2\u02a0\u02a1")
        buf.write("\7,\2\2\u02a1\u02a5\3\2\2\2\u02a2\u02a4\13\2\2\2\u02a3")
        buf.write("\u02a2\3\2\2\2\u02a4\u02a7\3\2\2\2\u02a5\u02a6\3\2\2\2")
        buf.write("\u02a5\u02a3\3\2\2\2\u02a6\u02a8\3\2\2\2\u02a7\u02a5\3")
        buf.write("\2\2\2\u02a8\u02a9\7,\2\2\u02a9\u02aa\7\61\2\2\u02aa\u02ab")
        buf.write("\3\2\2\2\u02ab\u02ac\bh\2\2\u02ac\u00d0\3\2\2\2\u02ad")
        buf.write("\u02ae\7\61\2\2\u02ae\u02af\7\61\2\2\u02af\u02b3\3\2\2")
        buf.write("\2\u02b0\u02b2\n\4\2\2\u02b1\u02b0\3\2\2\2\u02b2\u02b5")
        buf.write("\3\2\2\2\u02b3\u02b1\3\2\2\2\u02b3\u02b4\3\2\2\2\u02b4")
        buf.write("\u02b6\3\2\2\2\u02b5\u02b3\3\2\2\2\u02b6\u02b7\bi\2\2")
        buf.write("\u02b7\u00d2\3\2\2\2\u02b8\u02c5\5\u00a1Q\2\u02b9\u02c5")
        buf.write("\5\u00a3R\2\u02ba\u02c5\5\u00a5S\2\u02bb\u02c5\5\u00a7")
        buf.write("T\2\u02bc\u02c5\5\u00a9U\2\u02bd\u02c5\5\u00abV\2\u02be")
        buf.write("\u02c5\5\u00adW\2\u02bf\u02c5\5\u00afX\2\u02c0\u02c5\5")
        buf.write("\u00b1Y\2\u02c1\u02c5\5\u00b3Z\2\u02c2\u02c5\5\u00b5[")
        buf.write("\2\u02c3\u02c5\5\u00b7\\\2\u02c4\u02b8\3\2\2\2\u02c4\u02b9")
        buf.write("\3\2\2\2\u02c4\u02ba\3\2\2\2\u02c4\u02bb\3\2\2\2\u02c4")
        buf.write("\u02bc\3\2\2\2\u02c4\u02bd\3\2\2\2\u02c4\u02be\3\2\2\2")
        buf.write("\u02c4\u02bf\3\2\2\2\u02c4\u02c0\3\2\2\2\u02c4\u02c1\3")
        buf.write("\2\2\2\u02c4\u02c2\3\2\2\2\u02c4\u02c3\3\2\2\2\u02c5\u00d4")
        buf.write("\3\2\2\2\u02c6\u02cd\5\u00b9]\2\u02c7\u02cd\5\u00bb^\2")
        buf.write("\u02c8\u02cd\5\u00bd_\2\u02c9\u02cd\5\u00bf`\2\u02ca\u02cd")
        buf.write("\5\u00c3b\2\u02cb\u02cd\5\u00c5c\2\u02cc\u02c6\3\2\2\2")
        buf.write("\u02cc\u02c7\3\2\2\2\u02cc\u02c8\3\2\2\2\u02cc\u02c9\3")
        buf.write("\2\2\2\u02cc\u02ca\3\2\2\2\u02cc\u02cb\3\2\2\2\u02cd\u00d6")
        buf.write("\3\2\2\2\u02ce\u02d2\5\u00c9e\2\u02cf\u02d2\5\u00c7d\2")
        buf.write("\u02d0\u02d2\5\u00cbf\2\u02d1\u02ce\3\2\2\2\u02d1\u02cf")
        buf.write("\3\2\2\2\u02d1\u02d0\3\2\2\2\u02d2\u00d8\3\2\2\2\u02d3")
        buf.write("\u02db\t\5\2\2\u02d4\u02d6\t\6\2\2\u02d5\u02d4\3\2\2\2")
        buf.write("\u02d6\u02d9\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d7\u02d8\3")
        buf.write("\2\2\2\u02d8\u02da\3\2\2\2\u02d9\u02d7\3\2\2\2\u02da\u02dc")
        buf.write("\t\5\2\2\u02db\u02d7\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc")
        buf.write("\u00da\3\2\2\2\u02dd\u02e0\5\u00ddo\2\u02de\u02e0\t\5")
        buf.write("\2\2\u02df\u02dd\3\2\2\2\u02df\u02de\3\2\2\2\u02e0\u00dc")
        buf.write("\3\2\2\2\u02e1\u02e6\t\7\2\2\u02e2\u02e6\n\b\2\2\u02e3")
        buf.write("\u02e4\t\t\2\2\u02e4\u02e6\t\n\2\2\u02e5\u02e1\3\2\2\2")
        buf.write("\u02e5\u02e2\3\2\2\2\u02e5\u02e3\3\2\2\2\u02e6\u00de\3")
        buf.write("\2\2\2\u02e7\u02e8\7^\2\2\u02e8\u02f2\t\13\2\2\u02e9\u02ee")
        buf.write("\7^\2\2\u02ea\u02ec\t\f\2\2\u02eb\u02ea\3\2\2\2\u02eb")
        buf.write("\u02ec\3\2\2\2\u02ec\u02ed\3\2\2\2\u02ed\u02ef\t\r\2\2")
        buf.write("\u02ee\u02eb\3\2\2\2\u02ee\u02ef\3\2\2\2\u02ef\u02f0\3")
        buf.write("\2\2\2\u02f0\u02f2\t\r\2\2\u02f1\u02e7\3\2\2\2\u02f1\u02e9")
        buf.write("\3\2\2\2\u02f2\u00e0\3\2\2\2\u02f3\u02f5\t\16\2\2\u02f4")
        buf.write("\u02f3\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u02f4\3\2\2\2")
        buf.write("\u02f6\u02f7\3\2\2\2\u02f7\u00e2\3\2\2\2\u02f8\u02fa\7")
        buf.write("\17\2\2\u02f9\u02f8\3\2\2\2\u02f9\u02fa\3\2\2\2\u02fa")
        buf.write("\u02fb\3\2\2\2\u02fb\u02fe\7\f\2\2\u02fc\u02fe\4\16\17")
        buf.write("\2\u02fd\u02f9\3\2\2\2\u02fd\u02fc\3\2\2\2\u02fe\u00e4")
        buf.write("\3\2\2\2\35\2\u01a5\u01ab\u01ad\u01bb\u01c0\u01c4\u01ca")
        buf.write("\u01cf\u01d5\u01db\u029b\u02a5\u02b3\u02c4\u02cc\u02d1")
        buf.write("\u02d7\u02db\u02df\u02e5\u02eb\u02ee\u02f1\u02f6\u02f9")
        buf.write("\u02fd\3\2\3\2")
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
    MASS_NUMBER = 39
    EFFICIENCY_NUMBER = 40
    PRESSURE_NUMBER = 41
    FORCE_NUMBER = 42
    SPEED_NUMBER = 43
    FRICTION_NUMBER = 44
    USEBY = 45
    LPAREN = 46
    RPAREN = 47
    LBRACE = 48
    RBRACE = 49
    LBRACKET = 50
    RBRACKET = 51
    SEMICOLON = 52
    COMMA = 53
    DOT = 54
    ASSIGN = 55
    GT = 56
    LT = 57
    BANG = 58
    TILDE = 59
    QUESTION = 60
    COLON = 61
    EQUALITY = 62
    LTE = 63
    GTE = 64
    NOTEQUAL = 65
    AND = 66
    OR = 67
    INC = 68
    DEC = 69
    ADDITION = 70
    SUBTRACT = 71
    MULTIPLY = 72
    DIVIDE = 73
    BITAND = 74
    BITOR = 75
    CARET = 76
    MOD = 77
    UNDERSCORE = 78
    AT_SYMBOL = 79
    NANOSECOND = 80
    MICROSECOND = 81
    MILLISECOND = 82
    CENTISECOND = 83
    DECISECOND = 84
    SECOND = 85
    MINUTE = 86
    HOUR = 87
    DAY = 88
    WEEK = 89
    MONTH = 90
    YEAR = 91
    NANOLITRE = 92
    MICROLITRE = 93
    MILLILITRE = 94
    CENTILITRE = 95
    DECILITRE = 96
    LITRE = 97
    DECALITRE = 98
    CELSIUS = 99
    FAHRENHEIT = 100
    KELVIN = 101
    WS = 102
    COMMENT = 103
    LINE_COMMENT = 104

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'repeat'", "'while'", "'function'", "'return'", 
            "'manifest'", "'module'", "'stationary'", "'functions'", "'instructions'", 
            "'detect'", "'mix'", "'split'", "'heat'", "'drain'", "'dispense'", 
            "'dispose'", "'gradient'", "'at'", "'with'", "'for'", "'into'", 
            "'times'", "'on'", "'of'", "'nat'", "'real'", "'mat'", "'bool'", 
            "'mass'", "'efficiency'", "'pressure'", "'force'", "'speed'", 
            "'friction'", "'useby'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "';'", "','", "'.'", "'='", "'>'", "'<'", "'!'", "'~'", 
            "'?'", "':'", "'=='", "'<='", "'>='", "'!='", "'&&'", "'||'", 
            "'++'", "'--'", "'+'", "'-'", "'*'", "'/'", "'&'", "'|'", "'^'", 
            "'%'", "'_'", "'@'", "'ns'", "'us'", "'ms'", "'cs'", "'ds'", 
            "'s'", "'m'", "'h'", "'d'", "'w'", "'mo'", "'y'", "'nL'", "'uL'", 
            "'mL'", "'cL'", "'dL'", "'L'", "'daL'", "'c'", "'f'", "'k'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", "RETURN", "MANIFEST", 
            "MODULE", "STATIONARY", "FUNCTIONS", "INSTRUCTIONS", "DETECT", 
            "MIX", "SPLIT", "HEAT", "DRAIN", "DISPENSE", "DISPOSE", "GRADIENT", 
            "AT", "WITH", "FOR", "INTO", "TIMES", "ON", "OF", "NAT", "REAL", 
            "MAT", "BOOL", "IDENTIFIER", "STRING_LITERAL", "BOOL_LITERAL", 
            "FLOAT_LITERAL", "INTEGER_LITERAL", "TIME_NUMBER", "VOLUME_NUMBER", 
            "TEMP_NUMBER", "MASS_NUMBER", "EFFICIENCY_NUMBER", "PRESSURE_NUMBER", 
            "FORCE_NUMBER", "SPEED_NUMBER", "FRICTION_NUMBER", "USEBY", 
            "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
            "SEMICOLON", "COMMA", "DOT", "ASSIGN", "GT", "LT", "BANG", "TILDE", 
            "QUESTION", "COLON", "EQUALITY", "LTE", "GTE", "NOTEQUAL", "AND", 
            "OR", "INC", "DEC", "ADDITION", "SUBTRACT", "MULTIPLY", "DIVIDE", 
            "BITAND", "BITOR", "CARET", "MOD", "UNDERSCORE", "AT_SYMBOL", 
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
                  "TIME_NUMBER", "VOLUME_NUMBER", "TEMP_NUMBER", "MASS_NUMBER", 
                  "EFFICIENCY_NUMBER", "PRESSURE_NUMBER", "FORCE_NUMBER", 
                  "SPEED_NUMBER", "FRICTION_NUMBER", "USEBY", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                  "SEMICOLON", "COMMA", "DOT", "ASSIGN", "GT", "LT", "BANG", 
                  "TILDE", "QUESTION", "COLON", "EQUALITY", "LTE", "GTE", 
                  "NOTEQUAL", "AND", "OR", "INC", "DEC", "ADDITION", "SUBTRACT", 
                  "MULTIPLY", "DIVIDE", "BITAND", "BITOR", "CARET", "MOD", 
                  "UNDERSCORE", "AT_SYMBOL", "NANOSECOND", "MICROSECOND", 
                  "MILLISECOND", "CENTISECOND", "DECISECOND", "SECOND", 
                  "MINUTE", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", "NANOLITRE", 
                  "MICROLITRE", "MILLILITRE", "CENTILITRE", "DECILITRE", 
                  "LITRE", "DECALITRE", "CELSIUS", "FAHRENHEIT", "KELVIN", 
                  "WS", "COMMENT", "LINE_COMMENT", "TimeUnits", "VolumeUnits", 
                  "TempUnits", "Digits", "LetterOrDigit", "Letter", "EscapeSequence", 
                  "SPACES", "NEWLINE" ]

    grammarFileName = "BSLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


