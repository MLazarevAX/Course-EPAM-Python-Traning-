from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(
            self,
            brand_name: str,
            year_of_issue: int,
            base_price: int,
            mileage: int
    ):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    @abstractmethod
    def wheels_num(self) -> int:
        return 0

    @property
    def brand_name(self):
        return self.__brand_name

    @brand_name.setter
    def brand_name(self, value):
        if not isinstance(value, str):
            raise TypeError("brand_name must be str")
        self.__brand_name = value

    @property
    def year_of_issue(self):
        return self.__year_of_issue

    @year_of_issue.setter
    def year_of_issue(self, value):
        if not isinstance(value, int):
            raise TypeError("year_of_issue must be int")
        if value >= 2022:
            raise ValueError("year_of_issue must be < 2022  ")
        self.__year_of_issue = value

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, value):
        if not isinstance(value, int):
            raise TypeError("base_price must be int")
        self.__base_price = value

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        if not isinstance(value, int):
            raise TypeError("mileage must be int")
        self.__mileage = value

    def vehicle_type(self) -> str:
        return f"{self.brand_name} {self.__class__.__name__}"

    def is_motorcycle(self) -> bool:
        if self.__class__.__name__ == "Motorcycle":
            return True
        return False

    @property
    def purchase_price(self) -> float:
        purchase_price = self.base_price - 0.1 * self.mileage
        if purchase_price >= 100000:
            return purchase_price
        return 100000


# Don't change class implementation
class Car(Vehicle):
    def wheels_num(self):
        return 4


# Don't change class implementation
class Motorcycle(Vehicle):
    def wheels_num(self):
        return 2

    def isclass(self):
        print(self.__name__)


# Don't change class implementation
class Truck(Vehicle):
    def wheels_num(self):
        return 10


# Don't change class implementation
class Bus(Vehicle):
    def wheels_num(self):
        return 6

if __name__ == "__main__":
    vehicles = (
        Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
        Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
        Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
        Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
    )

    for vehicle in vehicles:
        print(
            f"Vehicle type={vehicle.vehicle_type()}\n"
            f"Is motorcycle={vehicle.is_motorcycle()}\n"
            f"Purchase price={vehicle.purchase_price}\n"
        )