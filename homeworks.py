class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def eat(self):
        print(f"{self.name} їсть")
        self.hunger -= 20
        self.energy += 10
        self.happiness += 5
        self._check_limits()

    def sleep(self):
        print(f"{self.name} спить")
        self.energy += 30
        self.hunger += 10
        self._check_limits()

    def play(self):
        print(f"{self.name} грається")
        self.happiness += 20
        self.energy -= 15
        self.hunger += 10
        self._check_limits()

    def walk(self):
        if self.species == "собака":
            print(f"{self.name} йде на прогулянку")
            self.happiness += 15
            self.energy -= 10
            self.hunger += 10
        else:
            print(f"{self.name} не любить гуляти")
            self.happiness -= 5
        self._check_limits()

    def _check_limits(self):

        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))
        self.happiness = max(0, min(100, self.happiness))

    def status(self):
        print(f"\nСтан {self.name}:")
        print(f"  Голод: {self.hunger}")
        print(f"  Енергія: {self.energy}")
        print(f"  Щастя: {self.happiness}")


cat = Pet("Мурчик", "кіт")
dog = Pet("Рекс", "собака")

cat.eat()
cat.play()
cat.sleep()
cat.status()



dog.walk()
dog.play()
dog.eat()
dog.status()
