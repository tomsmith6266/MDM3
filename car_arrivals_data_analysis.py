from scipy.stats import poisson
import numpy as np


def car_arrivals(Capacity):

    TPeriod = 2  # Arrival Time period (minutes)
    Interval = 1  # Interval of time you want to measure the number of live_cars arriving (seconds)

    # Calculate the mean for the poisson distribution
    TPeriod = TPeriod * 60
    mean = Capacity / (TPeriod / Interval)

    # Start the poisson distribution
    data_poisson = poisson.rvs(mu=mean, size=TPeriod)

    # sink variable
    sink = 0

    # for loop to separate arriving live_cars by units of time (never more than one car arriving each second)
    for i in range(len(data_poisson)):
        if data_poisson[i] > 1:
            while data_poisson[i] > 1:
                data_poisson[i] -= 1
                sink += 1
        elif data_poisson[i] == 0 and sink > 0:
            data_poisson[i] += 1
            sink -= 1

    if sum(data_poisson) < Capacity:
        data_poisson = np.append(data_poisson, np.ones([Capacity - sum(data_poisson)]))

    while sum(data_poisson) > Capacity:
        data_poisson = np.delete(data_poisson, -1)

    return data_poisson