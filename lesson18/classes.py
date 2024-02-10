# Classess are blueprints for simple objects

class Vehicle:
    # Using the initiliser function '__init__' we can set properties to the class vehicle
    def __init__(self, make, model):
        self.make = make  # refers the object to itself i.e the make & model
        self.model = model

    def moves(self):  # Defines moves and refers to self
        print('Moves alaong..')

    # Defines a function that will get the make and model which is easier to then call the output
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)

my_car.get_make_model()

my_car.moves()  # The 'my_car' is an object created from the class 'Vehicle'

# Creates a new object called 'your_car' from the vehicle class
your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()

# Inheratance

# Where we can provide more detail by creating a new class that is dependant on another class


class Airplane(Vehicle):  # Creates a new class called Airplane inside the vehicle class

    def __init__(self, make, model, faa_id):
        super().__init__(make, model)  # Inheret from the parent class
        self.faa_id = faa_id

    def moves(self):
        print('Flies along..')


class Truck(Vehicle):  # Creates a new class called Truck that calls the vehicle class
    def moves(self):
        print('Rumbles along..')


class GolfCart(Vehicle):  # Creates a new class called GolfCart.
    # Except as a class can not be empty we can use the 'pass'. This means ir will inherit everything as is.
    pass


# New object 'cessna' with values
# New object 'cessna' with values
cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')  # New object 'mack' with values
golfwagon = GolfCart('Yamaha', 'GC100')  # New object 'golfwagon' with values


cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


# Polymorthisim. The ability to behave differently in response to the same input messages.

# Just create an extra space to seperate the terminal code for clear seperation & identification
print('\n\n')

# Create a for loop

# Create a loop as all objects have the same input messages. But the each object will return different response with the values defined for them
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
