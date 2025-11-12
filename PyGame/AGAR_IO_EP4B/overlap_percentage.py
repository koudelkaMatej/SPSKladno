import math

def overlap_percentage(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    vzdalenost1 = distance - r1
    vzdalenost2 = distance - r2
    if distance >= r1 + r2:
        return 0
    else:
        if vzdalenost1 > 5:
            return 100
        return 0