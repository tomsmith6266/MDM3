import random
import numpy as np
import matplotlib.pyplot as plt
from car_arrivals_2 import data_poisson, Capacity
import seaborn as sns


# functions that determine behaviour of live_cars
def first_free_space(c, curr_space):
    if spaces[curr_space] == 0:
        desired_spaces[c] = curr_space
    elif curr_space != num_cars - 1:
        desired_spaces[c] = curr_space + 1
    else:
        desired_spaces[c] = 0


def random_space(c, curr_space):
    if curr_space != num_cars - 1:
        desired_spaces[c] = random.randint(0, num_cars - 1)
    else:
        desired_spaces[c] = random.randint(curr_space, num_cars - 1)


def optimal_space(c, num_trips):
    # number of spaces from the end considered optimal (increases with number of full trips done)
    opt_spaces = (num_cars // 20) + (num_cars // 20) * num_trips
    desired_spaces[c] = np.arange((num_cars - opt_spaces), num_cars, 1, dtype=object)


def eloy(c, curr_space):
    people_in_front = 0
    free_spaces = []

    for i in range(curr_space, Capacity):
        if spaces[i] == 0:
            free_spaces.append(i)
        if road[i] != 0:
            people_in_front += 1
    if len(free_spaces) > people_in_front:
        # below line works because people_in_front includes the car currently in question
        desired_spaces[c] = free_spaces[-people_in_front]
    else:
        desired_spaces[c] = free_spaces[0]


def choose_desired_spaces(id, driver_type, curr_space, num_trips):
    if driver_type == 1 or num_trips > 3:
        first_free_space(id, curr_space)
    elif driver_type == 2:
        optimal_space(id, num_trips)
    elif driver_type == 3:
        random_space(id, curr_space)
    else:
        eloy(id, curr_space)


num_cars = Capacity  # arbitrary value for number of live_cars
time_to_park = np.zeros(num_cars)  # keep track of time taken for each car to park
spaces = np.zeros(num_cars)  # assuming there are enough spaces for live_cars
spaces_heatmap = np.zeros(num_cars)
road = np.zeros(num_cars)  # road is same length as no. parking spaces

desired_spaces = [0] * num_cars  # each car has an array of spaces deemed acceptable to park in
cars = []   # each car will be appended to an array of cars
live_cars = []  # once cars are in the car park, they become live
queue = []  # live_cars that are queuing at entrance to car park

car_park_full = False  # the program will end when the car park is full
time_step = 0  # the program is an iteration
time_step_duration = 1  # arbitrary value for the duration of one time step (all live_cars move one space)

# THIS WILL DEPEND ON JOE'S CODE
add_car = True  # under certain circumstances a new car is allowed into the car park

new_car = 0  # each car has its own identification number

for i in range(0, Capacity):
    # We can add an if statement to give certain proportions of live_cars different behaviours
    driver_type = random.choices([1, 2, 3, 4], [0, 1, 0, 0])[0]

    # each car has an identification number, their driver type and the no. trips of the car park they have done
    cars.append([i + 1, driver_type, 0, 0])

# program runs for all live_cars until car park full
while not car_park_full:

    print("Spaces:" + str(spaces))
    print("Road:" + str(road))
    # live_cars are added arrive at the car park according to a Poisson distribution
    # a queue will form if live_cars cannot go straight into the car park
    if time_step < len(data_poisson) and data_poisson[time_step] == 1:
        queue.append(cars[new_car])
        new_car += 1

    if len(queue) and road[0] == 0:
        road[0] = queue[0][0]
        live_cars.append(queue[0])
        id_num = live_cars[-1][0]
        driver_type = live_cars[-1][1]
        curr_space = 0
        num_trips = 0
        choose_desired_spaces(id_num-1, driver_type, curr_space, num_trips)
        queue.pop(0)

    # for every car on road, un-parked
    for car in live_cars:

        parked = False
        id_num = car[0]
        driver_type = car[1]
        num_trips = car[2]
        parking_duration = car[3]

        # keeping track of time each car is taking to park
        time_to_park[id_num - 1] += time_step_duration

        # the space number the current car is in
        space_num = np.where(road == id_num)[0]

        # if the car is next to a space that it wants to park in that is not taken, park (takes a certain duration)
        # if the space is taken decide on a new set of spaces and move on
        if np.any(desired_spaces[id_num - 1] == space_num):
            if spaces[space_num] == 0:
                if parking_duration < 6:
                    car[3] += 1
                else:
                    road[space_num] = 0
                    spaces[space_num] = id_num
                    spaces_heatmap[space_num] = time_to_park[id_num - 1]
                    live_cars.remove(car)
                parked = True
            else:
                choose_desired_spaces(id_num - 1, driver_type, int(space_num[0]), num_trips)

        # if the car is unable to park and there is no car in front, move forward - else stay stationary
        if not parked:
            if int(space_num[0]) == len(spaces) - 1:
                if road[0] == 0:
                    road[space_num] = 0
                    road[0] = id_num
                    car[2] += 1
                    # add loads of time to do a loop
                    time_to_park[id_num - 1] += 20

            elif road[space_num + 1] == 0:
                road[space_num] = 0
                road[space_num + 1] = id_num

    time_step += 1

    car_park_full = np.all(spaces > 0)

# plt.figure(1)
# plt.scatter(spaces, time_to_park)
# plt.title("Final spaces vs time taken to park")
#
# plt.figure(2)
# plt.plot(time_to_park)
# plt.title("Time to park against id number")
# plt.show()
#
plt.figure(1)
spaces_heatmap = spaces_heatmap.reshape((10,10))
ax = sns.heatmap(spaces_heatmap, linewidth=0.5, xticklabels=False, yticklabels=False)
plt.savefig('EndParking.png')
plt.show()

