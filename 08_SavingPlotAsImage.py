import matplotlib.pyplot as plt

# Create subplots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2)

# First plot (Top-left)
axs[0, 0].plot([1, 2, 3, 4], [10, 20, 25, 30])
axs[0, 0].set_title("Line Plot")

# Second plot (Top-right)
axs[0, 1].bar(["A", "B", "C", "D"], [5, 15, 25, 35])
axs[0, 1].set_title("Bar Chart")

# Third plot (Bottom-left)
axs[1, 0].scatter([1, 2, 3, 4], [10, 20, 30, 40])
axs[1, 0].set_title("Scatter Plot")

# Fourth plot (Bottom-right)
axs[1, 1].hist([10, 20, 30, 40, 50, 60, 70], bins=5)
axs[1, 1].set_title("Histogram")

# Adjust layout
plt.tight_layout()

# saving figure to jpeg
plt.savefig("plot.jpeg", dpi=300)
plt.show()

