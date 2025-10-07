class StepeniDvoiky:
    def __init__(self, max_stepin):
        self.max_stepin = max_stepin
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_stepin:
            result = 2 ** self.current
            self.current += 1
            return result
        else:
            raise StopIteration


iter_2 = StepeniDvoiky(5)

for num in iter_2:
    print(num)
