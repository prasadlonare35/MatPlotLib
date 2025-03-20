import matplotlib.pyplot as plt
import numpy as np

# Basic Box Plot
data = np.random.randint(10, 100, 50)  # 50 random numbers between 10 and 100

plt.boxplot(data)
plt.title("Basic Box and Whisker Plot")
plt.ylabel("Values")
plt.show()

# for Multiple Data Sets
data1 = np.random.randint(10, 100, 50)
data2 = np.random.randint(20, 80, 50)
data3 = np.random.randint(30, 90, 50)

plt.boxplot([data1, data2, data3], labels=["Data 1", "Data 2", "Data 3"])
plt.title("Multiple Box Plots")
plt.grid(True)
plt.ylabel("Values")
plt.show()

# Customized Box Plot
plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor="lightblue"), flierprops=dict(marker="o", color="red", markersize=8))
plt.title("Customized Box Plot")
plt.grid(True, linestyle='--', color='gray', alpha=0.7)
plt.show()

# Horizontal Box Plot
plt.boxplot(data, vert=False)  # Set vert=False for horizontal
plt.title("Horizontal Box Plot")
plt.xlabel("Values")
plt.show()
