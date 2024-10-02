class Octant:
    def __init__(self, n, d=0):
        self.n = n
        self.cone = [[d]*i for i in range(n,0,-1)]
        
    def check(self, x, y):
        if not (0 <= y <= x < self.n):
            raise IndexError(f"Les coordonnées ne sont pas valides : x={x}, y={y}, n={self.n}")

        
    def get(self, x,y):
        pass
        
    def set(self, x, y, d):
        pass
    
    def __str__(self):
        mes = ""
        for i in range(self.n):
            mes = " "*i + str(self.cone[(4-i)]) +"\n"
        return mes
        
        
o = Octant(5)
print(o.cone)
o.check(4,3)
print(str(o))