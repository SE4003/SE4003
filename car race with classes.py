#This implements a car simulation to illustrate the concepts of class creation and usage.

class Car():
    #attributes that apply to all instances
    acceleration = 0.0 #class level attribute
    
    #methods (functions) are automatically called when a class is instantiated
    def __init__(self,position,velocity):  #requires 2 underscores and the mandatory self parameter
        #instance attributes
        self.position = position 
        self.velocity = velocity
    #methods to update position based on car's state and data
    def cruise(self,dt): #position update at constant speed
        self.position = self.position + self.velocity*dt
    def accelerate(self,dt): #position update when accelerating
        self.velocity = self.velocity + self.acceleration*dt  #acceleration is velocity change
        self.cruise(dt)
    def honk(self):
      print("HONK")

# main program

#initialize variables and constants
time = 0.
dt = 0.25 #time increment

#create car objects
Fiat = Car(50,60) # initial position, velocity
Tesla = Car(-100,90) # initial position, velocity
lamborghini = Car(-200, 185)

# header for time output
print ("Time  Position 1  Position 2 Position 3")

# Run for 10 hours
while time < 10:
    time += dt
    Fiat.cruise(dt) # cruise car for time increment
    Tesla.cruise(dt) # cruise car for time increment
    lamborghini.cruise(dt) # cruise car for time increment
    print ("%5.2f %9.2f %9.2f %9.2f" % (time, Fiat.position, Tesla.position, lamborghini.position))

print ("Final position: %6.2f" % Fiat.position)

Tesla.honk()
