# Marvish Chandra

# General formula
# Changes in the four drills


def generaLFormula(distance,armCycles,cycles,time):
    distanceperstroke = distance / armCycles
    strokeRate = cycles / time
    secondsStroke = time/ cycles

    print(distanceperstroke)
    print(strokeRate)
    print(secondsStroke)


# algebraic expression behind swimming
# d, total drag
# q, dyanmic pressure, SA = Surface Area
# fD, fluid density
# v, velocity
# w, weight
# K = constant of proportionality

def totalDrag(D,q,SA,Q,fD,V,K,W):
    swimmerDrag = [((D / (q * SA)) * (1 / 2 * Q * (V * V)) * SA) + (K * (W * W) / (1 / 2 * fD * V * V) * SA)]
    print(swimmerDrag)

# D, drag
# F, force
# R, turnover rate

# Applying arm acceleration for greatest velocity equation
def armAccel(D,F,R):
    swimmingSpeed = F * R - D
    print(swimmingSpeed)

# calculating buoyancy for a swimmer, force behind swimmer to float and not sink (larger the better)
# p = fluid density, V = volume, g = acceleration (-9.8)

def buoyancy(p,V,g):
    givenBuoyancy = p * V * g
    print(givenBuoyancy)


