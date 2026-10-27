# Timothy Vaculik
#  Code for plotting cubes
# I think is is difficulty of 8/10

import matplotlib.pyplot as plt
plt.style.available


x_values = (1, 2, 3, 4, 5)
y_values = [x**3 for x in x_values]


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax .tick_params(labelsize=14)

plt.show()

x_values = list(range(1, 5002))
cube_values_large = [x**3 for x in x_values]

ax.scatter(x_values, cube_values_large, c=cube_values_large, cmap=plt.cm.Blues, s=10)

ax.set_title("First 5000 Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

plt.show()

