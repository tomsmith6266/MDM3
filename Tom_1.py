import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

parking_spaces = [0]*100
cars = 100
total_time = 0
speed = 5
width = 2

space_time = width/speed

repeat_list = []
times = []

for i in range(1,100):
    for i in range(cars):
        list_spaces = range(cars)
        random_space = random.randint(1, len(parking_spaces)-1)
        travel_time = random_space * space_time
        total_time += travel_time
        while parking_spaces[random_space] == 1 and random_space not in repeat_list:
            repeat_list.append(random_space)
            if repeat_list[-1] < list_spaces[-1]:
                random_space = random.randint(repeat_list[-1], len(parking_spaces) - 1)
            else:
                random_space = random.randint(0, len(parking_spaces) - 1)

            if random_space > repeat_list[-1]:
                travel_time = (len(parking_spaces) - repeat_list[-1] + random_space) * space_time
            else:
                travel_time = (random_space - repeat_list[-1]) * space_time
            total_time += travel_time

        parking_spaces[random_space] = 1
        repeat_list = []

    times.append(total_time)
    total_time = 0
    parking_spaces = [0] * 100


# Calculating mean and standard deviation
mean = np.mean(times)
sd = np.std(times)

times.sort()

plt.figure(1)
plt.plot(times, norm.pdf(times, mean, sd))
plt.xlabel("Average parking times")
plt.ylabel('pdf')

plt.show()