# simple car race with 2 cars

import random
    
time = 0.
dt = .25 # Timestep

# car 1
position1 = 50 # Initial position (miles)
velocity1 = 60 # Velocity (miles/hour)

#car 2
position2 = 50 # Initial position (miles)
velocity2 = 60 # Velocity (miles/hour)

# print header for time output and initial states
print ("Time  Position 1  Position 2")
print ("%6.2f %6.2f %6.2f" % (time, position1, position2))

while time < 10: # Run for 10 hours
    time += dt
    #random velocity between 30 and 60
    velocity1 = random.randint(30, 60)
    velocity2 = random.randint(30, 60)
    position1 = position1 + velocity1*dt
    position2 = position2 + velocity2*dt
    print ("%6.2f %6.2f %6.2f" % (time, position1, position2))

print ("Final position car 1: %6.2f" % position1)
print ("Final position car 2: %6.2f" % position2)
