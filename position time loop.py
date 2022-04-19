# demonstrate while loop to calculate position over time with Euler's integration method

time = 0.
dt = .25 # Timestep
position = 50 # Initial position (miles)
velocity = 55 # Velocity (miles/hour)

# print header for time output and initial state
print ("Time Velocity Position  ")
print (f"{time:6.2f} {velocity:6.2f} {position:6.2f} ")

# Run for 8 hours
while time < 8:
    time = time + dt
    #integrate velocity to get new position: x(t) = x(t-1) + dx/dt(t-1) * dt
    position = position + velocity*dt
    print (f"{time:6.2f} {velocity:6.2f} {position:6.2f} ")

print (f"Final position: {position:6.2f}")
