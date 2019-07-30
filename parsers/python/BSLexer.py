# Generated from /home/warfield/Github/BioScriptGrammar/grammar/BSLexer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2n")
        buf.write("\u0366\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\3\2\3\2\3\2\3")
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
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3*\3*\3*\3+\3+\7+\u023f\n+\f+\16+\u0242\13+\3")
        buf.write(",\3,\3,\7,\u0247\n,\f,\16,\u024a\13,\3,\3,\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\5-\u0257\n-\3.\3.\3.\5.\u025c\n.\3.\3")
        buf.write(".\5.\u0260\n.\3/\3/\7/\u0264\n/\f/\16/\u0267\13/\3\60")
        buf.write("\3\60\5\60\u026b\n\60\3\60\3\60\3\61\3\61\5\61\u0271\n")
        buf.write("\61\3\61\3\61\3\62\3\62\5\62\u0277\n\62\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3")
        buf.write("B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3H\3")
        buf.write("H\3H\3I\3I\3I\3J\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3")
        buf.write("P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3U\3V\3V\3V\3W\3W\3")
        buf.write("W\3X\3X\3X\3Y\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3^\3^\3")
        buf.write("_\3_\3_\3`\3`\3a\3a\3a\3b\3b\3b\3c\3c\3c\3d\3d\3d\3e\3")
        buf.write("e\3e\3f\3f\3g\3g\3g\3g\3h\3h\3i\3i\3j\3j\3k\6k\u0301\n")
        buf.write("k\rk\16k\u0302\3k\3k\3l\3l\3l\3l\7l\u030b\nl\fl\16l\u030e")
        buf.write("\13l\3l\3l\3l\3l\3l\3m\3m\3m\3m\7m\u0319\nm\fm\16m\u031c")
        buf.write("\13m\3m\3m\3n\3n\3n\3n\3n\3n\3n\3n\3n\3n\3n\3n\5n\u032c")
        buf.write("\nn\3o\3o\3o\3o\3o\3o\5o\u0334\no\3p\3p\3p\5p\u0339\n")
        buf.write("p\3q\3q\7q\u033d\nq\fq\16q\u0340\13q\3q\5q\u0343\nq\3")
        buf.write("r\3r\5r\u0347\nr\3s\3s\3s\3s\5s\u034d\ns\3t\3t\3t\3t\5")
        buf.write("t\u0353\nt\3t\5t\u0356\nt\3t\5t\u0359\nt\3u\6u\u035c\n")
        buf.write("u\ru\16u\u035d\3v\5v\u0361\nv\3v\3v\5v\u0365\nv\3\u030c")
        buf.write("\2w\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F")
        buf.write("\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099")
        buf.write("N\u009bO\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7U\u00a9")
        buf.write("V\u00abW\u00adX\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7]\u00b9")
        buf.write("^\u00bb_\u00bd`\u00bfa\u00c1b\u00c3c\u00c5d\u00c7e\u00c9")
        buf.write("f\u00cbg\u00cdh\u00cfi\u00d1j\u00d3k\u00d5l\u00d7m\u00d9")
        buf.write("n\u00db\2\u00dd\2\u00df\2\u00e1\2\u00e3\2\u00e5\2\u00e7")
        buf.write("\2\u00e9\2\u00eb\2\3\2\17\6\2\f\f\17\17$$^^\5\2\13\f\16")
        buf.write("\17\"\"\4\2\f\f\17\17\3\2\62;\4\2\62;aa\6\2&&C\\aac|\4")
        buf.write("\2\2\u0081\ud802\udc01\3\2\ud802\udc01\3\2\udc02\ue001")
        buf.write("\n\2$$))^^ddhhppttvv\3\2\62\65\3\2\629\4\2\13\13\"\"\2")
        buf.write("\u0386\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
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
        buf.write("\3\2\2\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2\2\2\u00d5\3\2\2")
        buf.write("\2\2\u00d7\3\2\2\2\2\u00d9\3\2\2\2\3\u00ed\3\2\2\2\5\u00f0")
        buf.write("\3\2\2\2\7\u00f5\3\2\2\2\t\u00fc\3\2\2\2\13\u0102\3\2")
        buf.write("\2\2\r\u010b\3\2\2\2\17\u0112\3\2\2\2\21\u011b\3\2\2\2")
        buf.write("\23\u0122\3\2\2\2\25\u012d\3\2\2\2\27\u0137\3\2\2\2\31")
        buf.write("\u0144\3\2\2\2\33\u014b\3\2\2\2\35\u014f\3\2\2\2\37\u0155")
        buf.write("\3\2\2\2!\u015a\3\2\2\2#\u0160\3\2\2\2%\u0169\3\2\2\2")
        buf.write("\'\u0171\3\2\2\2)\u017a\3\2\2\2+\u017d\3\2\2\2-\u0182")
        buf.write("\3\2\2\2/\u0186\3\2\2\2\61\u018b\3\2\2\2\63\u0191\3\2")
        buf.write("\2\2\65\u0194\3\2\2\2\67\u0197\3\2\2\29\u019b\3\2\2\2")
        buf.write(";\u01a0\3\2\2\2=\u01a4\3\2\2\2?\u01a9\3\2\2\2A\u01b3\3")
        buf.write("\2\2\2C\u01c0\3\2\2\2E\u01d1\3\2\2\2G\u01e0\3\2\2\2I\u01f1")
        buf.write("\3\2\2\2K\u01ff\3\2\2\2M\u020f\3\2\2\2O\u021f\3\2\2\2")
        buf.write("Q\u022b\3\2\2\2S\u0236\3\2\2\2U\u023c\3\2\2\2W\u0243\3")
        buf.write("\2\2\2Y\u0256\3\2\2\2[\u025f\3\2\2\2]\u0261\3\2\2\2_\u026a")
        buf.write("\3\2\2\2a\u0270\3\2\2\2c\u0276\3\2\2\2e\u027a\3\2\2\2")
        buf.write("g\u027c\3\2\2\2i\u027e\3\2\2\2k\u0280\3\2\2\2m\u0282\3")
        buf.write("\2\2\2o\u0284\3\2\2\2q\u0286\3\2\2\2s\u0288\3\2\2\2u\u028a")
        buf.write("\3\2\2\2w\u028c\3\2\2\2y\u028e\3\2\2\2{\u0290\3\2\2\2")
        buf.write("}\u0292\3\2\2\2\177\u0294\3\2\2\2\u0081\u0296\3\2\2\2")
        buf.write("\u0083\u0298\3\2\2\2\u0085\u029a\3\2\2\2\u0087\u029d\3")
        buf.write("\2\2\2\u0089\u02a0\3\2\2\2\u008b\u02a3\3\2\2\2\u008d\u02a6")
        buf.write("\3\2\2\2\u008f\u02a9\3\2\2\2\u0091\u02ac\3\2\2\2\u0093")
        buf.write("\u02af\3\2\2\2\u0095\u02b2\3\2\2\2\u0097\u02b4\3\2\2\2")
        buf.write("\u0099\u02b6\3\2\2\2\u009b\u02b8\3\2\2\2\u009d\u02ba\3")
        buf.write("\2\2\2\u009f\u02bc\3\2\2\2\u00a1\u02be\3\2\2\2\u00a3\u02c0")
        buf.write("\3\2\2\2\u00a5\u02c2\3\2\2\2\u00a7\u02c4\3\2\2\2\u00a9")
        buf.write("\u02c6\3\2\2\2\u00ab\u02c9\3\2\2\2\u00ad\u02cc\3\2\2\2")
        buf.write("\u00af\u02cf\3\2\2\2\u00b1\u02d2\3\2\2\2\u00b3\u02d5\3")
        buf.write("\2\2\2\u00b5\u02d7\3\2\2\2\u00b7\u02d9\3\2\2\2\u00b9\u02db")
        buf.write("\3\2\2\2\u00bb\u02dd\3\2\2\2\u00bd\u02df\3\2\2\2\u00bf")
        buf.write("\u02e2\3\2\2\2\u00c1\u02e4\3\2\2\2\u00c3\u02e7\3\2\2\2")
        buf.write("\u00c5\u02ea\3\2\2\2\u00c7\u02ed\3\2\2\2\u00c9\u02f0\3")
        buf.write("\2\2\2\u00cb\u02f3\3\2\2\2\u00cd\u02f5\3\2\2\2\u00cf\u02f9")
        buf.write("\3\2\2\2\u00d1\u02fb\3\2\2\2\u00d3\u02fd\3\2\2\2\u00d5")
        buf.write("\u0300\3\2\2\2\u00d7\u0306\3\2\2\2\u00d9\u0314\3\2\2\2")
        buf.write("\u00db\u032b\3\2\2\2\u00dd\u0333\3\2\2\2\u00df\u0338\3")
        buf.write("\2\2\2\u00e1\u033a\3\2\2\2\u00e3\u0346\3\2\2\2\u00e5\u034c")
        buf.write("\3\2\2\2\u00e7\u0358\3\2\2\2\u00e9\u035b\3\2\2\2\u00eb")
        buf.write("\u0364\3\2\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7h\2\2\u00ef")
        buf.write("\4\3\2\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2\7n\2\2\u00f2")
        buf.write("\u00f3\7u\2\2\u00f3\u00f4\7g\2\2\u00f4\6\3\2\2\2\u00f5")
        buf.write("\u00f6\7t\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7r\2\2\u00f8")
        buf.write("\u00f9\7g\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7v\2\2\u00fb")
        buf.write("\b\3\2\2\2\u00fc\u00fd\7y\2\2\u00fd\u00fe\7j\2\2\u00fe")
        buf.write("\u00ff\7k\2\2\u00ff\u0100\7n\2\2\u0100\u0101\7g\2\2\u0101")
        buf.write("\n\3\2\2\2\u0102\u0103\7h\2\2\u0103\u0104\7w\2\2\u0104")
        buf.write("\u0105\7p\2\2\u0105\u0106\7e\2\2\u0106\u0107\7v\2\2\u0107")
        buf.write("\u0108\7k\2\2\u0108\u0109\7q\2\2\u0109\u010a\7p\2\2\u010a")
        buf.write("\f\3\2\2\2\u010b\u010c\7t\2\2\u010c\u010d\7g\2\2\u010d")
        buf.write("\u010e\7v\2\2\u010e\u010f\7w\2\2\u010f\u0110\7t\2\2\u0110")
        buf.write("\u0111\7p\2\2\u0111\16\3\2\2\2\u0112\u0113\7o\2\2\u0113")
        buf.write("\u0114\7c\2\2\u0114\u0115\7p\2\2\u0115\u0116\7k\2\2\u0116")
        buf.write("\u0117\7h\2\2\u0117\u0118\7g\2\2\u0118\u0119\7u\2\2\u0119")
        buf.write("\u011a\7v\2\2\u011a\20\3\2\2\2\u011b\u011c\7o\2\2\u011c")
        buf.write("\u011d\7q\2\2\u011d\u011e\7f\2\2\u011e\u011f\7w\2\2\u011f")
        buf.write("\u0120\7n\2\2\u0120\u0121\7g\2\2\u0121\22\3\2\2\2\u0122")
        buf.write("\u0123\7u\2\2\u0123\u0124\7v\2\2\u0124\u0125\7c\2\2\u0125")
        buf.write("\u0126\7v\2\2\u0126\u0127\7k\2\2\u0127\u0128\7q\2\2\u0128")
        buf.write("\u0129\7p\2\2\u0129\u012a\7c\2\2\u012a\u012b\7t\2\2\u012b")
        buf.write("\u012c\7{\2\2\u012c\24\3\2\2\2\u012d\u012e\7h\2\2\u012e")
        buf.write("\u012f\7w\2\2\u012f\u0130\7p\2\2\u0130\u0131\7e\2\2\u0131")
        buf.write("\u0132\7v\2\2\u0132\u0133\7k\2\2\u0133\u0134\7q\2\2\u0134")
        buf.write("\u0135\7p\2\2\u0135\u0136\7u\2\2\u0136\26\3\2\2\2\u0137")
        buf.write("\u0138\7k\2\2\u0138\u0139\7p\2\2\u0139\u013a\7u\2\2\u013a")
        buf.write("\u013b\7v\2\2\u013b\u013c\7t\2\2\u013c\u013d\7w\2\2\u013d")
        buf.write("\u013e\7e\2\2\u013e\u013f\7v\2\2\u013f\u0140\7k\2\2\u0140")
        buf.write("\u0141\7q\2\2\u0141\u0142\7p\2\2\u0142\u0143\7u\2\2\u0143")
        buf.write("\30\3\2\2\2\u0144\u0145\7f\2\2\u0145\u0146\7g\2\2\u0146")
        buf.write("\u0147\7v\2\2\u0147\u0148\7g\2\2\u0148\u0149\7e\2\2\u0149")
        buf.write("\u014a\7v\2\2\u014a\32\3\2\2\2\u014b\u014c\7o\2\2\u014c")
        buf.write("\u014d\7k\2\2\u014d\u014e\7z\2\2\u014e\34\3\2\2\2\u014f")
        buf.write("\u0150\7u\2\2\u0150\u0151\7r\2\2\u0151\u0152\7n\2\2\u0152")
        buf.write("\u0153\7k\2\2\u0153\u0154\7v\2\2\u0154\36\3\2\2\2\u0155")
        buf.write("\u0156\7j\2\2\u0156\u0157\7g\2\2\u0157\u0158\7c\2\2\u0158")
        buf.write("\u0159\7v\2\2\u0159 \3\2\2\2\u015a\u015b\7f\2\2\u015b")
        buf.write("\u015c\7t\2\2\u015c\u015d\7c\2\2\u015d\u015e\7k\2\2\u015e")
        buf.write("\u015f\7p\2\2\u015f\"\3\2\2\2\u0160\u0161\7f\2\2\u0161")
        buf.write("\u0162\7k\2\2\u0162\u0163\7u\2\2\u0163\u0164\7r\2\2\u0164")
        buf.write("\u0165\7g\2\2\u0165\u0166\7p\2\2\u0166\u0167\7u\2\2\u0167")
        buf.write("\u0168\7g\2\2\u0168$\3\2\2\2\u0169\u016a\7f\2\2\u016a")
        buf.write("\u016b\7k\2\2\u016b\u016c\7u\2\2\u016c\u016d\7r\2\2\u016d")
        buf.write("\u016e\7q\2\2\u016e\u016f\7u\2\2\u016f\u0170\7g\2\2\u0170")
        buf.write("&\3\2\2\2\u0171\u0172\7i\2\2\u0172\u0173\7t\2\2\u0173")
        buf.write("\u0174\7c\2\2\u0174\u0175\7f\2\2\u0175\u0176\7k\2\2\u0176")
        buf.write("\u0177\7g\2\2\u0177\u0178\7p\2\2\u0178\u0179\7v\2\2\u0179")
        buf.write("(\3\2\2\2\u017a\u017b\7c\2\2\u017b\u017c\7v\2\2\u017c")
        buf.write("*\3\2\2\2\u017d\u017e\7y\2\2\u017e\u017f\7k\2\2\u017f")
        buf.write("\u0180\7v\2\2\u0180\u0181\7j\2\2\u0181,\3\2\2\2\u0182")
        buf.write("\u0183\7h\2\2\u0183\u0184\7q\2\2\u0184\u0185\7t\2\2\u0185")
        buf.write(".\3\2\2\2\u0186\u0187\7k\2\2\u0187\u0188\7p\2\2\u0188")
        buf.write("\u0189\7v\2\2\u0189\u018a\7q\2\2\u018a\60\3\2\2\2\u018b")
        buf.write("\u018c\7v\2\2\u018c\u018d\7k\2\2\u018d\u018e\7o\2\2\u018e")
        buf.write("\u018f\7g\2\2\u018f\u0190\7u\2\2\u0190\62\3\2\2\2\u0191")
        buf.write("\u0192\7q\2\2\u0192\u0193\7p\2\2\u0193\64\3\2\2\2\u0194")
        buf.write("\u0195\7q\2\2\u0195\u0196\7h\2\2\u0196\66\3\2\2\2\u0197")
        buf.write("\u0198\7p\2\2\u0198\u0199\7c\2\2\u0199\u019a\7v\2\2\u019a")
        buf.write("8\3\2\2\2\u019b\u019c\7t\2\2\u019c\u019d\7g\2\2\u019d")
        buf.write("\u019e\7c\2\2\u019e\u019f\7n\2\2\u019f:\3\2\2\2\u01a0")
        buf.write("\u01a1\7o\2\2\u01a1\u01a2\7c\2\2\u01a2\u01a3\7v\2\2\u01a3")
        buf.write("<\3\2\2\2\u01a4\u01a5\7d\2\2\u01a5\u01a6\7q\2\2\u01a6")
        buf.write("\u01a7\7q\2\2\u01a7\u01a8\7n\2\2\u01a8>\3\2\2\2\u01a9")
        buf.write("\u01aa\7x\2\2\u01aa\u01ab\7k\2\2\u01ab\u01ac\7u\2\2\u01ac")
        buf.write("\u01ad\7e\2\2\u01ad\u01ae\7q\2\2\u01ae\u01af\7u\2\2\u01af")
        buf.write("\u01b0\7k\2\2\u01b0\u01b1\7v\2\2\u01b1\u01b2\7{\2\2\u01b2")
        buf.write("@\3\2\2\2\u01b3\u01b4\7o\2\2\u01b4\u01b5\7c\2\2\u01b5")
        buf.write("\u01b6\7u\2\2\u01b6\u01b7\7u\2\2\u01b7\u01b8\7a\2\2\u01b8")
        buf.write("\u01b9\7f\2\2\u01b9\u01ba\7g\2\2\u01ba\u01bb\7p\2\2\u01bb")
        buf.write("\u01bc\7u\2\2\u01bc\u01bd\7k\2\2\u01bd\u01be\7v\2\2\u01be")
        buf.write("\u01bf\7{\2\2\u01bfB\3\2\2\2\u01c0\u01c1\7t\2\2\u01c1")
        buf.write("\u01c2\7g\2\2\u01c2\u01c3\7n\2\2\u01c3\u01c4\7c\2\2\u01c4")
        buf.write("\u01c5\7v\2\2\u01c5\u01c6\7k\2\2\u01c6\u01c7\7x\2\2\u01c7")
        buf.write("\u01c8\7g\2\2\u01c8\u01c9\7a\2\2\u01c9\u01ca\7f\2\2\u01ca")
        buf.write("\u01cb\7g\2\2\u01cb\u01cc\7p\2\2\u01cc\u01cd\7u\2\2\u01cd")
        buf.write("\u01ce\7k\2\2\u01ce\u01cf\7v\2\2\u01cf\u01d0\7{\2\2\u01d0")
        buf.write("D\3\2\2\2\u01d1\u01d2\7y\2\2\u01d2\u01d3\7g\2\2\u01d3")
        buf.write("\u01d4\7k\2\2\u01d4\u01d5\7i\2\2\u01d5\u01d6\7j\2\2\u01d6")
        buf.write("\u01d7\7v\2\2\u01d7\u01d8\7a\2\2\u01d8\u01d9\7f\2\2\u01d9")
        buf.write("\u01da\7g\2\2\u01da\u01db\7p\2\2\u01db\u01dc\7u\2\2\u01dc")
        buf.write("\u01dd\7k\2\2\u01dd\u01de\7v\2\2\u01de\u01df\7{\2\2\u01df")
        buf.write("F\3\2\2\2\u01e0\u01e1\7u\2\2\u01e1\u01e2\7r\2\2\u01e2")
        buf.write("\u01e3\7g\2\2\u01e3\u01e4\7e\2\2\u01e4\u01e5\7k\2\2\u01e5")
        buf.write("\u01e6\7h\2\2\u01e6\u01e7\7k\2\2\u01e7\u01e8\7e\2\2\u01e8")
        buf.write("\u01e9\7a\2\2\u01e9\u01ea\7i\2\2\u01ea\u01eb\7t\2\2\u01eb")
        buf.write("\u01ec\7c\2\2\u01ec\u01ed\7x\2\2\u01ed\u01ee\7k\2\2\u01ee")
        buf.write("\u01ef\7v\2\2\u01ef\u01f0\7{\2\2\u01f0H\3\2\2\2\u01f1")
        buf.write("\u01f2\7e\2\2\u01f2\u01f3\7q\2\2\u01f3\u01f4\7p\2\2\u01f4")
        buf.write("\u01f5\7e\2\2\u01f5\u01f6\7g\2\2\u01f6\u01f7\7p\2\2\u01f7")
        buf.write("\u01f8\7v\2\2\u01f8\u01f9\7t\2\2\u01f9\u01fa\7c\2\2\u01fa")
        buf.write("\u01fb\7v\2\2\u01fb\u01fc\7k\2\2\u01fc\u01fd\7q\2\2\u01fd")
        buf.write("\u01fe\7p\2\2\u01feJ\3\2\2\2\u01ff\u0200\7u\2\2\u0200")
        buf.write("\u0201\7r\2\2\u0201\u0202\7g\2\2\u0202\u0203\7e\2\2\u0203")
        buf.write("\u0204\7k\2\2\u0204\u0205\7h\2\2\u0205\u0206\7k\2\2\u0206")
        buf.write("\u0207\7e\2\2\u0207\u0208\7a\2\2\u0208\u0209\7x\2\2\u0209")
        buf.write("\u020a\7q\2\2\u020a\u020b\7n\2\2\u020b\u020c\7w\2\2\u020c")
        buf.write("\u020d\7o\2\2\u020d\u020e\7g\2\2\u020eL\3\2\2\2\u020f")
        buf.write("\u0210\7e\2\2\u0210\u0211\7q\2\2\u0211\u0212\7o\2\2\u0212")
        buf.write("\u0213\7r\2\2\u0213\u0214\7t\2\2\u0214\u0215\7g\2\2\u0215")
        buf.write("\u0216\7u\2\2\u0216\u0217\7u\2\2\u0217\u0218\7k\2\2\u0218")
        buf.write("\u0219\7d\2\2\u0219\u021a\7k\2\2\u021a\u021b\7n\2\2\u021b")
        buf.write("\u021c\7k\2\2\u021c\u021d\7v\2\2\u021d\u021e\7{\2\2\u021e")
        buf.write("N\3\2\2\2\u021f\u0220\7e\2\2\u0220\u0221\7c\2\2\u0221")
        buf.write("\u0222\7r\2\2\u0222\u0223\7k\2\2\u0223\u0224\7n\2\2\u0224")
        buf.write("\u0225\7n\2\2\u0225\u0226\7c\2\2\u0226\u0227\7t\2\2\u0227")
        buf.write("\u0228\7k\2\2\u0228\u0229\7v\2\2\u0229\u022a\7{\2\2\u022a")
        buf.write("P\3\2\2\2\u022b\u022c\7g\2\2\u022c\u022d\7n\2\2\u022d")
        buf.write("\u022e\7c\2\2\u022e\u022f\7u\2\2\u022f\u0230\7v\2\2\u0230")
        buf.write("\u0231\7k\2\2\u0231\u0232\7e\2\2\u0232\u0233\7k\2\2\u0233")
        buf.write("\u0234\7v\2\2\u0234\u0235\7{\2\2\u0235R\3\2\2\2\u0236")
        buf.write("\u0237\7w\2\2\u0237\u0238\7u\2\2\u0238\u0239\7g\2\2\u0239")
        buf.write("\u023a\7d\2\2\u023a\u023b\7{\2\2\u023bT\3\2\2\2\u023c")
        buf.write("\u0240\5\u00e5s\2\u023d\u023f\5\u00e3r\2\u023e\u023d\3")
        buf.write("\2\2\2\u023f\u0242\3\2\2\2\u0240\u023e\3\2\2\2\u0240\u0241")
        buf.write("\3\2\2\2\u0241V\3\2\2\2\u0242\u0240\3\2\2\2\u0243\u0248")
        buf.write("\7$\2\2\u0244\u0247\n\2\2\2\u0245\u0247\5\u00e7t\2\u0246")
        buf.write("\u0244\3\2\2\2\u0246\u0245\3\2\2\2\u0247\u024a\3\2\2\2")
        buf.write("\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024b\3")
        buf.write("\2\2\2\u024a\u0248\3\2\2\2\u024b\u024c\7$\2\2\u024cX\3")
        buf.write("\2\2\2\u024d\u024e\7v\2\2\u024e\u024f\7t\2\2\u024f\u0250")
        buf.write("\7w\2\2\u0250\u0257\7g\2\2\u0251\u0252\7h\2\2\u0252\u0253")
        buf.write("\7c\2\2\u0253\u0254\7n\2\2\u0254\u0255\7u\2\2\u0255\u0257")
        buf.write("\7g\2\2\u0256\u024d\3\2\2\2\u0256\u0251\3\2\2\2\u0257")
        buf.write("Z\3\2\2\2\u0258\u0259\5\u00e1q\2\u0259\u025b\7\60\2\2")
        buf.write("\u025a\u025c\5\u00e1q\2\u025b\u025a\3\2\2\2\u025b\u025c")
        buf.write("\3\2\2\2\u025c\u0260\3\2\2\2\u025d\u025e\7\60\2\2\u025e")
        buf.write("\u0260\5\u00e1q\2\u025f\u0258\3\2\2\2\u025f\u025d\3\2")
        buf.write("\2\2\u0260\\\3\2\2\2\u0261\u0265\5\u00e1q\2\u0262\u0264")
        buf.write("\5\u00e1q\2\u0263\u0262\3\2\2\2\u0264\u0267\3\2\2\2\u0265")
        buf.write("\u0263\3\2\2\2\u0265\u0266\3\2\2\2\u0266^\3\2\2\2\u0267")
        buf.write("\u0265\3\2\2\2\u0268\u026b\5[.\2\u0269\u026b\5]/\2\u026a")
        buf.write("\u0268\3\2\2\2\u026a\u0269\3\2\2\2\u026b\u026c\3\2\2\2")
        buf.write("\u026c\u026d\5\u00dbn\2\u026d`\3\2\2\2\u026e\u0271\5[")
        buf.write(".\2\u026f\u0271\5]/\2\u0270\u026e\3\2\2\2\u0270\u026f")
        buf.write("\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u0273\5\u00ddo\2\u0273")
        buf.write("b\3\2\2\2\u0274\u0277\5[.\2\u0275\u0277\5]/\2\u0276\u0274")
        buf.write("\3\2\2\2\u0276\u0275\3\2\2\2\u0277\u0278\3\2\2\2\u0278")
        buf.write("\u0279\5\u00dfp\2\u0279d\3\2\2\2\u027a\u027b\7*\2\2\u027b")
        buf.write("f\3\2\2\2\u027c\u027d\7+\2\2\u027dh\3\2\2\2\u027e\u027f")
        buf.write("\7}\2\2\u027fj\3\2\2\2\u0280\u0281\7\177\2\2\u0281l\3")
        buf.write("\2\2\2\u0282\u0283\7]\2\2\u0283n\3\2\2\2\u0284\u0285\7")
        buf.write("_\2\2\u0285p\3\2\2\2\u0286\u0287\7=\2\2\u0287r\3\2\2\2")
        buf.write("\u0288\u0289\7.\2\2\u0289t\3\2\2\2\u028a\u028b\7\60\2")
        buf.write("\2\u028bv\3\2\2\2\u028c\u028d\7?\2\2\u028dx\3\2\2\2\u028e")
        buf.write("\u028f\7@\2\2\u028fz\3\2\2\2\u0290\u0291\7>\2\2\u0291")
        buf.write("|\3\2\2\2\u0292\u0293\7#\2\2\u0293~\3\2\2\2\u0294\u0295")
        buf.write("\7\u0080\2\2\u0295\u0080\3\2\2\2\u0296\u0297\7A\2\2\u0297")
        buf.write("\u0082\3\2\2\2\u0298\u0299\7<\2\2\u0299\u0084\3\2\2\2")
        buf.write("\u029a\u029b\7?\2\2\u029b\u029c\7?\2\2\u029c\u0086\3\2")
        buf.write("\2\2\u029d\u029e\7>\2\2\u029e\u029f\7?\2\2\u029f\u0088")
        buf.write("\3\2\2\2\u02a0\u02a1\7@\2\2\u02a1\u02a2\7?\2\2\u02a2\u008a")
        buf.write("\3\2\2\2\u02a3\u02a4\7#\2\2\u02a4\u02a5\7?\2\2\u02a5\u008c")
        buf.write("\3\2\2\2\u02a6\u02a7\7(\2\2\u02a7\u02a8\7(\2\2\u02a8\u008e")
        buf.write("\3\2\2\2\u02a9\u02aa\7~\2\2\u02aa\u02ab\7~\2\2\u02ab\u0090")
        buf.write("\3\2\2\2\u02ac\u02ad\7-\2\2\u02ad\u02ae\7-\2\2\u02ae\u0092")
        buf.write("\3\2\2\2\u02af\u02b0\7/\2\2\u02b0\u02b1\7/\2\2\u02b1\u0094")
        buf.write("\3\2\2\2\u02b2\u02b3\7-\2\2\u02b3\u0096\3\2\2\2\u02b4")
        buf.write("\u02b5\7/\2\2\u02b5\u0098\3\2\2\2\u02b6\u02b7\7,\2\2\u02b7")
        buf.write("\u009a\3\2\2\2\u02b8\u02b9\7\61\2\2\u02b9\u009c\3\2\2")
        buf.write("\2\u02ba\u02bb\7(\2\2\u02bb\u009e\3\2\2\2\u02bc\u02bd")
        buf.write("\7~\2\2\u02bd\u00a0\3\2\2\2\u02be\u02bf\7`\2\2\u02bf\u00a2")
        buf.write("\3\2\2\2\u02c0\u02c1\7\'\2\2\u02c1\u00a4\3\2\2\2\u02c2")
        buf.write("\u02c3\7a\2\2\u02c3\u00a6\3\2\2\2\u02c4\u02c5\7B\2\2\u02c5")
        buf.write("\u00a8\3\2\2\2\u02c6\u02c7\7p\2\2\u02c7\u02c8\7u\2\2\u02c8")
        buf.write("\u00aa\3\2\2\2\u02c9\u02ca\7w\2\2\u02ca\u02cb\7u\2\2\u02cb")
        buf.write("\u00ac\3\2\2\2\u02cc\u02cd\7o\2\2\u02cd\u02ce\7u\2\2\u02ce")
        buf.write("\u00ae\3\2\2\2\u02cf\u02d0\7e\2\2\u02d0\u02d1\7u\2\2\u02d1")
        buf.write("\u00b0\3\2\2\2\u02d2\u02d3\7f\2\2\u02d3\u02d4\7u\2\2\u02d4")
        buf.write("\u00b2\3\2\2\2\u02d5\u02d6\7u\2\2\u02d6\u00b4\3\2\2\2")
        buf.write("\u02d7\u02d8\7o\2\2\u02d8\u00b6\3\2\2\2\u02d9\u02da\7")
        buf.write("j\2\2\u02da\u00b8\3\2\2\2\u02db\u02dc\7f\2\2\u02dc\u00ba")
        buf.write("\3\2\2\2\u02dd\u02de\7y\2\2\u02de\u00bc\3\2\2\2\u02df")
        buf.write("\u02e0\7o\2\2\u02e0\u02e1\7q\2\2\u02e1\u00be\3\2\2\2\u02e2")
        buf.write("\u02e3\7{\2\2\u02e3\u00c0\3\2\2\2\u02e4\u02e5\7p\2\2\u02e5")
        buf.write("\u02e6\7N\2\2\u02e6\u00c2\3\2\2\2\u02e7\u02e8\7w\2\2\u02e8")
        buf.write("\u02e9\7N\2\2\u02e9\u00c4\3\2\2\2\u02ea\u02eb\7o\2\2\u02eb")
        buf.write("\u02ec\7N\2\2\u02ec\u00c6\3\2\2\2\u02ed\u02ee\7e\2\2\u02ee")
        buf.write("\u02ef\7N\2\2\u02ef\u00c8\3\2\2\2\u02f0\u02f1\7f\2\2\u02f1")
        buf.write("\u02f2\7N\2\2\u02f2\u00ca\3\2\2\2\u02f3\u02f4\7N\2\2\u02f4")
        buf.write("\u00cc\3\2\2\2\u02f5\u02f6\7f\2\2\u02f6\u02f7\7c\2\2\u02f7")
        buf.write("\u02f8\7N\2\2\u02f8\u00ce\3\2\2\2\u02f9\u02fa\7e\2\2\u02fa")
        buf.write("\u00d0\3\2\2\2\u02fb\u02fc\7h\2\2\u02fc\u00d2\3\2\2\2")
        buf.write("\u02fd\u02fe\7m\2\2\u02fe\u00d4\3\2\2\2\u02ff\u0301\t")
        buf.write("\3\2\2\u0300\u02ff\3\2\2\2\u0301\u0302\3\2\2\2\u0302\u0300")
        buf.write("\3\2\2\2\u0302\u0303\3\2\2\2\u0303\u0304\3\2\2\2\u0304")
        buf.write("\u0305\bk\2\2\u0305\u00d6\3\2\2\2\u0306\u0307\7\61\2\2")
        buf.write("\u0307\u0308\7,\2\2\u0308\u030c\3\2\2\2\u0309\u030b\13")
        buf.write("\2\2\2\u030a\u0309\3\2\2\2\u030b\u030e\3\2\2\2\u030c\u030d")
        buf.write("\3\2\2\2\u030c\u030a\3\2\2\2\u030d\u030f\3\2\2\2\u030e")
        buf.write("\u030c\3\2\2\2\u030f\u0310\7,\2\2\u0310\u0311\7\61\2\2")
        buf.write("\u0311\u0312\3\2\2\2\u0312\u0313\bl\2\2\u0313\u00d8\3")
        buf.write("\2\2\2\u0314\u0315\7\61\2\2\u0315\u0316\7\61\2\2\u0316")
        buf.write("\u031a\3\2\2\2\u0317\u0319\n\4\2\2\u0318\u0317\3\2\2\2")
        buf.write("\u0319\u031c\3\2\2\2\u031a\u0318\3\2\2\2\u031a\u031b\3")
        buf.write("\2\2\2\u031b\u031d\3\2\2\2\u031c\u031a\3\2\2\2\u031d\u031e")
        buf.write("\bm\2\2\u031e\u00da\3\2\2\2\u031f\u032c\5\u00a9U\2\u0320")
        buf.write("\u032c\5\u00abV\2\u0321\u032c\5\u00adW\2\u0322\u032c\5")
        buf.write("\u00afX\2\u0323\u032c\5\u00b1Y\2\u0324\u032c\5\u00b3Z")
        buf.write("\2\u0325\u032c\5\u00b5[\2\u0326\u032c\5\u00b7\\\2\u0327")
        buf.write("\u032c\5\u00b9]\2\u0328\u032c\5\u00bb^\2\u0329\u032c\5")
        buf.write("\u00bd_\2\u032a\u032c\5\u00bf`\2\u032b\u031f\3\2\2\2\u032b")
        buf.write("\u0320\3\2\2\2\u032b\u0321\3\2\2\2\u032b\u0322\3\2\2\2")
        buf.write("\u032b\u0323\3\2\2\2\u032b\u0324\3\2\2\2\u032b\u0325\3")
        buf.write("\2\2\2\u032b\u0326\3\2\2\2\u032b\u0327\3\2\2\2\u032b\u0328")
        buf.write("\3\2\2\2\u032b\u0329\3\2\2\2\u032b\u032a\3\2\2\2\u032c")
        buf.write("\u00dc\3\2\2\2\u032d\u0334\5\u00c1a\2\u032e\u0334\5\u00c3")
        buf.write("b\2\u032f\u0334\5\u00c5c\2\u0330\u0334\5\u00c7d\2\u0331")
        buf.write("\u0334\5\u00cbf\2\u0332\u0334\5\u00cdg\2\u0333\u032d\3")
        buf.write("\2\2\2\u0333\u032e\3\2\2\2\u0333\u032f\3\2\2\2\u0333\u0330")
        buf.write("\3\2\2\2\u0333\u0331\3\2\2\2\u0333\u0332\3\2\2\2\u0334")
        buf.write("\u00de\3\2\2\2\u0335\u0339\5\u00d1i\2\u0336\u0339\5\u00cf")
        buf.write("h\2\u0337\u0339\5\u00d3j\2\u0338\u0335\3\2\2\2\u0338\u0336")
        buf.write("\3\2\2\2\u0338\u0337\3\2\2\2\u0339\u00e0\3\2\2\2\u033a")
        buf.write("\u0342\t\5\2\2\u033b\u033d\t\6\2\2\u033c\u033b\3\2\2\2")
        buf.write("\u033d\u0340\3\2\2\2\u033e\u033c\3\2\2\2\u033e\u033f\3")
        buf.write("\2\2\2\u033f\u0341\3\2\2\2\u0340\u033e\3\2\2\2\u0341\u0343")
        buf.write("\t\5\2\2\u0342\u033e\3\2\2\2\u0342\u0343\3\2\2\2\u0343")
        buf.write("\u00e2\3\2\2\2\u0344\u0347\5\u00e5s\2\u0345\u0347\t\5")
        buf.write("\2\2\u0346\u0344\3\2\2\2\u0346\u0345\3\2\2\2\u0347\u00e4")
        buf.write("\3\2\2\2\u0348\u034d\t\7\2\2\u0349\u034d\n\b\2\2\u034a")
        buf.write("\u034b\t\t\2\2\u034b\u034d\t\n\2\2\u034c\u0348\3\2\2\2")
        buf.write("\u034c\u0349\3\2\2\2\u034c\u034a\3\2\2\2\u034d\u00e6\3")
        buf.write("\2\2\2\u034e\u034f\7^\2\2\u034f\u0359\t\13\2\2\u0350\u0355")
        buf.write("\7^\2\2\u0351\u0353\t\f\2\2\u0352\u0351\3\2\2\2\u0352")
        buf.write("\u0353\3\2\2\2\u0353\u0354\3\2\2\2\u0354\u0356\t\r\2\2")
        buf.write("\u0355\u0352\3\2\2\2\u0355\u0356\3\2\2\2\u0356\u0357\3")
        buf.write("\2\2\2\u0357\u0359\t\r\2\2\u0358\u034e\3\2\2\2\u0358\u0350")
        buf.write("\3\2\2\2\u0359\u00e8\3\2\2\2\u035a\u035c\t\16\2\2\u035b")
        buf.write("\u035a\3\2\2\2\u035c\u035d\3\2\2\2\u035d\u035b\3\2\2\2")
        buf.write("\u035d\u035e\3\2\2\2\u035e\u00ea\3\2\2\2\u035f\u0361\7")
        buf.write("\17\2\2\u0360\u035f\3\2\2\2\u0360\u0361\3\2\2\2\u0361")
        buf.write("\u0362\3\2\2\2\u0362\u0365\7\f\2\2\u0363\u0365\4\16\17")
        buf.write("\2\u0364\u0360\3\2\2\2\u0364\u0363\3\2\2\2\u0365\u00ec")
        buf.write("\3\2\2\2\35\2\u0240\u0246\u0248\u0256\u025b\u025f\u0265")
        buf.write("\u026a\u0270\u0276\u0302\u030c\u031a\u032b\u0333\u0338")
        buf.write("\u033e\u0342\u0346\u034c\u0352\u0355\u0358\u035d\u0360")
        buf.write("\u0364\3\2\3\2")
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
    VISCOSITY = 31
    MASS_DENSITY = 32
    RELATIVE_DENSITY = 33
    WEIGHT_DENSITY = 34
    SPECIFIC_GRAVITY = 35
    CONCENTRATION = 36
    SPECIFIC_VOLUME = 37
    COMPRESSIBILITY = 38
    CAPILLARITY = 39
    ELASTICITY = 40
    USEBY = 41
    IDENTIFIER = 42
    STRING_LITERAL = 43
    BOOL_LITERAL = 44
    FLOAT_LITERAL = 45
    INTEGER_LITERAL = 46
    TIME_NUMBER = 47
    VOLUME_NUMBER = 48
    TEMP_NUMBER = 49
    LPAREN = 50
    RPAREN = 51
    LBRACE = 52
    RBRACE = 53
    LBRACKET = 54
    RBRACKET = 55
    SEMICOLON = 56
    COMMA = 57
    DOT = 58
    ASSIGN = 59
    GT = 60
    LT = 61
    BANG = 62
    TILDE = 63
    QUESTION = 64
    COLON = 65
    EQUALITY = 66
    LTE = 67
    GTE = 68
    NOTEQUAL = 69
    AND = 70
    OR = 71
    INC = 72
    DEC = 73
    ADDITION = 74
    SUBTRACT = 75
    MULTIPLY = 76
    DIVIDE = 77
    BITAND = 78
    BITOR = 79
    CARET = 80
    MOD = 81
    UNDERSCORE = 82
    AT_SYMBOL = 83
    NANOSECOND = 84
    MICROSECOND = 85
    MILLISECOND = 86
    CENTISECOND = 87
    DECISECOND = 88
    SECOND = 89
    MINUTE = 90
    HOUR = 91
    DAY = 92
    WEEK = 93
    MONTH = 94
    YEAR = 95
    NANOLITRE = 96
    MICROLITRE = 97
    MILLILITRE = 98
    CENTILITRE = 99
    DECILITRE = 100
    LITRE = 101
    DECALITRE = 102
    CELSIUS = 103
    FAHRENHEIT = 104
    KELVIN = 105
    WS = 106
    COMMENT = 107
    LINE_COMMENT = 108

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'repeat'", "'while'", "'function'", "'return'", 
            "'manifest'", "'module'", "'stationary'", "'functions'", "'instructions'", 
            "'detect'", "'mix'", "'split'", "'heat'", "'drain'", "'dispense'", 
            "'dispose'", "'gradient'", "'at'", "'with'", "'for'", "'into'", 
            "'times'", "'on'", "'of'", "'nat'", "'real'", "'mat'", "'bool'", 
            "'viscosity'", "'mass_density'", "'relative_density'", "'weight_density'", 
            "'specific_gravity'", "'concentration'", "'specific_volume'", 
            "'compressibility'", "'capillarity'", "'elasticity'", "'useby'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", 
            "'='", "'>'", "'<'", "'!'", "'~'", "'?'", "':'", "'=='", "'<='", 
            "'>='", "'!='", "'&&'", "'||'", "'++'", "'--'", "'+'", "'-'", 
            "'*'", "'/'", "'&'", "'|'", "'^'", "'%'", "'_'", "'@'", "'ns'", 
            "'us'", "'ms'", "'cs'", "'ds'", "'s'", "'m'", "'h'", "'d'", 
            "'w'", "'mo'", "'y'", "'nL'", "'uL'", "'mL'", "'cL'", "'dL'", 
            "'L'", "'daL'", "'c'", "'f'", "'k'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", "RETURN", "MANIFEST", 
            "MODULE", "STATIONARY", "FUNCTIONS", "INSTRUCTIONS", "DETECT", 
            "MIX", "SPLIT", "HEAT", "DRAIN", "DISPENSE", "DISPOSE", "GRADIENT", 
            "AT", "WITH", "FOR", "INTO", "TIMES", "ON", "OF", "NAT", "REAL", 
            "MAT", "BOOL", "VISCOSITY", "MASS_DENSITY", "RELATIVE_DENSITY", 
            "WEIGHT_DENSITY", "SPECIFIC_GRAVITY", "CONCENTRATION", "SPECIFIC_VOLUME", 
            "COMPRESSIBILITY", "CAPILLARITY", "ELASTICITY", "USEBY", "IDENTIFIER", 
            "STRING_LITERAL", "BOOL_LITERAL", "FLOAT_LITERAL", "INTEGER_LITERAL", 
            "TIME_NUMBER", "VOLUME_NUMBER", "TEMP_NUMBER", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON", "COMMA", 
            "DOT", "ASSIGN", "GT", "LT", "BANG", "TILDE", "QUESTION", "COLON", 
            "EQUALITY", "LTE", "GTE", "NOTEQUAL", "AND", "OR", "INC", "DEC", 
            "ADDITION", "SUBTRACT", "MULTIPLY", "DIVIDE", "BITAND", "BITOR", 
            "CARET", "MOD", "UNDERSCORE", "AT_SYMBOL", "NANOSECOND", "MICROSECOND", 
            "MILLISECOND", "CENTISECOND", "DECISECOND", "SECOND", "MINUTE", 
            "HOUR", "DAY", "WEEK", "MONTH", "YEAR", "NANOLITRE", "MICROLITRE", 
            "MILLILITRE", "CENTILITRE", "DECILITRE", "LITRE", "DECALITRE", 
            "CELSIUS", "FAHRENHEIT", "KELVIN", "WS", "COMMENT", "LINE_COMMENT" ]

    ruleNames = [ "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", "RETURN", 
                  "MANIFEST", "MODULE", "STATIONARY", "FUNCTIONS", "INSTRUCTIONS", 
                  "DETECT", "MIX", "SPLIT", "HEAT", "DRAIN", "DISPENSE", 
                  "DISPOSE", "GRADIENT", "AT", "WITH", "FOR", "INTO", "TIMES", 
                  "ON", "OF", "NAT", "REAL", "MAT", "BOOL", "VISCOSITY", 
                  "MASS_DENSITY", "RELATIVE_DENSITY", "WEIGHT_DENSITY", 
                  "SPECIFIC_GRAVITY", "CONCENTRATION", "SPECIFIC_VOLUME", 
                  "COMPRESSIBILITY", "CAPILLARITY", "ELASTICITY", "USEBY", 
                  "IDENTIFIER", "STRING_LITERAL", "BOOL_LITERAL", "FLOAT_LITERAL", 
                  "INTEGER_LITERAL", "TIME_NUMBER", "VOLUME_NUMBER", "TEMP_NUMBER", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
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


