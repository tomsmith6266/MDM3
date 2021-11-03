import matplotlib.pyplot as plt
from car_arrivals_data_analysis import car_arrivals
from model_data_analysis import model

# keep same poisson arrival distribution and capacity for all runs of program
capacity = 50
data_poisson = car_arrivals(capacity)

num_runs = 10   # number of times to run program
avg_times = []

for i in range(0, num_runs):
    # run model num_runs number of times - Eloy user percentage going from 0 to 100, other behaviours equally likely
    a = (1-(i/num_runs))/3
    time_to_park, spaces, avg_time_to_park = model(capacity, data_poisson, [a, a, a, i])
    
    avg_times.append(avg_time_to_park)

plt.figure(1)
plt.plot(avg_times)
plt.title("Average waiting times with increasing proportion of Eloy users")
plt.show()


