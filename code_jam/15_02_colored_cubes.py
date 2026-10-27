# Timothy Vaculik
# Code for plotting colored cubes
# I think is is difficulty of 6/10

import matplotlib.pyplot as plt

x_values = list(range(1, 5002))
cubes = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Blues, s=10)

ax.set_title("Colored Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
plt.show()