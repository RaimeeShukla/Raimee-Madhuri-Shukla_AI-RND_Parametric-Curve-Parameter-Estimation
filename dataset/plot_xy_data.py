import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("dataset/xy_data.csv")

# Scatter plot
plt.figure(figsize=(8, 8))
plt.scatter(df["x"], df["y"], s=10)

# Label plot
plt.xlabel("x")
plt.ylabel("y")
plt.title("Curve from xy_data.csv")
plt.axis("equal")   
plt.grid(True)

# Save generated plot
plt.savefig("dataset/plot_xy_data.png", dpi=300, bbox_inches="tight")

# Vizualize plot
plt.show()