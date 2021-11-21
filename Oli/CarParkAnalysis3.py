import matplotlib.pyplot as plt
from car_arrivals_data_analysis import car_arrivals
from CarParkModel12 import model
import seaborn as sns

# keep same poisson arrival distribution and capacity for all runs of program
capacity = 100

arrival_time = 10
data_poisson = car_arrivals(capacity, arrival_time)

num_runs = 100 # number of times to run program

avg_time_save = []
end_parking = []

for i in range(0, num_runs):
    # run model num_runs number of times - Eloy user percentage going from 0 to 100, other behaviours equally likely

    time_to_park, spaces, avg_time_to_park, a, b, c, d = model(capacity, data_poisson, [0, 0.5, 0, 0.5], i+1, 6)

    #time_to_park, spaces, avg_time_to_park, a, b, c = model(capacity, data_poisson, [0, 0.5, 0, 0.5],i+1,3)

    avg_time_save.append(avg_time_to_park)

    end_parking.append(100-i)

    print(100-i)

# plt.figure(1) #Varying each type against Eloy
# plt.xlabel('Arrival time', fontsize = 13)
# plt.plot(end_parking, avg_time_save)
# plt.ylabel('Mean Time Taken to Park ($T_p$) (s)', fontsize = 13)
# plt.title("Varing the arrival time", fontsize = 18)
# plt.savefig('Arrival.png')
# plt.show()

plt.figure(1) #Varying each type against Eloy
plt.xlabel('Size of end zone (%)', fontsize = 12)
plt.plot(end_parking, avg_time_save)
plt.ylabel('Mean Time Taken to Park ($T_s$) (s)')
plt.title("How varing the size of the end zone\n effects mean time taken to park", fontsize = 18)
plt.savefig('EndZoneParking.png')
plt.show()

# plt.figure(1) #Varying each type against Eloy
# plt.xlabel('Time taken to park in bay ($T_b$) (s)')
# plt.plot(end_parking, avg_time_save)
# plt.ylabel('Mean Time Taken ($T_p$) (s)')
# plt.title("Varing the time taken to park")
# plt.savefig('ParkingTime.png')
# plt.show()

