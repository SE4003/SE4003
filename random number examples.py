# random number examples
# see random number documentation at https://docs.python.org/3.5/library/random.html

# random.random() #Return floating point number in the range [0.0, 1.0).
# random.uniform(a, b) #Return a random floating point number uniformly distributed in the range (a, b)
# random.randint(a, b) #Return a random integer N such that a <= N <= b.
# random.normalvariate(mu, sigma) #Normal distribution. mu is the mean, and sigma is the standard deviation.

import random

#random number between 0 and 1
a=random.random()
print("random number = ", a)

#random number from uniform distribution
random_uniform = random.uniform(120, 500)
print("random uniform number = ", random_uniform)

#random integer between 100 and 200
random_integer = random.randint(100, 200)
print ("random integer = %d" % random_integer)

#normal distribution variate with mean 100, standard deviation 15
normal = random.normalvariate(100, 15) 
print("normal variate = %6.2f" % normal)

#print 10 random numbers in loop
print ("10 random numbers: ")
for run in range(10):
    print(random.random()) #uniform number between 0 and 1
