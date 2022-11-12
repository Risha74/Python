class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def gatName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

    def getInfo(self):
        print(f'Имя животного: {self.name}\nПол животного: {self.gender}\nВозраст животного: {self.age}')

