# Generated from Skyline.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser
import random
import skyline as sk

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):
    def __init__(self):
        self.identificadors = {}

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#assignacio.
    def visitAssignacio(self, ctx:SkylineParser.AssignacioContext):
        ident = ctx.ID().getText()
        assig = self.visit(ctx.operacions())
        self.identificadors[ident] = assig
        return (self.identificadors, ident)


    # Visit a parse tree produced by SkylineParser#unioInter.
    def visitUnioInter(self, ctx:SkylineParser.UnioInterContext):
        plot1 = self.visit(ctx.operacions(0))
        plot2 = self.visit(ctx.operacions(1))
        if (ctx.PLUS()):
            return plot1+plot2
        else:
            # Fer la interseccio dels plots
            result = sk.intersection(plot1,plot2)
            return result


    # Visit a parse tree produced by SkylineParser#mirall.
    def visitMirall(self, ctx:SkylineParser.MirallContext):
        plot1 = self.visit(ctx.operacions())
        # Retorna el plot reflectit (voltear horiz.)
        yrev = [x[1] for x in plot1][::-1]
        xmin = [x[0] for x in plot1]
        xmax = [x[2] for x in plot1]
        mirror_build = zip(xmin,yrev,xmax)
        return list(mirror_build)

    # Visit a parse tree produced by SkylineParser#ident.
    def visitIdent(self, ctx:SkylineParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#replicacio.
    def visitReplicacio(self, ctx:SkylineParser.ReplicacioContext):
        plot1 = list(self.visit(ctx.operacions()))
        x = int(ctx.INT().getText())
        #Conseguir amplada del plot
        maxim = plot1[-1][2]
        minim = plot1[-1][0]
        for (xmin, y, xmax) in plot1:
            if(xmin < minim): minim = xmin
            if(xmax > maxim): maxim = xmax
        amplada = maxim - minim
        plotaux = plot1
        # Replicar X vegades el plot
        for i in range(1,x):
            new_plot = [ (xmin+amplada,y,xmax+amplada) for (xmin,y,xmax) in plotaux]
            plot1.extend(new_plot)
            plotaux = new_plot
        return plot1


    # Visit a parse tree produced by SkylineParser#desplaçament.
    def visitDesplaçament(self, ctx:SkylineParser.DesplaçamentContext):
        plot1 = self.visit(ctx.operacions())
        x = int(ctx.INT().getText())
        if(ctx.PLUS()):
            # Desplaçar a la dreta
            new_plot = [ (xmin+x,y,xmax+x) for (xmin,y,xmax) in plot1]
        else:
            new_plot = [ (xmin-x,y,xmax-x) for (xmin,y,xmax) in plot1]
        return new_plot


    # Visit a parse tree produced by SkylineParser#parenthesis.
    def visitParenthesis(self, ctx:SkylineParser.ParenthesisContext):
        return self.visit(ctx.operacions())


    # Visit a parse tree produced by SkylineParser#sky.
    def visitSky(self, ctx:SkylineParser.SkyContext):
        if(ctx.ID()): 
            index = ctx.ID().getText()
            if(self.identificadors[index]):
                return self.identificadors[index]
            else:
                print("Error: el skyline no existeix")
        else:
            return self.visit(ctx.creacions())


    # Visit a parse tree produced by SkylineParser#creacions.
    def visitCreacions(self, ctx:SkylineParser.CreacionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#simple.
    def visitSimple(self, ctx:SkylineParser.SimpleContext):
        xmin = int(ctx.INT(0).getText())
        alt = int(ctx.INT(1).getText())
        xmax = int(ctx.INT(2).getText())

        if(xmax > xmin and alt > 0):
            #Crear plot
            return [(xmin, alt, xmax)]
        else:
            print("Error: els parametres indicats no son correctes")


    # Visit a parse tree produced by SkylineParser#compost.
    def visitCompost(self, ctx:SkylineParser.CompostContext):
        buildings = []
        for i in range(0, len(ctx.INT()),3):
            xmin = int(ctx.INT(i).getText())
            alt = int(ctx.INT(i+1).getText())
            xmax = int(ctx.INT(i+2).getText())
            buildings.append((xmin, alt, xmax))
            #Crear plot
        return buildings


    # Visit a parse tree produced by SkylineParser#aleatori.
    def visitAleatori(self, ctx:SkylineParser.AleatoriContext):
        n = int(ctx.INT(0).getText())
        h = int(ctx.INT(1).getText())
        w = int(ctx.INT(2).getText())
        xmin = int(ctx.INT(3).getText())
        xmax = int(ctx.INT(4).getText())
        buildings = []
        if(n > 0 and h >= 0 and w >= 1 and xmax > xmin):
            for i in range(n):
                alt = random.randint(0, h)
                amp = random.randint(1, w)
                ini = random.randint(xmin,xmax)
                fi = ini + amp
                buildings.append((ini,alt,fi))
            #Crear plot
            return buildings

        else:
            print ("Error: els parametres indicats no son correctes")


del SkylineParser