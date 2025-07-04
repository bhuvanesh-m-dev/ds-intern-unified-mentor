import random
import pickle
data = [random.randint(1, 1000) for _ in range(500)]
sample_data = random.sample(data, 50)
with open('data.dat', 'wb') as f:
    pickle.dump({'data': data, 'sample_data': sample_data}, f)
