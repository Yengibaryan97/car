import datetime



class CarMarket:
    del_car = []
    existing_car = {}

    @staticmethod
    def add_car(car, seller):
        if f"{seller.name} {seller.surname}" not in CarMarket.existing_car:
            CarMarket.existing_car[f"{seller.name} {seller.surname}"] = []
        CarMarket.existing_car[f"{seller.name} {seller.surname}"].append([car.name, car.price])
        return CarMarket.existing_car

    def __remove_car(self, car):
        CarMarket.del_car.append(CarMarket.existing_car.pop(car.name))
        return CarMarket.del_car

    def _set_discount(self, car, size_discount):
        car.discount = size_discount

    def set_discount(self, car, size_discount=0):
        return self._set_discount(car, size_discount)

    def get_sold_car_history(self, seller):
        return f"{seller.sold_cars}"

    def return_car(self, car, seller):
        car_return = False
        if car_return:
            self.add_car(car, seller)
            CarMarket.existing_car[f"{seller.name} {seller.surname}"][1].append(f"{car.name} returned car")
        return CarMarket.existing_car[f"{seller.name} {seller.surname}"]

    def _get_seller_available_cars(self, seller):
        if f"{seller.name} {seller.surname}" not in CarMarket.existing_car:
            return []
        return CarMarket.existing_car[f"{seller.name} {seller.surname}"]

    def get_seller_available_cars(self, seller):
        return self._get_seller_available_cars(seller)

    def _get_car_available_discount(self, car):
        return car.discount

    @staticmethod
    def date():
        date_info = datetime.date.today()
        return date_info


class Car:
    def __init__(self, name, price, discount=0):
        self.price = price
        self.name = name
        self.discount = discount


class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city


class Seller(Person):
    def __init__(self, name, surname, city, cars):
        super().__init__(name, surname, city)
        self.car_shop = CarMarket()

        self.full_name = f"{self.name} {self.surname}"
        self.add_cars(cars)
        self.car_park = self.car_shop.get_seller_available_cars(self)
        self.money = 0
        self.sold_cars = []

    def add_cars(self, cars):
        if self.full_name not in self.car_shop.existing_car:
            self.car_shop.existing_car[self.full_name] = []
        for car in cars:
            self.car_shop.existing_car[self.full_name].append([car.name, car.price])

    def sell(self, car, buyer):  # ??????????? #nayeeeelll
        if [car.name, car.price] in self.car_park:
            self.money = self.__add_money(self.money, car.price, car.discount)
            self.add_sold_car(car, buyer)
            self.car_park.remove([car.name, car.price])

            return f"{self.name} sell his {car.name} to {buyer.name} and he have already had {self.money}"
        return f"{self.name} haven't already {car.name} and have {self.money}"

    @staticmethod
    def __add_money(where_add, money, discount):
        where_add += money * (100 - discount) / 100
        return where_add

    @staticmethod
    def __cut_down_money(where_less, money, discount):
        where_less -= money * (100 - discount) / 100
        return where_less

    def return_car(self, car, buyer):
        print("I take back my car")
        self.car_shop.add_car(car, self)
        self.money = self.__cut_down_money(self.money, car.price, car.discount)
        buyer.money = self.__add_money(buyer.money, car.price, car.discount)

        CarMarket.existing_car[self.full_name].append("Warning returned car")

        return CarMarket.existing_car[self.full_name]

    def check_discount(self, car):
        if car.discount == 0:
            return False
        return True

    @staticmethod
    def get_car_available_discount(size_discount):
        return size_discount

    def add_sold_car(self, car, buyer):
        self.sold_cars.append((car.name, car.price, car.discount, buyer.name, buyer.surname, buyer.city, self.car_shop.date()))
        return self.sold_cars


class Buyer(Person):
    money = 10000
    spent_money = 0
    bought_car = {}

    def __init__(self, name, surname, city):
        super().__init__(name, surname, city)

    def buy(self, car, seller):
        for i in range(len(seller.car_park)):
            if [car.name, car.price] in seller.car_park and self.money > car.price:
                seller.sell(car, self)
                self.money = self.__cut_down_money(self.money, car.price, car.discount)
                seller.money = self.__add_money(seller.money, car.price, car.discount)
                self.bought_car = self.add_bought_cars(car, seller)
                self.spent_money = self.__add_money(self.spent_money, car.price, car.discount)
                return f"{self.name} have already had {self.money} and buy {self.bought_car} spent {self.spent_money} dollar"
            elif car.name in seller.car_park[i] and self.money < car.price:
                return f"{self.name} don't have enough money"
        return f"{car} don't exist"

    def return_car(self, car, seller):
        print("sorry I can't love this car")
        self.spent_money = self.__cut_down_money(self.spent_money, car.price, car.discount)
        self.money = self.__add_money(self.money, car.price, car.discount)
        seller.money = self.__add_money(seller.money, car.price, car.discount)
        self.bought_car.pop(car.name)
        seller.add_cars([car])
        # CarMarket.existing_car[seller.full_name].append("Warning returned car")
        print(CarMarket.existing_car[seller.full_name], '-' * 100)
        for i in range(len(CarMarket.existing_car[seller.full_name])):
            if CarMarket.existing_car[seller.full_name][i] == [car.name, car.price]:
                CarMarket.existing_car[seller.full_name][i].append("Warning returned car")
        return CarMarket.existing_car[seller.full_name]

    @staticmethod
    def __add_money(where_add, money, discount):
        where_add = where_add + money * (100 - discount) / 100
        return where_add

    @staticmethod
    def __cut_down_money(where_less, money, discount):
        where_less -= money * (100 - discount) / 100
        return where_less

    def add_bought_cars(self, car, seller):
        self.bought_car[car.name] = (seller.name, seller.surname, CarMarket.date())
        return self.bought_car

    def print_my_cars(self):
        print(self.bought_car)


car = Car("Opel", 3000, 30)
jhon = Seller('Jhon', 'Smith', "London", [car])
print('-' * 100)
print(jhon.car_park)
car_shop = CarMarket()
car1 = Car("kia", 5000)  # gago
car_shop.add_car(car1, jhon)
print(jhon.car_park)
robert = Buyer('Robert', "Lee", "Moscow")
print('-' * 100)
# print(jhon.sell(car1,robert))
print(robert.buy(car, jhon))
print(jhon.car_park)
# print(jhon.return_car(car,robert))
print(jhon.car_park)
print(robert.return_car(car, jhon))
print(robert.money)
print(car_shop.get_sold_car_history(jhon))

