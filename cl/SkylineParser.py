# Generated from cl/Skyline.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\36\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3")
        buf.write(")\n\3\f\3\16\3,\13\3\3\4\3\4\5\4\60\n\4\3\5\3\5\3\5\5")
        buf.write("\5\65\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7")
        buf.write("\7O\n\7\f\7\16\7R\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\2\3\4\t\2\4\6\b\n\f\16\2")
        buf.write("\4\4\2\f\f\16\16\3\2\r\16\2d\2\20\3\2\2\2\4\35\3\2\2\2")
        buf.write("\6/\3\2\2\2\b\64\3\2\2\2\n\66\3\2\2\2\f>\3\2\2\2\16U\3")
        buf.write("\2\2\2\20\21\5\4\3\2\21\3\3\2\2\2\22\23\b\3\1\2\23\24")
        buf.write("\7\3\2\2\24\25\5\4\3\2\25\26\7\4\2\2\26\36\3\2\2\2\27")
        buf.write("\30\7\r\2\2\30\36\5\4\3\b\31\32\7\13\2\2\32\33\7\n\2\2")
        buf.write("\33\36\5\4\3\4\34\36\5\6\4\2\35\22\3\2\2\2\35\27\3\2\2")
        buf.write("\2\35\31\3\2\2\2\35\34\3\2\2\2\36*\3\2\2\2\37 \f\7\2\2")
        buf.write(" !\t\2\2\2!)\5\4\3\b\"#\f\6\2\2#$\7\f\2\2$)\7\17\2\2%")
        buf.write("&\f\5\2\2&\'\t\3\2\2\')\7\17\2\2(\37\3\2\2\2(\"\3\2\2")
        buf.write("\2(%\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\5\3\2\2\2")
        buf.write(",*\3\2\2\2-\60\7\13\2\2.\60\5\b\5\2/-\3\2\2\2/.\3\2\2")
        buf.write("\2\60\7\3\2\2\2\61\65\5\n\6\2\62\65\5\f\7\2\63\65\5\16")
        buf.write("\b\2\64\61\3\2\2\2\64\62\3\2\2\2\64\63\3\2\2\2\65\t\3")
        buf.write("\2\2\2\66\67\7\3\2\2\678\7\17\2\289\7\5\2\29:\7\17\2\2")
        buf.write(":;\7\5\2\2;<\7\17\2\2<=\7\4\2\2=\13\3\2\2\2>?\7\6\2\2")
        buf.write("?@\7\3\2\2@A\7\17\2\2AB\7\5\2\2BC\7\17\2\2CD\7\5\2\2D")
        buf.write("E\7\17\2\2EP\7\4\2\2FG\7\5\2\2GH\7\3\2\2HI\7\17\2\2IJ")
        buf.write("\7\5\2\2JK\7\17\2\2KL\7\5\2\2LM\7\17\2\2MO\7\4\2\2NF\3")
        buf.write("\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QS\3\2\2\2RP\3\2\2")
        buf.write("\2ST\7\7\2\2T\r\3\2\2\2UV\7\b\2\2VW\7\17\2\2WX\7\5\2\2")
        buf.write("XY\7\17\2\2YZ\7\5\2\2Z[\7\17\2\2[\\\7\5\2\2\\]\7\17\2")
        buf.write("\2]^\7\5\2\2^_\7\17\2\2_`\7\t\2\2`\17\3\2\2\2\b\35(*/")
        buf.write("\64P")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "'['", "']'", "'{'", 
                     "'}'", "':='", "<INVALID>", "'*'", "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ASSIG", "ID", "MUL", "SUB", "PLUS", "INT", "WS" ]

    RULE_root = 0
    RULE_operacions = 1
    RULE_sky = 2
    RULE_creacions = 3
    RULE_simple = 4
    RULE_compost = 5
    RULE_aleatori = 6

    ruleNames =  [ "root", "operacions", "sky", "creacions", "simple", "compost", 
                   "aleatori" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ASSIG=8
    ID=9
    MUL=10
    SUB=11
    PLUS=12
    INT=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operacions(self):
            return self.getTypedRuleContext(SkylineParser.OperacionsContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.operacions(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_operacions

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AssignacioContext(OperacionsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.OperacionsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)
        def ASSIG(self):
            return self.getToken(SkylineParser.ASSIG, 0)
        def operacions(self):
            return self.getTypedRuleContext(SkylineParser.OperacionsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignacio" ):
                return visitor.visitAssignacio(self)
            else:
                return visitor.visitChildren(self)


    class UnioInterContext(OperacionsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.OperacionsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operacions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.OperacionsContext)
            else:
                return self.getTypedRuleContext(SkylineParser.OperacionsContext,i)

        def PLUS(self):
            return self.getToken(SkylineParser.PLUS, 0)
        def MUL(self):
            return self.getToken(SkylineParser.MUL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnioInter" ):
                return visitor.visitUnioInter(self)
            else:
                return visitor.visitChildren(self)


    class MirallContext(OperacionsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.OperacionsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(SkylineParser.SUB, 0)
        def operacions(self):
            return self.getTypedRuleContext(SkylineParser.OperacionsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMirall" ):
                return visitor.visitMirall(self)
            else:
                return visitor.visitChildren(self)


    class IdentContext(OperacionsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.OperacionsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sky(self):
            return self.getTypedRuleContext(SkylineParser.SkyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdent" ):
                return visitor.visitIdent(self)
            else:
                return visitor.visitChildren(self)


    class ReplicacioContext(OperacionsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.OperacionsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operacions(self):
            return self.getTypedRuleContext(SkylineParser.OperacionsContext,0)

        def MUL(self):
            return self.getToken(SkylineParser.MUL, 0)
        def INT(self):
            return self.getToken(SkylineParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplicacio" ):
                return visitor.visitReplicacio(self)
            else:
                return visitor.visitChildren(self)


    class DesplaçamentContext(OperacionsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.OperacionsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operacions(self):
            return self.getTypedRuleContext(SkylineParser.OperacionsContext,0)

        def INT(self):
            return self.getToken(SkylineParser.INT, 0)
        def PLUS(self):
            return self.getToken(SkylineParser.PLUS, 0)
        def SUB(self):
            return self.getToken(SkylineParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesplaçament" ):
                return visitor.visitDesplaçament(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisContext(OperacionsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.OperacionsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operacions(self):
            return self.getTypedRuleContext(SkylineParser.OperacionsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)



    def operacions(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.OperacionsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_operacions, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = SkylineParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 17
                self.match(SkylineParser.T__0)
                self.state = 18
                self.operacions(0)
                self.state = 19
                self.match(SkylineParser.T__1)
                pass

            elif la_ == 2:
                localctx = SkylineParser.MirallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(SkylineParser.SUB)
                self.state = 22
                self.operacions(6)
                pass

            elif la_ == 3:
                localctx = SkylineParser.AssignacioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(SkylineParser.ID)
                self.state = 24
                self.match(SkylineParser.ASSIG)
                self.state = 25
                self.operacions(2)
                pass

            elif la_ == 4:
                localctx = SkylineParser.IdentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.sky()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.UnioInterContext(self, SkylineParser.OperacionsContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operacions)
                        self.state = 29
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 30
                        _la = self._input.LA(1)
                        if not(_la==SkylineParser.MUL or _la==SkylineParser.PLUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        self.operacions(6)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ReplicacioContext(self, SkylineParser.OperacionsContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operacions)
                        self.state = 32
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 33
                        self.match(SkylineParser.MUL)
                        self.state = 34
                        self.match(SkylineParser.INT)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.DesplaçamentContext(self, SkylineParser.OperacionsContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operacions)
                        self.state = 35
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 36
                        _la = self._input.LA(1)
                        if not(_la==SkylineParser.SUB or _la==SkylineParser.PLUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        self.match(SkylineParser.INT)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SkyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def creacions(self):
            return self.getTypedRuleContext(SkylineParser.CreacionsContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_sky

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSky" ):
                return visitor.visitSky(self)
            else:
                return visitor.visitChildren(self)




    def sky(self):

        localctx = SkylineParser.SkyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sky)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(SkylineParser.ID)
                pass
            elif token in [SkylineParser.T__0, SkylineParser.T__3, SkylineParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.creacions()
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


    class CreacionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple(self):
            return self.getTypedRuleContext(SkylineParser.SimpleContext,0)


        def compost(self):
            return self.getTypedRuleContext(SkylineParser.CompostContext,0)


        def aleatori(self):
            return self.getTypedRuleContext(SkylineParser.AleatoriContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_creacions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreacions" ):
                return visitor.visitCreacions(self)
            else:
                return visitor.visitChildren(self)




    def creacions(self):

        localctx = SkylineParser.CreacionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_creacions)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.simple()
                pass
            elif token in [SkylineParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.compost()
                pass
            elif token in [SkylineParser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.aleatori()
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


    class SimpleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.INT)
            else:
                return self.getToken(SkylineParser.INT, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_simple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple" ):
                return visitor.visitSimple(self)
            else:
                return visitor.visitChildren(self)




    def simple(self):

        localctx = SkylineParser.SimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(SkylineParser.T__0)
            self.state = 53
            self.match(SkylineParser.INT)
            self.state = 54
            self.match(SkylineParser.T__2)
            self.state = 55
            self.match(SkylineParser.INT)
            self.state = 56
            self.match(SkylineParser.T__2)
            self.state = 57
            self.match(SkylineParser.INT)
            self.state = 58
            self.match(SkylineParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompostContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.INT)
            else:
                return self.getToken(SkylineParser.INT, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_compost

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompost" ):
                return visitor.visitCompost(self)
            else:
                return visitor.visitChildren(self)




    def compost(self):

        localctx = SkylineParser.CompostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_compost)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(SkylineParser.T__3)
            self.state = 61
            self.match(SkylineParser.T__0)
            self.state = 62
            self.match(SkylineParser.INT)
            self.state = 63
            self.match(SkylineParser.T__2)
            self.state = 64
            self.match(SkylineParser.INT)
            self.state = 65
            self.match(SkylineParser.T__2)
            self.state = 66
            self.match(SkylineParser.INT)
            self.state = 67
            self.match(SkylineParser.T__1)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.T__2:
                self.state = 68
                self.match(SkylineParser.T__2)
                self.state = 69
                self.match(SkylineParser.T__0)
                self.state = 70
                self.match(SkylineParser.INT)
                self.state = 71
                self.match(SkylineParser.T__2)
                self.state = 72
                self.match(SkylineParser.INT)
                self.state = 73
                self.match(SkylineParser.T__2)
                self.state = 74
                self.match(SkylineParser.INT)
                self.state = 75
                self.match(SkylineParser.T__1)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(SkylineParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AleatoriContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.INT)
            else:
                return self.getToken(SkylineParser.INT, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_aleatori

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAleatori" ):
                return visitor.visitAleatori(self)
            else:
                return visitor.visitChildren(self)




    def aleatori(self):

        localctx = SkylineParser.AleatoriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_aleatori)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(SkylineParser.T__5)
            self.state = 84
            self.match(SkylineParser.INT)
            self.state = 85
            self.match(SkylineParser.T__2)
            self.state = 86
            self.match(SkylineParser.INT)
            self.state = 87
            self.match(SkylineParser.T__2)
            self.state = 88
            self.match(SkylineParser.INT)
            self.state = 89
            self.match(SkylineParser.T__2)
            self.state = 90
            self.match(SkylineParser.INT)
            self.state = 91
            self.match(SkylineParser.T__2)
            self.state = 92
            self.match(SkylineParser.INT)
            self.state = 93
            self.match(SkylineParser.T__6)
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
        self._predicates[1] = self.operacions_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def operacions_sempred(self, localctx:OperacionsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




