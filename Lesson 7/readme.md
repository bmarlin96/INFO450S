
# 📊 Lesson 7: Exploratory Data Analysis (EDA) with NumPy & Pandas

This notebook introduces **Exploratory Data Analysis (EDA)** — the critical process of understanding and summarizing data before building models. You’ll use **NumPy** for high-performance numerical operations and **Pandas** for rich data manipulation, visualization, and statistical summaries.

---

## 🧠 Learning Objectives

- Understand the purpose and importance of EDA
- Use NumPy to efficiently process large arrays
- Create and manipulate Pandas Series and DataFrames
- Visualize data and compute basic statistics
- Read and explore tabular data from CSV and TXT files

---

## 🔧 Tools Used

- `NumPy` for fast, vectorized calculations
- `Pandas` for data wrangling and summarization
- `.plot()` (Matplotlib backend) for quick visualizations

---

## 🚀 Key Code Examples

### ✅ NumPy vs. Python Lists (Performance Benchmark)

```python
import numpy as np
import time

size = 100_000_000
py_list = [x for x in range(size)]
np_array = np.arange(size)

# Python list squaring
start = time.time()
[x**2 for x in py_list]
py_time = time.time() - start

# NumPy array squaring
start = time.time()
np_array**2
np_time = time.time() - start

print("Python time:", py_time, "| NumPy time:", np_time)
```

---

### 📈 Simple EDA with Pandas Series

```python
import pandas as pd

my_series = pd.Series([1, 2, 3, 0, 8])
print("Mean:", my_series.mean())
my_series.plot()  # Quick visualization
```

---

### 🧱 Building and Plotting a DataFrame

```python
wrestlers = ['john cena', 'the rock', 'hulk', 'stone cold']
matches = [1500, 800, 1200, 1100]

df = pd.DataFrame({'Wrestler': wrestlers, 'Matches': matches})
df['Wins'] = [10, 20, 30, 40]
df.plot(x='Wrestler', y='Matches', kind='bar')
```

---

### 📄 Reading & Exploring a Delimited File

```python
df = pd.read_csv("your_file.txt", sep="\t")
print(df.head())
print(df.describe())
df.plot(x='SomeColumn', y='AnotherColumn', kind='scatter')
```

---

## 📌 Summary

This lesson emphasizes **Exploratory Data Analysis (EDA)** as a hands-on process of inspecting, describing, and visualizing data. By combining NumPy’s speed and Pandas’ flexibility, you gain the skills to explore real-world datasets effectively.

---

*Keep exploring! The insights you find here lay the groundwork for powerful data-driven decisions and machine learning workflows.*
