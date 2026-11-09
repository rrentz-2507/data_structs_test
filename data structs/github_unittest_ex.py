def findMaxSum(x,y,z):
    if x < y and x < z:
        return y + z
    elif y < x and y < z:
        return x + z
    else:
        return x + y