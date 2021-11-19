import matplotlib.pyplot as plt
from car_arrivals_data_analysis import car_arrivals
from CarParkModel12 import model
import seaborn as sns
import numpy as np

# keep same poisson arrival distribution and capacity for all runs of program
capacity = 100
arrival_time = 5
data_poisson = car_arrivals(capacity, arrival_time)

num_runs = 300 # number of times to run program

random = []
optimal = []
eloy = []
first = []

for i in range(0, num_runs):


    time_to_park, spaces, avg_time_to_park, a, b, flow_rate_random = model(capacity, data_poisson, [0, 0, 1, 0],0.05,3)
    time_to_park, spaces, avg_time_to_park, a, b, flow_rate_first = model(capacity, data_poisson, [1, 0, 0, 0], 0.05, 3)
    time_to_park, spaces, avg_time_to_park, a, b, flow_rate_optimal = model(capacity, data_poisson, [0, 1, 0, 0], 0.05, 3)
    time_to_park, spaces, avg_time_to_park, a, b, flow_rate_eloy = model(capacity, data_poisson, [0, 0, 0, 1], 0.05, 3)

    random = np.append(random, int(flow_rate_random))
    optimal = np.append(optimal, int(flow_rate_optimal))
    first = np.append(first, int(flow_rate_first))
    eloy = np.append(eloy, int(flow_rate_eloy))

    print(i)


print("Eloy " + str(np.average(eloy)))
print("Random " + str(np.average(random)))
print("End Parking " + str(np.average(optimal)))
print("First Parking " + str(np.average(first)))

Names = ['Random', 'End Parking', 'First Free Space', 'Eloy']
Values = [np.average(random), np.average(optimal), np.average(first), np.average(eloy)]

plt.figure(1)
plt.bar(Names, Values)
plt.ylabel('Mean flow rate (cars moving/time step)')
plt.xlabel('Driver Type')
plt.title('Driver type vs mean flow rate of cars')
plt.savefig('FlowRate')
plt.show()


