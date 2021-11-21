import matplotlib.pyplot as plt
from car_arrivals_data_analysis import car_arrivals
from CarParkModel12 import model
import seaborn as sns
import numpy as np

# keep same poisson arrival distribution and capacity for all runs of program
capacity = 100
arrival_time = 2
data_poisson = car_arrivals(capacity, arrival_time)

num_runs = 100 # number of times to run program

random = []
optimal = []
eloy = []
first = []

for i in range(0, num_runs):

    flow_rate_first = model(capacity, data_poisson, [1, 0, 0, 0], 20, 3)
    flow_rate_optimal = model(capacity, data_poisson, [0, 1, 0, 0], 20, 3)
    flow_rate_random = model(capacity, data_poisson, [0, 0, 1, 0], 20, 3)
    flow_rate_eloy = model(capacity, data_poisson, [0, 0, 0, 1], 20, 3)

    random = np.append(random, int(flow_rate_random))
    optimal = np.append(optimal, int(flow_rate_optimal))
    first = np.append(first, int(flow_rate_first))
    eloy = np.append(eloy, int(flow_rate_eloy))

    print(i)


print("Eloy " + str(np.average(eloy)))
print("Random " + str(np.average(random)))
print("End Parking " + str(np.average(optimal)))
print("First Parking " + str(np.average(first)))

Names = ['Random', 'End of Car Park', 'First Free Space', 'Eloy']
Values = [np.average(random), np.average(optimal), np.average(first), np.average(eloy)]

plt.figure(1)
plt.bar(Names, Values)
plt.ylabel('Mean flow rate (cars moving/time step)')
plt.xlabel('Driver Type')
plt.title('Mean flow rate for each driver type')
plt.savefig('FlowRate')
plt.show()


