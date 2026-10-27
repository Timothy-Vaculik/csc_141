# Timothy Vaculik
#  Code for rolling two D8 dice and plotting the results
# I think is is difficulty of 8/10

import plotly.express as px
import matplotlib.pyplot as plt

from die import Die

Die_1 = Die(num_sides=6)
Die_2 = Die(num_sides=6)

results = []
for roll_num in range(1000):
    result = Die_1.roll() + Die_2.roll()
    results.append(result)

frequencies = []
max_result = Die_1.num_sides + Die_2.num_sides
for value in range(2, max_result + 1):
    frequencies.append(results.count(value))

plt.style.use('classic')
fig, ax = plt.subplots()
values = range(2, max_result + 1)
ax.bar(values, frequencies)
ax.set_title('Results of Rolling Two Six-Sided Dice 1,000 Times')
ax.set_xlabel('Sum of the Dice')
ax.set_ylabel('Frequency')
plt.show()
