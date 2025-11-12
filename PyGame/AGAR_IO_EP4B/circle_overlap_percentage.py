import math

def circle_overlap_percentage(x1, y1, r1, x2, y2, r2):
    # Calculate the distance between the centers
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # If the circles don't overlap
    if distance >= r1 + r2:
        return 0

    # If one circle is completely inside the other
    if distance <= abs(r1 - r2):
        smaller_area = math.pi * min(r1, r2)**2
        return smaller_area

    # Calculate the overlapping area
    r1_sq, r2_sq = r1**2, r2**2
    part1 = r1_sq * math.acos((distance**2 + r1_sq - r2_sq) / (2 * distance * r1))
    part2 = r2_sq * math.acos((distance**2 + r2_sq - r1_sq) / (2 * distance * r2))
    part3 = 0.5 * math.sqrt((-distance + r1 + r2) * (distance + r1 - r2) * (distance - r1 + r2) * (distance + r1 + r2))
    overlap_area = part1 + part2 - part3

    # Calculate the percentage overlap relative to the smaller circle
    smaller_area = math.pi * min(r1, r2)**2
    return (overlap_area / smaller_area) * 100