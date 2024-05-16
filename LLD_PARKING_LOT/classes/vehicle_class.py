from LLD_PARKING_LOT.interfaces.vehicle_interface import VehicleInterface


class Vehicle(VehicleInterface):
    def __init__(self,type_,reg_no,color) -> None:
        super().__init__(type_,reg_no,color)
        
    