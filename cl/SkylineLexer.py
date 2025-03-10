# Generated from cl/Skyline.g by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\7\n\63\n\n\f\n")
        buf.write("\16\n\66\13\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16?\n\16")
        buf.write("\r\16\16\16@\3\17\6\17D\n\17\r\17\16\17E\3\17\3\17\2\2")
        buf.write("\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\3\2\6\4\2C\\c|\5\2\62;C\\c|\3\2\62")
        buf.write(";\5\2\13\f\16\17\"\"\2K\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5")
        buf.write("!\3\2\2\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r)\3\2\2")
        buf.write("\2\17+\3\2\2\2\21-\3\2\2\2\23\60\3\2\2\2\25\67\3\2\2\2")
        buf.write("\279\3\2\2\2\31;\3\2\2\2\33>\3\2\2\2\35C\3\2\2\2\37 \7")
        buf.write("*\2\2 \4\3\2\2\2!\"\7+\2\2\"\6\3\2\2\2#$\7.\2\2$\b\3\2")
        buf.write("\2\2%&\7]\2\2&\n\3\2\2\2\'(\7_\2\2(\f\3\2\2\2)*\7}\2\2")
        buf.write("*\16\3\2\2\2+,\7\177\2\2,\20\3\2\2\2-.\7<\2\2./\7?\2\2")
        buf.write("/\22\3\2\2\2\60\64\t\2\2\2\61\63\t\3\2\2\62\61\3\2\2\2")
        buf.write("\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\24\3\2\2")
        buf.write("\2\66\64\3\2\2\2\678\7,\2\28\26\3\2\2\29:\7/\2\2:\30\3")
        buf.write("\2\2\2;<\7-\2\2<\32\3\2\2\2=?\t\4\2\2>=\3\2\2\2?@\3\2")
        buf.write("\2\2@>\3\2\2\2@A\3\2\2\2A\34\3\2\2\2BD\t\5\2\2CB\3\2\2")
        buf.write("\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\b\17\2\2")
        buf.write("H\36\3\2\2\2\6\2\64@E\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    ASSIG = 8
    ID = 9
    MUL = 10
    SUB = 11
    PLUS = 12
    INT = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','", "'['", "']'", "'{'", "'}'", "':='", "'*'", 
            "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "ASSIG", "ID", "MUL", "SUB", "PLUS", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "ASSIG", "ID", "MUL", "SUB", "PLUS", "INT", "WS" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


