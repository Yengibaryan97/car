class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city


class Seller(Person):
    car_park = {"BMW": 10000, "KIA": 6000, "AUDI": 8000, "LADA": 3000}
    sold_cars = {}

    def __init__(self, name, surname, city):
        super().__init__(name, surname, city)
        self.money = 0

    def sell(self, car_model):
        if car_model in Seller.car_park:
            money = self.car_price(car_model)
            self.change_money(money)
            message = self.add_sold_car(car_model)
        else:
            message = "Good bye"
        return message

    def change_money(self, money):
        self.money += money

    # TODO add function which will print seller money+
    # TODO add function which will return car prise+
    def print_info_money(self):
        print(self.money)

    @staticmethod
    def car_price(car_model):
        return Seller.car_park[car_model]

    def add_sold_car(self, car_model):
        Seller.sold_cars[car_model] = self.car_price(car_model)
        return f"I will sell {car_model} for {self.car_price(car_model)}"


class Buyer(Person):

    def __init__(self, name, surname, city, money):
        super().__init__(name, surname, city)
        self.money = money
        self.spent_money = 0
        self.bought_cars = []

    # def enough_money(self, car_model):
    #     if self.money >= Seller.car_price(car_model):
    #         return self.change_money(car_model)
    #     else:
    #         return "I can't buy this car, sorry"

    def change_money(self, seller, car_model):
        print(f"{self.name} buy this car")
        self.money = self.money - seller.car_price(self, car_model)
        self.spent_money = self.spent_money + seller.car_price(car_model)
        return f"{self.name} spent {self.spent_money} and {self.name} have already had {self.money} dollar and " \
               f"{seller.name} get {self.spent_money} dollar for {car_model}"

    def buy(self, seller, wanted_car):
        seller.sell(wanted_car)
        if wanted_car in Seller.car_park and self.money > seller.car_price(wanted_car):
            return self.change_money(seller.name, wanted_car)
        elif wanted_car in Seller.car_park and self.money < seller.car_price(wanted_car):
            return f"{self.name} don't have enough money"
        return f"{wanted_car} don't exist"


john = Seller("John", "Smith", "New York")

simon = Buyer("Simon", "Lee", "New York", 13000)

print(simon.buy(john, "LADA"))
print(john.sell("KIA"))
print(john.sold_cars)
