from abc import ABC, abstractmethod


class SlotTypeInterface(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.name = None
        self.price = None

    @abstractmethod
    def price_calculation(self, hours):
        pass


class CarSlot(SlotTypeInterface):
    def __init__(self, price) -> None:
        super().__init__()
        self.name = 'Car'
        self.price = price

    def price_calculation(self, hours):
        return self.price * int(hours)


class BikeSlot(SlotTypeInterface):
    def __init__(self, price) -> None:
        super().__init__()
        self.name = 'Bike'
        self.price = price

    def price_calculation(self, hours):
        return self.price * int(hours)


class TruckSlot(SlotTypeInterface):
    def __init__(self, price) -> None:
        super().__init__()
        self.name = 'Truck'
        self.price = price

    def price_calculation(self, hours):
        return self.price * int(hours)


class SlotFactory():
    def __init__(self, truck_price, car_price, bike_price) -> None:
        self.factory = {
            'Car': CarSlot(car_price),
            'Bike': BikeSlot(bike_price),
            'Truck': TruckSlot(truck_price)
        }

    def slot_factory(self, inp):
        return self.factory[inp]
