class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'

    def getInfo(self):
        return f'{self.name} {self.surname}. {self.city}'

client_1 = Client('Иван','Петров','Москва',50)
client_2 = Client('Петр','Иванов','Пермь',100)

print(client_1)

clients = [client_1, client_2]
for client in clients:
    print(client.getInfo())