# Напишите класс, который описывает тетраэдр по заданным в конструкторе длинам сторон

# Добавьте методы, вычисляющие площадь поверхности и объём тетраэдра

# Продемонстрируйте на экземпляре

class Tetr:
    def __init__(self, AB=1, BC=1, AC=1, AD=1, BD=1, CD=1):
        self.AB = AB
        self.BC = BC
        self.AC = AC
        self.AD = AD
        self.BD = BD
        self.CD = CD

    def Height(self):
        return ((2 * self.AB) / 3) ** 0.5

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


    def Square2(self):
        return (self.AB * self.Height()) / 2

    def Tetr_S2(self):
        S1 = self.Square2()
        S2 = self.Square2()
        S3 = self.Square2()
        S4 = self.Square2()
        print(f'Площадь тетраэдара: {S1 + S2 + S3 + S4}')

    def Tetr_S3(self):
        print((3 ** 0.5) * (self.AB ** 3))


tetr1 = Tetr()

tetr1.Tetr_S()
tetr1.Volume()


# print(tetr1.Height())
print(tetr1.Square(1, 1, 1))
print(tetr1.Square2())
tetr1.Tetr_S2()
tetr1.Tetr_S3()