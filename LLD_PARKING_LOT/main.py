from classes.parking_lot_class import ParkingLot


class Main():
    def __init__(self) -> None:
        self.parking_lot = None
        self.stop = False
        self.start()
    
    def start(self):
        while not self.stop:
            command = int(input('1:create parking lot\n2:exit the parking lot'))
            commands = {
                1:self.create_parking_lot,
                2:self.exit_
            }
            commands[command]()

    def create_parking_lot(self):
        name = input('enter the name of the parkinglot: ')
        floors = int(input('enter the number of floors(minimum 1): '))
        no_of_slots = int(input('enter the number of slots per floor(minimum 4): '))
        if floors < 1 or no_of_slots < 4:
            print('Invalid Parking lot details')
        else:
            self.parking_lot = ParkingLot(name, floors, no_of_slots)

    def exit_(self):
        self.stop = True

Main()