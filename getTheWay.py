import math
import random
def F(points):
    res = 0.0
    for i in range(len(points) - 1):
        res += math.sqrt(((points[i].x - points[i + 1].x) ** 2) + ((points[i].y - points[i + 1].y) ** 2))
    res += math.sqrt(((points[0].x - points[len(points) - 1].x) ** 2) + ((points[0].y - points[len(points) - 1].y) ** 2))
    return res
def getTheWay(points):
    if len(points) < 2:
        return points
    Q1 = F(points)
    cnt = 0
    temp = 8000.0
    while temp > 0.00001:
        cnt += 1
        pos1 = random.randint(0, len(points) - 1)
        pos2 = random.randint(0, len(points) - 1)
        tem = points[pos2]
        points[pos2] = points[pos1]
        points[pos1] = tem
        Q2 = F(points)
        R = Q2 - Q1
        if R <= 0:
            Q1 = Q2
        else:
            P = math.exp(-R/temp)
            if random.random() < P:
                Q1 = Q2
            else:
                tem = points[pos2]
                points[pos2] = points[pos1]
                points[pos1] = tem
        temp *= 0.9997
    return points