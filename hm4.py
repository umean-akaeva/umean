class Tvarina:
    def __init__(self, imya, vik):
        self.imya = imya
        self.vik = vik

    def zvuk(self):
        print("Тварина видає звук")

    def info(self):
        print(f"Ім'я: {self.imya}, Вік: {self.vik} років")



class Sobaka(Tvarina):
    def zvuk(self):
        print("Гав-гав!")

    def prynesty_palicu(self):
        print(f"{self.imya} приніс палку!")



class Kit(Tvarina):
    def zvuk(self):
        print("Мяу-мяу!")

    def lovyty_mishu(self):
        print(f"{self.imya} впіймав мишу!")



sobaka = Sobaka("Бім", 3)
kit = Kit("Мурчик", 2)


sobaka.info()
sobaka.zvuk()
sobaka.prynesty_palicu()

kit.info()
kit.zvuk()
kit.lovyty_mishu()
