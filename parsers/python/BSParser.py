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
        4,1,178,568,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,
        46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,
        52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,
        59,7,59,2,60,7,60,1,0,4,0,124,8,0,11,0,12,0,125,1,0,3,0,129,8,0,
        1,0,1,0,1,0,5,0,134,8,0,10,0,12,0,137,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,3,1,145,8,1,1,2,1,2,1,2,1,3,3,3,151,8,3,1,3,1,3,1,3,1,4,3,4,157,
        8,4,1,4,1,4,1,4,1,5,1,5,3,5,164,8,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,
        5,7,173,8,7,10,7,12,7,176,9,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,4,
        9,186,8,9,11,9,12,9,187,1,10,1,10,1,10,1,10,3,10,194,8,10,1,10,1,
        10,5,10,198,8,10,10,10,12,10,201,9,10,1,10,3,10,204,8,10,1,10,1,
        10,1,11,1,11,3,11,210,8,11,1,11,1,11,1,12,1,12,1,12,5,12,217,8,12,
        10,12,12,12,220,9,12,1,13,3,13,223,8,13,1,13,1,13,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,3,15,234,8,15,1,16,1,16,5,16,238,8,16,10,16,
        12,16,241,9,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,263,8,17,
        1,18,1,18,1,18,1,18,1,18,3,18,270,8,18,1,19,1,19,1,19,1,19,1,20,
        1,20,1,20,1,21,1,21,1,21,3,21,282,8,21,1,21,1,21,1,21,1,22,3,22,
        288,8,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,296,8,22,1,23,1,23,1,
        23,1,23,5,23,302,8,23,10,23,12,23,305,9,23,1,23,1,23,1,23,1,23,5,
        23,311,8,23,10,23,12,23,314,9,23,1,23,1,23,1,24,1,24,1,24,1,24,3,
        24,322,8,24,1,25,3,25,325,8,25,1,25,1,25,1,25,3,25,330,8,25,1,25,
        1,25,1,25,3,25,335,8,25,1,25,1,25,1,25,3,25,340,8,25,1,26,1,26,1,
        26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,352,8,27,1,28,1,28,1,
        28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,
        31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,3,34,385,8,34,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,
        36,1,36,3,36,396,8,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,
        37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,
        40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,428,8,40,1,41,1,
        41,1,41,1,41,1,41,1,41,1,41,1,41,3,41,438,8,41,1,41,1,41,1,41,1,
        41,1,41,1,41,1,41,1,41,1,41,1,41,3,41,450,8,41,1,42,1,42,1,42,1,
        42,5,42,456,8,42,10,42,12,42,459,9,42,1,42,1,42,1,43,1,43,1,43,1,
        44,1,44,1,44,3,44,469,8,44,1,44,1,44,1,45,1,45,1,45,1,45,3,45,477,
        8,45,5,45,479,8,45,10,45,12,45,482,9,45,1,45,3,45,485,8,45,1,46,
        1,46,3,46,489,8,46,1,47,1,47,1,47,1,47,1,48,1,48,1,48,5,48,498,8,
        48,10,48,12,48,501,9,48,1,49,3,49,504,8,49,1,49,1,49,1,49,1,50,1,
        50,1,50,1,50,1,50,5,50,514,8,50,10,50,12,50,517,9,50,1,50,1,50,1,
        51,1,51,1,51,1,51,3,51,525,8,51,1,52,1,52,1,53,1,53,1,53,1,53,5,
        53,533,8,53,10,53,12,53,536,9,53,1,53,1,53,1,54,1,54,1,54,1,54,3,
        54,544,8,54,1,55,1,55,1,56,1,56,1,57,1,57,1,58,1,58,1,58,1,58,3,
        58,556,8,58,1,59,1,59,1,59,1,59,3,59,562,8,59,1,60,1,60,1,60,1,60,
        1,60,0,0,61,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,
        82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,
        120,0,10,2,0,73,74,78,78,1,0,71,72,2,0,57,58,64,65,2,0,63,63,66,
        66,1,0,67,68,1,0,40,43,1,0,36,39,2,0,43,43,104,175,1,0,86,89,1,0,
        100,102,581,0,123,1,0,0,0,2,144,1,0,0,0,4,146,1,0,0,0,6,150,1,0,
        0,0,8,156,1,0,0,0,10,163,1,0,0,0,12,165,1,0,0,0,14,168,1,0,0,0,16,
        179,1,0,0,0,18,182,1,0,0,0,20,189,1,0,0,0,22,207,1,0,0,0,24,213,
        1,0,0,0,26,222,1,0,0,0,28,226,1,0,0,0,30,233,1,0,0,0,32,235,1,0,
        0,0,34,262,1,0,0,0,36,264,1,0,0,0,38,271,1,0,0,0,40,275,1,0,0,0,
        42,278,1,0,0,0,44,287,1,0,0,0,46,297,1,0,0,0,48,321,1,0,0,0,50,324,
        1,0,0,0,52,341,1,0,0,0,54,351,1,0,0,0,56,353,1,0,0,0,58,357,1,0,
        0,0,60,361,1,0,0,0,62,365,1,0,0,0,64,369,1,0,0,0,66,373,1,0,0,0,
        68,377,1,0,0,0,70,386,1,0,0,0,72,392,1,0,0,0,74,399,1,0,0,0,76,411,
        1,0,0,0,78,414,1,0,0,0,80,427,1,0,0,0,82,449,1,0,0,0,84,451,1,0,
        0,0,86,462,1,0,0,0,88,465,1,0,0,0,90,484,1,0,0,0,92,488,1,0,0,0,
        94,490,1,0,0,0,96,494,1,0,0,0,98,503,1,0,0,0,100,508,1,0,0,0,102,
        520,1,0,0,0,104,526,1,0,0,0,106,528,1,0,0,0,108,543,1,0,0,0,110,
        545,1,0,0,0,112,547,1,0,0,0,114,549,1,0,0,0,116,555,1,0,0,0,118,
        561,1,0,0,0,120,563,1,0,0,0,122,124,3,2,1,0,123,122,1,0,0,0,124,
        125,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,
        129,3,18,9,0,128,127,1,0,0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,
        131,5,11,0,0,131,135,5,62,0,0,132,134,3,34,17,0,133,132,1,0,0,0,
        134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,
        137,135,1,0,0,0,138,139,5,0,0,1,139,1,1,0,0,0,140,145,3,4,2,0,141,
        145,3,6,3,0,142,145,3,8,4,0,143,145,3,10,5,0,144,140,1,0,0,0,144,
        141,1,0,0,0,144,142,1,0,0,0,144,143,1,0,0,0,145,3,1,0,0,0,146,147,
        5,8,0,0,147,148,5,103,0,0,148,5,1,0,0,0,149,151,3,94,47,0,150,149,
        1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,153,5,7,0,0,153,154,
        5,103,0,0,154,7,1,0,0,0,155,157,3,94,47,0,156,155,1,0,0,0,156,157,
        1,0,0,0,157,158,1,0,0,0,158,159,5,9,0,0,159,160,5,103,0,0,160,9,
        1,0,0,0,161,164,3,12,6,0,162,164,3,14,7,0,163,161,1,0,0,0,163,162,
        1,0,0,0,164,11,1,0,0,0,165,166,5,12,0,0,166,167,5,103,0,0,167,13,
        1,0,0,0,168,169,5,12,0,0,169,174,5,103,0,0,170,171,5,54,0,0,171,
        173,5,103,0,0,172,170,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,
        175,1,0,0,0,175,177,1,0,0,0,176,174,1,0,0,0,177,178,3,16,8,0,178,
        15,1,0,0,0,179,180,5,13,0,0,180,181,5,103,0,0,181,17,1,0,0,0,182,
        183,5,10,0,0,183,185,5,62,0,0,184,186,3,20,10,0,185,184,1,0,0,0,
        186,187,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,19,1,0,0,0,189,
        190,5,5,0,0,190,191,5,103,0,0,191,193,3,22,11,0,192,194,3,28,14,
        0,193,192,1,0,0,0,193,194,1,0,0,0,194,195,1,0,0,0,195,199,5,49,0,
        0,196,198,3,34,17,0,197,196,1,0,0,0,198,201,1,0,0,0,199,197,1,0,
        0,0,199,200,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,202,204,3,30,
        15,0,203,202,1,0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,206,5,50,
        0,0,206,21,1,0,0,0,207,209,5,47,0,0,208,210,3,24,12,0,209,208,1,
        0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,212,5,48,0,0,212,23,1,
        0,0,0,213,218,3,26,13,0,214,215,5,54,0,0,215,217,3,26,13,0,216,214,
        1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,25,1,
        0,0,0,220,218,1,0,0,0,221,223,3,94,47,0,222,221,1,0,0,0,222,223,
        1,0,0,0,223,224,1,0,0,0,224,225,5,103,0,0,225,27,1,0,0,0,226,227,
        5,62,0,0,227,228,3,94,47,0,228,29,1,0,0,0,229,230,5,6,0,0,230,234,
        3,108,54,0,231,232,5,6,0,0,232,234,3,88,44,0,233,229,1,0,0,0,233,
        231,1,0,0,0,234,31,1,0,0,0,235,239,5,49,0,0,236,238,3,34,17,0,237,
        236,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,
        242,1,0,0,0,241,239,1,0,0,0,242,243,5,50,0,0,243,33,1,0,0,0,244,
        263,3,36,18,0,245,263,3,38,19,0,246,263,3,46,23,0,247,263,3,98,49,
        0,248,263,3,100,50,0,249,263,3,42,21,0,250,263,3,44,22,0,251,263,
        3,48,24,0,252,263,3,50,25,0,253,263,3,72,36,0,254,263,3,70,35,0,
        255,263,3,86,43,0,256,263,3,74,37,0,257,263,3,68,34,0,258,263,3,
        76,38,0,259,263,3,80,40,0,260,263,3,78,39,0,261,263,3,40,20,0,262,
        244,1,0,0,0,262,245,1,0,0,0,262,246,1,0,0,0,262,247,1,0,0,0,262,
        248,1,0,0,0,262,249,1,0,0,0,262,250,1,0,0,0,262,251,1,0,0,0,262,
        252,1,0,0,0,262,253,1,0,0,0,262,254,1,0,0,0,262,255,1,0,0,0,262,
        256,1,0,0,0,262,257,1,0,0,0,262,258,1,0,0,0,262,259,1,0,0,0,262,
        260,1,0,0,0,262,261,1,0,0,0,263,35,1,0,0,0,264,265,5,1,0,0,265,266,
        3,84,42,0,266,269,3,32,16,0,267,268,5,2,0,0,268,270,3,32,16,0,269,
        267,1,0,0,0,269,270,1,0,0,0,270,37,1,0,0,0,271,272,5,4,0,0,272,273,
        3,84,42,0,273,274,3,32,16,0,274,39,1,0,0,0,275,276,3,98,49,0,276,
        277,3,102,51,0,277,41,1,0,0,0,278,281,5,3,0,0,279,282,5,43,0,0,280,
        282,3,102,51,0,281,279,1,0,0,0,281,280,1,0,0,0,282,283,1,0,0,0,283,
        284,5,28,0,0,284,285,3,32,16,0,285,43,1,0,0,0,286,288,3,52,26,0,
        287,286,1,0,0,0,287,288,1,0,0,0,288,289,1,0,0,0,289,290,5,17,0,0,
        290,291,3,102,51,0,291,292,5,24,0,0,292,295,3,118,59,0,293,294,5,
        26,0,0,294,296,3,116,58,0,295,293,1,0,0,0,295,296,1,0,0,0,296,45,
        1,0,0,0,297,298,5,26,0,0,298,303,3,108,54,0,299,300,5,54,0,0,300,
        302,3,108,54,0,301,299,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,
        304,1,0,0,0,304,306,1,0,0,0,305,303,1,0,0,0,306,307,5,31,0,0,307,
        312,3,108,54,0,308,309,5,54,0,0,309,311,3,108,54,0,310,308,1,0,0,
        0,311,314,1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,315,1,0,0,
        0,314,312,1,0,0,0,315,316,3,32,16,0,316,47,1,0,0,0,317,318,5,18,
        0,0,318,322,3,102,51,0,319,320,5,20,0,0,320,322,3,102,51,0,321,317,
        1,0,0,0,321,319,1,0,0,0,322,49,1,0,0,0,323,325,3,52,26,0,324,323,
        1,0,0,0,324,325,1,0,0,0,325,326,1,0,0,0,326,327,3,98,49,0,327,329,
        5,15,0,0,328,330,3,120,60,0,329,328,1,0,0,0,329,330,1,0,0,0,330,
        331,1,0,0,0,331,332,3,102,51,0,332,334,5,25,0,0,333,335,3,120,60,
        0,334,333,1,0,0,0,334,335,1,0,0,0,335,336,1,0,0,0,336,339,3,102,
        51,0,337,338,5,26,0,0,338,340,3,116,58,0,339,337,1,0,0,0,339,340,
        1,0,0,0,340,51,1,0,0,0,341,342,5,80,0,0,342,343,3,54,27,0,343,344,
        3,116,58,0,344,53,1,0,0,0,345,352,3,56,28,0,346,352,3,58,29,0,347,
        352,3,60,30,0,348,352,3,62,31,0,349,352,3,64,32,0,350,352,3,66,33,
        0,351,345,1,0,0,0,351,346,1,0,0,0,351,347,1,0,0,0,351,348,1,0,0,
        0,351,349,1,0,0,0,351,350,1,0,0,0,352,55,1,0,0,0,353,354,5,33,0,
        0,354,355,5,55,0,0,355,356,5,31,0,0,356,57,1,0,0,0,357,358,5,33,
        0,0,358,359,5,55,0,0,359,360,5,24,0,0,360,59,1,0,0,0,361,362,5,33,
        0,0,362,363,5,55,0,0,363,364,5,35,0,0,364,61,1,0,0,0,365,366,5,34,
        0,0,366,367,5,55,0,0,367,368,5,31,0,0,368,63,1,0,0,0,369,370,5,34,
        0,0,370,371,5,55,0,0,371,372,5,24,0,0,372,65,1,0,0,0,373,374,5,34,
        0,0,374,375,5,55,0,0,375,376,5,35,0,0,376,67,1,0,0,0,377,378,3,98,
        49,0,378,379,5,14,0,0,379,380,5,103,0,0,380,381,5,29,0,0,381,384,
        3,102,51,0,382,383,5,26,0,0,383,385,3,116,58,0,384,382,1,0,0,0,384,
        385,1,0,0,0,385,69,1,0,0,0,386,387,3,98,49,0,387,388,5,16,0,0,388,
        389,3,102,51,0,389,390,5,27,0,0,390,391,5,43,0,0,391,71,1,0,0,0,
        392,393,3,98,49,0,393,395,5,19,0,0,394,396,3,120,60,0,395,394,1,
        0,0,0,395,396,1,0,0,0,396,397,1,0,0,0,397,398,5,103,0,0,398,73,1,
        0,0,0,399,400,3,98,49,0,400,401,5,21,0,0,401,402,3,102,51,0,402,
        403,5,25,0,0,403,404,3,102,51,0,404,405,5,23,0,0,405,406,5,42,0,
        0,406,407,5,54,0,0,407,408,5,42,0,0,408,409,5,24,0,0,409,410,5,42,
        0,0,410,75,1,0,0,0,411,412,5,22,0,0,412,413,3,102,51,0,413,77,1,
        0,0,0,414,415,3,98,49,0,415,416,3,110,55,0,416,79,1,0,0,0,417,418,
        3,98,49,0,418,419,3,108,54,0,419,420,7,0,0,0,420,421,3,108,54,0,
        421,428,1,0,0,0,422,423,3,98,49,0,423,424,3,108,54,0,424,425,7,1,
        0,0,425,426,3,108,54,0,426,428,1,0,0,0,427,417,1,0,0,0,427,422,1,
        0,0,0,428,81,1,0,0,0,429,437,3,108,54,0,430,431,5,58,0,0,431,438,
        5,58,0,0,432,433,5,57,0,0,433,434,5,57,0,0,434,438,5,57,0,0,435,
        436,5,57,0,0,436,438,5,57,0,0,437,430,1,0,0,0,437,432,1,0,0,0,437,
        435,1,0,0,0,438,439,1,0,0,0,439,440,3,108,54,0,440,450,1,0,0,0,441,
        442,3,108,54,0,442,443,7,2,0,0,443,444,3,108,54,0,444,450,1,0,0,
        0,445,446,3,108,54,0,446,447,7,3,0,0,447,448,3,108,54,0,448,450,
        1,0,0,0,449,429,1,0,0,0,449,441,1,0,0,0,449,445,1,0,0,0,450,83,1,
        0,0,0,451,452,5,47,0,0,452,457,3,82,41,0,453,454,7,4,0,0,454,456,
        3,82,41,0,455,453,1,0,0,0,456,459,1,0,0,0,457,455,1,0,0,0,457,458,
        1,0,0,0,458,460,1,0,0,0,459,457,1,0,0,0,460,461,5,48,0,0,461,85,
        1,0,0,0,462,463,3,98,49,0,463,464,3,88,44,0,464,87,1,0,0,0,465,466,
        5,103,0,0,466,468,5,47,0,0,467,469,3,90,45,0,468,467,1,0,0,0,468,
        469,1,0,0,0,469,470,1,0,0,0,470,471,5,48,0,0,471,89,1,0,0,0,472,
        480,3,108,54,0,473,476,5,54,0,0,474,477,3,108,54,0,475,477,3,88,
        44,0,476,474,1,0,0,0,476,475,1,0,0,0,477,479,1,0,0,0,478,473,1,0,
        0,0,479,482,1,0,0,0,480,478,1,0,0,0,480,481,1,0,0,0,481,485,1,0,
        0,0,482,480,1,0,0,0,483,485,3,88,44,0,484,472,1,0,0,0,484,483,1,
        0,0,0,485,91,1,0,0,0,486,489,3,112,56,0,487,489,3,114,57,0,488,486,
        1,0,0,0,488,487,1,0,0,0,489,93,1,0,0,0,490,491,5,51,0,0,491,492,
        3,96,48,0,492,493,5,52,0,0,493,95,1,0,0,0,494,499,3,92,46,0,495,
        496,5,53,0,0,496,498,3,92,46,0,497,495,1,0,0,0,498,501,1,0,0,0,499,
        497,1,0,0,0,499,500,1,0,0,0,500,97,1,0,0,0,501,499,1,0,0,0,502,504,
        3,94,47,0,503,502,1,0,0,0,503,504,1,0,0,0,504,505,1,0,0,0,505,506,
        3,102,51,0,506,507,5,56,0,0,507,99,1,0,0,0,508,509,3,98,49,0,509,
        510,5,51,0,0,510,515,3,108,54,0,511,512,5,54,0,0,512,514,3,108,54,
        0,513,511,1,0,0,0,514,517,1,0,0,0,515,513,1,0,0,0,515,516,1,0,0,
        0,516,518,1,0,0,0,517,515,1,0,0,0,518,519,5,52,0,0,519,101,1,0,0,
        0,520,524,5,103,0,0,521,522,5,51,0,0,522,523,5,43,0,0,523,525,5,
        52,0,0,524,521,1,0,0,0,524,525,1,0,0,0,525,103,1,0,0,0,526,527,5,
        103,0,0,527,105,1,0,0,0,528,529,5,51,0,0,529,534,3,108,54,0,530,
        531,5,54,0,0,531,533,3,108,54,0,532,530,1,0,0,0,533,536,1,0,0,0,
        534,532,1,0,0,0,534,535,1,0,0,0,535,537,1,0,0,0,536,534,1,0,0,0,
        537,538,5,52,0,0,538,107,1,0,0,0,539,544,3,110,55,0,540,544,3,102,
        51,0,541,544,3,106,53,0,542,544,3,104,52,0,543,539,1,0,0,0,543,540,
        1,0,0,0,543,541,1,0,0,0,543,542,1,0,0,0,544,109,1,0,0,0,545,546,
        7,5,0,0,546,111,1,0,0,0,547,548,7,6,0,0,548,113,1,0,0,0,549,550,
        7,7,0,0,550,115,1,0,0,0,551,556,5,44,0,0,552,553,3,104,52,0,553,
        554,7,8,0,0,554,556,1,0,0,0,555,551,1,0,0,0,555,552,1,0,0,0,556,
        117,1,0,0,0,557,562,5,46,0,0,558,559,3,104,52,0,559,560,7,9,0,0,
        560,562,1,0,0,0,561,557,1,0,0,0,561,558,1,0,0,0,562,119,1,0,0,0,
        563,564,5,43,0,0,564,565,5,32,0,0,565,566,5,30,0,0,566,121,1,0,0,
        0,49,125,128,135,144,150,156,163,174,187,193,199,203,209,218,222,
        233,239,262,269,281,287,295,303,312,321,324,329,334,339,351,384,
        395,427,437,449,457,468,476,480,484,488,499,503,515,524,534,543,
        555,561
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
                     "'times'", "'on'", "'of'", "'in'", "'units'", "'use'", 
                     "'finish'", "'after'", "'nat'", "'real'", "'mat'", 
                     "'bool'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", "'='", 
                     "'>'", "'<'", "'!'", "'~'", "'?'", "':'", "'=='", "'<='", 
                     "'>='", "'!='", "'&&'", "'||'", "'++'", "'--'", "'+'", 
                     "'-'", "'*'", "'/'", "'&'", "'|'", "'^'", "'%'", "'_'", 
                     "'@'", "'ns'", "'us'", "'ms'", "'cs'", "'ds'", "'s'", 
                     "'m'", "'h'", "'d'", "'w'", "'mo'", "'y'", "'nL'", 
                     "'uL'", "'mL'", "'cL'", "'dL'", "'L'", "'daL'", "'c'", 
                     "'f'", "'k'", "<INVALID>", "'1'", "'2'", "'3'", "'4'", 
                     "'5'", "'6'", "'7'", "'8'", "'9'", "'10'", "'11'", 
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
                      "INSTRUCTIONS", "IMPORT", "FROM", "DETECT", "MIX", 
                      "SPLIT", "HEAT", "DRAIN", "DISPENSE", "DISPOSE", "GRADIENT", 
                      "STORE", "RANGE", "AT", "WITH", "FOR", "INTO", "TIMES", 
                      "ON", "OF", "IN", "UNITS", "USE", "FINISH", "AFTER", 
                      "NAT", "REAL", "MAT", "BOOL", "STRING_LITERAL", "BOOL_LITERAL", 
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
                      "KELVIN", "IDENTIFIER", "ACIDS_STRONG_NON_OXIDIZING", 
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
    RULE_whileStatement = 19
    RULE_renameVarStatement = 20
    RULE_repeat = 21
    RULE_heat = 22
    RULE_forInStatement = 23
    RULE_dispose = 24
    RULE_mix = 25
    RULE_usein = 26
    RULE_useinType = 27
    RULE_sle = 28
    RULE_seq = 29
    RULE_sge = 30
    RULE_fle = 31
    RULE_feq = 32
    RULE_fge = 33
    RULE_detect = 34
    RULE_split = 35
    RULE_dispense = 36
    RULE_gradient = 37
    RULE_store = 38
    RULE_numberAssignment = 39
    RULE_math = 40
    RULE_binops = 41
    RULE_parExpression = 42
    RULE_methodInvocation = 43
    RULE_methodCall = 44
    RULE_expressionList = 45
    RULE_typeType = 46
    RULE_unionType = 47
    RULE_typesList = 48
    RULE_variableDefinition = 49
    RULE_listDefinition = 50
    RULE_variable = 51
    RULE_numericAlias = 52
    RULE_list = 53
    RULE_primary = 54
    RULE_literal = 55
    RULE_primitiveType = 56
    RULE_chemicalType = 57
    RULE_timeIdentifier = 58
    RULE_temperatureIdentifier = 59
    RULE_unitTracker = 60

    ruleNames =  [ "program", "globalDeclarations", "moduleDeclaration", 
                   "manifestDeclaration", "stationaryDeclaration", "importStatement", 
                   "importLibrary", "importFuncFromLibrary", "fromLibrary", 
                   "functions", "functionDeclaration", "formalParameters", 
                   "formalParameterList", "formalParameter", "functionTyping", 
                   "returnStatement", "blockStatement", "statements", "ifStatement", 
                   "whileStatement", "renameVarStatement", "repeat", "heat", 
                   "forInStatement", "dispose", "mix", "usein", "useinType", 
                   "sle", "seq", "sge", "fle", "feq", "fge", "detect", "split", 
                   "dispense", "gradient", "store", "numberAssignment", 
                   "math", "binops", "parExpression", "methodInvocation", 
                   "methodCall", "expressionList", "typeType", "unionType", 
                   "typesList", "variableDefinition", "listDefinition", 
                   "variable", "numericAlias", "list", "primary", "literal", 
                   "primitiveType", "chemicalType", "timeIdentifier", "temperatureIdentifier", 
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
    USE=33
    FINISH=34
    AFTER=35
    NAT=36
    REAL=37
    MAT=38
    BOOL=39
    STRING_LITERAL=40
    BOOL_LITERAL=41
    FLOAT_LITERAL=42
    INTEGER_LITERAL=43
    TIME_NUMBER=44
    VOLUME_NUMBER=45
    TEMP_NUMBER=46
    LPAREN=47
    RPAREN=48
    LBRACE=49
    RBRACE=50
    LBRACKET=51
    RBRACKET=52
    SEMICOLON=53
    COMMA=54
    DOT=55
    ASSIGN=56
    GT=57
    LT=58
    BANG=59
    TILDE=60
    QUESTION=61
    COLON=62
    EQUALITY=63
    LTE=64
    GTE=65
    NOTEQUAL=66
    AND=67
    OR=68
    INC=69
    DEC=70
    ADDITION=71
    SUBTRACT=72
    MULTIPLY=73
    DIVIDE=74
    BITAND=75
    BITOR=76
    CARET=77
    MOD=78
    UNDERSCORE=79
    ATSIGN=80
    NANOSECOND=81
    MICROSECOND=82
    MILLISECOND=83
    CENTISECOND=84
    DECISECOND=85
    SECOND=86
    MINUTE=87
    HOUR=88
    DAY=89
    WEEK=90
    MONTH=91
    YEAR=92
    NANOLITRE=93
    MICROLITRE=94
    MILLILITRE=95
    CENTILITRE=96
    DECILITRE=97
    LITRE=98
    DECALITRE=99
    CELSIUS=100
    FAHRENHEIT=101
    KELVIN=102
    IDENTIFIER=103
    ACIDS_STRONG_NON_OXIDIZING=104
    ACIDS_STRONG_OXIDIZING=105
    ACIDS_CARBOXYLIC=106
    ALCOHOLS_AND_POLYOLS=107
    ALDEHYDES=108
    AMIDES_AND_IMIDES=109
    AMINES_PHOSPHINES_AND_PYRIDINES=110
    AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS=111
    CARBAMATES=112
    BASES_STRONG=113
    CYANIDES_INORGANIC=114
    THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS=115
    ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS=116
    ETHERS=117
    FLUORIDES_INORGANIC=118
    HYDROCARBONS_AROMATIC=119
    HALOGENATED_ORGANIC_COMPOUNDS=120
    ISOCYANATES_AND_ISOTHIOCYANATES=121
    KETONES=122
    SULFIDES_ORGANIC=123
    METALS_ALKALI_VERY_ACTIVE=124
    METALS_ELEMENTAL_AND_POWDER_ACTIVE=125
    METALS_LESS_REACTIVE=126
    METALS_AND_METAL_COMPOUNDS_TOXIC=127
    DIAZONIUM_SALTS=128
    NITRILES=129
    NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC=130
    HYDROCARBONS_ALIPHATIC_UNSATURATED=131
    HYDROCARBONS_ALIPHATIC_SATURATED=132
    PEROXIDES_ORGANIC=133
    PHENOLS_AND_CRESOLS=134
    SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC=135
    SULFIDES_INORGANIC=136
    EPOXIDES=137
    METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES=138
    ANHYDRIDES=139
    SALTS_ACIDIC=140
    SALTS_BASIC=141
    ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES=142
    ORGANOMETALLICS=143
    OXIDIZING_AGENTS_STRONG=144
    REDUCING_AGENTS_STRONG=145
    NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS=146
    FLUORINATED_ORGANIC_COMPOUNDS=147
    FLUORIDE_SALTS_SOLUBLE=148
    OXIDIZING_AGENTS_WEAK=149
    REDUCING_AGENTS_WEAK=150
    NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES=151
    CHLOROSILANES=152
    SILOXANES=153
    HALOGENATING_AGENTS=154
    ACIDS_WEAK=155
    BASES_WEAK=156
    CARBONATE_SALTS=157
    ALKYNES_WITH_ACETYLENIC_HYDROGEN=158
    ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN=159
    CONJUGATED_DIENES=160
    ARYL_HALIDES=161
    AMINES_AROMATIC=162
    NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC=163
    ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS=164
    ACRYLATES_AND_ACRYLIC_ACIDS=165
    PHENOLIC_SALTS=166
    QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS=167
    SULFITE_AND_THIOSULFATE_SALTS=168
    OXIMES=169
    POLYMERIZABLE_COMPOUNDS=170
    NOT_CHEMICALLY_REACTIVE=171
    INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION=172
    WATER_AND_AQUEOUS_SOLUTIONS=173
    NULL=174
    UNKNOWN=175
    WS=176
    COMMENT=177
    LINE_COMMENT=178

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
            self.state = 123 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 122
                self.globalDeclarations()
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.MANIFEST) | (1 << BSParser.MODULE) | (1 << BSParser.STATIONARY) | (1 << BSParser.IMPORT) | (1 << BSParser.LBRACKET))) != 0)):
                    break

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FUNCTIONS:
                self.state = 127
                self.functions()


            self.state = 130
            self.match(BSParser.INSTRUCTIONS)
            self.state = 131
            self.match(BSParser.COLON)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.FOR) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN or _la==BSParser.IDENTIFIER:
                self.state = 132
                self.statements()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
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
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.moduleDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.manifestDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.stationaryDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
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
            self.state = 146
            self.match(BSParser.MODULE)
            self.state = 147
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
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 149
                self.unionType()


            self.state = 152
            self.match(BSParser.MANIFEST)
            self.state = 153
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
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 155
                self.unionType()


            self.state = 158
            self.match(BSParser.STATIONARY)
            self.state = 159
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
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.importLibrary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
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
            self.state = 165
            self.match(BSParser.IMPORT)
            self.state = 166
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
            self.state = 168
            self.match(BSParser.IMPORT)
            self.state = 169
            self.match(BSParser.IDENTIFIER)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 170
                self.match(BSParser.COMMA)
                self.state = 171
                self.match(BSParser.IDENTIFIER)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
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
            self.state = 179
            self.match(BSParser.FROM)
            self.state = 180
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
            self.state = 182
            self.match(BSParser.FUNCTIONS)
            self.state = 183
            self.match(BSParser.COLON)
            self.state = 185 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 184
                self.functionDeclaration()
                self.state = 187 
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

        def RBRACE(self):
            return self.getToken(BSParser.RBRACE, 0)

        def functionTyping(self):
            return self.getTypedRuleContext(BSParser.FunctionTypingContext,0)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.StatementsContext)
            else:
                return self.getTypedRuleContext(BSParser.StatementsContext,i)


        def returnStatement(self):
            return self.getTypedRuleContext(BSParser.ReturnStatementContext,0)


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
            self.state = 189
            self.match(BSParser.FUNCTION)
            self.state = 190
            self.match(BSParser.IDENTIFIER)
            self.state = 191
            self.formalParameters()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.COLON:
                self.state = 192
                self.functionTyping()


            self.state = 195
            self.match(BSParser.LBRACE)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.FOR) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN or _la==BSParser.IDENTIFIER:
                self.state = 196
                self.statements()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.RETURN:
                self.state = 202
                self.returnStatement()


            self.state = 205
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
            self.state = 207
            self.match(BSParser.LPAREN)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET or _la==BSParser.IDENTIFIER:
                self.state = 208
                self.formalParameterList()


            self.state = 211
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
            self.state = 213
            self.formalParameter()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 214
                self.match(BSParser.COMMA)
                self.state = 215
                self.formalParameter()
                self.state = 220
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
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 221
                self.unionType()


            self.state = 224
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
            self.state = 226
            self.match(BSParser.COLON)
            self.state = 227
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
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(BSParser.RETURN)
                self.state = 230
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(BSParser.RETURN)
                self.state = 232
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
            self.state = 235
            self.match(BSParser.LBRACE)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.FOR) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN or _la==BSParser.IDENTIFIER:
                self.state = 236
                self.statements()
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
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


        def renameVarStatement(self):
            return self.getTypedRuleContext(BSParser.RenameVarStatementContext,0)


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
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.forInStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                self.variableDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 248
                self.listDefinition()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 249
                self.repeat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 250
                self.heat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 251
                self.dispose()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 252
                self.mix()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 253
                self.dispense()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 254
                self.split()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 255
                self.methodInvocation()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 256
                self.gradient()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 257
                self.detect()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 258
                self.store()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 259
                self.math()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 260
                self.numberAssignment()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 261
                self.renameVarStatement()
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
            self.state = 264
            self.match(BSParser.IF)
            self.state = 265
            self.parExpression()
            self.state = 266
            self.blockStatement()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ELSE:
                self.state = 267
                self.match(BSParser.ELSE)
                self.state = 268
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
        self.enterRule(localctx, 38, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(BSParser.WHILE)
            self.state = 272
            self.parExpression()
            self.state = 273
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RenameVarStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_renameVarStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRenameVarStatement" ):
                listener.enterRenameVarStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRenameVarStatement" ):
                listener.exitRenameVarStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRenameVarStatement" ):
                return visitor.visitRenameVarStatement(self)
            else:
                return visitor.visitChildren(self)




    def renameVarStatement(self):

        localctx = BSParser.RenameVarStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_renameVarStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.variableDefinition()
            self.state = 276
            self.variable()
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
            self.state = 278
            self.match(BSParser.REPEAT)
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.INTEGER_LITERAL]:
                self.state = 279
                self.match(BSParser.INTEGER_LITERAL)
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.state = 280
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 283
            self.match(BSParser.TIMES)
            self.state = 284
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
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ATSIGN:
                self.state = 286
                self.usein()


            self.state = 289
            self.match(BSParser.HEAT)
            self.state = 290
            self.variable()
            self.state = 291
            self.match(BSParser.AT)
            self.state = 292
            self.temperatureIdentifier()
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 293
                self.match(BSParser.FOR)
                self.state = 294
                self.timeIdentifier()


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

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BSParser.PrimaryContext,i)


        def IN(self):
            return self.getToken(BSParser.IN, 0)

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
        self.enterRule(localctx, 46, self.RULE_forInStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(BSParser.FOR)
            self.state = 298
            self.primary()
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 299
                self.match(BSParser.COMMA)
                self.state = 300
                self.primary()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 306
            self.match(BSParser.IN)
            self.state = 307
            self.primary()
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 308
                self.match(BSParser.COMMA)
                self.state = 309
                self.primary()
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 315
            self.blockStatement()
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
        self.enterRule(localctx, 48, self.RULE_dispose)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.DRAIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(BSParser.DRAIN)
                self.state = 318
                self.variable()
                pass
            elif token in [BSParser.DISPOSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(BSParser.DISPOSE)
                self.state = 320
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
        self.enterRule(localctx, 50, self.RULE_mix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ATSIGN:
                self.state = 323
                self.usein()


            self.state = 326
            self.variableDefinition()
            self.state = 327
            self.match(BSParser.MIX)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 328
                self.unitTracker()


            self.state = 331
            self.variable()
            self.state = 332
            self.match(BSParser.WITH)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 333
                self.unitTracker()


            self.state = 336
            self.variable()
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 337
                self.match(BSParser.FOR)
                self.state = 338
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

        def useinType(self):
            return self.getTypedRuleContext(BSParser.UseinTypeContext,0)


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
        self.enterRule(localctx, 52, self.RULE_usein)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(BSParser.ATSIGN)
            self.state = 342
            self.useinType()
            self.state = 343
            self.timeIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseinTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sle(self):
            return self.getTypedRuleContext(BSParser.SleContext,0)


        def seq(self):
            return self.getTypedRuleContext(BSParser.SeqContext,0)


        def sge(self):
            return self.getTypedRuleContext(BSParser.SgeContext,0)


        def fle(self):
            return self.getTypedRuleContext(BSParser.FleContext,0)


        def feq(self):
            return self.getTypedRuleContext(BSParser.FeqContext,0)


        def fge(self):
            return self.getTypedRuleContext(BSParser.FgeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_useinType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseinType" ):
                listener.enterUseinType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseinType" ):
                listener.exitUseinType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseinType" ):
                return visitor.visitUseinType(self)
            else:
                return visitor.visitChildren(self)




    def useinType(self):

        localctx = BSParser.UseinTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_useinType)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.sle()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.seq()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.sge()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 348
                self.fle()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 349
                self.feq()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 350
                self.fge()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(BSParser.USE, 0)

        def DOT(self):
            return self.getToken(BSParser.DOT, 0)

        def IN(self):
            return self.getToken(BSParser.IN, 0)

        def getRuleIndex(self):
            return BSParser.RULE_sle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSle" ):
                listener.enterSle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSle" ):
                listener.exitSle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSle" ):
                return visitor.visitSle(self)
            else:
                return visitor.visitChildren(self)




    def sle(self):

        localctx = BSParser.SleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_sle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(BSParser.USE)
            self.state = 354
            self.match(BSParser.DOT)
            self.state = 355
            self.match(BSParser.IN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(BSParser.USE, 0)

        def DOT(self):
            return self.getToken(BSParser.DOT, 0)

        def AT(self):
            return self.getToken(BSParser.AT, 0)

        def getRuleIndex(self):
            return BSParser.RULE_seq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeq" ):
                listener.enterSeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeq" ):
                listener.exitSeq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeq" ):
                return visitor.visitSeq(self)
            else:
                return visitor.visitChildren(self)




    def seq(self):

        localctx = BSParser.SeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_seq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(BSParser.USE)
            self.state = 358
            self.match(BSParser.DOT)
            self.state = 359
            self.match(BSParser.AT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(BSParser.USE, 0)

        def DOT(self):
            return self.getToken(BSParser.DOT, 0)

        def AFTER(self):
            return self.getToken(BSParser.AFTER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_sge

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSge" ):
                listener.enterSge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSge" ):
                listener.exitSge(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSge" ):
                return visitor.visitSge(self)
            else:
                return visitor.visitChildren(self)




    def sge(self):

        localctx = BSParser.SgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_sge)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(BSParser.USE)
            self.state = 362
            self.match(BSParser.DOT)
            self.state = 363
            self.match(BSParser.AFTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINISH(self):
            return self.getToken(BSParser.FINISH, 0)

        def DOT(self):
            return self.getToken(BSParser.DOT, 0)

        def IN(self):
            return self.getToken(BSParser.IN, 0)

        def getRuleIndex(self):
            return BSParser.RULE_fle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFle" ):
                listener.enterFle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFle" ):
                listener.exitFle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFle" ):
                return visitor.visitFle(self)
            else:
                return visitor.visitChildren(self)




    def fle(self):

        localctx = BSParser.FleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_fle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(BSParser.FINISH)
            self.state = 366
            self.match(BSParser.DOT)
            self.state = 367
            self.match(BSParser.IN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINISH(self):
            return self.getToken(BSParser.FINISH, 0)

        def DOT(self):
            return self.getToken(BSParser.DOT, 0)

        def AT(self):
            return self.getToken(BSParser.AT, 0)

        def getRuleIndex(self):
            return BSParser.RULE_feq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeq" ):
                listener.enterFeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeq" ):
                listener.exitFeq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFeq" ):
                return visitor.visitFeq(self)
            else:
                return visitor.visitChildren(self)




    def feq(self):

        localctx = BSParser.FeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_feq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(BSParser.FINISH)
            self.state = 370
            self.match(BSParser.DOT)
            self.state = 371
            self.match(BSParser.AT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINISH(self):
            return self.getToken(BSParser.FINISH, 0)

        def DOT(self):
            return self.getToken(BSParser.DOT, 0)

        def AFTER(self):
            return self.getToken(BSParser.AFTER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_fge

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFge" ):
                listener.enterFge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFge" ):
                listener.exitFge(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFge" ):
                return visitor.visitFge(self)
            else:
                return visitor.visitChildren(self)




    def fge(self):

        localctx = BSParser.FgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_fge)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(BSParser.FINISH)
            self.state = 374
            self.match(BSParser.DOT)
            self.state = 375
            self.match(BSParser.AFTER)
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
        self.enterRule(localctx, 68, self.RULE_detect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.variableDefinition()
            self.state = 378
            self.match(BSParser.DETECT)
            self.state = 379
            self.match(BSParser.IDENTIFIER)
            self.state = 380
            self.match(BSParser.ON)
            self.state = 381
            self.variable()
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 382
                self.match(BSParser.FOR)
                self.state = 383
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
        self.enterRule(localctx, 70, self.RULE_split)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.variableDefinition()
            self.state = 387
            self.match(BSParser.SPLIT)
            self.state = 388
            self.variable()
            self.state = 389
            self.match(BSParser.INTO)
            self.state = 390
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
        self.enterRule(localctx, 72, self.RULE_dispense)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.variableDefinition()
            self.state = 393
            self.match(BSParser.DISPENSE)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 394
                self.unitTracker()


            self.state = 397
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
        self.enterRule(localctx, 74, self.RULE_gradient)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.variableDefinition()
            self.state = 400
            self.match(BSParser.GRADIENT)
            self.state = 401
            self.variable()
            self.state = 402
            self.match(BSParser.WITH)
            self.state = 403
            self.variable()
            self.state = 404
            self.match(BSParser.RANGE)
            self.state = 405
            self.match(BSParser.FLOAT_LITERAL)
            self.state = 406
            self.match(BSParser.COMMA)
            self.state = 407
            self.match(BSParser.FLOAT_LITERAL)
            self.state = 408
            self.match(BSParser.AT)
            self.state = 409
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
        self.enterRule(localctx, 76, self.RULE_store)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(BSParser.STORE)
            self.state = 412
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
        self.enterRule(localctx, 78, self.RULE_numberAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.variableDefinition()
            self.state = 415
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
        self.enterRule(localctx, 80, self.RULE_math)
        self._la = 0 # Token type
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.variableDefinition()
                self.state = 418
                self.primary()
                self.state = 419
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (BSParser.MULTIPLY - 73)) | (1 << (BSParser.DIVIDE - 73)) | (1 << (BSParser.MOD - 73)))) != 0)):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 420
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.variableDefinition()
                self.state = 423
                self.primary()
                self.state = 424
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BSParser.ADDITION or _la==BSParser.SUBTRACT):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 425
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
        self.enterRule(localctx, 82, self.RULE_binops)
        self._la = 0 # Token type
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.primary()
                self.state = 437
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 430
                    self.match(BSParser.LT)
                    self.state = 431
                    self.match(BSParser.LT)
                    pass

                elif la_ == 2:
                    self.state = 432
                    self.match(BSParser.GT)
                    self.state = 433
                    self.match(BSParser.GT)
                    self.state = 434
                    self.match(BSParser.GT)
                    pass

                elif la_ == 3:
                    self.state = 435
                    self.match(BSParser.GT)
                    self.state = 436
                    self.match(BSParser.GT)
                    pass


                self.state = 439
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.primary()
                self.state = 442
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & ((1 << (BSParser.GT - 57)) | (1 << (BSParser.LT - 57)) | (1 << (BSParser.LTE - 57)) | (1 << (BSParser.GTE - 57)))) != 0)):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 443
                self.primary()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 445
                self.primary()
                self.state = 446
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BSParser.EQUALITY or _la==BSParser.NOTEQUAL):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 447
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
        self.enterRule(localctx, 84, self.RULE_parExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(BSParser.LPAREN)
            self.state = 452
            self.binops()
            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.AND or _la==BSParser.OR:
                self.state = 453
                _la = self._input.LA(1)
                if not(_la==BSParser.AND or _la==BSParser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 454
                self.binops()
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 460
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
        self.enterRule(localctx, 86, self.RULE_methodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.variableDefinition()
            self.state = 463
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
        self.enterRule(localctx, 88, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(BSParser.IDENTIFIER)
            self.state = 466
            self.match(BSParser.LPAREN)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 40)) & ~0x3f) == 0 and ((1 << (_la - 40)) & ((1 << (BSParser.STRING_LITERAL - 40)) | (1 << (BSParser.BOOL_LITERAL - 40)) | (1 << (BSParser.FLOAT_LITERAL - 40)) | (1 << (BSParser.INTEGER_LITERAL - 40)) | (1 << (BSParser.LBRACKET - 40)) | (1 << (BSParser.IDENTIFIER - 40)))) != 0):
                self.state = 467
                self.expressionList()


            self.state = 470
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
        self.enterRule(localctx, 90, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.state = 484
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.primary()
                self.state = 480
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BSParser.COMMA:
                    self.state = 473
                    self.match(BSParser.COMMA)
                    self.state = 476
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 474
                        self.primary()
                        pass

                    elif la_ == 2:
                        self.state = 475
                        self.methodCall()
                        pass


                    self.state = 482
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
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
        self.enterRule(localctx, 92, self.RULE_typeType)
        try:
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.NAT, BSParser.REAL, BSParser.MAT, BSParser.BOOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.primitiveType()
                pass
            elif token in [BSParser.INTEGER_LITERAL, BSParser.ACIDS_STRONG_NON_OXIDIZING, BSParser.ACIDS_STRONG_OXIDIZING, BSParser.ACIDS_CARBOXYLIC, BSParser.ALCOHOLS_AND_POLYOLS, BSParser.ALDEHYDES, BSParser.AMIDES_AND_IMIDES, BSParser.AMINES_PHOSPHINES_AND_PYRIDINES, BSParser.AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS, BSParser.CARBAMATES, BSParser.BASES_STRONG, BSParser.CYANIDES_INORGANIC, BSParser.THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS, BSParser.ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS, BSParser.ETHERS, BSParser.FLUORIDES_INORGANIC, BSParser.HYDROCARBONS_AROMATIC, BSParser.HALOGENATED_ORGANIC_COMPOUNDS, BSParser.ISOCYANATES_AND_ISOTHIOCYANATES, BSParser.KETONES, BSParser.SULFIDES_ORGANIC, BSParser.METALS_ALKALI_VERY_ACTIVE, BSParser.METALS_ELEMENTAL_AND_POWDER_ACTIVE, BSParser.METALS_LESS_REACTIVE, BSParser.METALS_AND_METAL_COMPOUNDS_TOXIC, BSParser.DIAZONIUM_SALTS, BSParser.NITRILES, BSParser.NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC, BSParser.HYDROCARBONS_ALIPHATIC_UNSATURATED, BSParser.HYDROCARBONS_ALIPHATIC_SATURATED, BSParser.PEROXIDES_ORGANIC, BSParser.PHENOLS_AND_CRESOLS, BSParser.SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC, BSParser.SULFIDES_INORGANIC, BSParser.EPOXIDES, BSParser.METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES, BSParser.ANHYDRIDES, BSParser.SALTS_ACIDIC, BSParser.SALTS_BASIC, BSParser.ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES, BSParser.ORGANOMETALLICS, BSParser.OXIDIZING_AGENTS_STRONG, BSParser.REDUCING_AGENTS_STRONG, BSParser.NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS, BSParser.FLUORINATED_ORGANIC_COMPOUNDS, BSParser.FLUORIDE_SALTS_SOLUBLE, BSParser.OXIDIZING_AGENTS_WEAK, BSParser.REDUCING_AGENTS_WEAK, BSParser.NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES, BSParser.CHLOROSILANES, BSParser.SILOXANES, BSParser.HALOGENATING_AGENTS, BSParser.ACIDS_WEAK, BSParser.BASES_WEAK, BSParser.CARBONATE_SALTS, BSParser.ALKYNES_WITH_ACETYLENIC_HYDROGEN, BSParser.ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN, BSParser.CONJUGATED_DIENES, BSParser.ARYL_HALIDES, BSParser.AMINES_AROMATIC, BSParser.NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC, BSParser.ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS, BSParser.ACRYLATES_AND_ACRYLIC_ACIDS, BSParser.PHENOLIC_SALTS, BSParser.QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS, BSParser.SULFITE_AND_THIOSULFATE_SALTS, BSParser.OXIMES, BSParser.POLYMERIZABLE_COMPOUNDS, BSParser.NOT_CHEMICALLY_REACTIVE, BSParser.INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION, BSParser.WATER_AND_AQUEOUS_SOLUTIONS, BSParser.NULL, BSParser.UNKNOWN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
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
        self.enterRule(localctx, 94, self.RULE_unionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(BSParser.LBRACKET)
            self.state = 491
            self.typesList()
            self.state = 492
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
        self.enterRule(localctx, 96, self.RULE_typesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.typeType()
            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.SEMICOLON:
                self.state = 495
                self.match(BSParser.SEMICOLON)
                self.state = 496
                self.typeType()
                self.state = 501
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
        self.enterRule(localctx, 98, self.RULE_variableDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 502
                self.unionType()


            self.state = 505
            self.variable()
            self.state = 506
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
        self.enterRule(localctx, 100, self.RULE_listDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.variableDefinition()
            self.state = 509
            self.match(BSParser.LBRACKET)
            self.state = 510
            self.primary()
            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 511
                self.match(BSParser.COMMA)
                self.state = 512
                self.primary()
                self.state = 517
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 518
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
        self.enterRule(localctx, 102, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(BSParser.IDENTIFIER)
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 521
                self.match(BSParser.LBRACKET)
                self.state = 522
                self.match(BSParser.INTEGER_LITERAL)
                self.state = 523
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
        self.enterRule(localctx, 104, self.RULE_numericAlias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
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
        self.enterRule(localctx, 106, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(BSParser.LBRACKET)
            self.state = 529
            self.primary()
            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 530
                self.match(BSParser.COMMA)
                self.state = 531
                self.primary()
                self.state = 536
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 537
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


        def numericAlias(self):
            return self.getTypedRuleContext(BSParser.NumericAliasContext,0)


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
        self.enterRule(localctx, 108, self.RULE_primary)
        try:
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 541
                self.list_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 542
                self.numericAlias()
                pass


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
        self.enterRule(localctx, 110, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
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
        self.enterRule(localctx, 112, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
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
        self.enterRule(localctx, 114, self.RULE_chemicalType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            _la = self._input.LA(1)
            if not(_la==BSParser.INTEGER_LITERAL or ((((_la - 104)) & ~0x3f) == 0 and ((1 << (_la - 104)) & ((1 << (BSParser.ACIDS_STRONG_NON_OXIDIZING - 104)) | (1 << (BSParser.ACIDS_STRONG_OXIDIZING - 104)) | (1 << (BSParser.ACIDS_CARBOXYLIC - 104)) | (1 << (BSParser.ALCOHOLS_AND_POLYOLS - 104)) | (1 << (BSParser.ALDEHYDES - 104)) | (1 << (BSParser.AMIDES_AND_IMIDES - 104)) | (1 << (BSParser.AMINES_PHOSPHINES_AND_PYRIDINES - 104)) | (1 << (BSParser.AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS - 104)) | (1 << (BSParser.CARBAMATES - 104)) | (1 << (BSParser.BASES_STRONG - 104)) | (1 << (BSParser.CYANIDES_INORGANIC - 104)) | (1 << (BSParser.THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS - 104)) | (1 << (BSParser.ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS - 104)) | (1 << (BSParser.ETHERS - 104)) | (1 << (BSParser.FLUORIDES_INORGANIC - 104)) | (1 << (BSParser.HYDROCARBONS_AROMATIC - 104)) | (1 << (BSParser.HALOGENATED_ORGANIC_COMPOUNDS - 104)) | (1 << (BSParser.ISOCYANATES_AND_ISOTHIOCYANATES - 104)) | (1 << (BSParser.KETONES - 104)) | (1 << (BSParser.SULFIDES_ORGANIC - 104)) | (1 << (BSParser.METALS_ALKALI_VERY_ACTIVE - 104)) | (1 << (BSParser.METALS_ELEMENTAL_AND_POWDER_ACTIVE - 104)) | (1 << (BSParser.METALS_LESS_REACTIVE - 104)) | (1 << (BSParser.METALS_AND_METAL_COMPOUNDS_TOXIC - 104)) | (1 << (BSParser.DIAZONIUM_SALTS - 104)) | (1 << (BSParser.NITRILES - 104)) | (1 << (BSParser.NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC - 104)) | (1 << (BSParser.HYDROCARBONS_ALIPHATIC_UNSATURATED - 104)) | (1 << (BSParser.HYDROCARBONS_ALIPHATIC_SATURATED - 104)) | (1 << (BSParser.PEROXIDES_ORGANIC - 104)) | (1 << (BSParser.PHENOLS_AND_CRESOLS - 104)) | (1 << (BSParser.SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC - 104)) | (1 << (BSParser.SULFIDES_INORGANIC - 104)) | (1 << (BSParser.EPOXIDES - 104)) | (1 << (BSParser.METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES - 104)) | (1 << (BSParser.ANHYDRIDES - 104)) | (1 << (BSParser.SALTS_ACIDIC - 104)) | (1 << (BSParser.SALTS_BASIC - 104)) | (1 << (BSParser.ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES - 104)) | (1 << (BSParser.ORGANOMETALLICS - 104)) | (1 << (BSParser.OXIDIZING_AGENTS_STRONG - 104)) | (1 << (BSParser.REDUCING_AGENTS_STRONG - 104)) | (1 << (BSParser.NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS - 104)) | (1 << (BSParser.FLUORINATED_ORGANIC_COMPOUNDS - 104)) | (1 << (BSParser.FLUORIDE_SALTS_SOLUBLE - 104)) | (1 << (BSParser.OXIDIZING_AGENTS_WEAK - 104)) | (1 << (BSParser.REDUCING_AGENTS_WEAK - 104)) | (1 << (BSParser.NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES - 104)) | (1 << (BSParser.CHLOROSILANES - 104)) | (1 << (BSParser.SILOXANES - 104)) | (1 << (BSParser.HALOGENATING_AGENTS - 104)) | (1 << (BSParser.ACIDS_WEAK - 104)) | (1 << (BSParser.BASES_WEAK - 104)) | (1 << (BSParser.CARBONATE_SALTS - 104)) | (1 << (BSParser.ALKYNES_WITH_ACETYLENIC_HYDROGEN - 104)) | (1 << (BSParser.ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN - 104)) | (1 << (BSParser.CONJUGATED_DIENES - 104)) | (1 << (BSParser.ARYL_HALIDES - 104)) | (1 << (BSParser.AMINES_AROMATIC - 104)) | (1 << (BSParser.NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC - 104)) | (1 << (BSParser.ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS - 104)) | (1 << (BSParser.ACRYLATES_AND_ACRYLIC_ACIDS - 104)) | (1 << (BSParser.PHENOLIC_SALTS - 104)) | (1 << (BSParser.QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS - 104)))) != 0) or ((((_la - 168)) & ~0x3f) == 0 and ((1 << (_la - 168)) & ((1 << (BSParser.SULFITE_AND_THIOSULFATE_SALTS - 168)) | (1 << (BSParser.OXIMES - 168)) | (1 << (BSParser.POLYMERIZABLE_COMPOUNDS - 168)) | (1 << (BSParser.NOT_CHEMICALLY_REACTIVE - 168)) | (1 << (BSParser.INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION - 168)) | (1 << (BSParser.WATER_AND_AQUEOUS_SOLUTIONS - 168)) | (1 << (BSParser.NULL - 168)) | (1 << (BSParser.UNKNOWN - 168)))) != 0)):
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

        def numericAlias(self):
            return self.getTypedRuleContext(BSParser.NumericAliasContext,0)


        def SECOND(self):
            return self.getToken(BSParser.SECOND, 0)

        def MINUTE(self):
            return self.getToken(BSParser.MINUTE, 0)

        def HOUR(self):
            return self.getToken(BSParser.HOUR, 0)

        def DAY(self):
            return self.getToken(BSParser.DAY, 0)

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
        self.enterRule(localctx, 116, self.RULE_timeIdentifier)
        self._la = 0 # Token type
        try:
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.TIME_NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.match(BSParser.TIME_NUMBER)
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.numericAlias()
                self.state = 553
                _la = self._input.LA(1)
                if not(((((_la - 86)) & ~0x3f) == 0 and ((1 << (_la - 86)) & ((1 << (BSParser.SECOND - 86)) | (1 << (BSParser.MINUTE - 86)) | (1 << (BSParser.HOUR - 86)) | (1 << (BSParser.DAY - 86)))) != 0)):
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


    class TemperatureIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEMP_NUMBER(self):
            return self.getToken(BSParser.TEMP_NUMBER, 0)

        def numericAlias(self):
            return self.getTypedRuleContext(BSParser.NumericAliasContext,0)


        def CELSIUS(self):
            return self.getToken(BSParser.CELSIUS, 0)

        def FAHRENHEIT(self):
            return self.getToken(BSParser.FAHRENHEIT, 0)

        def KELVIN(self):
            return self.getToken(BSParser.KELVIN, 0)

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
        self.enterRule(localctx, 118, self.RULE_temperatureIdentifier)
        self._la = 0 # Token type
        try:
            self.state = 561
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.TEMP_NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.match(BSParser.TEMP_NUMBER)
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 558
                self.numericAlias()
                self.state = 559
                _la = self._input.LA(1)
                if not(((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (BSParser.CELSIUS - 100)) | (1 << (BSParser.FAHRENHEIT - 100)) | (1 << (BSParser.KELVIN - 100)))) != 0)):
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
        self.enterRule(localctx, 120, self.RULE_unitTracker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.match(BSParser.INTEGER_LITERAL)
            self.state = 564
            self.match(BSParser.UNITS)
            self.state = 565
            self.match(BSParser.OF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





