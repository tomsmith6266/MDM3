import matplotlib.pyplot as plt
from car_arrivals_data_analysis import car_arrivals
from CarParkModel12 import model
import seaborn as sns

# # Say, "the default sans-serif font is COMIC SANS"
# plt.rcParams['font.sans-serif'] = "Computer Modern"
# # Then, "ALWAYS use sans-serif fonts"
# plt.rcParams['font.family'] = "sans-serif"

# keep same poisson arrival distribution and capacity for all runs of program
capacity = 100
arrival_time = 5
data_poisson = car_arrivals(capacity, arrival_time)

num_runs = 2 # number of times to run program
avg_times_first_free = []
avg_times_optimal = []
avg_times_random = []
avg_times = []

avg_times_no_eloy = []

avg_time_to_park_eloy_save = []

avg_times_optimal_no_eloy = []
avg_times_random_no_eloy = []
avg_times_first_free_no_eloy = []

for i in range(0, num_runs):
    # run model num_runs number of times - Eloy user percentage going from 0 to 100, other behaviours equally likely

    a = 0.01*i
    b = 1 - a

    # c = 0.01*i
    # d = (1 - c)/2

    e = (0.01 * i)
    f = (1 - e)/3
    time_to_park, spaces, avg_time_to_park, time_save, road_save, flow_rate, queue_length = model(capacity, data_poisson, [f, f, f, e],20,3)
    time_to_park, spaces, avg_time_to_park_first_free, time_save, road_save, flow_rate, queue_length = model(capacity, data_poisson, [b, 0, 0, a],20,3)
    time_to_park, spaces, avg_time_to_park_optimal, time_save, road_save, flow_rate, queue_length = model(capacity, data_poisson, [0, b, 0, a],20,3)
    time_to_park, spaces, avg_time_to_park_random, time_save, road_save, flow_rate, queue_length = model(capacity, data_poisson, [0, 0, b, a],20,3)

    avg_times_first_free.append(avg_time_to_park_first_free)
    avg_times_optimal.append(avg_time_to_park_optimal)
    avg_times_random.append(avg_time_to_park_random)
    avg_times.append(avg_time_to_park)

    # avg_times_first_free.append(avg_time_to_park_first_free)
    # avg_times_optimal.append(avg_time_to_park_optimal)
    # avg_times_random.append(avg_time_to_park_random)

    # time_to_park, spaces, avg_time_to_park_random = model(capacity, data_poisson, [d, c, c, 0],0.05)
    # time_to_park, spaces, avg_time_to_park_optimal = model(capacity, data_poisson, [c, d, c, 0],0.05)
    # time_to_park, spaces, avg_time_to_park_random = model(capacity, data_poisson, [c, c, d, 0],0.05)
    #
    # time_to_park, spaces, avg_time_to_park_eloy = model(capacity, data_poisson, [f, f, f, e],0.05)

    #avg_time_to_park_eloy_save.append(avg_time_to_park_eloy)

    # avg_times_first_free_no_eloy.append(avg_time_to_park_first_free)
    # avg_times_optimal_no_eloy.append(avg_time_to_park_optimal)
    # avg_times_random_no_eloy.append(avg_time_to_park_random)
    #avg_times.append(avg_time_to_park)
    #avg_times_no_eloy.append(avg_time_to_park1)

    print(i)

plt.figure(1) #Varying each type against Eloy
plt.plot(avg_times_first_free, label = 'First Free Space')
plt.plot(avg_times_optimal, label = 'End Parking')
plt.plot(avg_times_random, label = 'Random')
plt.plot(avg_times, label = 'Combined')
plt.legend(loc="upper right")
plt.xlabel('Arrival Time', fontsize = 13)
plt.ylabel('Mean Time Taken to Park ($T_p$) (s)', fontsize = 13)
plt.title("Mean waiting times with increasing \narrival time", fontsize = 18)
plt.savefig('ArrivalTime.png')
plt.show()

# plt.figure(1) #Varying each type against Eloy
# plt.plot(avg_times_first_free, label = 'First Free Space')
# plt.plot(avg_times_optimal, label = 'End Parking')
# plt.plot(avg_times_random, label = 'Random')
# plt.plot(avg_times, label = 'Combined')
# plt.legend(loc="upper right")
# plt.xlabel('Proportion of Eloy users (%)', fontsize = 13)
# plt.ylabel('Mean Time Taken to Park ($T_p$) (s)', fontsize = 13)
# plt.title("Mean waiting times with increasing proportion \nof Eloy users", fontsize = 18)
# plt.savefig('CombinedIncreasingGraph.png')
# plt.show()
#
# plt.figure(2) #Varying each type against Eloy
# plt.plot(avg_times_first_free_no_eloy, label = 'first free')
# plt.plot(avg_times_optimal_no_eloy, label = 'optimal')
# plt.plot(avg_times_random_no_eloy, label = 'random')
# plt.legend(loc="upper right")
# plt.ylabel('Average Time Taken')
# plt.title("Average waiting times with increasing proportion each driver type \n against the other two (no Eloy)")
# plt.xlabel('Proportion of driver type')
# plt.savefig('IncreasingType.png')
# plt.show()
#
# plt.figure(3)
# plt.plot(avg_time_to_park_eloy_save, label = 'first free')
# plt.title('Increasing Eloy while decreasing other driver types')
# plt.ylabel('Average Time Taken')
# plt.xlabel('Proportion of Eloy')
# plt.savefig('IncreasingEloy.png')
# plt.show()
# #
# #
# plt.figure(4)
# time_to_park = time_to_park.reshape((10,10))
# ax = sns.heatmap(time_to_park, linewidth=0.5)
# plt.show()
#
#
# plt.show()

