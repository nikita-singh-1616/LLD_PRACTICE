from classes.vehicle_class import Vehicle
from interfaces.slot_type_interface import SlotFactory
from classes.floor_class import Floor


class ParkingLot():
    def __init__(self,name,floors_no,slots_per_floor) -> None:
        self.name = name
        self.floors_no = floors_no
        self.no_of_slots_per_floor = slots_per_floor
        self.floors = []
        self.options = {
            1:self.park,
            2:self.unpark,
            3:self.display
        }
        self.get_info()
        
        

    
    def get_info(self):
        price_for_car = int(input('enter price for car slot: '))
        price_for_bike = int(input('enter price for bike slot: '))
        price_for_truck = int(input('enter price for truck slot: '))
        slot_factory = SlotFactory(price_for_truck,price_for_car,price_for_bike)
        for i in range(self.floors_no):
            self.floors.append(Floor(i+1,self.no_of_slots_per_floor,slot_factory))
        print(f'Parking Lot is ready\n')
        self.selection()


    def selection(self):
        while True:
            inp = input(f'1:park a vehicle\n2:unpark vehicle\n3:display vehicles\nexit:to exit')
            if inp == 'exit':
                return
            elif inp.isdigit() and int(inp) in self.options:
                self.options[int(inp)]()
            else:
                print('invalid input')

    def park(self):
        reg_no = input('enter vehicle reg no.: ')
        color = input('enter color of vehicle: ')
        type_ = input('enter type of vehicle(Car/Bike/Truck): ')
        vehicle_obj  = Vehicle(type_,reg_no,color)
        for i in self.floors:
            res = i.find_available_slot(vehicle_obj)
            if res:
                print(f"your vehicle has been parked. here is the ticket.{self.name+'_'+res}" )
                return 
        print('the parking lot is full.')
    
    def unpark(self):
        ticket_no = input('enter the ticket_no')
        vals = ticket_no.split('_')
        if len(vals)==3 and 0 not in vals and vals[0]== self.name and int(vals[1])<=self.floors_no and int(vals[2])<=self.no_of_slots_per_floor:
            floor = self.floors[int(vals[1])-1]
            price = floor.find_slot(int(vals[2]))
            if price == -1:
                return 'INVALID TICKETTT'
            else:
                print(f'Amount to be paid:{price}')


    
    def display(self):
        print('display')



