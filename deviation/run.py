import pickle
import math
print("Standard deviation (population): std_pop = sqrt(sum((x - mean)^2) / N)")
print("Standard deviation (sample): std_sample = sqrt(sum((x - mean)^2) / (n - 1))")


with open('data.dat', 'rb') as f:
    data_dict = pickle.load(f)

data = data_dict['data']
sample_data = data_dict['sample_data']


mean_data = sum(data) / len(data)
mean_sample = sum(sample_data) / len(sample_data)

std_pop = math.sqrt(sum((x - mean_data) ** 2 for x in data) / len(data))

std_sample = math.sqrt(sum((x - mean_sample) ** 2 for x in sample_data) / (len(sample_data) - 1))


print(f"Population standard deviation: {round(std_pop,3)}")
print(f"Sample standard deviation: {round(std_sample,3)}")
