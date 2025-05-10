class retangulo():
    def __init__(self):
        self.largura = int(input("qual a largura? \n"))
        self.altura = int(input("qual a altura \n"))

    def area(self):
        area = (self.largura*self.altura)
        return f"A area do retangulo é {area}"

areaRetangulo = retangulo()

print(areaRetangulo.area())