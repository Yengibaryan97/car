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
