# Timothy Vaculik
# Generating Data
# I think is is difficulty of 9/10

from die import Die 
import matplotlib.pyplot as plt

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    results = die_1.roll() + die_2.roll()
    results.append(results)

    frequencies = []
    