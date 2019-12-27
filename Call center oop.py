# 1. Call center instance
#     employees
#     dispatchCall()
#     engage()
#     disengage()

# 2. employee
#     description of the employee

# 3. personal_attribute


class Employee():

    def __int__(self, employee_type, compensation_plan, office_location, personal_attributes):

        self.employee_type=employee_type
        self.compensation_plan=compensation_plan
        self.office_location=office_location
        self.personal_attributes=personal_attributes
        self.on_call=False
    
    def on_call(self):
        self.on_call=True

    def not_on_call(self):
        self.on_call=False
    
class Director(Employee):

    def __init__(self, personal_attributes):

        super.__init__('Director', 'Plan 1', 'London', personal_attributes)
    
    # def ....

class Respondants(Employee):

    def __init__(self, personal_attributes):

        super.__init__('Respondants', 'Plan 2', 'London', personal_attributes)
    
    # def ....

class Manager(Employee):

    def __init__(self, personal_attributes):

        super.__init__('Manager', 'Plan 3', 'London', personal_attributes)
    
    # def ....

class Person():

    def __init__(self, first_name, last_name, age, qualifications):

        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.qualifications=qualifications

class Caller():

    def __init__(self, callers_info, callers_location, callers_number):

        self.callers_info=callers_info
        self.callers_location=callers_location
        self.callers_number=callers_number
    
class Call():

    def __init__(self, employee, caller):

        self.employee=employee
        self.caller=caller

        self.engage()
    
    def engage(self):

        self.employee.on_call()
    
    def disengage(self):

        self.employee.not_on_call()
    
    def switch(new_caller):

        self.caller=new_caller


class CallCenter():

    def __init__(self, location='London', area):

        self.managers=[]
        self.respondants=[]
        self.directors=[]
        self.free_respondants=self.respondants
        self.free_managers=self.managers
        self.free_directors=self.directors
        self.occupied_respondants=[]
        self.occupied_managers=[]
        self.occupied_directors=[]
        self.call_queue=[]
        self.location=location
        self.area=area

    def add_director(self, Person):

        new_director = Director(Person)
        self.directors.append(new_director)
        self.free_directors.append(new_director)

    def add_manager(self, Person):

        new_manager = Manager(Person)
        self.managers.append(new_manager)
        self.free_managers.append(new_manager)

    def add_respondant(self, Person):

        new_respondant = Respondant(Person)
        self.respondants.append(new_respondant)
        self.free_respondants.append(new_respondant)
    
    def __engage(self, employee, caller):

        if employee.employee_type=='DIRECTOR':
            self.free_directors=self.free_directors[1:]
            self.occupied_directors.append(employee)
        elif employee.employee_type=='MANAGER':
            self.free_managers=self.free_managers[1:]
            self.occupied_managers.append(employee)
        else:
            self.free_respondants=self.free_respondants[1:]
            self.occupied_respondants.append(employee)

    def __disengage(call):

        call.disengage()
        temp =[] 

        if len(call_queue)>0:
            call.switch(call_queue[0])
            call_queue=call_queue[1:]
            return
    
        if call.employee.employee_type=='DIRECTOR':

            for index in range(len(self.occupied_directors)):
                if self.occupied_directors[index].id == call.employee.id:
                    free_directors.append(call.employee)
                    temp = self.occupied_directors[:index]+self.occupied_directors[index+1:]
            self.occupied_directors=temp

        elif call.employee.employee_type=='MANAGER':

            for index in range(len(self.occupied_managers)):
                if self.occupied_managers[index].id == call.employee.id:
                    free_directors.append(call.employee)
                    temp = self.occupied_managers[:index]+self.occupied_managers[index+1:]
            self.occupied_managers=temp
            
        else:
            
            for index in range(len(self.occupied_respondants)):
                if self.occupied_respondants[index].id == call.employee.id:
                    free_directors.append(call.employee)
                    temp = self.occupied_respondants[:index]+self.occupied_respondants[index+1:]
            self.occupied_respondants=temp
    
        del call
    
    def dispatch_call(call):

        if len(free_respondants)>0:
            self.__engage(free_respondants[0], call)
        elif len(free_managers)>0:
            self.__engage(free_managers[0], call)
        elif len(free_directors)>0:
            self.__engage(free_directors[0], call)
        else:
            pass
            self.calls_queue.append(call)
        return





    

        


