# 3.3.8 OOP Balakirev
class RadiusVector:
    def __init__(self, n, *args) -> None:
        self.n = n
        self.args = [*args]
        if len(self.args) == 0:
            
    
    def set_coords(self, *args):
        pass

    def get_coords(self, *args):
        pass

    def len(vector):
        return len(vector)
    
    def abs(vector):
        pass


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)