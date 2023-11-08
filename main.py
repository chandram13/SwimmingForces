# Marvish Chandra

# General formula
# Changes in the four drills


def generaLFormula(distance,armCycles,cycles,time):
    distanceperstroke = distance / armCycles
    strokeRate = cycles / time
    secondsStroke = time/ cycles


# algebraic expression behind swimming
# d, total drag
# q, dyanmic pressure, SA = Surface Area
# fD, fluid density
# v, velocity
# w, weight
# K = constant of proportionality

def totalDrag(D,q,SA,Q,fD,V,K,W):
    swimmerDrag = [((D / (q * SA)) * (1 / 2 * Q * (V * V)) * SA) + (K * (W * W) / (1 / 2 * fD * V * V) * SA)]
