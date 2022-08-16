class Tetr:
    def __init__(self, AB=1, BC=1, AC=1, AD=1, BD=1, CD=1):
        self.AB = AB
        self.BC = BC
        self.AC = AC
        self.AD = AD
        self.BD = BD
        self.CD = CD

    def Height(self):
        return ((2 * self.AD) / 3) ** 0.5

    def Square(self, a, b, c):
        p = (a + b + c) / 2
        return (p * (p-a) * (p-b) * (p-c)) ** 0.5

    def Tetr_S(self):
        S1 = self.Square(self.AB, self.BC, self.AC)
        S2 = self.Square(self.AB, self.AD, self.BC)
        S3 = self.Square(self.BC, self.BD, self.CD)
        S4 = self.Square(self.AC, self.AD, self.CD)
        print(f'Площадь тетраэдара: {S1 + S2 + S3 + S4}')

    def Volume(self):
        V = (self.Square(self.AB, self.BC, self.AC) * self.Height()) / 3
        print(f'Объём тетраэдара: {V}')


t1 = Tetr()
t1.Tetr_S()
t1.Volume()