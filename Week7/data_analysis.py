#  Import required libraries
import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset

# Try loading from CSV first (simulating real-world use case)
try:
    iris_df = pd.read_csv("iris.csv")  # if you have a local iris.csv
    print("✅ Loaded dataset from CSV file.")
except FileNotFoundError:
    print("⚠️ CSV not found. Loading built-in Iris dataset instead.")
    iris = load_iris()
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
    iris_df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display first 5 rows
print("\n🔹 First 5 rows of dataset:")
print(iris_df.head())

# Check data info
print("\n🔹 Dataset Info:")
print(iris_df.info())

# Check missing values
print("\n🔹 Missing Values:")
print(iris_df.isnull().sum())

# Handle missing values if any (drop as example)
if iris_df.isnull().sum().any():
    iris_df = iris_df.dropna()
    print("⚠️ Missing values found and removed.")
else:
    print("✅ No missing values.")

# Task 2: Basic Data Analysis

# Descriptive statistics
print("\n🔹 Descriptive Statistics:")
print(iris_df.describe())

# Group by species and compute mean of numerical columns
grouped = iris_df.groupby("species").mean()
print("\n🔹 Mean values grouped by species:")
print(grouped)

# Observation example
print("\nObservation: Iris-virginica generally has larger petal length/width compared to the other species.")

# Task 3: Data Visualization

sns.set(style="whitegrid")  # Set style for all plots

# 1. Line Chart - trend across samples
plt.figure(figsize=(8,5))
plt.plot(iris_df.index, iris_df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart of Sepal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart - average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=iris_df, ci=None, palette="viridis")
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(iris_df["sepal width (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=iris_df, palette="deep")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

print("✅ Data analysis and visualization completed.")