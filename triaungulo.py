from figura_geometrica import FiguraGeometrica


class Triangular(FiguraGeometrica):

    def __init__(self, ancho: float = 0.0, alto: float = 0.0):
        super().__init__()
        self.ancho = ancho
        self.alto = alto

    def __str__(self):
        return f'Triangular [alto = {self.alto}, ancho = {self.ancho}]'

    def calcular_area(self):
        return (self.ancho * self.alto) / 2


if __name__ == '__main__':
    t1 = Triangular(ancho=5, alto=8)
    print(f'el ancho es:', t1.ancho)
    print(f'el alto es:', t1.alto)
    print(f'el área es:', t1.calcular_area())

    t1.ancho = 10
    t1.alto = 6
    print(f'\nel ancho es:', t1.ancho)
    print(f'el alto es:', t1.alto)
    print(f'el área es:', t1.calcular_area())
