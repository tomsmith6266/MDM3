import random
import numpy as np
import matplotlib.pyplot as plt


# instead of saving a whole array of acceptable spaces - save a single space with a distribution around it?
# or perhaps save a set of rules for seeing multiple free spaces - would require vision of spaces ahead/behind?


# functions that determine behaviour of cars
def first_free_space(c, curr_space):
    if curr_space != num_cars - 1:
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
    opt_spaces = (num_cars//20) + (num_cars//20) * num_trips
    desired_spaces[c] = np.arange((num_cars - opt_spaces), num_cars, 1, dtype=object)


num_cars = 200  # arbitrary value for number of cars
time_to_park = np.zeros(num_cars)  # keep track of time taken for each car to park
spaces = np.zeros(num_cars)  # assuming there are enough spaces for cars
road = np.zeros(num_cars)  # road is same length as no. parking spaces

desired_spaces = [0] * num_cars  # each car has an array of spaces deemed acceptable to park in
cars = []  # each car will be appended to an array of cars

car_park_full = False  # the program will end when the car park is full
time_step = 0  # the program is an iteration
time_step_duration = 1  # arbitrary value for the duration of one time step (all cars move one space)

# THIS WILL DEPEND ON JOE'S CODE
add_car = True  # under certain circumstances a new car is allowed into the car park

new_car = 1  # each car has its own identification number

# program runs for all cars until car park full
while not car_park_full:

    # conditions to add a new car into car park - currently adding a new car every time until 20 cars have entered
    # ADD CAR DEPENDENT ON JOE'S CODE!
    if len(cars) and max([item[0] for item in cars]) == num_cars:
        add_car = False

    # if the conditions are met to add a new car, add a new car and update identification number
    # ADD CAR DEPENDENT ON JOE'S CODE!
    if add_car and road[0] == 0:

        # We can add an if statement to give certain proportions of cars different behaviours
        driver_type = random.choices([1, 2, 3], [0.4, 0.2, 0.4])[0]
        if driver_type == 1:
            first_free_space(new_car - 1, 0)
        elif driver_type == 2:
            optimal_space(new_car - 1, 0)
        else:
            random_space(new_car - 1, 0)

        road[0] = new_car

        # each car has an identification number, their driver type and the no. trips of the car park they have done
        cars.append([new_car, driver_type, 0, 0])

        new_car += 1

    # for every car on road, un-parked
    for car in cars:

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
                if parking_duration < 3:
                    car[3] += 1
                else:
                    road[space_num] = 0
                    spaces[space_num] = id_num
                    cars.remove(car)
                parked = True
            else:
                if driver_type == 1 or num_trips > 2:
                    first_free_space(id_num - 1, space_num)
                elif driver_type == 2:
                    optimal_space(id_num - 1, num_trips)
                else:
                    random_space(id_num-1, space_num)

        # if the car is unable to park and there is no car in front, move forward - else stay stationary
        if not parked:
            if int(space_num[0]) == len(spaces) - 1:
                if road[0] == 0:
                    road[space_num] = 0
                    road[0] = id_num
                car[2] += 1
            elif road[space_num + 1] == 0:
                road[space_num] = 0
                road[space_num + 1] = id_num

    time_step += 1

    car_park_full = np.all(spaces > 0)


print(sum(time_to_park))
plt.plot(time_to_park)
plt.show()
