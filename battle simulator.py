# Battle Simulator Using Lanchester's Law

# simulation inputs
x0, y0 = 800, 1000
a, b = .9, .8
dt = .1

# initializations
time, x, y = 0, x0, y0

# print output header and starting values
print (f"{'time':<6} {'x':<6} {'y':<6}") # all columns left justified 6 characters
print (f"{time:<6.2f} {x:<6.0f} {y:<6.0f}")

# integration of troop levels using Euler's method
while x > 0 and y > 0: # run until a troop is eliminated
    time += dt 
    Δx = -b * y
    Δy = -a * x
    x += Δx * dt
    y += Δy * dt
    print (f"{time:<6.2f} {max(x, 0):<6.0f} {max(y, 0):<6.0f}") # max will clip negative end values due to dt timestep approximation
