# Timothy Vaculik
#  Code for rolling two D8 dice and plotting the results
# I think is is difficulty of 8/10

import plotly.express as px
from plotly.offline import plot

from die import die

Die_1 = die(num_sides=8)
Die_2 = die(num_sides=8)

results = []
for roll_num in range(1000):
    result = Die_1.roll() + Die_2.roll()
    results.append(result)

    frequency = []
    max_result = Die_1.num_sides + Die_2.num_sides
    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequency.append(frequency)

    x_values = list(range(2, max_result + 1))
    fig = px.bar(x=x_values, y=frequency, labels={'x': 'Result', 'y': 'Frequency'}, title='Results of rolling two D8 dice 1000 times')
    fig.show()