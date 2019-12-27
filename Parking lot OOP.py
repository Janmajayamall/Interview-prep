
class Space():

    def __init__(self, location, id, type):

        self.location=location
        self.id=id
        self.occupied=False
        self.assigned_vehicle=None
        self.space_type=type
    
    def park(self, vehicle):

        self.assigned_vehicle=vehicle
        self.occupied=True
    
    def unpark():

        self.occupied=False
        self.assigned_vehicle=None  

    
class CarSpace(Space):

    def __init__(self, location, id)
        super.__init__(location, id, 'Car')

class BikeSpace(Space):

    def __init__(self, location)
        super.__init__(location, id, 'Bike')

class Vehicle():

    def __init__(self, vehicle_number, model, type):

        self.id=vehicle_number
        self.model=model
        self.vehicle_type=
    
class Car(Vehicle):

    def __init__(self, vehicle_number, model):
        super.__init__(vehicle_number, model, 'Car')

class Bike(Vehicle):

    def __init__(self, vehicle_number, model):
        super.__init__(vehicle_number, model, 'Bike')

class VehicleHandler():

    def __init__(spaces):
        self.spaces=spaces
        self.vehicles_queue=[]
        self.free_spaces=self.spaces
        self.occupied_spaces=[]
    
    def addSpace(space):
        self.spaces.append(space)
        self.free_spaces.append(space)
    
    def parkVehicle(vehicle):

        if len(free_space)<=0:
            self.vehicles_queue.append(vehicle)
            return 
        
        free_space = self.free_spaces[0]
        self.free_spaces=self.free_spaces[1:]

        free_space.park(vehicle)
        self.occupied_spaces.append(free_space)

        return 

    def unpark(vehicle):

        space=None
        for spaces in self.occupied_spaces:

            if vehicle==spaces.assigned_vehicle:
                space=spaces

        if space==None:
            return
            
        space.unpark()

        mark=None
        if space.occupied:
            for index in range(len(self.occupied_spaces)):
                if space.id==self.occupied_spaces[index].id:
                    mark=index
                    break
            
        self.free_spaces.append(self.occupied_spaces[mark])
        self.occupied_spaces=self.occupied_spaces[:mark]+self.occupied_spaces[mark+1:]

        if len(self.vehicles_queue)>0:
            self.parkVehicle(self.vehicles_queue[0])
            self.vehicles_queue=self.vehicles_queue[1:]

        return        
    
class CarHandler(VehicleHandler):

    def __init__(spaces):
        super.__init__(spaces)

class BikeHandler(VehicleHandler):

    def __init__(spaces):
        super.__init__(spaces)

class ParkingLot():

    def __init__(car_spaces, bike_spaces):

        self.CarHandler=CarHandler(car_spaces)    
        self.BikeHandler=BikeHandler(bike_spaces)

    def park_vehicle(vehicle):
        if vehicle.type=='Car':
            self.CarHanlder.parkVehicle(car)
        else:
            self.CarHanlder.parkVehicle(car)
        
    def unpark(vehicle):
        if vehicle.type=='Car':
            self.CarHanlder.parkVehicle(car)
        else:
            self.CarHanlder.parkVehicle(car)
        

    

    
