# Timothy Vaculik
#  Code for plotting random walks
# I think is is difficulty of 9/10


from random import choice

def __init__(self, num_points=5000):
    self.num_points = num_points

    self.x_values = [0]
    self.values = [0]

    def more_step(self):
        """Determine the distance and the direction"""
        distance = choice([1, -1])
        direction = choice([0, 1, 2, 3])
        return distance*direction

    def fill_walk(me):
        """Calculate points by using more_step() """
        while len(me.x_values) < me.num_points:

            x_step = me.more_step()
            y_step = me.more_step()

            if x_step == 0 and y_step == 0:
                continue

            x = me.x_values[-1] + x_step
            y = me.y_values[-1] + y_step

            me.x_values.append(x)
            me.y_values.append(y)


            





    