import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


# instead of saving a whole array of acceptable spaces - save a single space with a distribution around it?
# or perhaps save a set of rules for seeing multiple free spaces - would require vision of spaces ahead/behind?

# functions that determine behaviour of cars
def one_random_space(c):
    desired_spaces[c] = random.randint(0, len(spaces)-1)


num_cars = 18  # arbitrary value for number of cars
spaces = np.zeros(num_cars)  # assuming there are enough spaces for cars
road = np.zeros(num_cars)  # road is same length as no. parking spaces
space_time = 2  # time taken to drive past one space (s)
return_time = num_cars * space_time  # time taken to return to start (s)
full_laps = 0  # number of cars that have completed a full lap

desired_spaces = np.zeros(num_cars)  # each car has an array of spaces deemed acceptable to park in
cars = np.array([])  # each car will be appended to an array of cars

car_park_full = False  # the program will end when the car park is full
time_step = 0  # the program is an iteration

# THIS WILL DEPEND ON JOE'S CODE
add_car = True  # under certain circumstances a new car is allowed into the car park

new_car = 1  # each car has its own identification number


# program runs for all cars until car park full
while not car_park_full:

    # conditions to add a new car into carpark
    # ADD CAR DEPENDENT ON JOE'S CODE!
    if cars.size and np.amax(cars) == num_cars:
        add_car = False


    # if the conditions are met to add a new car, add a new car and update identification number
    # ADD CAR DEPENDENT ON JOE'S CODE!
    if add_car and road[0] == 0:
        road[0] = new_car
        cars = np.append([new_car], cars)

        # We can add an if statement to give certain proportions of cars different behaviours
        one_random_space(new_car-1)

        new_car += 1

    # for every car on road, un-parked
    for car in cars:

        parked = False
        car = int(car)

        # the space number the current car is in
        # space_num = road.index(car)
        space_num = np.where(road == car)[0]


        # if the car is next to a space that it wants to park in that is not taken, park
        # if the space is taken, move on
        if space_num == desired_spaces[car-1]:
            if spaces[space_num] == 0:
                road[space_num] = 0
                spaces[space_num] = car
                index = np.where(cars == car)[0]
                cars = np.delete(cars, index)
                parked = True
            else:
                one_random_space(car-1)

        if not parked:
            if int(space_num[0]) == len(spaces)-1:
                if road[0] == 0:
                    road[space_num] = 0
                    road[0] = car
            elif road[space_num + 1] == 0:
                road[space_num] = 0
                road[space_num + 1] = car

    print(road)
    print(spaces)

    time_step += 1

    # NEED TO WORK OUT WHEN CAR PARK FULL
    car_park_full = np.all(spaces > 0)

