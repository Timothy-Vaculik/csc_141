# Timothy Vaculik
#  Code for rolling two dice and plotting the results
# I think is is difficulty of 6/10

from plotly.graph_objs import Figure, Bar, Layout
from plotly import offline

from die import Die

die_1, die_2 = Die(), Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

    max_result = die_1.num_sides + die_2.num_sides
    frequency = [results.count(value) for value in range(2, max_result + 1)]

    x_values = list(range(2, max_result + 1))
    data = [Bar(x=x_values, y=frequency)]

    xaxis_config = {'title': 'Result', 'dtick': 1}
    yaxis_config = {'title': 'Frequency'}
    my_layout = Layout(title='Results of rolling two D6 dice 1000 times', xaxis=xaxis_config, yaxis=yaxis_config)
    
offline.plot = ({'data': data, 'layout': my_layout})