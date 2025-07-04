# Standard Deviation and Population Calculation

This project demonstrates how to generate random data, store it in a binary file, and calculate both population and sample standard deviations using Python.

## Standard Deviation Formulas

- **Population Standard Deviation:**
  
  std_pop = sqrt(sum((x - mean)^2) / N)
  
  Where:
  - x = each value in the dataset
  - mean = average of the dataset
  - N = total number of data points (population size)

- **Sample Standard Deviation:**
  
  std_sample = sqrt(sum((x - mean)^2) / (n - 1))
  
  Where:
  - x = each value in the sample
  - mean = average of the sample
  - n = sample size

## How It Works

- The script `create_data.py` generates 500 random numbers and selects a random sample of 50 from them.
- Both the main data and sample data are stored in a binary file called `data.dat` using Python's `pickle` module.
- The data is saved using the `wb` (write binary) mode, so every time you run `create_data.py`, it will overwrite `data.dat` with new random data. This means the results will change each time you run the script.
- The scripts do not use or create any `.txt` files; all data is stored in `data.dat`.

## Usage

1. Run `create_data.py` to generate and store new random data in `data.dat`.
2. Run `run.py` to read the data from `data.dat` and calculate both the population and sample standard deviations, printing the formulas and results.

---

This setup is useful for understanding the difference between population and sample standard deviation, and for practicing with binary file operations in Python.
