import numpy as np
import matplotlib.pyplot as plt

ages = np.random.randint(10, 60, 100)  # Generate 100 random ages
plt.hist(ages, bins=10, color="orange", edgecolor="black")

plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()
