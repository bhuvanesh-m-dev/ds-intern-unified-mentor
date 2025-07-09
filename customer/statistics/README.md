# 📊 Customer Age Analysis

This simple Python script reads a CSV file containing customer data and computes basic statistics about customer ages.

## 📁 Dataset

* **File Name:** `data.csv`
* **Expected Column:** `Customer Age`

## 🧪 Code

```python
import pandas as pd

df = pd.read_csv('data.csv')
ages = df['Customer Age']

mean_age = ages.mean()
median_age = ages.median()
mode_age = ages.mode()[0]

print(f"Mean Customer Age: {mean_age:.2f}")
print(f"Median Customer Age: {median_age:.2f}")
print(f"Mode Customer Age: {mode_age:.2f}")
```

## 📈 Output

The output will display the:

* **Mean Customer Age**
* **Median Customer Age**
* **Mode Customer Age**

Example output:

```
Mean Customer Age: 35.42
Median Customer Age: 34.00
Mode Customer Age: 30.00
```

---
## 🙋‍♂️ Author

**Bhuvanesh M**   
🌐 [bhuvaneshm.in](https://bhuvaneshm.in)   
🔗 [linkedin.com/in/bhuvaneshm-developer](https://www.linkedin.com/in/bhuvaneshm-developer)   
✍️ [dev.to/bhuvaneshm\_dev](https://dev.to/bhuvaneshm_dev)   
📊 [kaggle.com/bhuvaneshm06](https://www.kaggle.com/bhuvaneshm06)    

---
