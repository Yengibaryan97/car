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

    def _set_discount(self, car, size_discount=0):
        car_discount = car.price - car.price * size_discount / 100
        return car_discount

    def set_discount(self, car, size_discount=0):
        return self._set_discount(car, size_discount)

    def get_sold_car_history(self, seller):
        pass

    # def __return_car(self, car, seller):
    #     car_return = False
    #     if car_return:
    #         print(f"I can't love {car.name}")
    #         CarMarket.existing_car[f"{seller.name} {seller.surname}"] = [car.name, car.price]

    def _get_seller_available_cars(self, seller):
        if f"{seller.name} {seller.surname}" in CarMarket.existing_car:
            return CarMarket.existing_car[f"{seller.name} {seller.surname}"]
        return []

    def get_seller_available_cars(self, seller):
        return self._get_seller_available_cars(seller)

    def _get_car_available_discount(self, car, seller, size_discount=0):
        has_discount = seller.check_discount(seller.seller_car)
        if has_discount:
            return self._set_discount(car, size_discount)
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
    def __init__(self, name, surname, city, cars):
        super().__init__(name, surname, city)
        self.car_shop = CarMarket()

        self.full_name = f"{self.name} {self.surname}"
        self.add_cars(cars)
        self.car_park = self.car_shop.get_seller_available_cars(self)
        self.money = 0
        self.sold_cars = []

    def add_cars(self, cars):
        self.car_shop.existing_car[self.full_name] = []
        for car in cars:
            self.car_shop.existing_car[self.full_name].append([car.name, car.price])

    def sell(self, car, buyer):  # ??????????? #nayeeeelll
        if car.name in self.car_park:
            self.__add_money(self.money, car.price)
            self.add_sold_car(car, buyer)

            return f"{self.name} sell his {car.name} to {buyer.name} and he have already had {self.money}"
        return f"{self.name} haven't already {car.name} and have {self.money}"

    @staticmethod
    def __add_money(where_add, money):
        where_add += money

    @staticmethod
    def __cut_down_money(where_less, money):
        where_less -= money

    # 3. return_car - ընդունելու է վերադարձի մեքենան։ Այստեղ պետք է նվազի վաճառողի
    # գումարը, ավլանա գնորդի գումարը, CarMar
    # ket֊ում փոխվի մեքենայի ստատւսը (պետք է գրվի վերադառձի մասին ինֆօ)։ Լինելու է public method
    def return_car(self, car, buyer):  # ????????????
        print("I take back my car")
        self.car_shop.add_car(car, self)
        self.__cut_down_money(self.money, car.price)
        self.__add_money(buyer.money, car.price)
        CarMarket.existing_car[self.full_name][car.name, car.price] = "Warning returned car"  # ewswsws
        return CarMarket.existing_car[f"{self.name} {self.surname}"]

    def check_discount(self, car):
        if CarMarket.existing_car[self.full_name][car.name] != car_shop.set_discount(car, size_discount=0):
            return True
        return False

    @staticmethod
    def get_car_available_discount(size_discount):
        return size_discount

    def add_sold_car(self, car, buyer):
        self.sold_cars.append((car.name, buyer.name, buyer.surname, buyer.city, self.car_shop.date))
        return self.sold_cars


class Buyer(Person):
    money = 10000
    spent_money = 0
    bought_car = {}

    def __init__(self, name, surname, city):
        super().__init__(name, surname, city)

    def buy(self, car,seller):
        if car.name in seller.car_park[seller.full_name] and self.money > car.price:
            seller.sell(car, self)
            self.__cut_down_money(self.money, car.price)
            self.__add_money(seller.money, car.price)
            self.add_bought_cars(car, seller)
            self.__add_money(self.spent_money, car.price)
        elif car.name in seller.car_park[seller.full_name] and self.money < car.price:
            return f"{self.name} don't have enough money"
        return f"{car} don't exist"

    def return_carr(self, car, seller):
        print("sorry I can't love this car")
        self.__cut_down_money(self.spent_money, car.price)
        self.__add_money(self.money, car.price)
        self.__add_money(seller.money, car.price)
        CarMarket.existing_car[seller.full_name][car.name, car.price] = "Warning returned car"
        self.bought_car.pop(car.name)
        return CarMarket.existing_car[seller.full_name]

    @staticmethod
    def __add_money(where_add, money):
        where_add += money

    @staticmethod
    def __cut_down_money(where_less, money):
        where_less -= money

    def add_bought_cars(self, car, seller):
        self.bought_car[car.name] = (seller.name, seller.surname, CarMarket.date())
        return self.bought_car

    def print_my_cars(self):
        print(self.bought_car)


car = Car("Opel", 'jhon', 3000)
jhon = Seller('Jhon', 'Smith', "London", [car])
print(jhon.car_park)
car_shop = CarMarket()
car1 = Car("kia", 'gago', 5000)
car_shop.add_car(car1, jhon)
robert = Buyer('Robert', "Lee", "Moscow")
jhon.sell(car1,robert)
print(robert.buy(car1,jhon))
print(car_shop.existing_car)
