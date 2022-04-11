import datetime
class CarMarket:
    def __init__(self):
        self.__del_car = []
        self.existing_car = {}

    def add_car(self, car):
        self.existing_car[car.name] = [car.price, car.seller.name]
        return self.existing_car

    def __remove_car(self, car):
        self.del_car.extend((car.name, car.price,))
        self.existing_car.pop(car.name)
        return self.del_car

    def _set_discount(self, car, size_discount=0):
        self.dis = car.price - car.car_price() * size_discount / 100
        return self.dis

    def get_sold_car_history(self, seller):
        pass

    def return_car(self, car):
        __car_return = False
        if __car_return:
            print(f"I can't love {car.name}")
            self.existing_car[car.name] = [car.price, car.seller]

    def _get_seller_available_cars(self):
        return self.existing_car

    def _get_car_available_discount(self, car, seller,size_discount=0):
        self.ch = Seller.check_discount(seller,size_discount)
        if self.ch:
            return self.set_discount(car, size_discount=0)
        return car.price


    @staticmethod
    def date():
        date_info = datetime.date.today()
        return date_info

class Car:
    def __init__(self, name, seller, price):
        self.seller = seller
        self.price = price
        self.name = name


class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city


class Seller(Person):
    c = CarMarket()
    car_park = c._get_seller_available_cars()
    money = 0
    sold_cars = []

    def __init__(self, name, surname, city):
        super().__init__(name, surname, city)

    def sell(self, car):
        if car.name in Seller.car_park:
            self.change = self.change_money(car.price)
            Seller.money = self.change

    def change_money(self, money):
        Seller.money += money
        return Seller.money

    def return_car(self, car):
        pass

    def check_discount(self, size_discount):
        if size_discount != 0:
            return True
        return False

    @staticmethod
    def get_car_available_discount(size_discount):
        return size_discount

    def add_sold_car(self, car, buyer):
        Seller.sold_cars.extend((car.name, buyer.name, buyer.surname, buyer.city))


class Buyer(Person):
    money = 10000
    spent_money = 0
    bought_car = []

    def __init__(self, name, surname, city):
        super().__init__(name, surname, city)


jhon = Seller("Jhon", "Smith", "London")
c = Car("Opel", jhon, 3000)
k = CarMarket()
print(k._get_car_available_discount(c,jhon))
print(k.add_car(c))
print(k._get_seller_available_cars())
# b = Buyer("Robert", "Lee", "Amsterdam")
print(k.date())print(123456)
