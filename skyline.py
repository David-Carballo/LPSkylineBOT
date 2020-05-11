import sys
from antlr4 import *
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.ticker import MaxNLocator
import pickle

from antlr4.InputStream import InputStream
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.SkylineVisitor import SkylineVisitor


# Processa una expressio
def compile(inp, visitor):
    input_stream = InputStream(inp)
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()
    result = visitor.visit(tree)
    return result


# Donada una llista d'edificis retorna la llista de punts necessaris pel Path
def get_skyline(buildings):
    if not buildings:
        return []
    if len(buildings) == 1:
        return [[buildings[0][0], buildings[0][1]], [buildings[0][2], 0]]

    mid = len(buildings) // 2
    left = get_skyline(buildings[:mid])
    right = get_skyline(buildings[mid:])
    return merge(left, right)


# Funcio auxiliar per get_skyline
def merge(left, right):
    y1, y2 = 0, 0
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            y1 = left[i][1]
            connect = left[i][0]
            i += 1
        elif right[j][0] < left[i][0]:
            y2 = right[j][1]
            connect = right[j][0]
            j += 1
        else:
            y1 = left[i][1]
            y2 = right[j][1]
            connect = right[j][0]
            i += 1
            j += 1
        if is_valid(result, max(y1, y2)):
            result.append([connect, max(y1, y2)])
    result.extend(right[j:])
    result.extend(left[i:])
    return result


# Funcio auxiliar per la funció merge
def is_valid(result, new_y):
    return not result or result[-1][1] != new_y


# Retorna el skyline reflectit
def mirror(buildings):
    yrev = [x[1] for x in buildings][::-1]
    xmin = [x[0] for x in buildings]
    xmax = [x[2] for x in buildings]
    mirror_build = zip(xmin, yrev, xmax)
    return list(mirror_build)


# Retorna el area i l'alçada del skyline
def get_info(plot):
    points = get_skyline(plot)
    area = 0
    ymax = 0
    for i in range(0, len(points)-1):
        area += points[i][1] * (points[i+1][0] - points[i][0])
        if(points[i][1] >= ymax):
            ymax = points[i][1]
    return (area, ymax)


# Donat tots els punts del plot
def all_points(points):
    new_points = []
    new_points.append(points[0])
    for i in range(0, len(points)-1):
        j = points[i][0]
        while (j < points[i+1][0]):
            new_points.append((j+1, points[i][1]))
            j += 1
    return new_points


# Retorna la intersecció de dos skylines
def intersection(plot1, plot2):
    p1 = all_points(get_skyline(plot1))
    p2 = all_points(get_skyline(plot2))

    xmin = min(p1[0][0], p2[0][0])
    xmax = max(p1[-1][0], p2[-1][0])

    dict1 = dict(p1)
    dict2 = dict(p2)
    valids = []
    first = True
    y = 0
    left = -1
    right = -1
    for i in range(xmin, xmax+1):
        aux = i
        if first:
            if(i in dict1 and i in dict2):
                right = i
                if(dict1[i] <= dict2[i]):
                    y = dict1[i]
                    left = i
                else:
                    y = dict2[i]
                    left = i
                first = False

        else:
            if(i in dict1 and i in dict2):
                right = i
                if((dict1[i] != y and dict2[i] != y)):
                    if(dict1[i] <= dict2[i]):
                        y = dict1[i]
                        left = i
                    else:
                        y = dict2[i]
                        left = i
    if(left != -1 and right != -1):
        valids.append((left, y, right))
    return valids


# Retorna l'amplada i l'altura del skyline
def get_measure(points):
    weight = points[len(points)-1][0]
    height = 0
    for [x, y] in points:
        if (y >= height):
            height = y
    return weight, height


# Retorna el plot del skyline
def get_plot(buildings):
    points = get_skyline(buildings)
    weight, height = get_measure(points)

    first_point = (points[0][0], 0)
    verts = []
    codes = []
    verts.append(first_point)
    codes.append(Path.MOVETO)
    for i in range(len(points)-1):
        verts.append(points[i])
        codes.append(Path.LINETO)
        verts.append((points[i+1][0], points[i][1]))
        codes.append(Path.LINETO)

    # Add final points
    verts.append(points[len(points)-1])
    codes.append(Path.LINETO)

    # Initialize the plot
    path = Path(verts, codes)
    poly = patches.Polygon(verts, facecolor='red', lw=2)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.add_patch(poly)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    return plt
