class Animal():
    def __init__(self, nom, atribut, edat):
        self.nom = nom
        self.atribut = atribut
        self.edat = edat

    def xerrar(self):
        pass

    def moure(self):
        pass

    def quisoc(self):
        print("Soc un animal")


class Cavall(Animal):
    def __init__(self, nom, edat):
        super().__init__(nom, "Cavall", edat)

    def xerrar(self):
        print("iiiii")

    def moure(self):
        print("En moc a trot")

    def quisoc(self):
        print("Soc un cavall")


class Dolfi(Animal):
    def __init__(self, nom, edat):
        super().__init__(nom, "Dolfi", edat)

    def xerrar(self):
        print("ichcichich")

    def moure(self):
        print("En moc nadant")

    def quisoc(self):
        print("Soc un dolfí")


class Abella(Animal):
    def __init__(self, nom, edat):
        super().__init__(nom, "Abella", edat)

    def xerrar(self):
        print("bzzzz")

    def moure(self):
        print("En moc volant")

    def quisoc(self):
        print("Soc un abella")


class Huma(Animal):
    def __init__(self, nom, atribut, edat):
        super().__init__(nom, atribut, edat)

    def xerrar(self):
        print("hola")

    def moure(self):
        print("En moc caminant")

    def quisoc(self):
        print("Soc un huma")


class Centaure(Animal):
    def __init__(self, nom, atribut, edat):
        super().__init__(nom, atribut, edat)

    def xerrar(self):
        print("Hola nosaltres utilitzam un idioma per parlar ")

    def moure(self):
        print("En moc a trot")

    def quisoc(self):
        print("Soc un centaure")


class Fiet(Huma):
    def __init__(self, nom, atribut, edat, llpares):
        super().__init__(nom, atribut, edat)
        self.pares = llpares

    def xerrar(self):
        print("UeeeUeee")

    def moure(self):
        print("En moc gatetjant")

    def quisoc(self):
        print("Soc un Fiet")

    def nompares(self):
        for e in self.pares:
            print(e.nom)


class Xou():
    def xerrar(self):
        print("Xou")

    def moure(self):
        print("En moc xou")

    def quisoc(self):
        print("Soc un xou")


# Programa principal
a = [Cavall("Marro", 4), Dolfi("Gris", 10), Abella("Negre i grog", 0.5),
     Huma("Silba", "Cristia", 7), Centaure("Fiona", "Marro", 18),
     Fiet("Jordi", "Moreno", 9, ["Fiona i Marc"])]


for e in a:
    e.xerrar()
    e.moure()
    e.quisoc()
