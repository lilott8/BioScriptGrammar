# Generated from /Users/life/PycharmProjects/BioScript/grammar/grammar/BSParser.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

# parser/listener/visitor header section */
def serializedATN():
    return [
        4,1,176,505,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,
        46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,
        52,1,0,4,0,108,8,0,11,0,12,0,109,1,0,3,0,113,8,0,1,0,1,0,1,0,5,0,
        118,8,0,10,0,12,0,121,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,129,8,1,1,
        2,1,2,1,2,1,3,3,3,135,8,3,1,3,1,3,1,3,1,4,3,4,141,8,4,1,4,1,4,1,
        4,1,5,1,5,3,5,148,8,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,157,8,7,10,
        7,12,7,160,9,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,4,9,170,8,9,11,9,
        12,9,171,1,10,1,10,1,10,1,10,3,10,178,8,10,1,10,1,10,5,10,182,8,
        10,10,10,12,10,185,9,10,1,10,1,10,1,10,1,11,1,11,3,11,192,8,11,1,
        11,1,11,1,12,1,12,1,12,5,12,199,8,12,10,12,12,12,202,9,12,1,13,3,
        13,205,8,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,216,
        8,15,1,16,1,16,5,16,220,8,16,10,16,12,16,223,9,16,1,16,1,16,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,3,17,244,8,17,1,18,1,18,1,18,1,18,1,18,3,18,251,8,
        18,1,19,1,19,1,19,1,19,5,19,257,8,19,10,19,12,19,260,9,19,1,19,1,
        19,1,19,1,19,5,19,266,8,19,10,19,12,19,269,9,19,1,19,1,19,1,20,1,
        20,1,20,1,20,1,21,1,21,1,21,3,21,280,8,21,1,21,1,21,1,21,1,22,3,
        22,286,8,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,294,8,22,1,23,1,23,
        1,23,1,23,3,23,300,8,23,1,24,3,24,303,8,24,1,24,1,24,1,24,3,24,308,
        8,24,1,24,1,24,1,24,3,24,313,8,24,1,24,1,24,1,24,3,24,318,8,24,1,
        25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,331,8,
        26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,3,28,342,8,28,1,
        28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,1,32,3,32,374,8,32,1,33,1,33,1,33,1,33,1,33,1,33,1,
        33,1,33,3,33,384,8,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,
        33,1,33,3,33,396,8,33,1,34,1,34,1,34,1,34,5,34,402,8,34,10,34,12,
        34,405,9,34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,36,3,36,415,8,36,
        1,36,1,36,1,37,1,37,1,37,1,37,3,37,423,8,37,5,37,425,8,37,10,37,
        12,37,428,9,37,1,37,3,37,431,8,37,1,38,1,38,3,38,435,8,38,1,39,1,
        39,1,39,1,39,1,40,1,40,1,40,5,40,444,8,40,10,40,12,40,447,9,40,1,
        41,3,41,450,8,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,5,42,460,
        8,42,10,42,12,42,463,9,42,1,42,1,42,1,43,1,43,1,43,1,43,3,43,471,
        8,43,1,44,1,44,1,45,1,45,1,45,1,45,5,45,479,8,45,10,45,12,45,482,
        9,45,1,45,1,45,1,46,1,46,1,46,3,46,489,8,46,1,47,1,47,1,48,1,48,
        1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,52,1,52,1,52,0,0,53,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,
        92,94,96,98,100,102,104,0,8,2,0,72,73,77,77,1,0,70,71,2,0,56,57,
        63,64,2,0,62,62,65,65,1,0,66,67,1,0,39,42,1,0,34,37,2,0,42,42,102,
        173,516,0,107,1,0,0,0,2,128,1,0,0,0,4,130,1,0,0,0,6,134,1,0,0,0,
        8,140,1,0,0,0,10,147,1,0,0,0,12,149,1,0,0,0,14,152,1,0,0,0,16,163,
        1,0,0,0,18,166,1,0,0,0,20,173,1,0,0,0,22,189,1,0,0,0,24,195,1,0,
        0,0,26,204,1,0,0,0,28,208,1,0,0,0,30,215,1,0,0,0,32,217,1,0,0,0,
        34,243,1,0,0,0,36,245,1,0,0,0,38,252,1,0,0,0,40,272,1,0,0,0,42,276,
        1,0,0,0,44,285,1,0,0,0,46,299,1,0,0,0,48,302,1,0,0,0,50,319,1,0,
        0,0,52,323,1,0,0,0,54,332,1,0,0,0,56,338,1,0,0,0,58,345,1,0,0,0,
        60,357,1,0,0,0,62,360,1,0,0,0,64,373,1,0,0,0,66,395,1,0,0,0,68,397,
        1,0,0,0,70,408,1,0,0,0,72,411,1,0,0,0,74,430,1,0,0,0,76,434,1,0,
        0,0,78,436,1,0,0,0,80,440,1,0,0,0,82,449,1,0,0,0,84,454,1,0,0,0,
        86,466,1,0,0,0,88,472,1,0,0,0,90,474,1,0,0,0,92,488,1,0,0,0,94,490,
        1,0,0,0,96,492,1,0,0,0,98,494,1,0,0,0,100,496,1,0,0,0,102,498,1,
        0,0,0,104,500,1,0,0,0,106,108,3,2,1,0,107,106,1,0,0,0,108,109,1,
        0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,113,3,
        18,9,0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,5,
        11,0,0,115,119,5,61,0,0,116,118,3,34,17,0,117,116,1,0,0,0,118,121,
        1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,119,
        1,0,0,0,122,123,5,0,0,1,123,1,1,0,0,0,124,129,3,4,2,0,125,129,3,
        6,3,0,126,129,3,8,4,0,127,129,3,10,5,0,128,124,1,0,0,0,128,125,1,
        0,0,0,128,126,1,0,0,0,128,127,1,0,0,0,129,3,1,0,0,0,130,131,5,8,
        0,0,131,132,5,38,0,0,132,5,1,0,0,0,133,135,3,78,39,0,134,133,1,0,
        0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,137,5,7,0,0,137,138,5,38,
        0,0,138,7,1,0,0,0,139,141,3,78,39,0,140,139,1,0,0,0,140,141,1,0,
        0,0,141,142,1,0,0,0,142,143,5,9,0,0,143,144,5,38,0,0,144,9,1,0,0,
        0,145,148,3,12,6,0,146,148,3,14,7,0,147,145,1,0,0,0,147,146,1,0,
        0,0,148,11,1,0,0,0,149,150,5,12,0,0,150,151,5,38,0,0,151,13,1,0,
        0,0,152,153,5,12,0,0,153,158,5,38,0,0,154,155,5,53,0,0,155,157,5,
        38,0,0,156,154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,
        0,0,0,159,161,1,0,0,0,160,158,1,0,0,0,161,162,3,16,8,0,162,15,1,
        0,0,0,163,164,5,13,0,0,164,165,5,38,0,0,165,17,1,0,0,0,166,167,5,
        10,0,0,167,169,5,61,0,0,168,170,3,20,10,0,169,168,1,0,0,0,170,171,
        1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,19,1,0,0,0,173,174,5,
        5,0,0,174,175,5,38,0,0,175,177,3,22,11,0,176,178,3,28,14,0,177,176,
        1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,183,5,48,0,0,180,182,
        3,34,17,0,181,180,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,
        1,0,0,0,184,186,1,0,0,0,185,183,1,0,0,0,186,187,3,30,15,0,187,188,
        5,49,0,0,188,21,1,0,0,0,189,191,5,46,0,0,190,192,3,24,12,0,191,190,
        1,0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,194,5,47,0,0,194,23,
        1,0,0,0,195,200,3,26,13,0,196,197,5,53,0,0,197,199,3,26,13,0,198,
        196,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,
        25,1,0,0,0,202,200,1,0,0,0,203,205,3,78,39,0,204,203,1,0,0,0,204,
        205,1,0,0,0,205,206,1,0,0,0,206,207,5,38,0,0,207,27,1,0,0,0,208,
        209,5,61,0,0,209,210,3,78,39,0,210,29,1,0,0,0,211,212,5,6,0,0,212,
        216,3,92,46,0,213,214,5,6,0,0,214,216,3,72,36,0,215,211,1,0,0,0,
        215,213,1,0,0,0,216,31,1,0,0,0,217,221,5,48,0,0,218,220,3,34,17,
        0,219,218,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,
        0,222,224,1,0,0,0,223,221,1,0,0,0,224,225,5,49,0,0,225,33,1,0,0,
        0,226,244,3,36,18,0,227,244,3,40,20,0,228,244,3,38,19,0,229,244,
        3,82,41,0,230,244,3,84,42,0,231,244,3,42,21,0,232,244,3,44,22,0,
        233,244,3,46,23,0,234,244,3,48,24,0,235,244,3,56,28,0,236,244,3,
        54,27,0,237,244,3,70,35,0,238,244,3,58,29,0,239,244,3,52,26,0,240,
        244,3,60,30,0,241,244,3,64,32,0,242,244,3,62,31,0,243,226,1,0,0,
        0,243,227,1,0,0,0,243,228,1,0,0,0,243,229,1,0,0,0,243,230,1,0,0,
        0,243,231,1,0,0,0,243,232,1,0,0,0,243,233,1,0,0,0,243,234,1,0,0,
        0,243,235,1,0,0,0,243,236,1,0,0,0,243,237,1,0,0,0,243,238,1,0,0,
        0,243,239,1,0,0,0,243,240,1,0,0,0,243,241,1,0,0,0,243,242,1,0,0,
        0,244,35,1,0,0,0,245,246,5,1,0,0,246,247,3,68,34,0,247,250,3,32,
        16,0,248,249,5,2,0,0,249,251,3,32,16,0,250,248,1,0,0,0,250,251,1,
        0,0,0,251,37,1,0,0,0,252,253,5,26,0,0,253,258,3,86,43,0,254,255,
        5,53,0,0,255,257,3,86,43,0,256,254,1,0,0,0,257,260,1,0,0,0,258,256,
        1,0,0,0,258,259,1,0,0,0,259,261,1,0,0,0,260,258,1,0,0,0,261,262,
        5,31,0,0,262,267,3,92,46,0,263,264,5,53,0,0,264,266,3,92,46,0,265,
        263,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,
        270,1,0,0,0,269,267,1,0,0,0,270,271,3,32,16,0,271,39,1,0,0,0,272,
        273,5,4,0,0,273,274,3,68,34,0,274,275,3,32,16,0,275,41,1,0,0,0,276,
        279,5,3,0,0,277,280,5,42,0,0,278,280,3,86,43,0,279,277,1,0,0,0,279,
        278,1,0,0,0,280,281,1,0,0,0,281,282,5,28,0,0,282,283,3,32,16,0,283,
        43,1,0,0,0,284,286,3,50,25,0,285,284,1,0,0,0,285,286,1,0,0,0,286,
        287,1,0,0,0,287,288,5,17,0,0,288,289,3,86,43,0,289,290,5,24,0,0,
        290,293,3,102,51,0,291,292,5,26,0,0,292,294,3,100,50,0,293,291,1,
        0,0,0,293,294,1,0,0,0,294,45,1,0,0,0,295,296,5,18,0,0,296,300,3,
        86,43,0,297,298,5,20,0,0,298,300,3,86,43,0,299,295,1,0,0,0,299,297,
        1,0,0,0,300,47,1,0,0,0,301,303,3,50,25,0,302,301,1,0,0,0,302,303,
        1,0,0,0,303,304,1,0,0,0,304,305,3,82,41,0,305,307,5,15,0,0,306,308,
        3,104,52,0,307,306,1,0,0,0,307,308,1,0,0,0,308,309,1,0,0,0,309,310,
        3,86,43,0,310,312,5,25,0,0,311,313,3,104,52,0,312,311,1,0,0,0,312,
        313,1,0,0,0,313,314,1,0,0,0,314,317,3,86,43,0,315,316,5,26,0,0,316,
        318,3,100,50,0,317,315,1,0,0,0,317,318,1,0,0,0,318,49,1,0,0,0,319,
        320,5,79,0,0,320,321,5,33,0,0,321,322,3,100,50,0,322,51,1,0,0,0,
        323,324,3,82,41,0,324,325,5,14,0,0,325,326,5,38,0,0,326,327,5,29,
        0,0,327,330,3,86,43,0,328,329,5,26,0,0,329,331,3,100,50,0,330,328,
        1,0,0,0,330,331,1,0,0,0,331,53,1,0,0,0,332,333,3,82,41,0,333,334,
        5,16,0,0,334,335,3,86,43,0,335,336,5,27,0,0,336,337,5,42,0,0,337,
        55,1,0,0,0,338,339,3,82,41,0,339,341,5,19,0,0,340,342,3,104,52,0,
        341,340,1,0,0,0,341,342,1,0,0,0,342,343,1,0,0,0,343,344,5,38,0,0,
        344,57,1,0,0,0,345,346,3,82,41,0,346,347,5,21,0,0,347,348,3,86,43,
        0,348,349,5,25,0,0,349,350,3,86,43,0,350,351,5,23,0,0,351,352,5,
        41,0,0,352,353,5,53,0,0,353,354,5,41,0,0,354,355,5,24,0,0,355,356,
        5,41,0,0,356,59,1,0,0,0,357,358,5,22,0,0,358,359,3,86,43,0,359,61,
        1,0,0,0,360,361,3,82,41,0,361,362,3,94,47,0,362,63,1,0,0,0,363,364,
        3,82,41,0,364,365,3,92,46,0,365,366,7,0,0,0,366,367,3,92,46,0,367,
        374,1,0,0,0,368,369,3,82,41,0,369,370,3,92,46,0,370,371,7,1,0,0,
        371,372,3,92,46,0,372,374,1,0,0,0,373,363,1,0,0,0,373,368,1,0,0,
        0,374,65,1,0,0,0,375,383,3,92,46,0,376,377,5,57,0,0,377,384,5,57,
        0,0,378,379,5,56,0,0,379,380,5,56,0,0,380,384,5,56,0,0,381,382,5,
        56,0,0,382,384,5,56,0,0,383,376,1,0,0,0,383,378,1,0,0,0,383,381,
        1,0,0,0,384,385,1,0,0,0,385,386,3,92,46,0,386,396,1,0,0,0,387,388,
        3,92,46,0,388,389,7,2,0,0,389,390,3,92,46,0,390,396,1,0,0,0,391,
        392,3,92,46,0,392,393,7,3,0,0,393,394,3,92,46,0,394,396,1,0,0,0,
        395,375,1,0,0,0,395,387,1,0,0,0,395,391,1,0,0,0,396,67,1,0,0,0,397,
        398,5,46,0,0,398,403,3,66,33,0,399,400,7,4,0,0,400,402,3,66,33,0,
        401,399,1,0,0,0,402,405,1,0,0,0,403,401,1,0,0,0,403,404,1,0,0,0,
        404,406,1,0,0,0,405,403,1,0,0,0,406,407,5,47,0,0,407,69,1,0,0,0,
        408,409,3,82,41,0,409,410,3,72,36,0,410,71,1,0,0,0,411,412,5,38,
        0,0,412,414,5,46,0,0,413,415,3,74,37,0,414,413,1,0,0,0,414,415,1,
        0,0,0,415,416,1,0,0,0,416,417,5,47,0,0,417,73,1,0,0,0,418,426,3,
        92,46,0,419,422,5,53,0,0,420,423,3,92,46,0,421,423,3,72,36,0,422,
        420,1,0,0,0,422,421,1,0,0,0,423,425,1,0,0,0,424,419,1,0,0,0,425,
        428,1,0,0,0,426,424,1,0,0,0,426,427,1,0,0,0,427,431,1,0,0,0,428,
        426,1,0,0,0,429,431,3,72,36,0,430,418,1,0,0,0,430,429,1,0,0,0,431,
        75,1,0,0,0,432,435,3,96,48,0,433,435,3,98,49,0,434,432,1,0,0,0,434,
        433,1,0,0,0,435,77,1,0,0,0,436,437,5,50,0,0,437,438,3,80,40,0,438,
        439,5,51,0,0,439,79,1,0,0,0,440,445,3,76,38,0,441,442,5,52,0,0,442,
        444,3,76,38,0,443,441,1,0,0,0,444,447,1,0,0,0,445,443,1,0,0,0,445,
        446,1,0,0,0,446,81,1,0,0,0,447,445,1,0,0,0,448,450,3,78,39,0,449,
        448,1,0,0,0,449,450,1,0,0,0,450,451,1,0,0,0,451,452,3,86,43,0,452,
        453,5,55,0,0,453,83,1,0,0,0,454,455,3,82,41,0,455,456,5,50,0,0,456,
        461,3,92,46,0,457,458,5,53,0,0,458,460,3,92,46,0,459,457,1,0,0,0,
        460,463,1,0,0,0,461,459,1,0,0,0,461,462,1,0,0,0,462,464,1,0,0,0,
        463,461,1,0,0,0,464,465,5,51,0,0,465,85,1,0,0,0,466,470,5,38,0,0,
        467,468,5,50,0,0,468,469,5,42,0,0,469,471,5,51,0,0,470,467,1,0,0,
        0,470,471,1,0,0,0,471,87,1,0,0,0,472,473,5,38,0,0,473,89,1,0,0,0,
        474,475,5,50,0,0,475,480,3,92,46,0,476,477,5,53,0,0,477,479,3,92,
        46,0,478,476,1,0,0,0,479,482,1,0,0,0,480,478,1,0,0,0,480,481,1,0,
        0,0,481,483,1,0,0,0,482,480,1,0,0,0,483,484,5,51,0,0,484,91,1,0,
        0,0,485,489,3,94,47,0,486,489,3,86,43,0,487,489,3,90,45,0,488,485,
        1,0,0,0,488,486,1,0,0,0,488,487,1,0,0,0,489,93,1,0,0,0,490,491,7,
        5,0,0,491,95,1,0,0,0,492,493,7,6,0,0,493,97,1,0,0,0,494,495,7,7,
        0,0,495,99,1,0,0,0,496,497,5,43,0,0,497,101,1,0,0,0,498,499,5,45,
        0,0,499,103,1,0,0,0,500,501,5,42,0,0,501,502,5,32,0,0,502,503,5,
        30,0,0,503,105,1,0,0,0,45,109,112,119,128,134,140,147,158,171,177,
        183,191,200,204,215,221,243,250,258,267,279,285,293,299,302,307,
        312,317,330,341,373,383,395,403,414,422,426,430,434,445,449,461,
        470,480,488
    ]

class BSParser ( Parser ):

    grammarFileName = "BSParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'repeat'", "'while'", 
                     "'function'", "'return'", "'manifest'", "'module'", 
                     "'stationary'", "'functions'", "'instructions'", "'import'", 
                     "'from'", "'detect'", "'mix'", "'split'", "'heat'", 
                     "'drain'", "'dispense'", "'dispose'", "'gradient'", 
                     "'store'", "'range'", "'at'", "'with'", "'for'", "'into'", 
                     "'times'", "'on'", "'of'", "'in'", "'units'", "'usein'", 
                     "'nat'", "'real'", "'mat'", "'bool'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", "'='", 
                     "'>'", "'<'", "'!'", "'~'", "'?'", "':'", "'=='", "'<='", 
                     "'>='", "'!='", "'&&'", "'||'", "'++'", "'--'", "'+'", 
                     "'-'", "'*'", "'/'", "'&'", "'|'", "'^'", "'%'", "'_'", 
                     "'@'", "'ns'", "'us'", "'ms'", "'cs'", "'ds'", "'s'", 
                     "'m'", "'h'", "'d'", "'w'", "'mo'", "'y'", "'nL'", 
                     "'uL'", "'mL'", "'cL'", "'dL'", "'L'", "'daL'", "'c'", 
                     "'f'", "'k'", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", 
                     "'7'", "'8'", "'9'", "'10'", "'11'", "'12'", "'13'", 
                     "'14'", "'15'", "'16'", "'17'", "'18'", "'19'", "'20'", 
                     "'21'", "'22'", "'23'", "'24'", "'25'", "'26'", "'27'", 
                     "'28'", "'29'", "'30'", "'31'", "'32'", "'33'", "'34'", 
                     "'35'", "'37'", "'38'", "'39'", "'40'", "'42'", "'44'", 
                     "'45'", "'46'", "'47'", "'48'", "'49'", "'50'", "'51'", 
                     "'55'", "'58'", "'59'", "'60'", "'61'", "'62'", "'63'", 
                     "'64'", "'65'", "'66'", "'68'", "'69'", "'70'", "'71'", 
                     "'72'", "'73'", "'74'", "'75'", "'76'", "'98'", "'99'", 
                     "'100'", "'134'", "'-1'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", 
                      "RETURN", "MANIFEST", "MODULE", "STATIONARY", "FUNCTIONS", 
                      "INSTRUCTIONS", "IMPORT", "FROM", "DETECT", "MIX", 
                      "SPLIT", "HEAT", "DRAIN", "DISPENSE", "DISPOSE", "GRADIENT", 
                      "STORE", "RANGE", "AT", "WITH", "FOR", "INTO", "TIMES", 
                      "ON", "OF", "IN", "UNITS", "USEIN", "NAT", "REAL", 
                      "MAT", "BOOL", "IDENTIFIER", "STRING_LITERAL", "BOOL_LITERAL", 
                      "FLOAT_LITERAL", "INTEGER_LITERAL", "TIME_NUMBER", 
                      "VOLUME_NUMBER", "TEMP_NUMBER", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON", 
                      "COMMA", "DOT", "ASSIGN", "GT", "LT", "BANG", "TILDE", 
                      "QUESTION", "COLON", "EQUALITY", "LTE", "GTE", "NOTEQUAL", 
                      "AND", "OR", "INC", "DEC", "ADDITION", "SUBTRACT", 
                      "MULTIPLY", "DIVIDE", "BITAND", "BITOR", "CARET", 
                      "MOD", "UNDERSCORE", "ATSIGN", "NANOSECOND", "MICROSECOND", 
                      "MILLISECOND", "CENTISECOND", "DECISECOND", "SECOND", 
                      "MINUTE", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", 
                      "NANOLITRE", "MICROLITRE", "MILLILITRE", "CENTILITRE", 
                      "DECILITRE", "LITRE", "DECALITRE", "CELSIUS", "FAHRENHEIT", 
                      "KELVIN", "ACIDS_STRONG_NON_OXIDIZING", "ACIDS_STRONG_OXIDIZING", 
                      "ACIDS_CARBOXYLIC", "ALCOHOLS_AND_POLYOLS", "ALDEHYDES", 
                      "AMIDES_AND_IMIDES", "AMINES_PHOSPHINES_AND_PYRIDINES", 
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
    RULE_importStatement = 5
    RULE_importLibrary = 6
    RULE_importFuncFromLibrary = 7
    RULE_fromLibrary = 8
    RULE_functions = 9
    RULE_functionDeclaration = 10
    RULE_formalParameters = 11
    RULE_formalParameterList = 12
    RULE_formalParameter = 13
    RULE_functionTyping = 14
    RULE_returnStatement = 15
    RULE_blockStatement = 16
    RULE_statements = 17
    RULE_ifStatement = 18
    RULE_forInStatement = 19
    RULE_whileStatement = 20
    RULE_repeat = 21
    RULE_heat = 22
    RULE_dispose = 23
    RULE_mix = 24
    RULE_usein = 25
    RULE_detect = 26
    RULE_split = 27
    RULE_dispense = 28
    RULE_gradient = 29
    RULE_store = 30
    RULE_numberAssignment = 31
    RULE_math = 32
    RULE_binops = 33
    RULE_parExpression = 34
    RULE_methodInvocation = 35
    RULE_methodCall = 36
    RULE_expressionList = 37
    RULE_typeType = 38
    RULE_unionType = 39
    RULE_typesList = 40
    RULE_variableDefinition = 41
    RULE_listDefinition = 42
    RULE_variable = 43
    RULE_numericAlias = 44
    RULE_list = 45
    RULE_primary = 46
    RULE_literal = 47
    RULE_primitiveType = 48
    RULE_chemicalType = 49
    RULE_timeIdentifier = 50
    RULE_temperatureIdentifier = 51
    RULE_unitTracker = 52

    ruleNames =  [ "program", "globalDeclarations", "moduleDeclaration", 
                   "manifestDeclaration", "stationaryDeclaration", "importStatement", 
                   "importLibrary", "importFuncFromLibrary", "fromLibrary", 
                   "functions", "functionDeclaration", "formalParameters", 
                   "formalParameterList", "formalParameter", "functionTyping", 
                   "returnStatement", "blockStatement", "statements", "ifStatement", 
                   "forInStatement", "whileStatement", "repeat", "heat", 
                   "dispose", "mix", "usein", "detect", "split", "dispense", 
                   "gradient", "store", "numberAssignment", "math", "binops", 
                   "parExpression", "methodInvocation", "methodCall", "expressionList", 
                   "typeType", "unionType", "typesList", "variableDefinition", 
                   "listDefinition", "variable", "numericAlias", "list", 
                   "primary", "literal", "primitiveType", "chemicalType", 
                   "timeIdentifier", "temperatureIdentifier", "unitTracker" ]

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
    IMPORT=12
    FROM=13
    DETECT=14
    MIX=15
    SPLIT=16
    HEAT=17
    DRAIN=18
    DISPENSE=19
    DISPOSE=20
    GRADIENT=21
    STORE=22
    RANGE=23
    AT=24
    WITH=25
    FOR=26
    INTO=27
    TIMES=28
    ON=29
    OF=30
    IN=31
    UNITS=32
    USEIN=33
    NAT=34
    REAL=35
    MAT=36
    BOOL=37
    IDENTIFIER=38
    STRING_LITERAL=39
    BOOL_LITERAL=40
    FLOAT_LITERAL=41
    INTEGER_LITERAL=42
    TIME_NUMBER=43
    VOLUME_NUMBER=44
    TEMP_NUMBER=45
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
    ATSIGN=79
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
    ACIDS_STRONG_NON_OXIDIZING=102
    ACIDS_STRONG_OXIDIZING=103
    ACIDS_CARBOXYLIC=104
    ALCOHOLS_AND_POLYOLS=105
    ALDEHYDES=106
    AMIDES_AND_IMIDES=107
    AMINES_PHOSPHINES_AND_PYRIDINES=108
    AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS=109
    CARBAMATES=110
    BASES_STRONG=111
    CYANIDES_INORGANIC=112
    THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS=113
    ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS=114
    ETHERS=115
    FLUORIDES_INORGANIC=116
    HYDROCARBONS_AROMATIC=117
    HALOGENATED_ORGANIC_COMPOUNDS=118
    ISOCYANATES_AND_ISOTHIOCYANATES=119
    KETONES=120
    SULFIDES_ORGANIC=121
    METALS_ALKALI_VERY_ACTIVE=122
    METALS_ELEMENTAL_AND_POWDER_ACTIVE=123
    METALS_LESS_REACTIVE=124
    METALS_AND_METAL_COMPOUNDS_TOXIC=125
    DIAZONIUM_SALTS=126
    NITRILES=127
    NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC=128
    HYDROCARBONS_ALIPHATIC_UNSATURATED=129
    HYDROCARBONS_ALIPHATIC_SATURATED=130
    PEROXIDES_ORGANIC=131
    PHENOLS_AND_CRESOLS=132
    SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC=133
    SULFIDES_INORGANIC=134
    EPOXIDES=135
    METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES=136
    ANHYDRIDES=137
    SALTS_ACIDIC=138
    SALTS_BASIC=139
    ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES=140
    ORGANOMETALLICS=141
    OXIDIZING_AGENTS_STRONG=142
    REDUCING_AGENTS_STRONG=143
    NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS=144
    FLUORINATED_ORGANIC_COMPOUNDS=145
    FLUORIDE_SALTS_SOLUBLE=146
    OXIDIZING_AGENTS_WEAK=147
    REDUCING_AGENTS_WEAK=148
    NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES=149
    CHLOROSILANES=150
    SILOXANES=151
    HALOGENATING_AGENTS=152
    ACIDS_WEAK=153
    BASES_WEAK=154
    CARBONATE_SALTS=155
    ALKYNES_WITH_ACETYLENIC_HYDROGEN=156
    ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN=157
    CONJUGATED_DIENES=158
    ARYL_HALIDES=159
    AMINES_AROMATIC=160
    NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC=161
    ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS=162
    ACRYLATES_AND_ACRYLIC_ACIDS=163
    PHENOLIC_SALTS=164
    QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS=165
    SULFITE_AND_THIOSULFATE_SALTS=166
    OXIMES=167
    POLYMERIZABLE_COMPOUNDS=168
    NOT_CHEMICALLY_REACTIVE=169
    INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION=170
    WATER_AND_AQUEOUS_SOLUTIONS=171
    NULL=172
    UNKNOWN=173
    WS=174
    COMMENT=175
    LINE_COMMENT=176

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.globalDeclarations()
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.MANIFEST) | (1 << BSParser.MODULE) | (1 << BSParser.STATIONARY) | (1 << BSParser.IMPORT) | (1 << BSParser.LBRACKET))) != 0)):
                    break

            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FUNCTIONS:
                self.state = 111
                self.functions()


            self.state = 114
            self.match(BSParser.INSTRUCTIONS)
            self.state = 115
            self.match(BSParser.COLON)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.FOR) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN:
                self.state = 116
                self.statements()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(BSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalDeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moduleDeclaration(self):
            return self.getTypedRuleContext(BSParser.ModuleDeclarationContext,0)


        def manifestDeclaration(self):
            return self.getTypedRuleContext(BSParser.ManifestDeclarationContext,0)


        def stationaryDeclaration(self):
            return self.getTypedRuleContext(BSParser.StationaryDeclarationContext,0)


        def importStatement(self):
            return self.getTypedRuleContext(BSParser.ImportStatementContext,0)


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
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.moduleDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.manifestDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.stationaryDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.importStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModuleDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 130
            self.match(BSParser.MODULE)
            self.state = 131
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManifestDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 133
                self.unionType()


            self.state = 136
            self.match(BSParser.MANIFEST)
            self.state = 137
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StationaryDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 139
                self.unionType()


            self.state = 142
            self.match(BSParser.STATIONARY)
            self.state = 143
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def importLibrary(self):
            return self.getTypedRuleContext(BSParser.ImportLibraryContext,0)


        def importFuncFromLibrary(self):
            return self.getTypedRuleContext(BSParser.ImportFuncFromLibraryContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_importStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStatement" ):
                listener.enterImportStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStatement" ):
                listener.exitImportStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStatement" ):
                return visitor.visitImportStatement(self)
            else:
                return visitor.visitChildren(self)




    def importStatement(self):

        localctx = BSParser.ImportStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_importStatement)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.importLibrary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.importFuncFromLibrary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportLibraryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(BSParser.IMPORT, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_importLibrary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportLibrary" ):
                listener.enterImportLibrary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportLibrary" ):
                listener.exitImportLibrary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportLibrary" ):
                return visitor.visitImportLibrary(self)
            else:
                return visitor.visitChildren(self)




    def importLibrary(self):

        localctx = BSParser.ImportLibraryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_importLibrary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(BSParser.IMPORT)
            self.state = 150
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportFuncFromLibraryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(BSParser.IMPORT, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.IDENTIFIER)
            else:
                return self.getToken(BSParser.IDENTIFIER, i)

        def fromLibrary(self):
            return self.getTypedRuleContext(BSParser.FromLibraryContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.COMMA)
            else:
                return self.getToken(BSParser.COMMA, i)

        def getRuleIndex(self):
            return BSParser.RULE_importFuncFromLibrary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportFuncFromLibrary" ):
                listener.enterImportFuncFromLibrary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportFuncFromLibrary" ):
                listener.exitImportFuncFromLibrary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportFuncFromLibrary" ):
                return visitor.visitImportFuncFromLibrary(self)
            else:
                return visitor.visitChildren(self)




    def importFuncFromLibrary(self):

        localctx = BSParser.ImportFuncFromLibraryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_importFuncFromLibrary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(BSParser.IMPORT)
            self.state = 153
            self.match(BSParser.IDENTIFIER)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 154
                self.match(BSParser.COMMA)
                self.state = 155
                self.match(BSParser.IDENTIFIER)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self.fromLibrary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FromLibraryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(BSParser.FROM, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_fromLibrary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromLibrary" ):
                listener.enterFromLibrary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromLibrary" ):
                listener.exitFromLibrary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFromLibrary" ):
                return visitor.visitFromLibrary(self)
            else:
                return visitor.visitChildren(self)




    def fromLibrary(self):

        localctx = BSParser.FromLibraryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fromLibrary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(BSParser.FROM)
            self.state = 164
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 18, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(BSParser.FUNCTIONS)
            self.state = 167
            self.match(BSParser.COLON)
            self.state = 169 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 168
                self.functionDeclaration()
                self.state = 171 
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 20, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(BSParser.FUNCTION)
            self.state = 174
            self.match(BSParser.IDENTIFIER)
            self.state = 175
            self.formalParameters()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.COLON:
                self.state = 176
                self.functionTyping()


            self.state = 179
            self.match(BSParser.LBRACE)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.FOR) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN:
                self.state = 180
                self.statements()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
            self.returnStatement()
            self.state = 187
            self.match(BSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParametersContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 22, self.RULE_formalParameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(BSParser.LPAREN)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.IDENTIFIER or _la==BSParser.LBRACKET:
                self.state = 190
                self.formalParameterList()


            self.state = 193
            self.match(BSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 24, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.formalParameter()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 196
                self.match(BSParser.COMMA)
                self.state = 197
                self.formalParameter()
                self.state = 202
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 26, self.RULE_formalParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 203
                self.unionType()


            self.state = 206
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionTypingContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 28, self.RULE_functionTyping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(BSParser.COLON)
            self.state = 209
            self.unionType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 30, self.RULE_returnStatement)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(BSParser.RETURN)
                self.state = 212
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(BSParser.RETURN)
                self.state = 214
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 32, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(BSParser.LBRACE)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.FOR) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN:
                self.state = 218
                self.statements()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 224
            self.match(BSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(BSParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(BSParser.WhileStatementContext,0)


        def forInStatement(self):
            return self.getTypedRuleContext(BSParser.ForInStatementContext,0)


        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def listDefinition(self):
            return self.getTypedRuleContext(BSParser.ListDefinitionContext,0)


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
        self.enterRule(localctx, 34, self.RULE_statements)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.forInStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 229
                self.variableDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 230
                self.listDefinition()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 231
                self.repeat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 232
                self.heat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 233
                self.dispose()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 234
                self.mix()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 235
                self.dispense()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 236
                self.split()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 237
                self.methodInvocation()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 238
                self.gradient()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 239
                self.detect()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 240
                self.store()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 241
                self.math()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 242
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 36, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(BSParser.IF)
            self.state = 246
            self.parExpression()
            self.state = 247
            self.blockStatement()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ELSE:
                self.state = 248
                self.match(BSParser.ELSE)
                self.state = 249
                self.blockStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BSParser.FOR, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.VariableContext)
            else:
                return self.getTypedRuleContext(BSParser.VariableContext,i)


        def IN(self):
            return self.getToken(BSParser.IN, 0)

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BSParser.PrimaryContext,i)


        def blockStatement(self):
            return self.getTypedRuleContext(BSParser.BlockStatementContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.COMMA)
            else:
                return self.getToken(BSParser.COMMA, i)

        def getRuleIndex(self):
            return BSParser.RULE_forInStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInStatement" ):
                listener.enterForInStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInStatement" ):
                listener.exitForInStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInStatement" ):
                return visitor.visitForInStatement(self)
            else:
                return visitor.visitChildren(self)




    def forInStatement(self):

        localctx = BSParser.ForInStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_forInStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(BSParser.FOR)
            self.state = 253
            self.variable()
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 254
                self.match(BSParser.COMMA)
                self.state = 255
                self.variable()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 261
            self.match(BSParser.IN)
            self.state = 262
            self.primary()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 263
                self.match(BSParser.COMMA)
                self.state = 264
                self.primary()
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 270
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 40, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(BSParser.WHILE)
            self.state = 273
            self.parExpression()
            self.state = 274
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT(self):
            return self.getToken(BSParser.REPEAT, 0)

        def TIMES(self):
            return self.getToken(BSParser.TIMES, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(BSParser.BlockStatementContext,0)


        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


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
        self.enterRule(localctx, 42, self.RULE_repeat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(BSParser.REPEAT)
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.INTEGER_LITERAL]:
                self.state = 277
                self.match(BSParser.INTEGER_LITERAL)
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.state = 278
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 281
            self.match(BSParser.TIMES)
            self.state = 282
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeatContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 44, self.RULE_heat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ATSIGN:
                self.state = 284
                self.usein()


            self.state = 287
            self.match(BSParser.HEAT)
            self.state = 288
            self.variable()
            self.state = 289
            self.match(BSParser.AT)
            self.state = 290
            self.temperatureIdentifier()
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 291
                self.match(BSParser.FOR)
                self.state = 292
                self.timeIdentifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisposeContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 46, self.RULE_dispose)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.DRAIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(BSParser.DRAIN)
                self.state = 296
                self.variable()
                pass
            elif token in [BSParser.DISPOSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(BSParser.DISPOSE)
                self.state = 298
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 48, self.RULE_mix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ATSIGN:
                self.state = 301
                self.usein()


            self.state = 304
            self.variableDefinition()
            self.state = 305
            self.match(BSParser.MIX)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 306
                self.unitTracker()


            self.state = 309
            self.variable()
            self.state = 310
            self.match(BSParser.WITH)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 311
                self.unitTracker()


            self.state = 314
            self.variable()
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 315
                self.match(BSParser.FOR)
                self.state = 316
                self.timeIdentifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseinContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 50, self.RULE_usein)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(BSParser.ATSIGN)
            self.state = 320
            self.match(BSParser.USEIN)
            self.state = 321
            self.timeIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DetectContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 52, self.RULE_detect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.variableDefinition()
            self.state = 324
            self.match(BSParser.DETECT)
            self.state = 325
            self.match(BSParser.IDENTIFIER)
            self.state = 326
            self.match(BSParser.ON)
            self.state = 327
            self.variable()
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 328
                self.match(BSParser.FOR)
                self.state = 329
                self.timeIdentifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SplitContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 54, self.RULE_split)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.variableDefinition()
            self.state = 333
            self.match(BSParser.SPLIT)
            self.state = 334
            self.variable()
            self.state = 335
            self.match(BSParser.INTO)
            self.state = 336
            self.match(BSParser.INTEGER_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DispenseContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 56, self.RULE_dispense)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.variableDefinition()
            self.state = 339
            self.match(BSParser.DISPENSE)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 340
                self.unitTracker()


            self.state = 343
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GradientContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 58, self.RULE_gradient)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.variableDefinition()
            self.state = 346
            self.match(BSParser.GRADIENT)
            self.state = 347
            self.variable()
            self.state = 348
            self.match(BSParser.WITH)
            self.state = 349
            self.variable()
            self.state = 350
            self.match(BSParser.RANGE)
            self.state = 351
            self.match(BSParser.FLOAT_LITERAL)
            self.state = 352
            self.match(BSParser.COMMA)
            self.state = 353
            self.match(BSParser.FLOAT_LITERAL)
            self.state = 354
            self.match(BSParser.AT)
            self.state = 355
            self.match(BSParser.FLOAT_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 60, self.RULE_store)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(BSParser.STORE)
            self.state = 358
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 62, self.RULE_numberAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.variableDefinition()
            self.state = 361
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 64, self.RULE_math)
        self._la = 0 # Token type
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.variableDefinition()
                self.state = 364
                self.primary()
                self.state = 365
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & ((1 << (BSParser.MULTIPLY - 72)) | (1 << (BSParser.DIVIDE - 72)) | (1 << (BSParser.MOD - 72)))) != 0)):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 366
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.variableDefinition()
                self.state = 369
                self.primary()
                self.state = 370
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BSParser.ADDITION or _la==BSParser.SUBTRACT):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 371
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 66, self.RULE_binops)
        self._la = 0 # Token type
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.primary()
                self.state = 383
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 376
                    self.match(BSParser.LT)
                    self.state = 377
                    self.match(BSParser.LT)
                    pass

                elif la_ == 2:
                    self.state = 378
                    self.match(BSParser.GT)
                    self.state = 379
                    self.match(BSParser.GT)
                    self.state = 380
                    self.match(BSParser.GT)
                    pass

                elif la_ == 3:
                    self.state = 381
                    self.match(BSParser.GT)
                    self.state = 382
                    self.match(BSParser.GT)
                    pass


                self.state = 385
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.primary()
                self.state = 388
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 56)) & ~0x3f) == 0 and ((1 << (_la - 56)) & ((1 << (BSParser.GT - 56)) | (1 << (BSParser.LT - 56)) | (1 << (BSParser.LTE - 56)) | (1 << (BSParser.GTE - 56)))) != 0)):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 389
                self.primary()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 391
                self.primary()
                self.state = 392
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BSParser.EQUALITY or _la==BSParser.NOTEQUAL):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 393
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 68, self.RULE_parExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(BSParser.LPAREN)
            self.state = 398
            self.binops()
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.AND or _la==BSParser.OR:
                self.state = 399
                _la = self._input.LA(1)
                if not(_la==BSParser.AND or _la==BSParser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 400
                self.binops()
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 406
            self.match(BSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvocationContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 70, self.RULE_methodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.variableDefinition()
            self.state = 409
            self.methodCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 72, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(BSParser.IDENTIFIER)
            self.state = 412
            self.match(BSParser.LPAREN)
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IDENTIFIER) | (1 << BSParser.STRING_LITERAL) | (1 << BSParser.BOOL_LITERAL) | (1 << BSParser.FLOAT_LITERAL) | (1 << BSParser.INTEGER_LITERAL) | (1 << BSParser.LBRACKET))) != 0):
                self.state = 413
                self.expressionList()


            self.state = 416
            self.match(BSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def methodCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.MethodCallContext)
            else:
                return self.getTypedRuleContext(BSParser.MethodCallContext,i)


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
        self.enterRule(localctx, 74, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.primary()
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BSParser.COMMA:
                    self.state = 419
                    self.match(BSParser.COMMA)
                    self.state = 422
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 420
                        self.primary()
                        pass

                    elif la_ == 2:
                        self.state = 421
                        self.methodCall()
                        pass


                    self.state = 428
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.methodCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeTypeContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 76, self.RULE_typeType)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.NAT, BSParser.REAL, BSParser.MAT, BSParser.BOOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.primitiveType()
                pass
            elif token in [BSParser.INTEGER_LITERAL, BSParser.ACIDS_STRONG_NON_OXIDIZING, BSParser.ACIDS_STRONG_OXIDIZING, BSParser.ACIDS_CARBOXYLIC, BSParser.ALCOHOLS_AND_POLYOLS, BSParser.ALDEHYDES, BSParser.AMIDES_AND_IMIDES, BSParser.AMINES_PHOSPHINES_AND_PYRIDINES, BSParser.AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS, BSParser.CARBAMATES, BSParser.BASES_STRONG, BSParser.CYANIDES_INORGANIC, BSParser.THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS, BSParser.ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS, BSParser.ETHERS, BSParser.FLUORIDES_INORGANIC, BSParser.HYDROCARBONS_AROMATIC, BSParser.HALOGENATED_ORGANIC_COMPOUNDS, BSParser.ISOCYANATES_AND_ISOTHIOCYANATES, BSParser.KETONES, BSParser.SULFIDES_ORGANIC, BSParser.METALS_ALKALI_VERY_ACTIVE, BSParser.METALS_ELEMENTAL_AND_POWDER_ACTIVE, BSParser.METALS_LESS_REACTIVE, BSParser.METALS_AND_METAL_COMPOUNDS_TOXIC, BSParser.DIAZONIUM_SALTS, BSParser.NITRILES, BSParser.NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC, BSParser.HYDROCARBONS_ALIPHATIC_UNSATURATED, BSParser.HYDROCARBONS_ALIPHATIC_SATURATED, BSParser.PEROXIDES_ORGANIC, BSParser.PHENOLS_AND_CRESOLS, BSParser.SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC, BSParser.SULFIDES_INORGANIC, BSParser.EPOXIDES, BSParser.METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES, BSParser.ANHYDRIDES, BSParser.SALTS_ACIDIC, BSParser.SALTS_BASIC, BSParser.ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES, BSParser.ORGANOMETALLICS, BSParser.OXIDIZING_AGENTS_STRONG, BSParser.REDUCING_AGENTS_STRONG, BSParser.NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS, BSParser.FLUORINATED_ORGANIC_COMPOUNDS, BSParser.FLUORIDE_SALTS_SOLUBLE, BSParser.OXIDIZING_AGENTS_WEAK, BSParser.REDUCING_AGENTS_WEAK, BSParser.NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES, BSParser.CHLOROSILANES, BSParser.SILOXANES, BSParser.HALOGENATING_AGENTS, BSParser.ACIDS_WEAK, BSParser.BASES_WEAK, BSParser.CARBONATE_SALTS, BSParser.ALKYNES_WITH_ACETYLENIC_HYDROGEN, BSParser.ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN, BSParser.CONJUGATED_DIENES, BSParser.ARYL_HALIDES, BSParser.AMINES_AROMATIC, BSParser.NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC, BSParser.ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS, BSParser.ACRYLATES_AND_ACRYLIC_ACIDS, BSParser.PHENOLIC_SALTS, BSParser.QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS, BSParser.SULFITE_AND_THIOSULFATE_SALTS, BSParser.OXIMES, BSParser.POLYMERIZABLE_COMPOUNDS, BSParser.NOT_CHEMICALLY_REACTIVE, BSParser.INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION, BSParser.WATER_AND_AQUEOUS_SOLUTIONS, BSParser.NULL, BSParser.UNKNOWN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 78, self.RULE_unionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(BSParser.LBRACKET)
            self.state = 437
            self.typesList()
            self.state = 438
            self.match(BSParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesListContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 80, self.RULE_typesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.typeType()
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.SEMICOLON:
                self.state = 441
                self.match(BSParser.SEMICOLON)
                self.state = 442
                self.typeType()
                self.state = 447
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 82, self.RULE_variableDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 448
                self.unionType()


            self.state = 451
            self.variable()
            self.state = 452
            self.match(BSParser.ASSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BSParser.PrimaryContext,i)


        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.COMMA)
            else:
                return self.getToken(BSParser.COMMA, i)

        def getRuleIndex(self):
            return BSParser.RULE_listDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListDefinition" ):
                listener.enterListDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListDefinition" ):
                listener.exitListDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListDefinition" ):
                return visitor.visitListDefinition(self)
            else:
                return visitor.visitChildren(self)




    def listDefinition(self):

        localctx = BSParser.ListDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_listDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.variableDefinition()
            self.state = 455
            self.match(BSParser.LBRACKET)
            self.state = 456
            self.primary()
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 457
                self.match(BSParser.COMMA)
                self.state = 458
                self.primary()
                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 464
            self.match(BSParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 86, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(BSParser.IDENTIFIER)
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 467
                self.match(BSParser.LBRACKET)
                self.state = 468
                self.match(BSParser.INTEGER_LITERAL)
                self.state = 469
                self.match(BSParser.RBRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericAliasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_numericAlias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericAlias" ):
                listener.enterNumericAlias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericAlias" ):
                listener.exitNumericAlias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericAlias" ):
                return visitor.visitNumericAlias(self)
            else:
                return visitor.visitChildren(self)




    def numericAlias(self):

        localctx = BSParser.NumericAliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_numericAlias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BSParser.PrimaryContext,i)


        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.COMMA)
            else:
                return self.getToken(BSParser.COMMA, i)

        def getRuleIndex(self):
            return BSParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = BSParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(BSParser.LBRACKET)
            self.state = 475
            self.primary()
            self.state = 480
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 476
                self.match(BSParser.COMMA)
                self.state = 477
                self.primary()
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 483
            self.match(BSParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BSParser.LiteralContext,0)


        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


        def list_(self):
            return self.getTypedRuleContext(BSParser.ListContext,0)


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
        self.enterRule(localctx, 92, self.RULE_primary)
        try:
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.STRING_LITERAL, BSParser.BOOL_LITERAL, BSParser.FLOAT_LITERAL, BSParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.literal()
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 486
                self.variable()
                pass
            elif token in [BSParser.LBRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 487
                self.list_()
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 94, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 96, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 98, self.RULE_chemicalType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            _la = self._input.LA(1)
            if not(_la==BSParser.INTEGER_LITERAL or ((((_la - 102)) & ~0x3f) == 0 and ((1 << (_la - 102)) & ((1 << (BSParser.ACIDS_STRONG_NON_OXIDIZING - 102)) | (1 << (BSParser.ACIDS_STRONG_OXIDIZING - 102)) | (1 << (BSParser.ACIDS_CARBOXYLIC - 102)) | (1 << (BSParser.ALCOHOLS_AND_POLYOLS - 102)) | (1 << (BSParser.ALDEHYDES - 102)) | (1 << (BSParser.AMIDES_AND_IMIDES - 102)) | (1 << (BSParser.AMINES_PHOSPHINES_AND_PYRIDINES - 102)) | (1 << (BSParser.AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS - 102)) | (1 << (BSParser.CARBAMATES - 102)) | (1 << (BSParser.BASES_STRONG - 102)) | (1 << (BSParser.CYANIDES_INORGANIC - 102)) | (1 << (BSParser.THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS - 102)) | (1 << (BSParser.ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS - 102)) | (1 << (BSParser.ETHERS - 102)) | (1 << (BSParser.FLUORIDES_INORGANIC - 102)) | (1 << (BSParser.HYDROCARBONS_AROMATIC - 102)) | (1 << (BSParser.HALOGENATED_ORGANIC_COMPOUNDS - 102)) | (1 << (BSParser.ISOCYANATES_AND_ISOTHIOCYANATES - 102)) | (1 << (BSParser.KETONES - 102)) | (1 << (BSParser.SULFIDES_ORGANIC - 102)) | (1 << (BSParser.METALS_ALKALI_VERY_ACTIVE - 102)) | (1 << (BSParser.METALS_ELEMENTAL_AND_POWDER_ACTIVE - 102)) | (1 << (BSParser.METALS_LESS_REACTIVE - 102)) | (1 << (BSParser.METALS_AND_METAL_COMPOUNDS_TOXIC - 102)) | (1 << (BSParser.DIAZONIUM_SALTS - 102)) | (1 << (BSParser.NITRILES - 102)) | (1 << (BSParser.NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC - 102)) | (1 << (BSParser.HYDROCARBONS_ALIPHATIC_UNSATURATED - 102)) | (1 << (BSParser.HYDROCARBONS_ALIPHATIC_SATURATED - 102)) | (1 << (BSParser.PEROXIDES_ORGANIC - 102)) | (1 << (BSParser.PHENOLS_AND_CRESOLS - 102)) | (1 << (BSParser.SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC - 102)) | (1 << (BSParser.SULFIDES_INORGANIC - 102)) | (1 << (BSParser.EPOXIDES - 102)) | (1 << (BSParser.METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES - 102)) | (1 << (BSParser.ANHYDRIDES - 102)) | (1 << (BSParser.SALTS_ACIDIC - 102)) | (1 << (BSParser.SALTS_BASIC - 102)) | (1 << (BSParser.ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES - 102)) | (1 << (BSParser.ORGANOMETALLICS - 102)) | (1 << (BSParser.OXIDIZING_AGENTS_STRONG - 102)) | (1 << (BSParser.REDUCING_AGENTS_STRONG - 102)) | (1 << (BSParser.NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS - 102)) | (1 << (BSParser.FLUORINATED_ORGANIC_COMPOUNDS - 102)) | (1 << (BSParser.FLUORIDE_SALTS_SOLUBLE - 102)) | (1 << (BSParser.OXIDIZING_AGENTS_WEAK - 102)) | (1 << (BSParser.REDUCING_AGENTS_WEAK - 102)) | (1 << (BSParser.NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES - 102)) | (1 << (BSParser.CHLOROSILANES - 102)) | (1 << (BSParser.SILOXANES - 102)) | (1 << (BSParser.HALOGENATING_AGENTS - 102)) | (1 << (BSParser.ACIDS_WEAK - 102)) | (1 << (BSParser.BASES_WEAK - 102)) | (1 << (BSParser.CARBONATE_SALTS - 102)) | (1 << (BSParser.ALKYNES_WITH_ACETYLENIC_HYDROGEN - 102)) | (1 << (BSParser.ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN - 102)) | (1 << (BSParser.CONJUGATED_DIENES - 102)) | (1 << (BSParser.ARYL_HALIDES - 102)) | (1 << (BSParser.AMINES_AROMATIC - 102)) | (1 << (BSParser.NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC - 102)) | (1 << (BSParser.ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS - 102)) | (1 << (BSParser.ACRYLATES_AND_ACRYLIC_ACIDS - 102)) | (1 << (BSParser.PHENOLIC_SALTS - 102)) | (1 << (BSParser.QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS - 102)))) != 0) or ((((_la - 166)) & ~0x3f) == 0 and ((1 << (_la - 166)) & ((1 << (BSParser.SULFITE_AND_THIOSULFATE_SALTS - 166)) | (1 << (BSParser.OXIMES - 166)) | (1 << (BSParser.POLYMERIZABLE_COMPOUNDS - 166)) | (1 << (BSParser.NOT_CHEMICALLY_REACTIVE - 166)) | (1 << (BSParser.INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION - 166)) | (1 << (BSParser.WATER_AND_AQUEOUS_SOLUTIONS - 166)) | (1 << (BSParser.NULL - 166)) | (1 << (BSParser.UNKNOWN - 166)))) != 0)):
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
        __slots__ = 'parser'

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
        self.enterRule(localctx, 100, self.RULE_timeIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(BSParser.TIME_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemperatureIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 102, self.RULE_temperatureIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(BSParser.TEMP_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitTrackerContext(ParserRuleContext):
        __slots__ = 'parser'

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
        self.enterRule(localctx, 104, self.RULE_unitTracker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(BSParser.INTEGER_LITERAL)
            self.state = 501
            self.match(BSParser.UNITS)
            self.state = 502
            self.match(BSParser.OF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





