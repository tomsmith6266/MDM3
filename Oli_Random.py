import array
import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
from scipy.stats import norm

parking_spaces = [0]*100
cars = 100
total_time = 0
car_park_length = 1/8
speed = 5
repeat_list = []
width = 2
times = []

for i in range(1,100):
    for i in range(len(parking_spaces)):
        random_space = random.randint(1,len(parking_spaces)-1)
        travel_time = (random_space*width)/speed
        while parking_spaces[random_space]==1:
            repeat_list.append(random_space)
            random_space = random.randint(1, len(parking_spaces) - 1)
            while random_space in repeat_list:
                random_space = random.randint(0, len(parking_spaces) - 1)
            travel_time = (abs(random_space-repeat_list[-1]) * width) / speed
            total_time = total_time + travel_time
        parking_spaces[random_space]=1
        total_time = total_time + travel_time
        repeat_list = []
    times.append(total_time)
    total_time = 0
    parking_spaces = [0] * 100


# Calculating mean and standard deviation
mean = np.mean(times)
sd = np.std(times)

times.sort()

plt.plot(times, norm.pdf(times, mean, sd))
plt.show()