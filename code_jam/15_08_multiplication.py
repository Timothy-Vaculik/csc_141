# Timothy Vaculik
# Code for rolling two dice and multiplying the results
# I think is is difficulty of 8/10

from plotly.graph_objects import Figure, Bar, Layout
from plotly import offline

from die import Die


die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

    frequencies = []
    for value in range(1, die_1.num_sides * die_2.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

        x_values = list(range(1, die_1.num_sides * die_2.num_sides + 1))
        data = [Bar(x=x_values, y=frequencies)]

        xaxis_config = {'title': 'Result', 'dtick': 1}
        yaxis_config = {'title': 'Frequency'}
        my_layout = Layout(title='Results of rolling two D6 dice 1000 times and multiplying the results', xaxis=xaxis_config, yaxis=yaxis_config)

    offline.plot({'data': data, 'layout': my_layout}, filename='multiplication_dice.html')