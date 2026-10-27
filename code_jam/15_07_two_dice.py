# Timothy Vaculik
#  Code for rolling three dice and plotting the results
# I think is is difficulty of 9/10

from plotly import graph_objects as go
from plotly.offline import plot

die_1 = Die()
die_2 = Die()   
die_3 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

    for value in range(3, die_1.num_sides + die_2.num_sides + die_3.num_sides + 1):
        frequency = results.count(value)
        frequency.append(frequency)

        x_values = list(range(3, die_1.num_sides + die_2.num_sides + die_3.num_sides + 1))
        data = [go.Bar(x=x_values, y=frequency)]

        xaxis_config = {'title': 'Result', 'dtick': 1}
        yaxis_config = {'title': 'Frequency'}
        my_layout = go.Layout(title='Results of rolling three D6 dice 1000 times', xaxis=xaxis_config, yaxis=yaxis_config)

        offline_plot = go.Figure(data=data, layout=my_layout)
