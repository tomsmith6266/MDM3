import matplotlib.pyplot as plt
from car_arrivals_data_analysis import car_arrivals
from CarParkModel12 import model
import seaborn as sns
import numpy as np

# keep same poisson arrival distribution and capacity for all runs of program
capacity = 100


num_runs = 100 # number of times to run program

random = []
optimal = []
eloy = []
first = []

time_random = []
time_optimal = []
time_first = []
time_eloy = []

for i in range(0, num_runs):
    arrival_time = i+1
    data_poisson = car_arrivals(capacity, arrival_time)

    time_to_park, spaces, avg_time_to_park_first, time_save, road_save, flow_rate_first, queue_length = model(capacity, data_poisson, [0.25, 0.25, 0.25, 0.25], 20, 6)
    # time_to_park, spaces, avg_time_to_park_optimal, time_save, road_save, flow_rate_optimal, queue_length = model(capacity, data_poisson, [0, 1, 0, 0], 20, 3)
    # time_to_park, spaces, avg_time_to_park_random, time_save, road_save, flow_rate_random, queue_length = model(capacity, data_poisson, [0, 0, 1, 0], 20, 3)
    # time_to_park, spaces, avg_time_to_park_eloy, time_save, road_save, flow_rate_eloy, queue_length = model(capacity, data_poisson, [0, 0, 0, 1], 20, 3)

    # time_random = np.append(time_random, int(avg_time_to_park_random))
    # time_optimal = np.append(time_optimal, int(avg_time_to_park_optimal))
    time_first = np.append(time_first, int(avg_time_to_park_first))
    # time_eloy = np.append(time_eloy, int(avg_time_to_park_eloy))

    # random = np.append(random, int(flow_rate_random))
    # optimal = np.append(optimal, int(flow_rate_optimal))
    first = np.append(first, int(flow_rate_first))
    # eloy = np.append(eloy, int(flow_rate_eloy))

    print(i)


plt.figure(1) #Varying each type against Eloy
plt.plot(first, label = 'First Free Space')
# plt.plot(optimal, label = 'End Parking')
# plt.plot(random, label = 'Random')
# plt.plot(eloy, label = 'Eloy')
plt.legend(loc="upper right")
plt.xlabel('Arrival Time', fontsize = 13)
plt.ylabel('Flow Rate', fontsize = 13)
plt.title("How flow rate varies with increasing \narrival time duration", fontsize = 18)
plt.savefig('ArrivalTime.png')
plt.show()

# print("Random " + str(np.average(time_random)))
# print("End Parking " + str(np.average(time_optimal)))
# print("First Parking " + str(np.average(time_first)))
# print("Eloy " + str(np.average(time_eloy)))
# #
# Names = ['Random', 'End of Car\nPark', 'First Free\nSpace', 'Eloy']
# ValuesFlow = [np.average(random), np.average(optimal), np.average(first), np.average(eloy)]
# ValuesTime = [np.average(time_random), np.average(time_optimal), np.average(time_first), np.average(time_eloy)]


# plt.figure(1)
# plt.bar(Names, Values)
# plt.ylabel('Mean flow rate (cars moving/time step)')
# plt.xlabel('Driver Type')
# plt.title('Mean flow rate for each driver type')
# plt.savefig('FlowRate')
# plt.show()

# X_axis = np.arange(len(Names))
#
# plt.bar(X_axis - 0.2, ValuesFlow, 0.4, label='Flow Rate')
# plt.bar(X_axis + 0.2, ValuesTime, 0.4, label='Average $T_s$')
#
# plt.xticks(X_axis, Names)
# plt.xlabel("Driver Type")
# plt.ylabel("Number of Students")
# plt.title("Number of Students in each group")
# plt.legend()
# plt.show()

# plt.figure(1)
# X_axis = np.arange(len(Names))
#
# fig, ax1 = plt.subplots()
#
# plt.xticks(X_axis, Names, fontsize = 12)
# plt.title("Comparing Flow rate with Time \nTaken to park", fontsize = 18)
#
# color = 'tab:red'
# ax1.set_xlabel('Drive Type', fontsize = 13)
# ax1.set_ylabel('Flow Rate', color=color, fontsize = 13)
# ax1.bar(X_axis - 0.2, ValuesFlow, 0.4, label='Flow Rate', color = color)
# ax1.tick_params(axis='y', labelcolor=color)
#
# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
#
# color = 'tab:blue'
# ax2.set_ylabel('Average Time Taken to Park ($T_s$) (s)', color=color, fontsize = 13)  # we already handled the x-label with ax1
# ax2.bar(X_axis + 0.2, ValuesTime, 0.4, label='Average $T_s$', color = color)
# ax2.tick_params(axis='y', labelcolor=color)
#
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.savefig('FlowvsTimeTaken.png')
# plt.show()
