import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BSLexer extends Lexer {
    static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

    protected static final DFA[] _decisionToDFA;
    protected static final PredictionContextCache _sharedContextCache =
            new PredictionContextCache();
    public static final int
            IF=1, ELSE=2, REPEAT=3, WHILE=4, FUNCTION=5, RETURN=6, MANIFEST=7, MODULE=8,
            STATIONARY=9, FUNCTIONS=10, INSTRUCTIONS=11, DETECT=12, MIX=13, SPLIT=14,
            HEAT=15, DRAIN=16, DISPENSE=17, DISPOSE=18, AT=19, WITH=20, FOR=21, INTO=22,
            TIMES=23, ON=24, OF=25, NAT=26, REAL=27, MAT=28, BOOL=29, IDENTIFIER=30,
            STRING_LITERAL=31, BOOL_LITERAL=32, FLOAT_LITERAL=33, INTEGER_LITERAL=34,
            TIME_NUMBER=35, VOLUME_NUMBER=36, TEMP_NUMBER=37, LPAREN=38, RPAREN=39,
            LBRACE=40, RBRACE=41, LBRACKET=42, RBRACKET=43, SEMICOLON=44, COMMA=45,
            DOT=46, ASSIGN=47, GT=48, LT=49, BANG=50, TILDE=51, QUESTION=52, COLON=53,
            EQUALITY=54, LTE=55, GTE=56, NOTEQUAL=57, AND=58, OR=59, INC=60, DEC=61,
            ADDITION=62, SUBTRACT=63, MULTIPLY=64, DIVIDE=65, BITAND=66, BITOR=67,
            CARET=68, MOD=69, UNDERSCORE=70, MILLISECOND=71, SECOND=72, HOUR=73, DAY=74,
            WEEK=75, YEAR=76, NANOLITRE=77, MICROLITRE=78, MILLILITRE=79, CENTILITRE=80,
            DECILITRE=81, LITRE=82, DECALITRE=83, CELSIUS=84, FAHRENHEIT=85, WS=86,
            COMMENT=87, LINE_COMMENT=88;
    public static String[] channelNames = {
            "DEFAULT_TOKEN_CHANNEL", "HIDDEN"
    };

    public static String[] modeNames = {
            "DEFAULT_MODE"
    };

    public static final String[] ruleNames = {
            "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", "RETURN", "MANIFEST", "MODULE",
            "STATIONARY", "FUNCTIONS", "INSTRUCTIONS", "DETECT", "MIX", "SPLIT", "HEAT",
            "DRAIN", "DISPENSE", "DISPOSE", "AT", "WITH", "FOR", "INTO", "TIMES",
            "ON", "OF", "NAT", "REAL", "MAT", "BOOL", "IDENTIFIER", "STRING_LITERAL",
            "BOOL_LITERAL", "FLOAT_LITERAL", "INTEGER_LITERAL", "TIME_NUMBER", "VOLUME_NUMBER",
            "TEMP_NUMBER", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET",
            "SEMICOLON", "COMMA", "DOT", "ASSIGN", "GT", "LT", "BANG", "TILDE", "QUESTION",
            "COLON", "EQUALITY", "LTE", "GTE", "NOTEQUAL", "AND", "OR", "INC", "DEC",
            "ADDITION", "SUBTRACT", "MULTIPLY", "DIVIDE", "BITAND", "BITOR", "CARET",
            "MOD", "UNDERSCORE", "MILLISECOND", "SECOND", "HOUR", "DAY", "WEEK", "YEAR",
            "NANOLITRE", "MICROLITRE", "MILLILITRE", "CENTILITRE", "DECILITRE", "LITRE",
            "DECALITRE", "CELSIUS", "FAHRENHEIT", "WS", "COMMENT", "LINE_COMMENT",
            "TimeUnits", "VolumeUnits", "TempUnits", "Digits", "LetterOrDigit", "Letter",
            "EscapeSequence", "SPACES", "NEWLINE"
    };

    private static final String[] _LITERAL_NAMES = {
            null, "'if'", "'else'", "'repeat'", "'while'", "'function'", "'return'",
            "'manifest'", "'module'", "'stationary'", "'functions'", "'instructions'",
            "'detect'", "'mix'", "'split'", "'heat'", "'drain'", "'dispense'", "'dispose'",
            "'at'", "'with'", "'for'", "'into'", "'times'", "'on'", "'of'", "'nat'",
            "'real'", "'mat'", "'bool'", null, null, null, null, null, null, null,
            null, "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", "'='",
            "'>'", "'<'", "'!'", "'~'", "'?'", "':'", "'=='", "'<='", "'>='", "'!='",
            "'&&'", "'||'", "'++'", "'--'", "'+'", "'-'", "'*'", "'/'", "'&'", "'|'",
            "'^'", "'%'", "'_'", "'ms'", "'s'", "'h'", "'d'", "'w'", "'y'", "'nL'",
            "'uL'", "'mL'", "'cL'", "'dL'", "'L'", "'daL'", "'c'", "'f'"
    };
    private static final String[] _SYMBOLIC_NAMES = {
            null, "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", "RETURN", "MANIFEST",
            "MODULE", "STATIONARY", "FUNCTIONS", "INSTRUCTIONS", "DETECT", "MIX",
            "SPLIT", "HEAT", "DRAIN", "DISPENSE", "DISPOSE", "AT", "WITH", "FOR",
            "INTO", "TIMES", "ON", "OF", "NAT", "REAL", "MAT", "BOOL", "IDENTIFIER",
            "STRING_LITERAL", "BOOL_LITERAL", "FLOAT_LITERAL", "INTEGER_LITERAL",
            "TIME_NUMBER", "VOLUME_NUMBER", "TEMP_NUMBER", "LPAREN", "RPAREN", "LBRACE",
            "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON", "COMMA", "DOT", "ASSIGN",
            "GT", "LT", "BANG", "TILDE", "QUESTION", "COLON", "EQUALITY", "LTE", "GTE",
            "NOTEQUAL", "AND", "OR", "INC", "DEC", "ADDITION", "SUBTRACT", "MULTIPLY",
            "DIVIDE", "BITAND", "BITOR", "CARET", "MOD", "UNDERSCORE", "MILLISECOND",
            "SECOND", "HOUR", "DAY", "WEEK", "YEAR", "NANOLITRE", "MICROLITRE", "MILLILITRE",
            "CENTILITRE", "DECILITRE", "LITRE", "DECALITRE", "CELSIUS", "FAHRENHEIT",
            "WS", "COMMENT", "LINE_COMMENT"
    };
    public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

    /**
     * @deprecated Use {@link #VOCABULARY} instead.
     */
    @Deprecated
    public static final String[] tokenNames;
    static {
        tokenNames = new String[_SYMBOLIC_NAMES.length];
        for (int i = 0; i < tokenNames.length; i++) {
            tokenNames[i] = VOCABULARY.getLiteralName(i);
            if (tokenNames[i] == null) {
                tokenNames[i] = VOCABULARY.getSymbolicName(i);
            }

            if (tokenNames[i] == null) {
                tokenNames[i] = "<INVALID>";
            }
        }
    }

    @Override
    @Deprecated
    public String[] getTokenNames() {
        return tokenNames;
    }

    @Override

    public Vocabulary getVocabulary() {
        return VOCABULARY;
    }


    public BSLexer(CharStream input) {
        super(input);
        _interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
    }

    @Override
    public String getGrammarFileName() { return "BSLexer.g4"; }

    @Override
    public String[] getRuleNames() { return ruleNames; }

    @Override
    public String getSerializedATN() { return _serializedATN; }

    @Override
    public String[] getChannelNames() { return channelNames; }

    @Override
    public String[] getModeNames() { return modeNames; }

    @Override
    public ATN getATN() { return _ATN; }

    public static final String _serializedATN =
            "\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2Z\u0286\b\1\4\2\t"+
                    "\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
                    "\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
                    "\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
                    "\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
                    "\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
                    ",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
                    "\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
                    "\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
                    "\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
                    "\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4"+
                    "`\t`\4a\ta\4b\tb\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3"+
                    "\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7"+
                    "\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3"+
                    "\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3"+
                    "\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3"+
                    "\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16"+
                    "\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21"+
                    "\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23"+
                    "\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25"+
                    "\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30"+
                    "\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34"+
                    "\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37"+
                    "\7\37\u017b\n\37\f\37\16\37\u017e\13\37\3 \3 \3 \7 \u0183\n \f \16 \u0186"+
                    "\13 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0193\n!\3\"\3\"\3\"\5\"\u0198"+
                    "\n\"\3\"\3\"\5\"\u019c\n\"\3#\3#\7#\u01a0\n#\f#\16#\u01a3\13#\3$\3$\5"+
                    "$\u01a7\n$\3$\3$\3%\3%\5%\u01ad\n%\3%\3%\3&\3&\5&\u01b3\n&\3&\3&\3\'\3"+
                    "\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61"+
                    "\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\38\3"+
                    "8\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3@\3"+
                    "@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3H\3I\3I\3J\3J\3K\3"+
                    "K\3L\3L\3M\3M\3N\3N\3N\3O\3O\3O\3P\3P\3P\3Q\3Q\3Q\3R\3R\3R\3S\3S\3T\3"+
                    "T\3T\3T\3U\3U\3V\3V\3W\6W\u0228\nW\rW\16W\u0229\3W\3W\3X\3X\3X\3X\7X\u0232"+
                    "\nX\fX\16X\u0235\13X\3X\3X\3X\3X\3X\3Y\3Y\3Y\3Y\7Y\u0240\nY\fY\16Y\u0243"+
                    "\13Y\3Y\3Y\3Z\3Z\3Z\3Z\3Z\3Z\5Z\u024d\nZ\3[\3[\3[\3[\3[\3[\5[\u0255\n"+
                    "[\3\\\3\\\5\\\u0259\n\\\3]\3]\7]\u025d\n]\f]\16]\u0260\13]\3]\5]\u0263"+
                    "\n]\3^\3^\5^\u0267\n^\3_\3_\3_\3_\5_\u026d\n_\3`\3`\3`\3`\5`\u0273\n`"+
                    "\3`\5`\u0276\n`\3`\5`\u0279\n`\3a\6a\u027c\na\ra\16a\u027d\3b\5b\u0281"+
                    "\nb\3b\3b\5b\u0285\nb\3\u0233\2c\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23"+
                    "\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31"+
                    "\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60"+
                    "_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085"+
                    "D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099"+
                    "N\u009bO\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7U\u00a9V\u00abW\u00ad"+
                    "X\u00afY\u00b1Z\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf"+
                    "\2\u00c1\2\u00c3\2\3\2\17\6\2\f\f\17\17$$^^\5\2\13\f\16\17\"\"\4\2\f\f"+
                    "\17\17\3\2\62;\4\2\62;aa\6\2&&C\\aac|\4\2\2\u0081\ud802\udc01\3\2\ud802"+
                    "\udc01\3\2\udc02\ue001\n\2$$))^^ddhhppttvv\3\2\62\65\3\2\629\4\2\13\13"+
                    "\"\"\2\u029f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2"+
                    "\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2"+
                    "\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2"+
                    "\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2"+
                    "\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3"+
                    "\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2"+
                    "\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2"+
                    "S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3"+
                    "\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2"+
                    "\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2"+
                    "y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083"+
                    "\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2"+
                    "\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095"+
                    "\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2"+
                    "\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7"+
                    "\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2"+
                    "\2\2\u00b1\3\2\2\2\3\u00c5\3\2\2\2\5\u00c8\3\2\2\2\7\u00cd\3\2\2\2\t\u00d4"+
                    "\3\2\2\2\13\u00da\3\2\2\2\r\u00e3\3\2\2\2\17\u00ea\3\2\2\2\21\u00f3\3"+
                    "\2\2\2\23\u00fa\3\2\2\2\25\u0105\3\2\2\2\27\u010f\3\2\2\2\31\u011c\3\2"+
                    "\2\2\33\u0123\3\2\2\2\35\u0127\3\2\2\2\37\u012d\3\2\2\2!\u0132\3\2\2\2"+
                    "#\u0138\3\2\2\2%\u0141\3\2\2\2\'\u0149\3\2\2\2)\u014c\3\2\2\2+\u0151\3"+
                    "\2\2\2-\u0155\3\2\2\2/\u015a\3\2\2\2\61\u0160\3\2\2\2\63\u0163\3\2\2\2"+
                    "\65\u0166\3\2\2\2\67\u016a\3\2\2\29\u016f\3\2\2\2;\u0173\3\2\2\2=\u0178"+
                    "\3\2\2\2?\u017f\3\2\2\2A\u0192\3\2\2\2C\u019b\3\2\2\2E\u019d\3\2\2\2G"+
                    "\u01a6\3\2\2\2I\u01ac\3\2\2\2K\u01b2\3\2\2\2M\u01b6\3\2\2\2O\u01b8\3\2"+
                    "\2\2Q\u01ba\3\2\2\2S\u01bc\3\2\2\2U\u01be\3\2\2\2W\u01c0\3\2\2\2Y\u01c2"+
                    "\3\2\2\2[\u01c4\3\2\2\2]\u01c6\3\2\2\2_\u01c8\3\2\2\2a\u01ca\3\2\2\2c"+
                    "\u01cc\3\2\2\2e\u01ce\3\2\2\2g\u01d0\3\2\2\2i\u01d2\3\2\2\2k\u01d4\3\2"+
                    "\2\2m\u01d6\3\2\2\2o\u01d9\3\2\2\2q\u01dc\3\2\2\2s\u01df\3\2\2\2u\u01e2"+
                    "\3\2\2\2w\u01e5\3\2\2\2y\u01e8\3\2\2\2{\u01eb\3\2\2\2}\u01ee\3\2\2\2\177"+
                    "\u01f0\3\2\2\2\u0081\u01f2\3\2\2\2\u0083\u01f4\3\2\2\2\u0085\u01f6\3\2"+
                    "\2\2\u0087\u01f8\3\2\2\2\u0089\u01fa\3\2\2\2\u008b\u01fc\3\2\2\2\u008d"+
                    "\u01fe\3\2\2\2\u008f\u0200\3\2\2\2\u0091\u0203\3\2\2\2\u0093\u0205\3\2"+
                    "\2\2\u0095\u0207\3\2\2\2\u0097\u0209\3\2\2\2\u0099\u020b\3\2\2\2\u009b"+
                    "\u020d\3\2\2\2\u009d\u0210\3\2\2\2\u009f\u0213\3\2\2\2\u00a1\u0216\3\2"+
                    "\2\2\u00a3\u0219\3\2\2\2\u00a5\u021c\3\2\2\2\u00a7\u021e\3\2\2\2\u00a9"+
                    "\u0222\3\2\2\2\u00ab\u0224\3\2\2\2\u00ad\u0227\3\2\2\2\u00af\u022d\3\2"+
                    "\2\2\u00b1\u023b\3\2\2\2\u00b3\u024c\3\2\2\2\u00b5\u0254\3\2\2\2\u00b7"+
                    "\u0258\3\2\2\2\u00b9\u025a\3\2\2\2\u00bb\u0266\3\2\2\2\u00bd\u026c\3\2"+
                    "\2\2\u00bf\u0278\3\2\2\2\u00c1\u027b\3\2\2\2\u00c3\u0284\3\2\2\2\u00c5"+
                    "\u00c6\7k\2\2\u00c6\u00c7\7h\2\2\u00c7\4\3\2\2\2\u00c8\u00c9\7g\2\2\u00c9"+
                    "\u00ca\7n\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7g\2\2\u00cc\6\3\2\2\2\u00cd"+
                    "\u00ce\7t\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7r\2\2\u00d0\u00d1\7g\2\2"+
                    "\u00d1\u00d2\7c\2\2\u00d2\u00d3\7v\2\2\u00d3\b\3\2\2\2\u00d4\u00d5\7y"+
                    "\2\2\u00d5\u00d6\7j\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9"+
                    "\7g\2\2\u00d9\n\3\2\2\2\u00da\u00db\7h\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd"+
                    "\7p\2\2\u00dd\u00de\7e\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7k\2\2\u00e0"+
                    "\u00e1\7q\2\2\u00e1\u00e2\7p\2\2\u00e2\f\3\2\2\2\u00e3\u00e4\7t\2\2\u00e4"+
                    "\u00e5\7g\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8\7t\2\2"+
                    "\u00e8\u00e9\7p\2\2\u00e9\16\3\2\2\2\u00ea\u00eb\7o\2\2\u00eb\u00ec\7"+
                    "c\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7h\2\2\u00ef\u00f0"+
                    "\7g\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2\7v\2\2\u00f2\20\3\2\2\2\u00f3\u00f4"+
                    "\7o\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7f\2\2\u00f6\u00f7\7w\2\2\u00f7"+
                    "\u00f8\7n\2\2\u00f8\u00f9\7g\2\2\u00f9\22\3\2\2\2\u00fa\u00fb\7u\2\2\u00fb"+
                    "\u00fc\7v\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7k\2\2"+
                    "\u00ff\u0100\7q\2\2\u0100\u0101\7p\2\2\u0101\u0102\7c\2\2\u0102\u0103"+
                    "\7t\2\2\u0103\u0104\7{\2\2\u0104\24\3\2\2\2\u0105\u0106\7h\2\2\u0106\u0107"+
                    "\7w\2\2\u0107\u0108\7p\2\2\u0108\u0109\7e\2\2\u0109\u010a\7v\2\2\u010a"+
                    "\u010b\7k\2\2\u010b\u010c\7q\2\2\u010c\u010d\7p\2\2\u010d\u010e\7u\2\2"+
                    "\u010e\26\3\2\2\2\u010f\u0110\7k\2\2\u0110\u0111\7p\2\2\u0111\u0112\7"+
                    "u\2\2\u0112\u0113\7v\2\2\u0113\u0114\7t\2\2\u0114\u0115\7w\2\2\u0115\u0116"+
                    "\7e\2\2\u0116\u0117\7v\2\2\u0117\u0118\7k\2\2\u0118\u0119\7q\2\2\u0119"+
                    "\u011a\7p\2\2\u011a\u011b\7u\2\2\u011b\30\3\2\2\2\u011c\u011d\7f\2\2\u011d"+
                    "\u011e\7g\2\2\u011e\u011f\7v\2\2\u011f\u0120\7g\2\2\u0120\u0121\7e\2\2"+
                    "\u0121\u0122\7v\2\2\u0122\32\3\2\2\2\u0123\u0124\7o\2\2\u0124\u0125\7"+
                    "k\2\2\u0125\u0126\7z\2\2\u0126\34\3\2\2\2\u0127\u0128\7u\2\2\u0128\u0129"+
                    "\7r\2\2\u0129\u012a\7n\2\2\u012a\u012b\7k\2\2\u012b\u012c\7v\2\2\u012c"+
                    "\36\3\2\2\2\u012d\u012e\7j\2\2\u012e\u012f\7g\2\2\u012f\u0130\7c\2\2\u0130"+
                    "\u0131\7v\2\2\u0131 \3\2\2\2\u0132\u0133\7f\2\2\u0133\u0134\7t\2\2\u0134"+
                    "\u0135\7c\2\2\u0135\u0136\7k\2\2\u0136\u0137\7p\2\2\u0137\"\3\2\2\2\u0138"+
                    "\u0139\7f\2\2\u0139\u013a\7k\2\2\u013a\u013b\7u\2\2\u013b\u013c\7r\2\2"+
                    "\u013c\u013d\7g\2\2\u013d\u013e\7p\2\2\u013e\u013f\7u\2\2\u013f\u0140"+
                    "\7g\2\2\u0140$\3\2\2\2\u0141\u0142\7f\2\2\u0142\u0143\7k\2\2\u0143\u0144"+
                    "\7u\2\2\u0144\u0145\7r\2\2\u0145\u0146\7q\2\2\u0146\u0147\7u\2\2\u0147"+
                    "\u0148\7g\2\2\u0148&\3\2\2\2\u0149\u014a\7c\2\2\u014a\u014b\7v\2\2\u014b"+
                    "(\3\2\2\2\u014c\u014d\7y\2\2\u014d\u014e\7k\2\2\u014e\u014f\7v\2\2\u014f"+
                    "\u0150\7j\2\2\u0150*\3\2\2\2\u0151\u0152\7h\2\2\u0152\u0153\7q\2\2\u0153"+
                    "\u0154\7t\2\2\u0154,\3\2\2\2\u0155\u0156\7k\2\2\u0156\u0157\7p\2\2\u0157"+
                    "\u0158\7v\2\2\u0158\u0159\7q\2\2\u0159.\3\2\2\2\u015a\u015b\7v\2\2\u015b"+
                    "\u015c\7k\2\2\u015c\u015d\7o\2\2\u015d\u015e\7g\2\2\u015e\u015f\7u\2\2"+
                    "\u015f\60\3\2\2\2\u0160\u0161\7q\2\2\u0161\u0162\7p\2\2\u0162\62\3\2\2"+
                    "\2\u0163\u0164\7q\2\2\u0164\u0165\7h\2\2\u0165\64\3\2\2\2\u0166\u0167"+
                    "\7p\2\2\u0167\u0168\7c\2\2\u0168\u0169\7v\2\2\u0169\66\3\2\2\2\u016a\u016b"+
                    "\7t\2\2\u016b\u016c\7g\2\2\u016c\u016d\7c\2\2\u016d\u016e\7n\2\2\u016e"+
                    "8\3\2\2\2\u016f\u0170\7o\2\2\u0170\u0171\7c\2\2\u0171\u0172\7v\2\2\u0172"+
                    ":\3\2\2\2\u0173\u0174\7d\2\2\u0174\u0175\7q\2\2\u0175\u0176\7q\2\2\u0176"+
                    "\u0177\7n\2\2\u0177<\3\2\2\2\u0178\u017c\5\u00bd_\2\u0179\u017b\5\u00bb"+
                    "^\2\u017a\u0179\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c"+
                    "\u017d\3\2\2\2\u017d>\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0184\7$\2\2\u0180"+
                    "\u0183\n\2\2\2\u0181\u0183\5\u00bf`\2\u0182\u0180\3\2\2\2\u0182\u0181"+
                    "\3\2\2\2\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185"+
                    "\u0187\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188\7$\2\2\u0188@\3\2\2\2\u0189"+
                    "\u018a\7v\2\2\u018a\u018b\7t\2\2\u018b\u018c\7w\2\2\u018c\u0193\7g\2\2"+
                    "\u018d\u018e\7h\2\2\u018e\u018f\7c\2\2\u018f\u0190\7n\2\2\u0190\u0191"+
                    "\7u\2\2\u0191\u0193\7g\2\2\u0192\u0189\3\2\2\2\u0192\u018d\3\2\2\2\u0193"+
                    "B\3\2\2\2\u0194\u0195\5\u00b9]\2\u0195\u0197\7\60\2\2\u0196\u0198\5\u00b9"+
                    "]\2\u0197\u0196\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019c\3\2\2\2\u0199"+
                    "\u019a\7\60\2\2\u019a\u019c\5\u00b9]\2\u019b\u0194\3\2\2\2\u019b\u0199"+
                    "\3\2\2\2\u019cD\3\2\2\2\u019d\u01a1\5\u00b9]\2\u019e\u01a0\5\u00b9]\2"+
                    "\u019f\u019e\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2"+
                    "\3\2\2\2\u01a2F\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a7\5C\"\2\u01a5\u01a7"+
                    "\5E#\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8"+
                    "\u01a9\5\u00b3Z\2\u01a9H\3\2\2\2\u01aa\u01ad\5C\"\2\u01ab\u01ad\5E#\2"+
                    "\u01ac\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af"+
                    "\5\u00b5[\2\u01afJ\3\2\2\2\u01b0\u01b3\5C\"\2\u01b1\u01b3\5E#\2\u01b2"+
                    "\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\5\u00b7"+
                    "\\\2\u01b5L\3\2\2\2\u01b6\u01b7\7*\2\2\u01b7N\3\2\2\2\u01b8\u01b9\7+\2"+
                    "\2\u01b9P\3\2\2\2\u01ba\u01bb\7}\2\2\u01bbR\3\2\2\2\u01bc\u01bd\7\177"+
                    "\2\2\u01bdT\3\2\2\2\u01be\u01bf\7]\2\2\u01bfV\3\2\2\2\u01c0\u01c1\7_\2"+
                    "\2\u01c1X\3\2\2\2\u01c2\u01c3\7=\2\2\u01c3Z\3\2\2\2\u01c4\u01c5\7.\2\2"+
                    "\u01c5\\\3\2\2\2\u01c6\u01c7\7\60\2\2\u01c7^\3\2\2\2\u01c8\u01c9\7?\2"+
                    "\2\u01c9`\3\2\2\2\u01ca\u01cb\7@\2\2\u01cbb\3\2\2\2\u01cc\u01cd\7>\2\2"+
                    "\u01cdd\3\2\2\2\u01ce\u01cf\7#\2\2\u01cff\3\2\2\2\u01d0\u01d1\7\u0080"+
                    "\2\2\u01d1h\3\2\2\2\u01d2\u01d3\7A\2\2\u01d3j\3\2\2\2\u01d4\u01d5\7<\2"+
                    "\2\u01d5l\3\2\2\2\u01d6\u01d7\7?\2\2\u01d7\u01d8\7?\2\2\u01d8n\3\2\2\2"+
                    "\u01d9\u01da\7>\2\2\u01da\u01db\7?\2\2\u01dbp\3\2\2\2\u01dc\u01dd\7@\2"+
                    "\2\u01dd\u01de\7?\2\2\u01der\3\2\2\2\u01df\u01e0\7#\2\2\u01e0\u01e1\7"+
                    "?\2\2\u01e1t\3\2\2\2\u01e2\u01e3\7(\2\2\u01e3\u01e4\7(\2\2\u01e4v\3\2"+
                    "\2\2\u01e5\u01e6\7~\2\2\u01e6\u01e7\7~\2\2\u01e7x\3\2\2\2\u01e8\u01e9"+
                    "\7-\2\2\u01e9\u01ea\7-\2\2\u01eaz\3\2\2\2\u01eb\u01ec\7/\2\2\u01ec\u01ed"+
                    "\7/\2\2\u01ed|\3\2\2\2\u01ee\u01ef\7-\2\2\u01ef~\3\2\2\2\u01f0\u01f1\7"+
                    "/\2\2\u01f1\u0080\3\2\2\2\u01f2\u01f3\7,\2\2\u01f3\u0082\3\2\2\2\u01f4"+
                    "\u01f5\7\61\2\2\u01f5\u0084\3\2\2\2\u01f6\u01f7\7(\2\2\u01f7\u0086\3\2"+
                    "\2\2\u01f8\u01f9\7~\2\2\u01f9\u0088\3\2\2\2\u01fa\u01fb\7`\2\2\u01fb\u008a"+
                    "\3\2\2\2\u01fc\u01fd\7\'\2\2\u01fd\u008c\3\2\2\2\u01fe\u01ff\7a\2\2\u01ff"+
                    "\u008e\3\2\2\2\u0200\u0201\7o\2\2\u0201\u0202\7u\2\2\u0202\u0090\3\2\2"+
                    "\2\u0203\u0204\7u\2\2\u0204\u0092\3\2\2\2\u0205\u0206\7j\2\2\u0206\u0094"+
                    "\3\2\2\2\u0207\u0208\7f\2\2\u0208\u0096\3\2\2\2\u0209\u020a\7y\2\2\u020a"+
                    "\u0098\3\2\2\2\u020b\u020c\7{\2\2\u020c\u009a\3\2\2\2\u020d\u020e\7p\2"+
                    "\2\u020e\u020f\7N\2\2\u020f\u009c\3\2\2\2\u0210\u0211\7w\2\2\u0211\u0212"+
                    "\7N\2\2\u0212\u009e\3\2\2\2\u0213\u0214\7o\2\2\u0214\u0215\7N\2\2\u0215"+
                    "\u00a0\3\2\2\2\u0216\u0217\7e\2\2\u0217\u0218\7N\2\2\u0218\u00a2\3\2\2"+
                    "\2\u0219\u021a\7f\2\2\u021a\u021b\7N\2\2\u021b\u00a4\3\2\2\2\u021c\u021d"+
                    "\7N\2\2\u021d\u00a6\3\2\2\2\u021e\u021f\7f\2\2\u021f\u0220\7c\2\2\u0220"+
                    "\u0221\7N\2\2\u0221\u00a8\3\2\2\2\u0222\u0223\7e\2\2\u0223\u00aa\3\2\2"+
                    "\2\u0224\u0225\7h\2\2\u0225\u00ac\3\2\2\2\u0226\u0228\t\3\2\2\u0227\u0226"+
                    "\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a"+
                    "\u022b\3\2\2\2\u022b\u022c\bW\2\2\u022c\u00ae\3\2\2\2\u022d\u022e\7\61"+
                    "\2\2\u022e\u022f\7,\2\2\u022f\u0233\3\2\2\2\u0230\u0232\13\2\2\2\u0231"+
                    "\u0230\3\2\2\2\u0232\u0235\3\2\2\2\u0233\u0234\3\2\2\2\u0233\u0231\3\2"+
                    "\2\2\u0234\u0236\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0237\7,\2\2\u0237"+
                    "\u0238\7\61\2\2\u0238\u0239\3\2\2\2\u0239\u023a\bX\2\2\u023a\u00b0\3\2"+
                    "\2\2\u023b\u023c\7\61\2\2\u023c\u023d\7\61\2\2\u023d\u0241\3\2\2\2\u023e"+
                    "\u0240\n\4\2\2\u023f\u023e\3\2\2\2\u0240\u0243\3\2\2\2\u0241\u023f\3\2"+
                    "\2\2\u0241\u0242\3\2\2\2\u0242\u0244\3\2\2\2\u0243\u0241\3\2\2\2\u0244"+
                    "\u0245\bY\2\2\u0245\u00b2\3\2\2\2\u0246\u024d\5\u008fH\2\u0247\u024d\5"+
                    "\u0091I\2\u0248\u024d\5\u0093J\2\u0249\u024d\5\u0095K\2\u024a\u024d\5"+
                    "\u0097L\2\u024b\u024d\5\u0099M\2\u024c\u0246\3\2\2\2\u024c\u0247\3\2\2"+
                    "\2\u024c\u0248\3\2\2\2\u024c\u0249\3\2\2\2\u024c\u024a\3\2\2\2\u024c\u024b"+
                    "\3\2\2\2\u024d\u00b4\3\2\2\2\u024e\u0255\5\u009bN\2\u024f\u0255\5\u009d"+
                    "O\2\u0250\u0255\5\u009fP\2\u0251\u0255\5\u00a1Q\2\u0252\u0255\5\u00a5"+
                    "S\2\u0253\u0255\5\u00a7T\2\u0254\u024e\3\2\2\2\u0254\u024f\3\2\2\2\u0254"+
                    "\u0250\3\2\2\2\u0254\u0251\3\2\2\2\u0254\u0252\3\2\2\2\u0254\u0253\3\2"+
                    "\2\2\u0255\u00b6\3\2\2\2\u0256\u0259\5\u00abV\2\u0257\u0259\5\u00a9U\2"+
                    "\u0258\u0256\3\2\2\2\u0258\u0257\3\2\2\2\u0259\u00b8\3\2\2\2\u025a\u0262"+
                    "\t\5\2\2\u025b\u025d\t\6\2\2\u025c\u025b\3\2\2\2\u025d\u0260\3\2\2\2\u025e"+
                    "\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u0261\3\2\2\2\u0260\u025e\3\2"+
                    "\2\2\u0261\u0263\t\5\2\2\u0262\u025e\3\2\2\2\u0262\u0263\3\2\2\2\u0263"+
                    "\u00ba\3\2\2\2\u0264\u0267\5\u00bd_\2\u0265\u0267\t\5\2\2\u0266\u0264"+
                    "\3\2\2\2\u0266\u0265\3\2\2\2\u0267\u00bc\3\2\2\2\u0268\u026d\t\7\2\2\u0269"+
                    "\u026d\n\b\2\2\u026a\u026b\t\t\2\2\u026b\u026d\t\n\2\2\u026c\u0268\3\2"+
                    "\2\2\u026c\u0269\3\2\2\2\u026c\u026a\3\2\2\2\u026d\u00be\3\2\2\2\u026e"+
                    "\u026f\7^\2\2\u026f\u0279\t\13\2\2\u0270\u0275\7^\2\2\u0271\u0273\t\f"+
                    "\2\2\u0272\u0271\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0274\3\2\2\2\u0274"+
                    "\u0276\t\r\2\2\u0275\u0272\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0277\3\2"+
                    "\2\2\u0277\u0279\t\r\2\2\u0278\u026e\3\2\2\2\u0278\u0270\3\2\2\2\u0279"+
                    "\u00c0\3\2\2\2\u027a\u027c\t\16\2\2\u027b\u027a\3\2\2\2\u027c\u027d\3"+
                    "\2\2\2\u027d\u027b\3\2\2\2\u027d\u027e\3\2\2\2\u027e\u00c2\3\2\2\2\u027f"+
                    "\u0281\7\17\2\2\u0280\u027f\3\2\2\2\u0280\u0281\3\2\2\2\u0281\u0282\3"+
                    "\2\2\2\u0282\u0285\7\f\2\2\u0283\u0285\4\16\17\2\u0284\u0280\3\2\2\2\u0284"+
                    "\u0283\3\2\2\2\u0285\u00c4\3\2\2\2\35\2\u017c\u0182\u0184\u0192\u0197"+
                    "\u019b\u01a1\u01a6\u01ac\u01b2\u0229\u0233\u0241\u024c\u0254\u0258\u025e"+
                    "\u0262\u0266\u026c\u0272\u0275\u0278\u027d\u0280\u0284\3\2\3\2";
    public static final ATN _ATN =
            new ATNDeserializer().deserialize(_serializedATN.toCharArray());
    static {
        _decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
        for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
            _decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
        }
    }
}