# Timothy Vaculik
# Generating Data
# I think is is difficulty of 9/10

from die import Die
import matplotlib.pyplot as plt

die_1, die_2, die_3  = Die(), Die(), Die()

results = [die_1.num_sides + die_2.roll() for _ in range(5000)]


max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result + 1)]
plt.bar(range(3, max_result + 1), frequencies)
plt.title('Results of Rolling Two Six-Sided Dice 5,000 Times')
plt.xlabel('Sum of the Dice')
plt.ylabel('Frequency')
plt.show()