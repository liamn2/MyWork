# 3609. Minimum Moves to Reach Target in Grid
class Solution(object):
    def minMoves(self, sx, sy, tx, ty):
        self.sx = None
        self.sy = None
        self.tx = None
        self.ty = None
        
        S = (sx, sy)
        T = (tx, ty)

        X = abs(sx) - abs(tx)
        Y = abs(sy) - abs(ty)

        if abs(X) > abs(Y):
            return abs(Y)
        elif abs(Y) > abs(X):
            return abs(X)
        #elif X==Y:
        elif X<0 or Y<0:
            return -1
