import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Example data
data = np.random.normal(50, 10, 1000)  # Normally distributed data

# Plot histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.title("Data Distribution")
plt.show()

# Calculate descriptive statistics
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

print(f"Mean: {mean}, Median: {median}, Std Dev: {std_dev}")
print(f"Skewness: {skewness}, Kurtosis: {kurtosis}")

# Test for normality
stat, p = stats.shapiro(data)
print(f"Shapiro-Wilk Test: Stat={stat}, p-value={p}")
if p > 0.05:
    print("Data is likely normally distributed.")
else:
    print("Data is NOT normally distributed.")