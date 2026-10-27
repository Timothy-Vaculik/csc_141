
from plotly.graph_objs import Layout, Scatter
from plotly import offline
import my_random
from my_random import RandomWalk

rw = RandomWalk(1000)
rw.fill_walk()

data = [Scatter(x=rw.x_values, y=rw.y_values, mode='markers')]

my_layout = Layout(
    title='Random Walk Around',
    xaxis={'title': 'X Value'},
    yaxis={'title': 'Y Value'}
)

offline.plot({'data': data, 'layout': my_layout}, filename='random_walk_around.html')